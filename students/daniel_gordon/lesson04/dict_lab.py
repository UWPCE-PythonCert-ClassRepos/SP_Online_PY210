#!/usr/bin/env python3

#Dictionaries 1
items = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate" }
print(items)
items.pop("cake")
print(items)
items["fruit"] = "Mango"
print(items)
print(items.keys())
print(items.values())
print("cake" in items)
print("Mango" in items.values())

#Dictionaries 2
items = {"name" : "Chris", "city" : "Seattle", "cake" : "Chocolate" }
t_count = {}
for item in items:
    t_count[item] = items[item].lower().count('t')
print(t_count)

#Sets
s2 = set(range(0, 20, 2))
s3 = set(range(0, 20, 3))
s4 = set(range(0, 20, 4))
print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
set_py = set("Python")
set_py.add('i')
set_run = frozenset("marathon")
print(set_py.union(set_run))
print(set_py.intersection(set_run))