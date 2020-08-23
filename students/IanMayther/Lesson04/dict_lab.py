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
    return string.count('t')

people = dict({})
for keys in person.keys():
    people.update({person[keys]: count_t(person[value])})

print(people)