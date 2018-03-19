#!/usr/bin/python
#show "Hello World on the LCD screen"
# Kinglow

import Adafruit_CharLCD as LCD
import time
import subprocess

lcd = LCD.Adafruit_CharLCDPlate()
IP = subprocess.check_output(['hostname', '-I'])
Name = subprocess.check_output(['hostname']).strip()

displaytext1 = Name
displaytext = "hello World"

lcd.clear()
lcd.message(displaytext)

refresh = True
wrefresh = True
while (True):
        if lcd.is_pressed(LCD.SELECT):
            if wrefresh:
                lcd.clear()
                lcd.set_backlight(1)
                lcd.message(displaytext)
                refresh = True
                wrefresh = False
        else:
            if refresh:
                lcd.clear()
                lcd.set_backlight(1)
                lcd.message(IP)
                lcd.message(Name)
                refresh = False
                wrefresh = True
            time.sleep(0.5)

