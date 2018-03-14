#!/usr/bin/python
#show "Hello World on the LCD screen"
# Kinglow

import Adafruit_CharLCD as LCD


lcd = LCD.Adafruit_CharLCDPlate()


displayText = "hello World"

lcd.clear()
lcd.message(displayText)

