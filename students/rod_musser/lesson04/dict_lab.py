#!/usr/bin/env python3
# Dictionaries 1
bakery = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(bakery)
bakery.pop('cake')
print(bakery)
bakery['fruit'] = 'Mango'
print(bakery)
print(bakery.keys())
print(bakery.values())
print('Is cake in dictionary? ' + str('cake' in bakery))
print('Is fruit in dictionary? ' + str('fruit' in bakery))

# Dictionaries 2
bakery_2 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
t_dict = {}
for k, v in bakery_2.items():
    t_dict[k] = v.lower().count('t')
print(t_dict)

# Set 1
s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)

# Set 2
py_set = set('Python')
py_set.add('i')

f_set = ('marathon')
print(py_set.union(f_set))
print(py_set.intersection(f_set))


