#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pinLED = 17
pinButton = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pinLED, GPIO.OUT)	# LED output
GPIO.setup(pinButton, GPIO.IN)	# Button input


currentState = GPIO.input(pinButton)
prevState = GPIO.input(pinButton)

while True:
    if(GPIO.input(pinButton)) == 1:
        currentState = 1
    else:
        currentState = 0

    if((currentState != prevState) and (currentState == 0)):
        print("Button Pressed")
        GPIO.output(pinLED, GPIO.HIGH)
        time.sleep(.1)
    elif((currentState != prevState) and (currentState == 1)):
        print("Button Released")
        GPIO.output(pinLED, GPIO.LOW)
        time.sleep(.1)

    prevState = currentState

GPIO.cleanup()
