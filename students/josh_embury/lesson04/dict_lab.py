#!/usr/bin/env python3

#Dictionaries 1:
# create dictionary:
dict1 = {'name':'Chris', 'city':'Seattle','cake':'chocolate'}
#display dictionary:
for val in dict1.items():
    print(val)
#delete entry:
del dict1['cake']
#display dictionary:
print()
for val in dict1.items():
    print(val)
#add entry
dict1['fruit'] = 'Mango'
# display keys
print('\nKeys in dict:')
for keys in dict1.keys():
    print(keys)
# display values
print('\nValues in dict:')
for vals in dict1.values():
    print(vals)
print('\nIs cake in dict?')
print('cake' in dict1)
print('\nIs mango in dict?')
print('Mango' in dict1.values())