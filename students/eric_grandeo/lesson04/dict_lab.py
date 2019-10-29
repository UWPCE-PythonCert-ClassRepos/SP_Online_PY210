#!/usr/bin/env python3

#Dictionary 1
dict_1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

#Display the dict
print(dict_1)

#Delete the entry for cake, display the dict
dict_1.pop("cake")
print(dict_1)

#add fruit, display dict
dict_1["fruit"] = "Mango"
print(dict_1)

#display dict keys
print(dict_1.keys())

#display the dict values
print(dict_1.values())

#is cake in dict
print("cake" in dict_1)

#is mango in dict
print("Mango" in dict_1.values())

print("-" * 100)

#Dictionaries 2
dict_1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

def count_letters(dictionary, letter):
    dict_2 = {}
    for x,y in dictionary.items():
        dict_2[x] = y.lower().count(letter)
    return dict_2

print(count_letters(dict_1, "t"))

#Sets
#Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
#divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
#display the sets

print("-" * 100)
s2 = set([x for x in range(21) if x%2==0])
s3 = set([x for x in range(21) if x%3==0])
s4 = set([x for x in range(21) if x%4==0])

print(s2)
print(s3)
print(s4)

#is s3 a subset of s2? (False)
print(s2.issubset(s3))

#if s4 is a subset of s2 (True)
print(s4.issubset(s2))

#Sets2

#Create a set with the letters in ‘Python’ and add ‘i’ to the set
py_set = set(list('Python'))
print(py_set)

py_set.update(['i'])
print(py_set)

#Create a frozenset with the letters in ‘marathon’
fs = frozenset(list('marathon'))
print(fs)

#Display the union and intersection of the two sets
print('')
print(py_set.union(fs))
print(py_set.intersection(fs))

