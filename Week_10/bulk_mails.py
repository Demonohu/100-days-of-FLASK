from flask import *
from flask_mail import *
import os

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

receivers = {}
no_receivers = int(input('\nHow many people are getting a mail? '))
print('Fill in the receivers details.')
for i in range(no_receivers):
    receiver_name = input('\nName: ')
    receiver_addy = input('Email address: ')
    receivers[receiver_name] = receiver_addy

@app.route('/')
def index():
    with mail.connect() as con:  
        for receiver in receivers:
            message = "Hello %s" %receiver 
            msgs = Message(recipients=[receivers[receiver]], body = str(message), subject = "Hello from the other side!", sender = 'ademonohu@gmail.com')
            con.send(msgs)  
    return "Sent" 
