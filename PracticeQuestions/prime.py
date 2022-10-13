def is_prime(value):
    if value%3 == 0:
        return '%d is a prime number' % value
    else:
        return '%d is not prime number' % value


num = int(input('Enter a number: '))
print(is_prime(num))
