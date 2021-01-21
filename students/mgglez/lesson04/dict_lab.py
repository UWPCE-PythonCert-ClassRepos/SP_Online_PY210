#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson04 - Activity 4.1 - Dict Lab
# Description: Exercise from Lesson04 - Dict Lab
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-10-2021, Developed Dict Lab Exercise
# ------------------------------------------------------------------------------ #

def dictionaries_1():
    """
    Implement all the instructions from Dict Lab dictionaries 1
    """
    # Create a dictionary containing “name”, “city”, and “cake” for “Chris”
    # from “Seattle” who likes “Chocolate” (so the keys should be: “name”,
    # etc, and values: “Chris”, etc.)
    person_dict = {
        'name': 'Chris',
        'city': 'Seattle',
        'cake': 'Chocolate'
    }
    # Display the dictionary.
    print(person_dict)
    for k,v in person_dict.item():
        print(k, v)
    # Delete the entry for “cake”.
    person_dict.pop('cake')
    #Display the dictionary.
    print(person_dict)
    for k, v in person_dict.item():
        print(k, v)
    # Add an entry for “fruit” with “Mango” and display the dictionary.
    person_dict['fruit'] = 'Mango'
    print(person_dict)
    #     Display the dictionary keys.
    print(person_dict.keys())
    #     Display the dictionary values.
    print(person_dict.values())
    #     Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    print('cake' in person_dict)
    #     Display whether or not “Mango” is a value in the dictionary (i.e. True).
    print('Mango' in person_dict.values())

def dictionaries_2():
    """
    Implement all the instructions from Dict Lab dictionaries 2
    """
    # Using the dictionary from item 1: Make a dictionary using the same keys
    # but with the number of ‘t’s in each value as the value (consider upper
    # and lower case?).
    person_dict = {
        'name': 'Chris',
        'city': 'Seattle',
        'cake': 'Chocolate'
    }
    new_person_dict = {}
    for k,v in person_dict.items():
        new_person_dict[k] = v.lower().strip().count('t')
    print(new_person_dict)

def sets_1():
    """
    Implement all the instructions from Dict Lab sets 1
    """
    # Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    # divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
    s2, s3, s4 = set(), set(), set()
    for num in range(21):
        if num%2 == 0:
            s2.add(num)
        if num%3 == 0:
            s3.add(num)
        if num%4 == 0:
            s4.add(num)
    # Display the sets
    print(s2)
    print(s3)
    print(s4)
    # Display if s3 is a subset of s2 (False)
    print(s3.issubset(s2))
    # and if s4 is a subset of s2 (True).
    print(s4.issubset(s2))

def sets_2():
    """
    Implement all the instructions from Dict Lab sets 2
    """
    # Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    s = set('Python')
    s.add('i')
    # Create a frozenset with the letters in ‘marathon’.
    fs = frozenset('marathon')
    # Display the union and intersection of the two sets.
    union = s.union(fs)
    print(union)
    intersection = s.intersection(fs)
    print(intersection)

if __name__ == "__main__":
    dictionaries_1()
    dictionaries_2()
    sets_1()
    sets_2()