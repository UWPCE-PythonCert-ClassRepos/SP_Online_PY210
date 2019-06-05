#!/usr/bin/env  python

# Item 1
main_dict = {"name": "Chris",
             "city": "Seattle",
            "cake": "Chocolate",
             }

def display(main_thingy):
    print(main_thingy)

def deletey(main_thingy):
    main_thingy.pop('cake')
    display(main_thingy)

def fruity(main_thingy):
    main_thingy['fruit'] = 'Mango'
    display(main_thingy)
    print('cake' in main_thingy.keys())
    for key in main_dict:
        if 'Mango' in main_dict[key]:
            print('True')

# Item 2

def tees():
    main_thingy = {"name": "Chris",
             "city": "Seattle",
            "cake": "Chocolate",
             }
    for key in main_thingy:
        main_thingy[key] = main_thingy[key].lower().count('t')
    print(main_thingy)

# Sets 1
def set1():
    s2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    s3 = {3, 6, 9, 12, 15, 18}
    s4 = {4, 8, 12, 16, 20}
    display(s2)
    display(s3)
    display(s4)
    print("s3 is a subset of s2: " + str(s3.issubset(s2)))
    print("s4 is a subset of s2: " + str(s4.issubset(s2)))

# Sets 2
#
#    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
#    Create a frozenset with the letters in ‘marathon’.
#    display the union and intersection of the two sets.

def set2():
    s1 = set('python')
    s1.add('i')
    s5 = frozenset('Marathon')
    print(s5.union(s1))
    print(s5.intersection(s1))

if __name__ == "__main__":

    display(main_dict)
    deletey(main_dict)
    fruity(main_dict)
    tees()
    set1()
    set2()
