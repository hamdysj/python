# Write a Python script to print F pattern
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    for j in range(0, i):
        print('*', end='')
    print()