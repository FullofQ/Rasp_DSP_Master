#!/usr/bin/python2.7

import sqlite3
import time

conn = sqlite3.connect('Test.db')

print "Opened database successfully";

c = conn.cursor()
'''
name = 'Eating'
c.execute("SELECT * FROM COMANY WHERE NAME= '%s' " % name);
'''

t = ('Paul',)
c.execute('SELECT * FROM COMANY WHERE NAME=?', t)
print c.fetchone

data = [(2,'Eating',21,'Taiwan',50000),
        (3,'Yi-Ting',15,'UK',100000),
        (4,'QQ',56,'USA',20000)]

c.executemany('INSERT INTO COMANY VALUES(?,?,?,?,?)', data)

conn.commit()
print "Records created successfully";

for row in c.execute('SELECT * FROM COMANY'):
    print row
    time.sleep(1)
    
conn.close()