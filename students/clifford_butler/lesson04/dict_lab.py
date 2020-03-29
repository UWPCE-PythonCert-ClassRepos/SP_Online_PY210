#!/usr/bin/env python3

'''
Goal:
Learn the basic ins and outs of Python dictionaries and sets.

Dictionaries 1

Create a dictionary containing “name”, “city”, and “cake” for “Chris” from 
“Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and 
values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).


Dictionaries 2

Using the dictionary from item 1: Make a dictionary using the same keys but with 
the number of ‘t’s in each value as the value (consider upper and lower case?).

Sets

Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible by 2, 3 and 4 (figure out a way to compute those – don’t just type them in).
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).

Sets 2

Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’.
Display the union and intersection of the two sets.
'''
# Create a dictionary, add specified keys and values
d = {}
d = {'name': "Chris", 'city': "Seattle", 'cake': "Chocolate"}

def d_one(d):
    # Create a dictionary, remove cake and add fruit
    dict_one = d.copy()
    print(dict_one)
    dict_one.pop('cake')
    print(dict_one)
    dict_one['fruit'] = 'Mango'
    print(dict_one)
    print(dict_one.keys())
    print(dict_one.values())
    
    # Dsiplay whether or not the key is in the dictionary
    while True:
        i = 'cake'
        if i in dict_one.keys():
            print('True! {} is a key in the dictionary'.format(i))
            break
        
        print('False! {} is not a key in the dictionary.'.format(i))
        break
    
    # Dsiplay whether or not the key is in the dictionary
    while True:
        n = 'Mango'
        if n in dict_one.values():
            print('True! {} is a value in the dictionary'.format(n))
            break
        
        print('False! {} is not a value in the dictionary.'.format(n))
        break    

def d_two():
    '''
    Using the dictionary from item 1: Make a dictionary using the 
    same keys but with the number of ‘t’s in each value as the value 
    (consider upper and lower case?).
    '''
    dict_two = d.copy()
    for k, v in dict_two.items():
        dict_two[k.lower()] = v.lower()
    for i in dict_two: 
        dict_two[i] = dict_two[i].count('t')
    print(dict_two)
    
def sets(n):
    a_list=[]
    for i in range(21):
        if i % n == 0:
            a_list.append(i)
    a_set = set(a_list)
    return a_set

def main():
    
    print ('Dictionaries 1: \n')
    
    d_one(d)
   
    print ('\n' + 'Dictionaries 2: \n')
    
    d_two()
    
    print ('\n' + 'Sets: \n')
    
    # create sets
    s2 = sets(2)
    s3 = sets(3)
    s4 = sets(4)
    
    # display sets
    print('s2:', s2)
    print('s3:', s3)
    print('s4:', s4)
    
    # display if s3 is subset of s3, and if s4 is a subset of s2
    print (s3.issubset(s2))
    print (s4.issubset(s2))
    
    print ('\n' + 'Sets 2: \n')
    
    # create a set with the letters in ‘Python’ and add ‘i’ to the set.
    set_letters = set({"P", "y", "t", "h", "o", "n"})
    set_letters.add("i")
    
    # create a frozenset with the letters in ‘marathon’
    frozenset_letters = frozenset({"m", "a", "r", "a", "t", "h", "o", "n"})
    
    # display the union and intersection of the two sets
    print(set_letters.union(frozenset_letters))
    print(set_letters.intersection(frozenset_letters))
    
if __name__ == '__main__':
   main()
   