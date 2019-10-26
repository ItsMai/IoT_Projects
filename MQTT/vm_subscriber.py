"""EE 250L Lab 04 Starter Code
Mailani Gelles and Emily Kuo
http://github.com/usc-ee250-fall2019/lab04-emily-mailani
Mailani's RPI private IP : '192.168.0.239'
Emily's RPI's private IP : '192.168.1.229'

Run vm_subscriber.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("rpi-mgelles/ultrasonicRanger")
    client.message_callback_add("rpi-mgelles/ultrasonicRanger", ultrasonicRanger)
    client.subscribe("rpi-mgelles/button")
    client.message_callback_add("rpi-mgelles/button", button)

    #subscribe to the ultrasonic ranger topic here

def button(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print(str(message.payload, "utf-8"))



def ultrasonicRanger(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("VM: " + shtr(message.payload, "utf-8") + " cm" )


#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
            

