# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:29:33 2019

@author: ottil
"""

from flask import Flask, render_template, request
# Importing flask

app = Flask("MyApp")
# Creating a flask object called app. Passing it one parameter,
# "my app"

@app.route("/")
# This is a decorator (python syntax). Syntactic sugar.
# By putting it above the function, passing the function below through the URL. 
    
def hello():
    return "Hello World"

# You can put HTML in the return function. 
    
@app.route("/<name>") # name is a variable
#whatever you pass in after the / becomes a variable called name.

def hello_someone(name):
    return render_template("hello.html")

@app.route("/lastname/<lastname>") 

def goodbye(lastname):
    return render_template("goodbye.html", lastname = lastname)

@app.route("/howareyou/<status>") 

def howAreYou(status):
    return render_template("howareyou.html", status = status)


app.run(debug=True)
# Calling run on the app object.

# To make the HTML easier to read, set variables equal to the HTML. 