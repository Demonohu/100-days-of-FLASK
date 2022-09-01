from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "You are welcome."


@app.route('/<name>')
def individual(name):
    return "Hi, " + name


@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent