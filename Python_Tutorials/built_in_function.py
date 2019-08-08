"""
some built-in functions
max() : It takes any number of arguments and return largest one.

min() : It takes any number of arguments and return smallest one.

abs() : It returns the absolute value of the number, that number's distance from 0.
It always return a positive value and it only takes a single number.

type() : It returns the type of data it received as arguments.
"""

def largest_num(*args):                  # * is use for multiple argument
    print(max(args))
    return(max(args))

x = largest_num(-20, -10, 0, 10, 20)


def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 20)

def abs_func(a):
    print(abs(a))

abs_func(-20)
abs_func(10)


print(type(99))
print(type(99.9))
print(type("99.9"))

l = [1, 2, 3, 4]
print(type(l))
