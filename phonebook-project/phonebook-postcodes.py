# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:52:12 2019

@author: ottil
"""

import sqlite3
import json 
import requests

conn = sqlite3.connect('phonebook_postcodes.db') 
# This connects to the database.

c = conn.cursor()
# link your database with cursor.

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS phonebook_postcodes (
            postcode TEXT, 
            longitude REAL, 
            latitude REAL)''')

with open('personal_database_json.js') as f:
    data = json.load(f)

def personal_postcode_data_entry():
    for item in data:
        values_list = list(item.values())
        postcode = values_list[5]
        c.execute('''INSERT INTO phonebook_postcodes (postcode)
                  VALUES(?)''', (postcode,))
        conn.commit()
        
with open('business_database_json.js') as f:
    data = json.load(f)

def business_postcode_data_entry():
    for item in data:
        values_list = list(item.values())
        postcode = values_list[4]
        c.execute('''INSERT INTO phonebook_postcodes (postcode)
                  VALUES(?)''', (postcode,))
        conn.commit()

def convert_postcode():
    response = requests.get("https://api.postcodes.io")
    print(response.status_code)
    

#postcode = requests.get(https://api.postcodes.io/postcodes/:cb1 1eg)

#def postcode_data_entry():
#    c.execute('''SELECT postcode
#              FROM phonebook-business.db INNER JOIN phonebook-personal.db 
#              ON postcode = postcode ''')
#    conn.commit()
    
    
