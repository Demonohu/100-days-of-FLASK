# Write and deploy a script to any hosting service of your choice. 
# It must have the following end points. “/port” when this is 
# accessed, a string response of “The script is running on [port]”,
#  with the appropriate response header must be sent. If the 
#  endpoint accessed is “/fibonacci” is accessed, an array of 
#  the first 100 fibonacci numbers is sent as a string response.

from flask import Flask, request
app = Flask(__name__)

@app.route('/home')
def home():
    port = request.endpoint
    return f'<h1>This script is running on {port}</h1>'

@app.route('/fibonacci')
def fib():
    fib_nums = [0, 1]
    for no in range(3, 101):
        fib_nums.append(fib_nums[-1]+fib_nums[-2])
    
    return fib_nums
    