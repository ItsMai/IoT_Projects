# Ultrasonic Sensor Client
# 
# This code runs on the Raspberry Pi. It should sit in a loop which reads from
# the Grove Ultrasonic Ranger and sends the reading to the Ultrasonic Sensor 
# Server running on your VM via UDP packets. 
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
    # Change the host and port as needed. For ports, use a number in the 10000s
    # range. 
    host = '192.168.1.229' #RPi's IP address
    port = 10000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    # UDP is connectionless, so a client does not formally connect to a server
    # before sending a message.
    #emily 
    server_addr = '192.168.0.176' #OS's IP address
    #mailani: server_addr = '192.168.0.239'
    dst_port = 9000
    server = (server_addr, dst_port)
    dist = 0
    ranger = 4
    
    while True:
        time.sleep(0.2)

        dist = ultrasonicRead(ranger)
        message = str(dist)
        print("RPi: " + message + " cm")

        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(message.encode('utf-8'), server)

if __name__ == '__main__':
    Main()
