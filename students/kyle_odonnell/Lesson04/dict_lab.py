#!/usr/bin/env python3



# Dictionaries 1

chris_dict = {"Name": "Chris", "City": "Seattle", "Cake": "Chocolate"}
print("Dictionary Display:")
print(chris_dict.items())

chris_dict.pop("Cake")
print("Pop Cake:")
print(chris_dict.items())

chris_dict["Fruit"] = "Mango"
print("Added Fruit:")
print(chris_dict.items())

print("Dictionary Keys:")
print(chris_dict.keys())

print("Dictionary Values:")
print(chris_dict.values())

print("Cake key:")
print('Cake' in chris_dict)

print("Mango value:")
print("Mango" in chris_dict.values())


# Dictionaries 2
chris_dict = {"Name": "Chris", "City": "Seattle", "Cake": "Chocolate"}


def count_ts(dict1):
    """
    Create dictionary based on number of ts in argument dictionary values
    :param dict1: dictionary argument
    :return: dictionary with same keys and new values
    """
    dict2 = {}
    for i, v in dict1.items():
        dict2[i] = v.count("t")
    return dict2

t_dict = (count_ts(chris_dict))
print("New dictionary of t counts:")
print(t_dict.items())


# Sets
def factors_set(fact):
    s = set()
    for i in range(0, 20):
        if not i % fact:
            s.update([i])
    return s


s2 = factors_set(2)
s3 = factors_set(3)
s4 = factors_set(4)

print("s2:", s2)
print("s3:", s3)
print("s4:", s4)

print("s2 is a subset of s3:", s2.issubset(s3))
print("s4 is a subset of s2:", s4.issubset(s2))

p = set("Python")
p.update("i")
print(p)


fs = frozenset(("marathon"))

print(p.union(fs))