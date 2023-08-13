#Write a function to print the first 100 fibonacci numbers.


from flask import Flask
app = Flask(__name__)

@app.route('/')
def fib():
    fib_nums = [0, 1]
    for no in range(3, 101):
        fib_nums.append(fib_nums[-1]+fib_nums[-2])

    fib_nums = dict(enumerate(fib_nums, 1))
    
    return fib_nums