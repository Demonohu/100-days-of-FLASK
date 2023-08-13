from flask import *
from flask_mail import *
import os

app = Flask(__name__)
mail = Mail(app) #Instantiate Mail class

#Flask mail configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')  
def index():  
    msg = Message('Hello!', sender = 'ademonohu@gmail.com', recipients=['folasayoayoakwe@gmail.com'])  
    msg.body = 'Hi, this mail was sent by using the flask web application.'
    mail.send(msg)
    return "Sent"

   