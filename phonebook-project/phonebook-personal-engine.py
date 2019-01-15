# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 13:51:24 2019

@author: ottil
"""

import sqlite3
import json 

conn = sqlite3.connect('phonebook_personal.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook_personal (first_name TEXT, last_name TEXT, addressline1 TEXT, addressline2 TEXT, addressline3 TEXT, postcode TEXT, country TEXT, telephone_number REAL)')

with open('personal_database_json.js') as f:
    data = json.load(f)

def personal_data_entry():
    for item in data:
        values_list = list(item.values())
        c.execute('''INSERT INTO phonebook_personal (first_name, last_name, addressline1, addressline2, addressline3, postcode, country, telephone_number)
                  VALUES(?,?,?,?,?,?,?,?)''', (values_list))
        conn.commit()

def find_data_for_last_names_and_location():
    last_name = input('Please search by last name: ')
    addressline2 = input('Please enter their city, town, or village: ')
    
    c.execute('SELECT * FROM phonebook_personal WHERE last_name = ? and addressline2 = ? ', (last_name.title(), addressline2.title(),))

    results = c.fetchall()
    if results: # (means == true)
        print(len(results), 'result found.')
        for row in results:
            print(row[0], row[1] + '\n' + row[2] + '\n' + row[3] + '\n' + row[5] + '\n' + row[6])
    else:
        print('Person not found.')
    

find_data_for_last_names_and_location()

c.close()
conn.close()


    