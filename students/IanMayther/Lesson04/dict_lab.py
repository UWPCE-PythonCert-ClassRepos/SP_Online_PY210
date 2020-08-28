#!/usr/bin/env python3

#Dictionaries 1
person = dict({('name','Chris'),('city','Seattle'),('cake','Chocolate')})

print(person)

del person['cake']

print(person)

person.update({'fruit': 'Mango'})

print(person.keys())
print(person.values())

#Dictionaries 2
#return to original
del person['fruit']

person.update({'cake': "Chocolate"})

#count 't's
def count_t(string):
    return int(string.count('t'))

people = dict({})
for key in person.keys():
    people[key] = count_t(person[key])

print(people)

#Sets 1
#Initialize sets
s2 = set()
s3 = set()
s4 = set()

#Populate sets
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

#Display sets
print(s2)
print(s3)
print(s4)

#Confirm sub-sets
print(f"Is s3 a subset of s2? {s2.issuperset(s3)}")
print(f"Is s4 a subset of s2? {s2.issuperset(s4)}")

#Sets 2
p = set('python')
m = frozenset('marathon')

p.add('i')

u = p.union(m)
inter = p.intersection(m)

print(f"P = {p}")
print(f"M = {m}")
print(f"Union = {u}")
print(f"Intersection = {inter}")