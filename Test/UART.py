#!/usr/bin/env python

import serial
import time

ser = serial.Serial(
    port='/dev/serial0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )
counter = 0
 
while 1:
    x=ser.read(100)
    #print x
    time.sleep(0.5)
    alarm = __builtins__.str(x)
    print alarm
    if x == '':
        print('Nothing')
    else:
        print('Got it')