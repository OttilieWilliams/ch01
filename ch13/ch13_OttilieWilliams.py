# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:11:59 2018

@author: ottil
"""

class Person:
    def greetingAgeBased(self):
        if self.age < 18:
            print("Welcome, young ", self.name)
        elif self.age > 60:
            print("Welcome, venerable ", self.name)
        else:
            self.greetingFormal()

class Wizard(Person):
    def greetingFormal(self):
        print("Welcome, Mr ", self.name, end=" ")
        print("- you're a fine wizard!")
        