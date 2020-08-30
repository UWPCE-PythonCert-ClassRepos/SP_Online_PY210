#!/usr/bin/env python3
'''
DICTIONARIES 1
  - Create a dictionary with keys "name, city, and cake" and values
    "Chris, Seattle, and Chocolate"
  - Display the dictionary.
  - Delete the entry for "Cake"
  - Display the Dictionary
  - Add an entry for "fruit" with "Mango and display the dictionary
      - Display the dictionary keys.
      - Display the dictionary values
      - Display whether or nor "cake" is in the dictionary
      - Display whether or not "mango" is in the dictionary
'''

dict1 = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
print(dict1)
dict1.pop('Cake')
print(dict1)
dict1['Fruit']='Mango'
print(dict1.keys())
print(dict1.values())
print('Cake' in dict1.keys())
print('Mango' in dict1.values())

'''
DICTIONARIES 2
  - Using original dictionary from above, make a new dictionary except:
      - Use same keys
      - Values are now the number of t's in the original values
'''

dict2 = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'}
for k in dict2:
    dict2[k] = dict2[k].lower().count('t')
print(dict2)

'''
SETS
  - Create sets S2, S3, and S4 containing numbers 0-20 divisible
    by 2, 3, and 4, respectively (computer these)
  - Display the sets
  - Displat is S3 is a subset of S2 (false)
  - Display if S4 is a subset of S2 (true)
'''
s2 = set()
s3 = set()
s4 = set()
for i in range (0, 21):
    if i%2 == 0:
        s2.update([i])
    if i%3 == 0:
        s3.update([i])
    if i%4 == 0:
        s4.update([i])

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

'''
SETS 2
  - Create a set of the letters in 'Python' and add 'i' to it
  - Create a frozenset with the letters in 'marathon'
  - Display the union and intersection of the two sets
'''
pyset = set('Python')    # set defined with 'Python'
pyset.update('i')    # add 'i' to it
print(pyset)    # print it because why not

froset = frozenset('marathon')    # create frozen set w/ 'marathon'

print(froset.intersection(pyset))
print(froset.union(pyset))
