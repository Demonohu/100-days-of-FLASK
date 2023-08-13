from flask import *
app = Flask(__name__)

@app.route('/index')  
def home():  
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None;  
    if request.method == "POST":  
        if request.form['pass'] != 'jtp':  
            error = "invalid password"  
        else:  
            flash("you are successfuly logged in")  
            return redirect(url_for('home'))  
    return render_template('login.html',error=error)