#To return the value in a variable, use [startAtIndex:endIndex] --- eg.[0:3]
course = 'Python for Beginners'
print(course[0])
print(course[4:9])
print(course[-3]) #returns 3rd character from the end
print(course[2:]) #returns all letters from the 2nd character
print(course[1:-3])
newC = (course[:]) #returns all character
print('newC '  + newC)


#When a function belongs to a specific object. its referred to as Methods
print(course.upper()) #upper() function here is a method
print(len(course))  #To print number of characters in a string, len() here is a Function and not method because its a general purpose function
print(course.replace('o', 'O'))
print(course.find('Py')) #returns the index of the first character
print('for' in course) #returns a boolean value
print(course.split(" ")) #returnslist[]
print(course.rpartition(' '))#returns tuples()

a="Hello"
b="there"
c="All"

strg="{} {}, {}!".format(a,b,c)
print(strg)

#To assign sentences to a variable, declare with ''''''
value = '''
This is sentences of many paragraph

Paragraph 1

Paragraph 2

Paragraph 3
'''