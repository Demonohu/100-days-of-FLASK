# Day 1: Bolu or Odun
# Task:
# Write a function that takes in a string of one word without any spaces or special character.
# If the string contains any special character, print "Please remove all spaces or special characters".
# If the string passed to the function is either Bolu or Odun, print "Welcome back, Bolu" or
# "Welcome back, Odun". If the string passed is none of the two, print "It is nice to meet you," 
# concatenated with the string passed.

import re

def get_user_name():
    user_name=input('What is your name, bae? ')
    return user_name.lower()

def check_validity(user_name):
    if re.search("[^a-z]",str(user_name)):
        is_valid = False
    else:
        is_valid= True
    return is_valid

def comp_response(user_name, is_valid):
    if is_valid:
        if user_name == 'bolu' or user_name== 'odun':
            print('Welcome back,', user_name.capitalize())
        else:
            print('It is nice to meet you,', user_name.capitalize())

    else:
        print('Please remove all spaces or special characters')

def main():
    user_name = get_user_name()
    is_valid = check_validity(user_name)
    comp_response(user_name, is_valid)

main()
