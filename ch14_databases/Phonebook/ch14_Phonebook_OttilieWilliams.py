# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 09:29:00 2019

@author: ottil
"""

import sqlite3

conn = sqlite3.connect('phonebook.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook (firstname TEXT, lastname TEXT, addressline1 TEXT, city TEXT, postcode TEXT, telephoneno REAL, businesscategory TEXT, xcoordinate REAL, ycoordinate REAL)')

# CREATE TABLE IF NOT EXISTS - to create and 
# check table table existence. SQL language rather than python

# stuffToBuild - database table name.
# unix, datestamp, keword, value - column names
# REAl and TEXT - the data types and format in each column
    
# Put the SQL language in caps and the table and column names in 
# lower case - makes it easier to distinguish. 
    
def data_entry():
    c.execute("INSERT INTO phonebook VALUES('Harriet', 'Williams', 'BT Head Office', 'London', 'LN1 123', 0123456789, 'Tech', 0, 0)")
    conn.commit() # similar to git, commit after inserting values
    c.close() # close the table 
    conn.close() # close the connection to the database

create_table()
data_entry()

## function to insert data
#def dynamic_data_entry():
#    unix = time.time()
#    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#    keyword = 'Python'
#    value = random.randrange(0,10)
#    c.execute('INSERT INTO stuffToBuild(unix,datestamp, keyword, value) VALUES (?, ?, ?, ?)', (unix, date, keyword, value))
#    conn.commit()
#    
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#    # this generates time since the unix system start.
#    # You don't usually need this.
##c.close()
##conn.close()
#
#
##def read_from_db_all():
##    c.execute('SELECT * FROM stuffToBuild WHERE value =8')
##    for row in c.fetchall():
##        print(row)
#        
## fetchall() is similar to pull in Git. 
#    
#def read_from_db_all():
#    c.execute('SELECT * FROM stuffToBuild WHERE value =8')
#    for row in c.fetchall():
#        print(row)
#        
#def read_from_db2():
#    x = []
#    c.execute('SELECT * FROM stuffToBuild WHERE value =8 and unix >14223322 and unix < 1547032684 ')
#    for row in c.fetchall():
#        x.append(row[0])
#        print(row[0])
#    print(x)
#        
#        
#read_from_db2()
#
#c.close()
#conn.close()

    