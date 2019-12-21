#!/usr/bin/env python3

def dict_test_one(): 

    about_chris = {
        'name' : 'Chris', 
        'city' : 'Seattle', 
        'cake' : 'German Chocolate'
    }

    print(about_chris)

    print("[+] deleting cake..")
    del about_chris['cake']

    print(about_chris)

    about_chris['fruit'] = 'Mango'

    print("[+] about_chris keys")
    for key in about_chris.keys(): 
        print(key) 

    print("[+] about_chris values")
    for value in about_chris.values():
        print(value)

    print("[+] is there cake? ", end='')
    if 'cake' in about_chris: 
        print("True!")
    else: 
        print("False!")

    print("[+] is there a mango? ", end='')
    if 'Mango' in about_chris.values(): 
        print("True!")
    else:
        print("False!")
    
    return about_chris

def dict_test_two(): 
    """
    calculates the number of t's in value, per dict key 
    """
    # mapping of about_chris dict keys to num of t's per value.
    num_of_ts = {}
    about_chris = dict_test_one()
    
    count_of_ts = 0 
    for key,value in about_chris.items(): 
        for c in value: 
            if c == 't':
                count_of_ts = count_of_ts + 1 
        num_of_ts[key] = count_of_ts
        # reset count for next iteration.
        count_of_ts = 0
    print("[+] number of t's per key..")
    print(num_of_ts)

def set_test_one():
    """
    computes a set of values divisible by 2, 3, and 4, respectively. 
    """

    divisible_by_2 = [] 
    divisible_by_3 = []
    divisible_by_4 = [] 

    for value in range(0, 21):
        if value % 2 == 0: 
            divisible_by_2.append(value) 
        if value % 3 == 0:
            divisible_by_3.append(value) 
        if value % 4 == 0: 
            divisible_by_4.append(value)
    
    s2 = set(divisible_by_2) 
    print("[+] Displaying set 2..")
    print(s2)

    s3 = set(divisible_by_3)
    print("[+] Displaying set 3..")
    print(s3)

    s4 = set(divisible_by_4)
    print("[+] Displaying set 4..")
    print(s4)
    
    print("[+] Performing is subset checks..")
    if s3.issubset(s2):
        print("Set 3 is subset of Set 2")
    if s4.issubset(s2): 
        print("Set 4 is subset of Set 2")

def set_test_two(): 
    """
    demonstrates the difference between a set and a 
    frozen set. Note: add, and update features are 
    not available in a frozen set.
    """
    python_set = set(list("Python"))
    python_set.add('i')
    print("[+] Python Set: ", python_set)

    marathon_frozen_set = frozenset(list("marathon"))
    print("[+] Marathon Frozen set: ", marathon_frozen_set)

    print("[+] Union of Python Set and Marathon Frozen Set..")
    print(python_set.union(marathon_frozen_set))

    print("[+] Intersection of Python Set and Marathon Frozen Set..")
    print(python_set.intersection(marathon_frozen_set))

if __name__ == '__main__':
    #dict_test_one()
    #dict_test_two()
    #set_test_one()
    set_test_two()
