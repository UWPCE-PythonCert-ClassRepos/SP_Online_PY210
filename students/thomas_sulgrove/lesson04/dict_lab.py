#!/usr/bin/env python3
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html

#Dict1
def dictionaries_1():
    #create a dict contatining name, city and cake, for chris from seattle who likes chocolate
    dict1 = {"Name": "Chris",
             "City": "Seattle",
             "Cake": "Chocolate"
             }
    #display the dict
    print(dict1)
    #delete Cake entry
    del(dict1["Cake"])
    #display
    print(dict1)
    #add in entry for fruit with mango 
    dict1.update({'Fruit' : "Mango"})
    #display
    print(dict1)
    #display keys
    for key, value in dict1.items() :
        print (key)
    #discplay values
    for key, value in dict1.items() :
        print (value)
    #display whether nor not cake is a key
    print("Cake" in dict1)
    #display whether nor not mango is a value
    print('Mango' in dict1.values())
    pass


def dictionaries_2():
    dict2 = {"Name": "Chris",
             "City": "Seattle",
             "Cake": "Chocolate"
             }
    
    for key, value in dict2.items():
        dict2[key] = value.lower().count("t")
    print(dict2)
    pass

def sets():
    s2 = set([])
    s3 = set([])
    s4 = set([])
    for i in range(0,21):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i)
        if i % 4 == 0:
            s4.add(i)
    print(s2)
    print(s3)
    print(s4)
    print(s3 < s2)
    print(s4 < s2)

def sets_2():
    py_set = set(["P", "y", "t", "h", "o", "n"])
    py_set.add("i")
    mar_set = frozenset(['e', 'g', 'f'])
    print(py_set | mar_set)
    print(py_set & mar_set)
    
    
    
    
    
    
    
    
    
    
    
