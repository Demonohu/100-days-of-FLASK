from flask_wtf import Form  
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError  

class ContactForm(Form):  
   name = StringField("Candidate Name ",[validators.InputRequired ("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])  
   Address = TextAreaField("Address")  
     
   email = StringField("Email",[validators.InputRequired ("Please enter your email address."),  
   validators.Email("Please enter your email address.")])  
     
   Age = IntegerField("Age")  
   language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')])  
  
   submit = SubmitField("Submit")  