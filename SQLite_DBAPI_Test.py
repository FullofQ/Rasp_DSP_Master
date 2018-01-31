#!/usr/bin/python2.7

import sqlite3
import time
import serial

def update_task(conn,task):
    sql = 'UPDATE Master_A SET SLAVE = ?,PROGRAM = ? WHERE ID = ?'
    cur = conn.cursor()
    cur.execute(sql, task)


def create_connection(target_database):
    
    try:
        conn = sqlite3.connect(target_database)
        return conn
    except Error as e:
        print(e)
    return None

def main():
    database = "/home/pi/Desktop/Rasp_DSP_Master/Monitor.db"
    conn = create_connection(database)
    
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
    time.sleep(1)
    
    #update_task
    with conn:
        update_task(conn, (Slave,Program,1))
    
    #display
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM Master_A'):
        print row
        time.sleep(1)
    
while 1:
    main()

    
    
  

