from flask import *
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname.lower()=='toma' and passwrd=='feminist':
        return "Welcome %s" %uname.capitalize()
    else:
        return "Who the fuck are you?"