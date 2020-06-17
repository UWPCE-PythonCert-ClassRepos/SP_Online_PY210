#!/usr/bin/env python3
#Create a dictionary
print("Dictionaries 1")
dValues = {
"name":"Cris",
"city":"Seattle",
"cake":"Chocolate"
}
print(dValues)
#Delete the entry
print("Deleting entery for 'city'")
if "city" in dValues:
    del dValues["city"]
    print(dValues)
#Add an entry
print("Adding a new item")
dValues.update({"fruit":"Mango"})
print(dValues)

print("Display the dictionary keys")
print(dValues.keys())

print("Display the dictionary values")
print(dValues.values())

print("Is 'cake' a key?")
print("cake" in dValues.keys())

print("is 'Mango' a value?")
print("Mango" in dValues.values())
#Using the dictionary from item 1: Make a dictionary 
#using the same keys but with the number of ‘t’s in each value as the value 
print("Dictionaries 2")
print("Changing values")
dValues["name"]=0
dValues["fruit"]=2
dValues["cake"]=2
print(dValues)

print("Create sets")
#Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
#divisible by 2, 3 and 4
print("s2:")
s2 = set()
for i in range(20):
    if i % 2 == 0: 
        s2.update([i])
    else:
	    pass
print(s2)
print("s3")
s3 = set()
for i in range(20):
    if i % 3 == 0: 
        s3.update([i])
    else:
	    pass
print(s3)
print("s4")
s4 = set()
for i in range(20):
    if i % 4 == 0: 
        s4.update([i])
    else:
	    pass
print(s4)
#Display if s3 is a subset of s2 and if s4 is a subset of s2
print("Is s3 a subset of s2?")
s3.issubset(s2)
print("Is s4 subset of s2?")
s4.issubset(s2)

#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
print("Sets2")
wPython = set()
wPython = set({"p","y","t","h","o","n"})
print(wPython)
wPython.add("i")
print(wPython)
#Create a frozenset with the letters in ‘marathon’.
wMarathon = frozenset({"m","a","r","a","t","h","o","n"})
print(wMarathon)
#Display the union and intersection of the two sets.
print(wPython.intersection(wMarathon))  



