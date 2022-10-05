#Print multiples of a number
#for i in range(0,39,3): #multiples of 3
#    print(i)

#pattern
n = int(input('Enter a Number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()