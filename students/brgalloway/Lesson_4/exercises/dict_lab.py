#!/usr/bin/env python3

a_dict = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

a_dict.pop("cake")
a_dict.setdefault("fruit","mango")

for k in a_dict:
    print(k)
for v in a_dict:
    print(a_dict[v])
for v in a_dict.keys():
    print(v)

print("cake" in a_dict)
print("mango" in a_dict["fruit"])
print("mango" in a_dict.values())
print("cake" in a_dict.keys())
print(a_dict)