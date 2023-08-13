"""
The test was to understand how to use redirect(url_for). 
Also to make me understand the difference between how 
URL rules, view functions and endpoints, and how they 
work.
"""

from flask import *

app = Flask(__name__)

@app.route('/first') #first is the URL rule
def admin(): # admin is the view function here
    return 'The admin'

@app.route('/second')
def librarion():
    return 'The librarion'

@app.route('/third')
def student():
    return 'The student'

@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))
    elif name == 'librarion':
        return redirect(url_for('librarion')) 
    elif name == 'student':  
        return redirect(url_for('student')) 
    else:
        return 'Wrong input'

# Using endpoint
def show_user(username):
    return f'Hello {username.capitalize()} !'

app.add_url_rule('/trial/<username>', 'reveal_user', show_user)
#/trial/<username> = URL rule, reveal_user = endpoint, show_user = view function