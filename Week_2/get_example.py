from flask import *
app = Flask(__name__)

@app.route('/login',methods=['GET'])
def login():
    uname=request.args.get('uname')
    passwrd=request.args.get('pass')
    if uname.lower()=='toma' and passwrd=='feminist':
        return "Welcome %s" %uname.capitalize()
    else:
        return "Fuck out of here, imposter."