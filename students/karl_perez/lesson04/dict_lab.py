#!/usr/bin/env python3

#Dictionaries 1

#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)

dictionary = {
     'name': 'city', 
     'cake': 'Chris', 
     'Seattle': 'Chocolate'}
#Display the dictionary.
print(dictionary)
#Delete the entry for “cake”.
dictionary.pop('cake')
print(dictionary)
#Add an entry for “fruit” with “Mango” and display the dictionary.
dictionary['fruit'] = 'Mango'
print(dictionary)
#Display the dictionary keys.
print(dictionary.keys())
#Display the dictionary values.
print(dictionary.values())
#Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print('cake' in dictionary.keys())
#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print('Mango' in dictionary.values())

#Dictionaries 2
dictionary2 = {
     'name': 'city', 
     'cake': 'Chris', 
     'Seattle': 'Chocolate'}

count = [] # empty list
for things in dictionary2.values():
    count.append(things.lower().count('t'))  # number of t's
dictionary2 = dict(name=count[0], cake=count[1], Seattle=count[2])  # create new dict
print(dictionary2)

#Sets1

s2 = set()
for s in range(0,21):
	if s % 2 ==0:
		s2.update([s])
print(s2)

s3 = set()
for s in range(0,21):
    if s % 3 ==0:
    	s3.update([s])
print(s3)

s4 = set()
for s in range(0,21):
    if s % 4 ==0:
    	s4.update([s])
print(s4)

print('s3 is subset of s2? ' + str(s3.issubset(s2)))
print('s4 is subset of s2? ' + str(s4.issubset(s2)))

#Sets 2
# sets 2
set1 = set("Python")
print(set1)
set1.add("i")
print(set1)
set2 = set("marathon")
print(set1.union(set2))
print(set1.intersection(set2))


