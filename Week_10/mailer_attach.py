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
# "C:/Users/USER/Pictures/Twitter/20210606_123240.jpg" okqugascpouppsyz
@app.route("/")  
def index():
    receiver = input("Enter the email address of the receiver: ")  
    msg = Message(subject = "Hello", body = "A copy of the slippers design", sender = 'ademonohu@gmail.com', recipients = [receiver])  
    with app.open_resource("C:/Users/USER/Pictures/Twitter/20210606_123240.jpg") as fp:  
        msg.attach("20210606_123240.jpg","image/png",fp.read())  
        mail.send(msg)  
    return "sent"