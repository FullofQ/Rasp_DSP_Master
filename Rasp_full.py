#!/usr/bin/python2.7

import time
import serial
import urllib2  
import json

def main():
    
    #serial_task
    ser = serial.Serial(
        port='/dev/serial0',
        baudrate = 115200,
        parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
	)
    
    #serial
    x = ser.read(2)
    x_hex = x.encode("hex")
    Slave = x_hex[0:2]
    Program = x_hex[2:5]
    #time.sleep(1)
    
    #JSON
    post_data = {'SLAVE':Slave,'PROGRAM':Program}
    ret = urllib2.urlopen(url='http://120.119.72.53:8080/SQLI/full.php', data=json.dumps(post_data))
    #print "JSON is done"
    print ret.read()
    time.sleep(1)
    
while 1:
    
    main()

    
    
  



