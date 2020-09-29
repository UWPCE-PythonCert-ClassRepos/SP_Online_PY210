#!/usr/bin/env python3

# Dictionaries 1

def dict1(my_dict):
    new_dict = my_dict.copy()
    print(new_dict)
    new_dict.pop("cake")
    print(new_dict)
    new_dict["fruit"] = "Mango"
    print(new_dict)
    print(new_dict.values())
    print("cake" in new_dict.keys())
    print("Mango" in new_dict.values())

# Dictionaries 2

def dict2(my_dict):
    new_dict = my_dict.copy()
    t_count = 0
    for i,j in new_dict.items():
        t_count = j.count("t")
        new_dict[i] = t_count
    print(new_dict)

my_dict = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate",
}

# Sets 1

def set1():
    s2 = set()
    s3 = set()
    s4 = set()
    for num in range(0, 21):
        if num % 2 == 0:
            s2.update([num])
        if num % 3 == 0:
            s3.update([num])
        if num % 4 == 0:
            s4.update([num])
    print(s2, s3, s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))

# Sets 2

def set2():
    python_set = set("python")
    print(python_set)
    python_set.update(["i"])
    print(python_set)
    f_set = frozenset("marathon")
    print(python_set.union(f_set))
    print(python_set.intersection(f_set))

if __name__ == "__main__": 
    dict1(my_dict)
    dict2(my_dict)
    set1()
    set2()