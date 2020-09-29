#!/usr/bin/env python3

"""
Lesson 4: dict lab
Course: UW PY210
Author: Jason Jenkins
"""


def dictionaries_1(d):
    tmp_d = d.copy()

    print("\nTesting dictionaries_1")
    tmp_d = dict(name="Chris", city="Seattle", cake="Chocolate")
    print(tmp_d)
    tmp_d.pop('city')
    print(tmp_d)
    tmp_d.update({'fruit': 'Mango'})
    print(tmp_d)

    print("Keys: ", end='')
    for v in tmp_d.keys():
        print(v, end=', ')
    print()

    print("Values: ", end='')
    for v in tmp_d.values():
        print(v, end=', ')
    print()

    print(f"Cake is in dictionary: {'cake' in tmp_d.keys()}")
    print(f"Mango is in dictionary: {'Mango' in tmp_d.values()}")


def dictionaries_2(d):
    tmp_d = d.copy()

    print("\nTesting dictionaries_2")
    for k, v in tmp_d.items():
        tmp_d[k] = v.lower().count('t')

    print(tmp_d)


def sets_1():
    print("\nTesting sets_1")

    s2 = set()
    s3 = set()
    s4 = set()

    for i in range(21):
        if(i % 2 == 0):
            s2.update({i})
        if(i % 3 == 0):
            s3.update({i})
        if(i % 4 == 0):
            s4.update({i})

    print(f"Set_2 = {s2}")
    print(f"Set_3 = {s3}")
    print(f"Set_4 = {s4}")

    print(f"Set 3 is a subset of Set 2: {s3.issubset(s2)}")
    print(f"Set 4 is a subset of Set 2: {s4.issubset(s2)}")


def sets_2():
    print("\nTesting sets_2")
    s_python = set()

    for i in "Python":
        s_python.update({i})
    s_python.update({"i"})
    print(s_python)

    s_maration_frozen = frozenset({"m", "a", "r", "a", "t", "h", "o", "n"})
    print(s_maration_frozen)

    print(f"Union: {s_python.union(s_maration_frozen)}")
    print(f"Intersection: {s_python.intersection(s_maration_frozen)}")


if __name__ == "__main__":
    # Create a list
    d = dict(name="Chris", city="Seattle", cake="Chocolate")
    dictionaries_1(d)
    dictionaries_2(d)
    sets_1()
    sets_2()
