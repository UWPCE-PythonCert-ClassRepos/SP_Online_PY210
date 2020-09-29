#!/usr/bin/env python3
#Chris Dela Pena
#UW PCE PY210
#Assignment 3 - Mailroom Part 1
#2020/6/25

#Dictionaries 1
dict = {"name":"Chris","city":"Seattle","cake":"Chocolate"}
print(dict)
del(dict["cake"])
print(dict)
dict["fruit"] = "Mango"
print(dict.keys())
print(dict.values())
print("Is cake in dictionary?", "cake" in dict)
print("Is Mango in dictionary?", "Mango" in dict.values())

#Dictionaries 2
dict_t = dict
for key in dict_t.keys():
    n = key.lower().count("t")
    dict[key] = n
print(dict_t)

#Sets
def modulus_div(divisor, number):
    collector = set()
    n = 1
    while n <= number:
        if n % divisor == 0:
            collector.update({n})
        n = n + 1
    return collector
s2 = modulus_div(2, 20)
s3 = modulus_div(3, 20)
s4 = modulus_div(4, 20)
print("s2 = ", s2)
print("s3 = ", s3)
print("s4 = ", s4)

#Sets2
set1 = set("Python")
set1.update("i")
frozenset1 = frozenset("marathon")
print(set1.union(frozenset1))
