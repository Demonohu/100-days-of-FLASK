# Day 1: Bolu or Odun
# Task:
# Write a function that takes in a string of one word without any spaces or special character.
# If the string contains any special character, print "Please remove all spaces or special characters".
# If the string passed to the function is either Bolu or Odun, print "Welcome back, Bolu" or
# "Welcome back, Odun". If the string passed is none of the two, print "It is nice to meet you," 
# concatenated with the string passed.

import re
from flask import Flask
app=Flask(__name__)

def user_name():
    user_name=input('What is your name, bae? ')
    return user_name.lower()

def is_valid(user_name):
    if re.search("[^a-z]",str(user_name)):
        is_valid = False
    else:
        is_valid= True
    return is_valid


user = user_name()
is_valid(user_name)


@app.route('/')
def index():
    if is_valid(user):
        
        if user == 'bolu' or user== 'odun':
            return '<h2>Welcome back, '+ '\t' + user.capitalize()
        else:
            return '<h2>It is nice to meet you, '+ '\t' + user.capitalize()

    else:
        return '<h2>Please remove all spaces or special characters'