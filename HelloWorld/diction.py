#Dictionaries
dic={} #empty dictionary
dic={1:"Name",2:"Age",3:"Job"}
dic1={"name":"Hamdy","age":32,"job":"DBAdmin"}

print(dic,dic1)

#Nested Dictionary
dic3 = dict({"name":{"first":"Hamdy","second":"SJ"},"age":32,"job":"DBAdmin"})
print(dic3)

#Adding elements
d={}
d[0] = ("Hi", "there!") #adding tuples(immutable)
d[1] = ["Welcome","to",345] #adding list(mutable)
d[2] = {"How may I help you"} #adding dictionary
d["name"] = {"Hamdy"}

print(d)

#Accessing Elements
print(d.get(2))
print(d["name"])


#Deleting Elements
#dictName.pop(keyName or keyID)
#dictName.popitems() deletes the last index

#Builtin Functions
print(d.values())

keys=('a','b','c','d')
entry = 5
v = dict.fromkeys(keys,entry)
print(v)

v.clear()

print(f"V equals {v}")

#Sets - unordered collection of unique elements
s1=set([1,3,6,4,9])
s2=set([2,7,0,5,9,9])

#end

print(f'Union: {s1.union(s2)}')
print(f'Difference S1: {s1.difference(s2)}')
print(f'DifferenceS2: {s2.difference(s1)}')


