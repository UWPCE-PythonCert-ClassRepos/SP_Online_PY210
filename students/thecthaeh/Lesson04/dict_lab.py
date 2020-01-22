#!/usr/bin/env python3

"""Create a dict for 'name', 'city', and 'cake' and manipulate it in various ways."""
#Dictionaries 1
d = {}
d['name'] = 'Chris'
d['city'] = 'Seattle'
d['cake'] = 'Chocolate'

print(d)

d.pop('cake')
print(d)

d.setdefault('fruit', 'Mango')

for key in d:
    print(key)

for val in d.values():
    print(val)

'cake' in d #check for 'cake' key in the dict (should return False)
'Mango' in d #check for 'Mango' value in dict (should return True)

"""Use the dict from Dictionaries 1 but set the values to reflect the number of 't's in each value."""
#Dictionaries 2
orig_d = {}
orig_d['name'] = 'Chris'
orig_d['city'] = 'Seattle'
orig_d['cake'] = 'Chocolate'

for k, val in orig_d.items():
    print(val.lower()) #test
    orig_d[k] = val.count('t')
    print(orig_d)