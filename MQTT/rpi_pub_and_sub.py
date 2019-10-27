"""EE 250L 
Mailani Gelles and Emily Kuo
Mailani's RPI private IP : '192.168.0.239'
Emily's RPI's private IP : '192.168.1.229'
Run rpi_pub_and_sub.py on your Raspberry Pi."""
import sys
sys.path.append('../../Software/Python/')
sys.path.append('../../Software/Python/grove_rgb_lcd')

import paho.mqtt.client as mqtt
import time
from grovepi import*
from grove_rgb_lcd import*

ultrasonic_ranger = 3       #range finder on d3
distant = 0
led = 4                     #led attached to port D4
button = 7
pinMode(button, "INPUT")

def led_output(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message
    if str(message.payload, "utf-8") == "LED_OFF":
        digitalWrite(led,0)
    elif str(message.payload, "utf-8") == "LED_ON":
        digitalWrite(led,1)

def lcd(client, userdata, message):
    x = (str(message.payload, "utf-8") )

    setText_norefresh(x)

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("rpi-mgelles/led")
    client.message_callback_add("rpi-mgelles/led", led_output)
    client.subscribe("rpi-mgelles/lcd")
    client.message_callback_add("rpi-mgelles/lcd", lcd)



    #subscribe to topics of interest here

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
    print("on_message: msg.payload is of type " + str(type(msg.payload)))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        distance = ultrasonicRead(ultrasonic_ranger)
        time.sleep(1)
        if (digitalRead(button)) == 1:
            client.publish("rpi-mgelles/button", "Button pressed!")
        client.publish("rpi-mgelles/ultrasonicRanger", distance)
