value = 0
for num in range(0,1000):
    if num % 3 == 0 or num % 5 == 0:
        value += num

print('Multiples of 3 or 5 below 1000 =', value)