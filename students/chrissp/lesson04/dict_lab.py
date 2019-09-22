#!/usr/bin/env python3

user1 = {"name": "Chris",
         "city": "Seattle",
         "cake": "Chololate"}


def dict1(user_input):
    print(user_input)
    user_input.pop("cake")
    print(user_input)
    user_input.update({"fruit": "Mango"})
    print(user_input.keys())
    print(user_input.values())
    print("cake" in user_input.keys())
    print("Mango" in user_input.values())


def dict2(user_input):
    for key, val in user_input.items():
        print("%s: %s" % (key, val.lower().count('t')))


def sets_1():
    s2 = set()
    s3 = set()
    s4 = set()
    for num in range(1, 21):
        if num % 2 == 0:
            s2.update([num])
        if num % 3 == 0:
            s3.update([num])
        if num % 4 == 0:
            s4.update([num])
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def sets_2():
    py_set = set('python')
    py_set.update(['i'])
    print(py_set)

    fs = frozenset('marathon')
    union_set = fs.union(py_set)
    inter_set = fs.intersection(py_set)
    print(union_set)
    print(inter_set)

sets_2()

