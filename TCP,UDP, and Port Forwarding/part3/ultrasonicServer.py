# Ultrasonic Sensor Server
#
# This code runs on your VM and receives a stream of packets holding ultrasonic
# sensor data and prints it to stdout. Use a UDP socket here.
# 
# Team members: Emily Kuo, Mailani Gelles
# Github repository link:
# https://github.com/usc-ee250-fall2019/lab03-emily-mailani.git

import socket

def Main():
    # Change the host and port as needed. For ports, use a number in the 10000s
    # range. 
    #emily: host = '172.16.10.137' #VM's IP address
    #mailani:
    host = '192.168.0.239'
    port = 9000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Ultrasonic Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        #print("Data From: " + str(addr))
        print("VM: " + data + " cm")
    c.close()

if __name__ == '__main__':
    Main()