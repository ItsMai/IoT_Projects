# Mailani Gelles / Emily Kuo 
import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import my_reddit
import my_weather
import my_app


PORT_BUZZER = 2     # D2
PORT_BUTTON = 4     # D4

LCD_LINE_LEN = 16
potentiometer = 0           #rotary angle sensor to analog port A0

# Setup
grovepi.pinMode(PORT_BUZZER, "OUTPUT")
grovepi.pinMode(PORT_BUTTON, "INPUT")

lcd.setRGB(0, 128, 0)

# Installed Apps!
APPS = [
    my_weather.WEATHER_APP,
    my_reddit.QOTD_APP,
    my_app.CAT_APP
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

while True:
    try:
        turn = grovepi.analogRead(potentiometer)
        if turn > 0 and turn < 205:
            lcd.setRGB(255, 0, 0)        #red
        elif turn > 205 and turn < 410:
            lcd.setRGB(255, 165, 0)      #orange
        elif turn > 410 and turn < 615:
            lcd.setRGB(255, 255, 0)      #yellow
        elif turn > 615 and turn < 820:
            lcd.setRGB(0, 255, 0)        #green
        elif turn > 820 and turn < 1023:
            lcd.setRGB(0, 0, 255)        #cyan
        
        # Check for input
        if grovepi.digitalRead(PORT_BUTTON):
            # BEEP!
            grovepi.digitalWrite(PORT_BUZZER, 1)

            # Switch app
            app = (app + 1) % len(APPS)
            ind = 0

        time.sleep(0.1)

        grovepi.digitalWrite(PORT_BUZZER, 0)

        # Display app name
        lcd.setText_norefresh(APPS[app]['name']) 

        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        ind +=1
        if ind is 16:
            ind = 0


    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        # Turn buzzer off just in case
        grovepi.digitalWrite(PORT_BUZZER, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise
