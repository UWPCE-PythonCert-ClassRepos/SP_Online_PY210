#!/usr/bin/env python3

#Dictionaries 1:
# create dictionary:
dict1 = {'name':'Chris', 'city':'Seattle','cake':'chocolate'}
#display dictionary:
for val in dict1.items():
    print(val)
#delete entry:
del dict1['cake']
#display dictionary:
print()
for val in dict1.items():
    print(val)
#add entry
dict1['fruit'] = 'Mango'
# display keys
print('\nKeys in dict:')
for keys in dict1.keys():
    print(keys)
# display values
print('\nValues in dict:')
for vals in dict1.values():
    print(vals)
print('\nIs cake in dict?')
print('cake' in dict1)
print('\nIs mango in dict?')
print('Mango' in dict1.values())

#Dictionaries 2:
dict2 = {}
for dicval in dict1:
    dict2[dicval] = dict1[dicval].lower().count('t')
print('Creating new dict with t count:')
for val in dict2.items():
    print(val)
print()
#Sets
s2=set()
s3=set()
s4=set()
for i in range(0,21):
    if i%2 == 0:
        s2.update([i])
    if i%3 == 0:
        s3.update([i])
    if i%4 == 0:
        s4.update([i])
print(s2)
print(s3)
print(s4)

print('\n is s3 a subset of s2?:')
print(s3.issubset(s2))
print('\n is s4 a subset of s2?:')
print(s4.issubset(s2))

#Set 2:
seta = set(['P','y','t','h','o','n'])
setb = set(['m','a','r','t','h','o','n'])
print('\n union of python and maration:')
print(seta.union(setb))
print('\n Intersection of python and marathon:')
print(seta.intersection(setb))