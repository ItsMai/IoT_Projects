"""EE 250L 
Mailani Gelles and Emily Kuo
Mailani's RPI private IP : '192.168.0.239'
Emily's RPI's private IP : '192.168.1.229'
Run vm_publisher.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time
from pynput import keyboard



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print(message.payload + "      			 ")

def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    	
    if k == 'w':
        print("w")
        client.publish("rpi-mgelles/lcd", "w")
        #send "w" character to rpi
    elif k == 'a':
        print("a")
        client.publish("rpi-mgelles/led", "LED_ON")
        client.publish("rpi-mgelles/lcd", "a")
        # send "a" character to rpi
        #send "LED_ON"
    elif k == 's':
        print("s")
        client.publish("rpi-mgelles/lcd", "s")
        # send "s" character to rpi
    elif k == 'd':
        print("d")
        client.publish("rpi-mgelles/led", "LED_OFF")
        # send "d" character to rpi
        client.publish("rpi-mgelles/lcd", "d")
        # send "LED_OFF"

if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread

    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
