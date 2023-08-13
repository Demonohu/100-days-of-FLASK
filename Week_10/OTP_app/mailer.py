from flask import *
from flask_mail import *
from random import *
import os

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)

otp = randint(000000,999999)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    email = request.form["email"]  
    msg = Message('OTP',sender = 'ademonohu@gmail.com', recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')

@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if int(user_otp) == otp:  
        return "<h3>Email verified successfully</h3>"  
    else:
        return "<h3>failure</h3>"
