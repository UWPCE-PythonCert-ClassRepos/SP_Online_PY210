#!/usr/bin/env python3

# Dictionary with name, city, and cake
main_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}


def print_dict(printer):
    for i in printer:
        print(f'{i}: {printer[i]}')
    print('----------------------------')
    return


def dict_1(dict1):
    print('------------Dictionaries 1------------')
    # Print dict1
    print_dict(dict1)
    # Delete entry for "cake"
    dict1.pop('cake')
    # Print dict1
    print_dict(dict1)
    # Add an entry for fruit (mango)
    dict1['fruit'] = 'mango'
    # Print dict1
    print_dict(dict1)
    # Display dict keys
    print(dict1.keys())
    print(dict1.values())
    # Print check for cake as a key
    print('cake' in dict1.keys())
    # Print check for mango as a value
    print('mango' in dict1.values())
    return


def dict_2(dict2):
    print('------------Dictionaries 2------------')
    # Create dict with number of T's
    for i, j in dict2.items():
        counter = j.count('t')
        dict2[i] = counter
    print_dict(dict2)
    return


def sets_1():
    print('----------------Sets------------------')
    # Create s2, s3, s4
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(0, 20):
        if i % 2 == 0:
            s2.update([i])
        if i % 3 == 0:
            s3.update([i])
        if i % 4 == 0:
            s4.update([i])
    # Display sets
    print(f' Set s2: {s2}')
    print(f' Set s3: {s3}')
    print(f' Set s4: {s4}')

    # Print check for s3 as subset of s2
    print(f' s3 is a subset of s2: {s3.issubset(s2)}')
    # Print check for s4 as subset of s2
    print(f' s4 is a subset of s2: {s4.issubset(s2)}')
    return


def sets_2():
    print('----------------Sets 2----------------')
    sp = {'P', 'y', 't', 'h', 'o', 'n'}
    sp.update(['i'])

    sm = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
    print(f'Union of Python and Marathon: {sm.union(sp)}')
    print(f'Intersection of Python and Marathon: {sm.intersection(sp)}')
    return


if __name__ == "__main__":
    dict_1(main_dict)
    dict_2(main_dict)
    sets_1()
    sets_2()
