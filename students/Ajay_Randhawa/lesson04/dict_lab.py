#Dictionaries 1
print('Dictionaries 1:')
d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(d)
d.popitem()
print(d)
d['fruit'] = 'Mango'
print(d)
print(d.keys())
print(d.values())
print('cake' in d.keys())
print('Mango' in d.values())

#Dictionaries 2
print('\n')
print('Dictionaries 2:')
e = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
e['name'] = e['name'].count('t')
e['city'] = e['city'].count('t')
e['cake'] = e['cake'].count('t')
print(e)

#Sets
print('\n')
print('Sets:')
s2 = set(list(range(0,20,2)))
s3 = set(list(range(0,20,3)))
s4 = set(list(range(0,20,4)))
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
print('\n')
print('Sets 2:')
s1 = set('Python')
print(s1)
s1.update('i')
print(s1)

s5 = frozenset('marathon')
print(s5)
print(s5.union(s1))
print(s5.intersection(s1))