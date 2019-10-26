# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.
# 
# Team members: Emily Kuo, Mailani Gelles
# Github repository link:
# https://github.com/usc-ee250-fall2019/lab03-emily-mailani.git

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi`
sys.path.append('../../../Software/Python/')

from grovepi import *
import time
import socket

def Main():
	host = '192.168.1.229'
	port = 9001

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c, addr = s.accept()
	#print("Connection from: " + str(addr))
	message = ""

	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		if data == "LED_ON":
			digitalWrite(5,1)
			message = "LED_ON Success"
		elif data == "LED_OFF":
			digitalWrite(5,0)
			message = "LED_OFF Success"
		else:
			message = "Command Not Recognized"
		c.send(message.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	Main()