from flask import *
app = Flask(__name__)
app.secret_key = 'girll'

@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")  
    session['response']='session#1'  
    return res 

@app.route('/get')
def get_variable():
    s = session.get('response')
    if s:
        return render_template('get_session.html',name = s) 