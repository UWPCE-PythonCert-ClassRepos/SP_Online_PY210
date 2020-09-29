#!/usr/bin/env python

"""
dictionaries 1
"""
print("-----DICTIONARIES 2-----\n")
# create dictionary
_dict = {'name': 'Chris', 
          'city': 'Seattle', 
          'cake': 'Chocolate'}

_dict1 = _dict.copy()
# display dictionary
print("display dictionary: {}".format(_dict1))

# delete the "cake" entry
_dict1.pop('cake')

# display the dictionary
print("delete cake entry: {}".format(_dict1))

# add "fruit entry"
_dict1['fruit'] = 'Mango'

# display the dictionary 
print("add fruit:mango entry: {}".format(_dict1))

# display the dictionary keys; values
print(_dict1.keys())
print(_dict1.values())

# determine whether 'cake' and 'Mango' is in the dictionary
print("is cake a key?: ", end="")
print('cake' in _dict1.keys())
print("is mango a value?: ", end="")
print('Mango' in _dict1.values())

"""
dictionaries 2
"""
print("\n\n-----DICTIONARIES 2-----\n")
_dict2 = {}

# make dictionary with keys from _dict except with the values being number of t's in original
for k,v in _dict.items():
    _key = k
    _value = (v.lower()).count('t')
    _dict2[_key] = _value

print("display dictionary: {}".format(_dict2))

"""
sets 1
"""
print("\n\n-----SETS 1-----\n")
# create inital set with numbers from 0 to 20
s1 = set(range(21))

# create sets that contain numbers that are divisible by 2,3,4
s2 = set()
s3 = set()
s4 = set()

for item in s1:
    if (item%2) == 0:
        s2.update([item])
    if (item%3) == 0:
        s3.update([item])
    if (item%4) == 0:
        s4.update([item])
        
# display the sets
print("s1={}\ns2={}\ns3={}\ns4={}".format(s1,s2,s3,s4))

# display if s() is a subset of s2
print("is s3 a subset of s2?: ",end='')
print(s3.issubset(s2))
print("is s4 a subset of s2?: ",end='')
print(s4.issubset(s2))

"""
sets 2
"""
print("\n\n-----SETS 2-----\n")

# create set with letters in 'python'
_set2 = set()
_str1 = []
_str1.extend('python')
_set2.update(_str1)
print("set={}".format(_set2))

# add 'i' to the set 
_set2.update('i')
print("set={}".format(_set2))

# create frozen set with letters in 'marathon'
_str2 = []
_str2.extend('marathon')
_fset = frozenset(_str2)
print(_fset)

# display the union and intersection of the two sets 
_union = _set2.union(_fset)
print("union={}".format(_union))

_intsct = _set2.intersection(_fset)
print("intersection={}".format(_intsct))