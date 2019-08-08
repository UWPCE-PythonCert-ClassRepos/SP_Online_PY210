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

# dictionaries 2
d2 = {}
for key, value in d1.items():
    d2.update({key: value.lower().count('t')})

print(d2)

# sets 1
s2 = []
s3 = []
s4 = []
for n in range(0,21):
    if n % 2 == 0: s2.append(n)
    if n % 3 == 0: s3.append(n)
    if n % 4 == 0: s4.append(n)
print(s2)
print(s3)
print(s4)
