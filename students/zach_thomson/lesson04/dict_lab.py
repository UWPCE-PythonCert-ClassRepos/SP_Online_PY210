#!/usr/bin/env python3

#Dictionaries1
d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
d2 = d1.copy()
print(d1)

d1.pop('cake')

print(d1)

d1['fruit'] = 'Mango'

print(d1)
print(d1.keys())
print(d1.values())
print('cake' in d1)
print('Mango' in d1.values())

#Dictionaries2
def count_num_t(value):
    i=0
    total = 0
    while i < len(value):
        if value[i].lower() == 't':
            total += 1
            i += 1
        else:
            i += 1
    return total

def change_dict(d):
    for i in d:
        d[i] = count_num_t(d[i])
    return d

print(change_dict(d2))

#Sets1
def add_num(num):
    l = []
    i = 1
    while i <= 20:
        if i % num == 0:
            l.append(i)
            i += 1
        else:
            i += 1
    return l

s2 = set(add_num(2))
s3 = set(add_num(3))
s4 = set(add_num(4))

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets2

python_set = set(list('Python'))
python_set.update('i')
marathon_set = frozenset(list('Marathon'))
print(python_set.union(marathon_set))
print(python_set.intersection(marathon_set))
