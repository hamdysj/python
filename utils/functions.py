# A Function is a set of code that performs some task
# def welcome():
#   fname = input('Enter your FirstName: ')
# sname = input('Enter your Surname: ')
#    print(f'Welcome {fname}, {sname}')

# welcome()

# Sum
# def sumUp(a, b):
#    print(f'Sum is {a+b}')

# To set default values
# def sumUp(a=0, b=0):

# To set parameters/arguments as list
def sumUp(*a):
    add = 0
    for i in a:
        add = add + i
    return ('Sum is', add)


sumUp(50, 12, 45)


# To return a function
def sumUp(*a):
    add = 0
    for i in a:
        add = add + i
    return add


value = sumUp(1, 45, 78)


# print('Sum is', value)


# To define a function with unknown anumber of arguments
def auto(*args):
    result = []
    for i in args:
        result.append(i)
    return (result)


# auto(2,4,5,'eagle')

def auto_n(*args, **kwargs):
    for i in kwargs.items():
        return (i)


auto_n(a=2, b=4, c=5)


# Nested Function Example
def func1(value):
    return 'First Function to be called'

    def func2():
        return ('Second Function to be called')
        value()

    return func2


@func1  # Decorator - This means that I am calling func3() from func1. i.e func1(func3)- using func3 as an object
def func3():
    return "Third function to be called"

# func3()
