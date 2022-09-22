from flask import *  
app = Flask(__name__)
@app.route('/')  
def message():  
      return render_template('message.html')  

@app.route('/user/<uname>')
def personal_greeting(uname):
      return render_template('name.html', name=uname)

@app.route('/timestable/<int:num>')
def timestable(num):
      return render_template('timestable.html', n=num)

@app.route('/styled')
def styled_greeting():
      return render_template('styled_message.html')

if __name__ == '__main__':  
   app.run(debug = True)  