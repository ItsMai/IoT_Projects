# LED Client 
#
# This code runs on yoru VM and sends requests to the Raspberry Pi to turn on 
# and off the Grove LED using TCP packets.
# 
# Team members: Emily Kuo, Mailani Gelles
# Github repository link:

import socket

def Main():
    host = '192.168.1.229'
    port = 9001

    s = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    s.connect((host,port))

    command = input("-> ")
    while True:
        s.send(command.encode('utf-8')) 
        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 
        message = s.recv(1024).decode('utf-8') 
        print("Received from server: " + message)
        command = input("-> ")
    s.close()

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 tcpClient.py` in terminal, this if-statement will be 
true"""
if __name__ == '__main__':
    Main()
