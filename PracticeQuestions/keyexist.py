# Write a Python script to check whether a given key already exists in a dictionary
value = int(input('Enter a key: '))
numbers = {
    1: "Name",
    2: "Age",
    3: "Job"
}
if value in numbers.keys():
    print('Key %d already exist' % value)
else:
    print('Key %d doesn\'t exist' % value)
