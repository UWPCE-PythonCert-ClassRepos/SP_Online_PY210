#!/usr/bin/env python3
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict_1)
dict_1.pop('cake')
print(dict_1)
dict_1['fruit'] = "Mango"

for item in dict_1:
    print(item)

for values in dict_1.values():
    print(values)

if(dict_1.get('cake')):
    print("True")
else:
    print("False")

print('Mango' in dict_1.values())

dict_2 = {}

for item in dict_1.copy():
    dict_2[item] = dict_1.get(item).lower().count('t')

print(dict_2)

# -------------- Sets --------------------
