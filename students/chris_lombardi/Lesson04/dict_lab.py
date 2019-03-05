#UWPCE, PY210
#Lesson04, Dict Lab

#!/usr/bin/env python3

#Dictionaries 1
def dict1():
    print("{}Dictionaries 1{}".format('-'*6,'-'*6))
    d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d1)
    del d1['cake']
    d1['fruit'] = 'Mango'
    print(d1.keys())
    print(d1.values())
    print('cake' in d1)
    print('Mango' in d1.values())
    return d1

#Dictionaries 2
def dict2(d1):
    print("{}Dictionaries 2{}".format('-'*6,'-'*6))
    d2 = d1.copy()
    for key in d2:
        num_t = key.lower().count('t')
        d2[key] = num_t
    print(d2)

#Sets 1
def set1():
    print('{}Sets{}'.format('-'*6,'-'*6))
    s2, s3, s4 = set(), set(), set()
    for num in range(20):
        if num % 2 == 0:
            s2.add(num)
        elif num % 3 == 0:
            s3.add(num)
        elif num % 4 == 0:
            s4.add(num)

    print(s2)
    print(s3)
    print(s4)

    print(s3.issubset(s4))
    print(s4.issubset(s2))

#Sets 2
def set2():
    print('{}Sets2{}'.format('-'*6,'-'*6))
    set_py = set(['p', 'y', 't', 'h', 'o', 'n'])
    set_py.add('i')
    set_mar = frozenset(['m', 'a', 'r', 'a', 't', 'h', 'o', 'n'])
    print("Union:")
    print(set_py.union(set_mar))
    print("Intersection:")
    print(set_py.intersection(set_mar))

if __name__ == '__main__':
    d1 = dict1()
    dict2(d1)
    set1()
    set2()