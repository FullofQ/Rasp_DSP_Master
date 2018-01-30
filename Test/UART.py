#!/usr/bin/env python

__builtins__

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
    x = ser.read(2)
    x_hex = x.encode("hex")
    Slave = x_hex[0:2]
    Program = x_hex[2:5]
    print Slave
    print Program
    time.sleep(1)
    '''
    if x_hex == '':
        print('Nothing')
    else:
        print('Got it')
    '''