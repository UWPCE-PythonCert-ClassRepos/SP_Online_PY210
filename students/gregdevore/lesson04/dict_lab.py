#!/usr/bin/env python3

def printsection(s):
    print('--------------')
    print('Dictionaries {:d}'.format(s))
    print('--------------')

# Dictionaries 1
printsection(1)
dict1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
# Print dictionary
print('Displaying initial dictionary')
print(dict1)
# Delete entry for cake
del dict1['cake']
# Print dictionary
print('Displaying dictionary after deleting \'cake\' key')
print(dict1)
# Add entry for fruit
dict1['fruit'] = 'Mango'
print('Displaying dictionary after adding \'fruit\' key')
print(dict1)
# Display keys and values
print('Dictionary keys:')
print(dict1.keys())
print('Dictionary values:')
print(dict1.values())
# Look for 'cake' as keys
looking_for_key = 'cake'
contains_key = looking_for_key in dict1
print('Is key \'{}\' in dictionary? {}'.format(looking_for_key, contains_key))
# Look for 'Mango' as value
looking_for_value = 'Mango'
contains_value = looking_for_value in dict1.values()
print('Is value \'{}\' in dictionary? {}'.format(looking_for_value, contains_value))
