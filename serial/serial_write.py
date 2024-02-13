#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
        port='/dev/ttyACM0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
        )

counter = 0

while 1:
    write_string  = "Write Counter: {} \n".format(counter)
    ser.write(str.encode(write_string))
    time.sleep(1)
    counter += 1
