#!/usr/bin/env python3
# PY210 Lesson 04 Dict Lab - Chase Dullinger

# Dictionaries 1
dict1 = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}

print(dict1)

dict1.pop("cake", None)
print(dict1)

dict1["fruit"] = "Mango"

print(dict1)

print(dict1.keys())

print(dict1.values())

print("cake" in dict1)

print("Mango" in dict1.values())

# Dictionaries 2
dict2 = {}
for k, v in dict1.items():
    dict2[k] = v.count("t")
    dict2[k] += v.count("T")

print(dict2)

# Sets 1

s2 = set([])
s3 = set([])
s4 = set([])

switching_dict = {2: s2, 3: s3, 4: s4}

for i in range(0,21):
    for j in switching_dict:
        if i % j == 0:
            switching_dict[j].add(i)

for s in switching_dict.values():
    print(s)

print(s3.issubset(s2))

print(s4.issubset(s2))

# Sets 2
python_set = set([])
for l in "Python":
    python_set.add(l)

python_set.add("i")

print(python_set)

marathon = []
for l in "marathon":
    marathon.append(l)

marathon_frozen_set = frozenset(marathon)
print(marathon_frozen_set)

print(python_set.union(marathon_frozen_set))
print(python_set.intersection(marathon_frozen_set))
