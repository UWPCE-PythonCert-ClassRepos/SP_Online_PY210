#!/usr/bin/env python3

# Dictionaries 1
cake_info = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print(cake_info)

cake_info.pop("cake")

print(cake_info)

cake_info["fruit"] = "Mango"

print(cake_info)

print(cake_info.keys())

print(cake_info.values())

print("cake" in cake_info)

print("Mango" in cake_info.values())

# Dictionaries 2
count_t = {}
for key, value in cake_info.items():
    count_t[key] = value.lower().count("t")
print(count_t)

# Sets 1
s2 = set(range(2, 21, 2))
print(s2)
s3 = set(range(3, 21, 3))
print(s3)
s4 = set(range(4, 21, 4))
print(s4)

print(s3.issubset(s2))

print(s4.issubset(s2))

py_set = set("Python")
py_set.add("i")
print(py_set)

frozen = frozenset("marathon")

print(py_set.union(frozen))

print(py_set.intersection(frozen))