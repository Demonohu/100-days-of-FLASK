from flask import *
app = Flask(__name__)
app.secret_key = 'girll'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/success',methods = ["POST"])  
# def success():  
#     if request.method == "POST":  
#         session['email']=request.form['email']  
#     return render_template('success.html') 
@app.route('/success', methods=['POST'])
def success():
    session['email']=request.form['email']  
    return render_template('success.html')

@app.route('/logout')
def logout():
    addy = session.get('email')
    if addy:
        session.pop('addy',None)  
        return render_template('logout.html');   
    else:  
        return '<p>User not logged in</p>' 

@app.route('/profile')
def view_profile():
    addy = session.get('email')
    if addy:
        return render_template('profile.html',name=addy)
    else:
        return '<p>Please login first</p>'