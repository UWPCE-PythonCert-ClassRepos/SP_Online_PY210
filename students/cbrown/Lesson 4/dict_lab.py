#!/usr/bin/env python
#Dictionary Set Lab: Lesson 4

#Dictionaries 1
dict_1 = {'Name':'Chris','City':'Seattle','Cake':'Chocolate'}
print(dict_1)

dict_1.pop('Cake',None)
print(dict_1)

dict_1['Fruit'] = 'Mango'
print(dict_1)
print(dict_1.keys())
print(dict_1.values())

print('Cake' in dict_1.keys())
print('Mango' in dict_1.values())

#Dictionaries 2
dict_1 = {'Name':'Chris','City':'Seattle','Cake':'Chocolate'}
dict_2 = {}

for k,v in dict_1.items():
    dict_2[k] = v.count('t')

print(dict_2)

#Set Excercises
def set_create(num):
    num_set = []
    for i in range(21):
        if i % num == 0:
            num_set.append(i)
    return num_set


s2 = set(set_create(2))
s3 = set(set_create(3))
s4 = set(set_create(4))

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

#Set 2
py = set([i for i in 'Python'])
py.add('i')
print(py)

mar = frozenset([i for i in 'marathon'])

print(py.union(mar))
print(py.intersection(mar))
