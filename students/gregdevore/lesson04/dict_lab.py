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
