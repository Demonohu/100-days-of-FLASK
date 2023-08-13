# Without using a database, retrieve user data for only 
# “id”, “name”, “Username”, “email” from the api below and 
# store it on your server it must be persistent.
# Create an api such that when the "/users" endpoint is accessed,
#  an array containing all the user objects is the response.
# When the route with the name of any of the object keys in the 
# array of objects is accessed, like "/name" or "/username" or 
# "/email" is accessed, respond with an array of all the 
# corresponding properties of the array of user objects.
# When the route “/delete” is accessed, the last object in the array is deleted.
# When the route “/deleteall” is accessed, let all the objects in the array be deleted
# A new user object can be added to the array via post request on the route “/newuser”. The expected data is 
# {
#     "name": "name",
#     "username": "username",
#     "email": "email"
# }
# The id would be automatically generated.

from flask import *
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newuser')
def add_user():
    return render_template('add.html')

@app.route('/saveuser', methods=['GET', 'POST'])
def save_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        id = len(session.get('users', [])) + 1

        user_data = {
            'id': id,
            'name': name,
            'email': email,
            'username': username
        }

        users = session.get('users', [])
        users.append(user_data)

        session['users'] = users

        return render_template('success.html')

    else:
        return 'An error has been encountered somewhere.<br><a href="/">Go to home</a>'

@app.route('/usersdb')
def view_usersdb():
    users = session.get('users', None)
    if users:
        return render_template('users.html', users=users)
    else:
        return 'No input yet. <br><a href="/">Go to home</a>'

@app.route('/users')
def view_users():
    users = session.get('users', None)
    if users:
        return str(users) + '<br><a href="/">Go to home</a>'
    else:
        return 'No input yet. <br><a href="/">Go to home</a>'

@app.route('/name')
def view_names():
    names = []
    users = session.get('users', None)
    if users:
        for user in users:
            for data in user:
                if data == 'name':
                    names.append(user[data])
        return str(names) + '<br><a href="/">Go to home</a>'
    else:
        return 'No input yet. <br><a href="/">Go to home</a>'

@app.route('/username')
def view_usernames():
    usernames = []
    users = session.get('users', None)
    if users:
        for user in users:
            for data in user:
                if data == 'username':
                    usernames.append(user[data])
        return str(usernames) + '<br><a href="/">Go to home</a>'
    else:
        return 'No input yet. <br><a href="/">Go to home</a>'

@app.route('/email')
def view_emails():
    emails = []
    users = session.get('users', None)
    if users:
        for user in users:
            for data in user:
                if data == 'email':
                    emails.append(user[data])
        return str(emails) + '<br><a href="/">Go to home</a>'
    else:
        return 'No input yet. <br><a href="/">Go to home</a>'

@app.route('/delete')
def delete_user():
    users = session.get('users')
    users.pop()
    session['users'] = users
    return '<h3>Last user deleted.</h3>  <br><a href="/">Go to home</a>'

@app.route('/deleteall')
def delete_users():
    session.pop('users', None)
    return '<h3>All users have been deleted.</h3>  <br><a href="/">Go to home</a>'
