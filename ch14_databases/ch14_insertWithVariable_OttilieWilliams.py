# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:29:00 2019

@author: ottil
"""

import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('task1.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild (unix REAL , datestamp TEXT, keyword TEXT, value REAL)')

# CREATE TABLE IF NOT EXISTS - to create and 
# check table table existence. SQL language rather than python

# stuffToBuild - database table name.
# unix, datestamp, keword, value - column names
# REAl and TEXT - the data types and format in each column
    
# Put the SQL language in caps and the table and column names in 
# lower case - makes it easier to distinguish. 
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(14223322, '2018-01-01', 'python', 5)")
    conn.commit() # similar to git, commit after inserting values
    c.close() # close the table 
    conn.close() # close the connection to the database

#create_table()
#data_entry()

# TASK 2: INSERT DATA AUTOMATICALLY WITH VARIABLES

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute('INSERT INTO stuffToBuild(unix,datestamp, keyword, value) VALUES (?, ?, ?, ?)', (unix, date, keyword, value))
    conn.commit()
    
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
    # this generates time since the unix system start.
    # You don't usually need this.
#c.close()
#conn.close()

#TASK 3: READ/SELECT FROM DATABASE

#def read_from_db_all():
#    c.execute('SELECT * FROM stuffToBuild WHERE value =8')
#    for row in c.fetchall():
#        print(row)
        
# fetchall() is similar to pull in Git. 
    
def read_from_db_all():
    c.execute('SELECT * FROM stuffToBuild WHERE value =8')
    for row in c.fetchall():
        print(row)

# Task 3 extended
        
def read_from_db2():
    x = []
    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix >14223322 and unix < 1547032684 ')
    for row in c.fetchall():
        x.append(row[0])
        print(row[0])
    print(x)
        
read_from_db_all()    
#read_from_db2()

c.close()
conn.close()

    