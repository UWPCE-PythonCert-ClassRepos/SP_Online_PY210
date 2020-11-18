#!/usr/bin/env python
#Dictionary Set Lab: Lesson 4

#Dictionaries 1
dict = {'Name':'Chris','City':'Seattle','Cake':'Chocolate'}
print(dict)

dict.pop('Cake',None)
print(dict)

dict['Fruit'] = 'Mango'
print(dict)
print(dict.keys())
print(dict.values())

print('Cake' in dict.keys())
print('Mango' in dict.values())  
