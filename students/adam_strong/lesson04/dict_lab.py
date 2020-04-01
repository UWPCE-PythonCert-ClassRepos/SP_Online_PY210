#!/usr/bin/env python3

# Dictionary and set lab - Lesson04 Exercise

# Dictionaires 1

dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
dict2 = dict1.copy()
print(dict1)
dict1.popitem()
print(dict1)
dict1['fruit'] = "Mango"
print(dict1.keys())
print(dict1.values())
print('cake' in dict1.keys())
print('Mango' in dict1.values())

# Dictionaries 2

for value in dict2:
    dict2[value] = dict2[value].count('t')
print(dict2)

# Sets 1

s2 = set([])
s3 = set([])
s4 = set([])
for i in range(0,21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2,s3,s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2

s_py = set(['P','y','t','h','o','n'])
s_py.add('i')
s_ma = frozenset(['m','a','r','a','t','h','o','n'])
print(s_py.union(s_ma), s_py.intersection(s_ma))
