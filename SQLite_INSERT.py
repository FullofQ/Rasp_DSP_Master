#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Test.db')

print "Opened database successfully";

c = conn.cursor()

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.commit()
print "Records created successfully";
conn.close()