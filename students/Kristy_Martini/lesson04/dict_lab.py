#!/usr/bin/env python3
$ chmod +x dict_lab.py

def dict1(test_dict):
    # Create a dictionary containing name, city, and cake. Display result
    dict1 = test_dict
    print(dict1)
    # Delete the entry for cake and display result
    dict1.pop('cake')
    print(dict1)
    # Add entry for fruit as key with 'mango'. Display result
    dict1['fruit'] = 'mango'
    print(dict1)
    # Display the dictionary keys
    print("The dictionary keys are: ", dict1.keys())
    # Display the dictionary values
    print("The dictionary values are: ",dict1.values())
    # Display whether or not "cake" a key in the dictionary
    print("The dictionary contains the key 'cake'? ", dict1.get('cake', 'False'))
    # Display whether or not "mango" is a value in the dictionary
    print("The dictionary contains the value 'mango'? ", bool('mango' == dict1.get('fruit')))

def dict2(test_dict):
    # Count number of t's in each key's value 
    # Display new test dictionary
    for item in test_dict:
        word = test_dict[item]
        test_dict[item] = word.count('t')
    print(test_dict)

def sets1():
    # Create the sets
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range(20):
        if not (i % 2):
            s2.add(i)
        if not (i % 3):
            s3.add(i)
        if not (i % 4):
            s4.add(i)
    # Display the sets
    print("s2: ", s2)
    print("s3: ", s3)
    print("s4: ", s4)
    # Display if s3 is a subset of s2
    print("Is s3 a subset of s2? ", s3.issubset(s2))
    # Display if s4 is a subset of s4
    print("Is s4 a subset of s2? ", s4.issubset(s2))

def sets2():
    # Create the set for 'python'
    python_set = set()
    for letter in "python":
        python_set.add(letter)
    python_set.add("i")
    print(python_set)
    # Create the frozenset for 'marathon'
    marathon_set = set()
    for letter in "marathon":
        marathon_set.add(letter)
    marathon_fs = frozenset(marathon_set)
    print(marathon_fs)
    # Display the unuion and intersection between the sets
    print("Union of sets 'python' and 'marathon': ", python_set.union(marathon_fs))
    print("Intersection of sets 'python' and 'marathon': ", python_set.intersection(marathon_fs))

if __name__ == "__main__":
    test_dict = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}
    dict1(test_dict)
    dict2(test_dict)
    sets1()
    sets2()