# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:29:00 2019

@author: ottil
"""

import sqlite3

# TASK 1: CREATE TABLE AND INSERT DATA

conn = sqlite3.connect('task1.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToBuild (unix REAL , datestame TEXT, keyword TEXT, value REAL)')

# CREATE TABLE IF NOT EXISTS - to create and 
# check table table existence. SQL language rather than python

# stuffToBuild - database table name.
# unix, datestamp, keword, value - column names
# REAl and TEXT - the data types and format in each column
    
# Put the SQL language in caps and the table and column names in 
# lower case - makes it easier to distinguish. 
    
def data_entry():
    c.execute("INSERT INTO stuffToBuild VALUES(14223322, '2018-01-01', 'python', 5)")
    conn.commit()
    c.close()
    conn.close()

# similar to git, after inserting values you need to run 
# the commit command. 
    
create_table()
data_entry()
    