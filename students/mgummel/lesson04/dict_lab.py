#!/usr/bin/env python3

def dict_exercise1():
    #Dictionaries 1
    information = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(information)

    #Make copy for exercise 2
    exercise2_copy = information.copy()

    information.pop('cake')
    information['fruit'] = 'Mango'
    
    print("\nThese are the current keys")
    for key in information.keys():
        print(key)
    
    print("\nThere are the current values")
    for value in information.values():
        print(value)

    print("\n\n")
    print('cake' in information.keys())
    print('Mango' in information.values())

    #Dictionary exercise 2
    print("\nThis the dictionary 2 section")
    t_dict = {}
    for key, value in exercise2_copy.items():
        t_dict[key] = value.count('t')
    print(t_dict)


#Set exercise for the lab.
def set_exercise():
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))

    print(f"This is s2: {s2}")
    print(f"This is s3: {s3}")
    print(f"This is s4: {s4}")

    print(f"Is a s3 a subset of s2? {s3.issubset(s2)}")
    print(f"Is a s4 a subset of s2? {s4.issubset(s2)}")

    #Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    #Create a frozenset with the letters in ‘marathon’.
    #Display the union and intersection of the two sets.
    mutable_set = set("Python")
    mutable_set.update("s")
    print(mutable_set)
    frozen = frozenset('marathon') 

    print(mutable_set.union(frozen))
    print(mutable_set.intersection(frozen))

if __name__ == '__main__':
    dict_exercise1()
    set_exercise()