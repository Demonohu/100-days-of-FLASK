from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
