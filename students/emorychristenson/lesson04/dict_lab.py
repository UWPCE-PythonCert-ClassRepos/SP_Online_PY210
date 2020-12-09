#!/usr/bin/env python3

# Dictionaries 1
things = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "chocolate"
}

copy = things.copy()
print(copy)
print("\nRemoving 'cake' entry...\n")

# Remove "cake" entry
copy.pop("cake")

print(things, "\n")

# Add an entry for the fruit
copy["fruit"] = "Mango"

print(copy.keys())
print(copy.values())

print("\nIs 'cake' in this dict?")
print("cake" in copy)

print("\nIs 'mango' in this dict?")
print("Mango" in copy.values(), "\n")

# Dictionaries 2

# Create new dict, where the values are the number of times "t" appears in the original ones
new_things = {}
for k, v in things.items():
    new_things[k] = v.count("t")
print("Number of times 't' appears in the dict values:")
print(new_things)


# Sets 1
print("\nStarting sets!\n")

s2 = set()
s3 = set()
s4 = set()
r = range(21)
for i in r:
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)


print(s2)
print(s3)
print(s4)
print(s2.issubset(s3))
print(s4.issubset(s2))


# Sets 2

print("\nStarting sets 2!\n")

set2 = set("Python")
set2.add("i")
print(set2)

set3 = frozenset("Marathon")

print(set2.union(set3))
print(set2.intersection(set3))

