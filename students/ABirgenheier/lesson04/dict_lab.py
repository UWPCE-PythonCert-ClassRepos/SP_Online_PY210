_dict = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}


def dictionary_one():
    #
    print("Dictionary")
    print(_dict)
    print("-"*20)
    #
    print("Deleted 'cake'")
    del _dict['cake']
    print(_dict)
    print("-"*20)
    #
    print("Added 'fruits'")
    _dict.update({"fruit": "Mangos"})
    print(_dict)
    print("-"*20)
    #
    print("Added 'fruits'")
    _dict.update({"fruit": "Mangos"})
    print(_dict)
    print("-"*20)
    #
    print("Keys only")
    for key, value in _dict.items():
        print(key)
    print("-"*20)
    #
    print("Values only")
    for key, value in _dict.items():
        print(value)
    print("-"*20)
    #
    print("If Mango is Key")
    if "Mango" in _dict.keys():
        print("True")
    else:
        print("False")
    print("-"*20)
    #
    print("If Mango is Value")
    if "Mangos" in _dict.values():
        print("True")
    else:
        print("False")
    print("-"*20)

# Works
# dictionary_one()


for value in dict2:
    dict2[value] = dict2[value].count('t')
print(dict2)


# Kinda Works
# dictionary_two()

def sets_one():
    s2 = set([])
    s3 = set([])
    s4 = set([])
    i = 0
    j = 0
    k = 0
    while i < 20:
        if i % 2 == 0:
            s2.add(i)
        i += 1
    while j < 20:
        if j % 3 == 0:
            s3.add(j)
        j += 1
    while k < 20:
        if k % 4 == 0:
            s4.add(k)
        k += 1
    print(s2)
    print(s3)
    print(s4)

# Works
# sets_one()


def sets_two():
    _python = {"p", "y", "t", "h", "o", "n"}
    _marathon = {"m", "a", "r", "a", "t", "h", "o", "n"}
    _intersection = _python.intersection(_marathon)
    _union = _python.union(_marathon)
    print(_intersection)
    print(_union)


# Works
# sets_two()
