# Write a function that takes in 2 strings. The first one is 
# the email address, the second one is the password and 
# returns an object specified below.
# Verify that the email adress is valid. If valid, create an object 
# with property 'email' and assign true, else assign as false. For 
# the password verify that it has at least one uppercase letter, at
# least one lowercase letter, at least one non-alphanumeric character, 
# at least one number and at least 8 character long. If the password 
# is valid, let the object have property 'password' assigned to true else, false

import re

def user_data():
    email = input("Enter your email address ")
    password = input("Enter your password: ")
    return email, password

class EmailValidator:
    def __init__(self, addy):
        self.addy = addy

    def is_valid(self):
        email = {}
        # Regular expression to match a valid email address format
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the pattern
        if re.match(email_pattern, self.addy):
            email['email'] = True
        else:
            email['email'] = False

        return email

class PasswordValidator:
    def __init__(self, pword):
        self.pword = pword

    def is_valid(self):
        password={}
        # Regular expressions for password validation
        uppercase_pattern = r'[A-Z]'
        lowercase_pattern = r'[a-z]'
        alphanumeric_pattern = r'[a-zA-Z0-9]'
        number_pattern = r'[0-9]'

        # Check if the password meets all requirements
        if len(self.pword) >= 8 and \
           re.search(uppercase_pattern, self.pword) and \
           re.search(lowercase_pattern, self.pword) and \
           re.search(alphanumeric_pattern, self.pword) and \
            re.search(number_pattern, self.pword):
            password["password"]= True
        else:
            password["password"]= False

        return password 


def main():
    email, password = user_data()
    email_validator = EmailValidator(email)
    password_validator = PasswordValidator(password)

    print(email_validator.is_valid())
    print(password_validator.is_valid())

main()
