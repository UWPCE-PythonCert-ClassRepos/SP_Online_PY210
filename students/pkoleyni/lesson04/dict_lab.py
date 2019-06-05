#!/usr/bin/env python3
import  math

#Dictionaries 1
dict_1 = {'name':'Chris', 'city':'Seattle', 'cake':'Chocolate'}

print(dict_1)

dict_1.pop('cake')
print(dict_1)

dict_1['fruit'] = 'Mango'
print(dict_1)

#printing Keys and values
print ('dic_1 keys are: ',dict_1.keys())
print ('dic_1 values are: ',dict_1.values())

# Different way to print key and value
print ('Keys are:')
for key in dict_1.keys():
    print('\t', key)

print ('Values are:')
for value in dict_1.values():
    print('\t', value)

print('\n',dict_1)

print('Is cake in dict1 ?...{}'.format('cake' in dict_1.keys()))

print('Is Mango in dict1 ?...{}'.format('Mango' in dict_1.items()))


#Dictionaries 2
print ('_____Dictionaries 2_____')
dict_2 = {'name':'Chris'.count('t'), 'city':'Seattle'.count('t'), 'cake':'Chocolate'.count('t')}
print (dict_2)


#Sets
print ('_____SETs_____')
s2, s3, s4 =set(), set(), set()

for i in range(0,20):
    if i%2 == 0:
        s2.update(str(i))

for i in range(0,20):
    if i%3 == 0:
        s3.update(str(i))

for i in range(0,20):
    if i%4 == 0:
        s4.update(str(i))

print (s2, s3, s4)

print ('s3 set subset of s2 ? ...{}'.format(s3.issubset(s2)))

print ('s4 set subset of s2 ? ...{}'.format(s4.issubset(s2)))

print ('_____Sets 2_____')
my_string = 'Python'
my_set_1 = set(list(my_string))
print (my_set_1)

my_frozen_set_1 = frozenset(list('marathon'))
print (my_frozen_set_1)

print ('Smallest set which contains all the elements of both the sets ', my_set_1.union(my_frozen_set_1))
print ('The largest set which contains all the elements that are common to both the sets is ',my_set_1.intersection(my_frozen_set_1))

