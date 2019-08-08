#!/usr/bin/env python3

# dictionaries 1
d1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}
print(d1)

del d1['cake']
print(d1)

d1.update({'fruit':'Mango'})

print('Dictionary keys: ')
print(d1.keys())
print('Dictionary values:')
print(d1.values())
print('Is cake a key? ' + str('cake' in d1.keys()))
print('Is Mango a value? ' + str('Mango' in d1.values()))
