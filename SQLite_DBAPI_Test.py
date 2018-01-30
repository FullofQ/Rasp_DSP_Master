#!/usr/bin/python2.7

import sqlite3
import time

def update_task(conn,task):
    
    sql = 'UPDATE Test SET SLAVE = ?,PROGRAM = ? WHERE ID = ?'
    
    cur = conn.cursor()
    cur.execute(sql, task)

def create_connection(Monitor):
    
    try:
        conn = sqlite3.connect('Monitor.db')
        return conn
    except Error as e:
        print(e)
    return None

def main():
    database = "/home/pi/Desktop/Rasp_DSP_Master/Monitor.db"
    
    conn = create_connection(database)
    with conn:
        update_task(conn, ('0a','99',1))
        
    #display table
    cur = conn.cursor()
    for row in cur.execute('SELECT * FROM Test'):
        print row
        time.sleep(1)
    
    conn.close()
    
    
main()

'''
conn = sqlite3.connect('Monitor.db')

print "Opened database successfully";

c = conn.cursor()

data = [(10,'0a','01'),
        (11,'0a','02'),
        (12,'0a','03')]

a_data = [(1,'0a','01')]

c.executemany('INSERT INTO Test VALUES(?,?,?)', data)

conn.commit()
print "Records created successfully";

for row in c.execute('SELECT * FROM Test'):
    print row
    time.sleep(1)
    
conn.close()
'''