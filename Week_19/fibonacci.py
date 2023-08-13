#Write a function to print the first 100 fibonacci numbers.

def fib():
    for no in range(3, 101):
        print(no)

def fib_array():
    fib_nums = [0, 1]
    for no in range(3, 101):
        fib_nums.append(fib_nums[-1]+fib_nums[-2])
    print(fib_nums)

fib()
print()
fib_array()
