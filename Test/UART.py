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
    #str_x = __builtins__.str(x)
    x_hex = x.encode("hex")
    print x_hex
    #int_x = __builtins__.int(str_x)
    time.sleep(1)
    if x_hex == '':
        print('Nothing')
    else:
        print('Got it')