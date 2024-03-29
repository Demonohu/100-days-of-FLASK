# Write a function that takes in 2 integer parameters. 
# The first parameter, Y, represents a year, while the second
# parameter, N, is the number of leap years after Y. Write a
# function that prints an array of the first N leap years after Y.

def get_years():
    year = int(input("Enter a year: "))
    no_of_leap_years = int(input("How many leap years do you want? "))
    return year, no_of_leap_years

def calc_leap_years(year, no_of_leap_years):
    leap_years = []

    if year % 4 == 0:
        for i in range(no_of_leap_years):
            year += 4
            leap_years.append(year)
        return leap_years
    
    else:
        for i in [1, 2, 3]:
            if (year + i) % 4 == 0:
                year += i
                leap_years.append(year)
        for i in range(no_of_leap_years-1):
            year += 4
            leap_years.append(year)
        return leap_years

def print_leap_years():
    year, no_of_leap_years = get_years()
    print(calc_leap_years(year, no_of_leap_years))

print_leap_years()
