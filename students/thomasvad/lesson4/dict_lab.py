# dictionary 1
# creating dict
dict1 = {'name': 'chris', 'city': 'seattle', 'cake': 'chocolate'}
print (dict1, '\n')

#removing cake
dict1.pop('cake')
print(dict1, '\n')

#adding fruit
dict1['fruit'] = 'mango'
print(dict1.keys())
print(dict1.values(), '\n')

# cheking keys and values
print('is cake a key:', 'cake' in dict1.keys())
print('is mango a value:', 'mango' in dict1.values(), '\n')


# dic 2
dict2 = {}
for k,v in dict1.items():
    if k not in dict2:
        dict2[k]= v.count('t')
print(dict2,'\n')


# set1
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))
print('s2, s3, s4: ', s2, s3, s4)
print ('is s3 a subset of s2: ', s3.issubset(s2))
print('is s4 a subset of s2: ', s4.issubset(s2), '\n')

# set2
set2 = set('Python')
set2.add('i')
set3 = frozenset('marathon')
print(set2, set3, '\n')

print('set2 and set3 intersection: ', set2.intersection(set3))
print('set2 and set3 union: ', set2.union(set3))
