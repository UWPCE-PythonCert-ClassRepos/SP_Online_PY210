#!/usr/bin/env python

# Dictionaries 1

d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
print(d)
d.pop("cake")
print(d)
d["fruit"] = "Mango"
print(d)

for key in d:
    print(key)

for value in d.values():
    print(value)

print("cake" in d)
print("Mango" in d.values())

# Dictionaries 2

d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}

for key in d:
    t_count = 0
    for c in range(len(d[key])):
        if d[key][c] in ['t', 'T']:
            t_count += 1
    d[key] = t_count

print(d)

# Sets

s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)

print(s2, s3, s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Sets 2

p_set = {'P', 'y', 't', 'h', 'o', 'n'}
f_set = frozenset({'m', 'a', 'r', 'a', 't', 'h', 'o', 'n'})

print("Union:", p_set.union(f_set))
print("Intersection:", p_set.intersection(f_set))



