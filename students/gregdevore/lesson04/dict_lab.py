#!/usr/bin/env python3

def printsection(type,s):
    print('--------------')
    print('{} {:d}'.format(type, s))
    print('--------------')

def find_in_dict(lookup_dict,item,type='key'):
    """ Look for specific key or value in dictionary
    Arguments:
    lookup_dict -- Dictionary to search
    item -- Item (key or value) to find

    Keyword Arguments:
    type -- 'key' (default) or 'value'
    """
    if type == 'key':
        result = item in lookup_dict
    elif type == 'value':
        result = item in lookup_dict.values()
    else:
        print('Unknown type \'{}\' for dictionary lookup, only \'key\' or \'value\' accepted'.format(type))
        return
    print('Is {} \'{}\' in dictionary? {}'.format(type, item, result))

# Dictionaries 1
printsection('Dictionaries',1)
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
find_in_dict(dict1,'cake')
# Look for 'Mango' as value
find_in_dict(dict1,'Mango','value')

# Dictionaries 2
printsection('Dictionaries',2)
dict2 = {}
for key,value in dict1.items():
    dict2[key] = value.lower().count('t')
print('Displaying count of \'t\' in dict1 values:')
print(dict2)

# Sets 1
printsection('Sets',1)
# Creates sets for numbers divisible by 2,3,4 in interval [0,20]
s2,s3,s4 = set(),set(),set()
for num in range(21):
    if num % 2 == 0:
        s2.add(num)
    if num % 3 == 0:
        s3.add(num)
    if num % 4 == 0:
        s4.add(num)
print('s2',s2)
print('s3',s3)
print('s4',s4)
# Check if s3 is a subset of s2
print('Is s3 a subset of s2? {}'.format(s3.issubset(s2)))
# Check if s4 is a subset of s2
print('Is s4 a subset of s2? {}'.format(s4.issubset(s2)))
