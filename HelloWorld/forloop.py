#Print multiples of a number

#For Loop is used to iterate over a sequence, which could be a list, tuple, array or string


#for i in range(0,39,3): #multiples of 3
#    print(i)

#pattern
#n = int(input('Enter a Number: '))
#for i in range(1,n+1):
#    for j in range(1,i+1):
 #       print(j,end='')
 #   print()

#Matrices
row = 2
col = 2
val = []
x=[]
y = []

for i in range(0, row):
    for j in range(0, col):
        val.insert(j, int(input('Enter %d x %d number: ' %(i,j))))
    x.insert(i,val)
    val=[]
for i in range(0, row):
    for j in range(0, col):
        val.insert(j, int(input('Enter %d x %d number: ' %(i,j))))
    y.insert(i,val)
    val=[]

sum=[]
for i in range(0, row):
    for j in range(0, col):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i,val)
    val=[]

print(x)
print(y)
print(sum)

