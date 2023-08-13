from flask import *
app = Flask(__name__)
app.secret_key = 'bcghgbuikool'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def validate():
    if request.method == 'POST':
        if request.form['email']=='':
            flash('Please log in first')
            return redirect(url_for('home')) 

        if request.form['pass']=='':
            flash('Please enter your password')
            return redirect(url_for('home')) 

        if request.form['pass']=='jomape':
            flash('Log in succesful.')
            return render_template('success.html', name=request.form['email'])

        else:
            trial = 0; max_trials =5
            while trial < max_trials:
                trial += 1
                flash('Incorrect details provided. Please try again.')
                print(trial)
                return render_template('login.html')
            else:
                abort(Response('Maximum number of trials exceeded.'))
                