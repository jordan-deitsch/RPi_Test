#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import time
import csv

class GpioMonitor:
    def __init__(self, pinNumber, eventName, eventOptions):
        self.eventName = eventName
        self.eventOptions = eventOptions
        self.eventDict = {'Timestamp':"NULL",
                          'Event': eventName,
                          'Value': eventOptions[0]}

        # Set GPIO pin as input and get initial value
        GPIO.setup(pinNumber, GPIO.IN)
        self.pinNumber = pinNumber
        self.eventValue = GPIO.input(self.pinNumber)
        time.sleep(.1)



    def CheckPin(self):
        value = GPIO.input(self.pinNumber)
        time.sleep(.1)

        if(value != self.eventValue):
            self.eventValue = value
            self.eventDict['Timestamp'] = datetime.datetime.now()
            self.eventDict['Value'] = self.eventOptions[value]
            return 1
            
        return 0
			
		

pinButton = 22

# Setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ButtonMonitor = GpioMonitor(pinButton, "Button Event", 
                            {0: "Press", 1:"Release"})

with open('event_log.csv', 'w', newline='') as csvfile:
    fieldnames = ['Timestamp', 'Event', 'Value']
    dWriter = csv.DictWriter(csvfile, fieldnames=fieldnames,
                             restval='0', extrasaction='raise')

    dWriter.writeheader()
    eventDict = {'Timestamp': 'NULL', 'Event':'NULL', 'Value':"NULL"}
    
    t0 = datetime.datetime.now()
    endTime = 10
    Run = True
    
    while (Run == True):

        if(ButtonMonitor.CheckPin() == 1):
            try:
                print(ButtonMonitor.eventDict)
                dWriter.writerow(ButtonMonitor.eventDict)
            except ValueError:
                print("Invalid dictionary write")
            except:
                print("Unknown error")
                quit()
            finally:
                pass

        t1 = datetime.datetime.now()
        if((t1 - t0).seconds > endTime):
            Run = False	

GPIO.cleanup()
