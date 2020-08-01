#!/usr/bin/env python3
#Christine Kim Lessson 4 dict lab

#Dictionaries 1
d = {}
d["name"] = "Chris"
d["city"] = "Seattle"
d["cake"] = "Chocolate"

item1 = d.copy()
print(d)

d.popitem()

print(d)
d["fruit"] = "Mango"
print(d.keys())
print(d.values())
print(("cake") in d)
print(d["fruit"] == "Mango")

#Dictionaries 2
item2 = {}
for x, y in item1.items():
    item2[x] = y.lower().count("t")
print(item2.items())

#Set1
s2 = set()
s3 = set()
s4 = set()
for i in range(0, 21):
    if i % 4 == 0:
        s4.update([i])
        s2.update([i])
        if i % 3 == 0:
            s3.update([i])
    elif i % 3 == 0:
        s3.update([i])
        if i % 2 == 0:
            s2.update([i])
    elif i % 2 == 0:
        s2.update([i])
    else:
        pass

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

#Set2
s_p = set("python")
s_p.update(["i"])

s_m = frozenset("marathon")

print(s_p.union(s_m))
print(s_p.intersection(s_m))