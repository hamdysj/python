#List: Is a collection of data, it can hold values of multiple data types. it is a mutable (Can undergo changes) heterogenous python objects
x = [1, 2, "name","level", "get"]
x2 = ['a','b',45,'Hello','there']
x3 = x+x2
#print(x[2], x[-1], x[:3])
#print(x2[1:3]) #return b 45
#print(x2[3:5]) #return Hello there
#print(x2[3:5]) #return Hello there

#print(x3)
#print(x3[::3]) #returns the value in next 3 index
#print(x[::-1])#returns the values in reverse order
#print(x3[1:7:2])

#var = list("Furious")
#print(var)

#first, *second = x
#print(first)
#print(second)

#x4=['a']*4
#print(x4)

#x.append('NewValue') #add a single element
#print(x)

#x.extend(x3) #add an entire list
#print(x)

x.insert(2, 3) #to add value to a list
x.remove('get') #to remove a value form the list
print(x)







#Tuple: is an immutable heterogenous python objects