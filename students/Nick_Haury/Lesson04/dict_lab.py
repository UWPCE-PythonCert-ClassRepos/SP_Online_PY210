#!/usr/bin/env python3
'''
Practice script for creating and manipulating dictionaries and sets
'''

# Dictionaries 1

print("Dictionaries 1:\n")

my_dict = {
    "name":"Chris", 
    "city":"Seattle", 
    "cake":"Chocolate"
    }

print(my_dict)
my_dict.pop("cake")
print(my_dict)
my_dict["fruit"] = "Mango"
print(my_dict.keys())
print(my_dict.values())
print("Is 'cake' a key in the dictionary?: " + str(("cake" in my_dict)))
print("Is 'Mango' a value in the dictionary?: " + str(("Mango" in my_dict.values())))

# Dictionaries 2

print("\nDictionaries 2:\n")

dict_t = dict()
for key in my_dict:
    dict_t[key] = my_dict[key].count("t")
print(dict_t)

# Sets 1

print("\nSets 1:\n")

s1, s2, s3, s4 = set(), set(), set(), set()
for i in range(20):
    s1.add(i)

for key in s1:
    if key % 2 == 0:
        s2.add(key)
    if key % 3 == 0:
        s3.add(key)
    if key % 4 == 0:
        s4.add(key)

print("s1: ", s1, "\ns2: ", s2, "\ns3: ", s3, "\ns4: ", s4, sep="")

print("Is s3 a subset of s2?: " + str(s3.issubset(s2)))
print("Is s4 a subset of s2?: " + str(s4.issubset(s2)))

# Sets 2

print("\nSets 2:\n")

p_set = set("Python")
p_set.add("i")
print("p_set is:", p_set)

f_set = frozenset("marathon")
print("f_set is:", f_set)

print("The union of p_set and f_set is: " + str(p_set.union(f_set)))
print("The intersection of p_set and f_set is: " + str(p_set.intersection(f_set)))
