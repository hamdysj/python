#A Function is a set of code that performs some task
#def welcome():
 #   fname = input('Enter your FirstName: ')
# sname = input('Enter your Surname: ')
#    print(f'Welcome {fname}, {sname}')

#welcome()

#Sum
#def sumUp(a, b):
#    print(f'Sum is {a+b}')

#To set default values
#def sumUp(a=0, b=0):

#To set parameters/arguments as list
def sumUp(*a):
    add = 0
    for i in a:
        add = add + i
    print('Sum is', add)

sumUp(50,12,45)

#To return a function
def sumUp(*a):
    add = 0
    for i in a:
        add = add + i
    return add

value = sumUp(1,45,78)
print('Sum is', value)