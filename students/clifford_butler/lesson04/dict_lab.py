#!/usr/bin/env python3

'''
Goal:
Learn the basic ins and outs of Python dictionaries and sets.

Dictionaries 1

Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate” (so the keys should be: “name”, etc, and values: “Chris”, etc.)
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
    Display the dictionary keys.
    Display the dictionary values.
    Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
    Display whether or not “Mango” is a value in the dictionary (i.e. True).
'''

# Create a dictionary, add specified keys and values
d = {}

def add_to_d():
    d['name'] = 'Chris'
    d['city'] = 'Seattle'
    d['cake'] = 'Chocolate'

def check_for_key(n):
    # Dsiplay whether or not the key is in the dictionary
    while True:
        if n in d.keys():
            print('True! {} is a key in the dictionary'.format(n))
            break
        
        print('False! {} is not a key in the dictionary.'.format(n))
        break
    
def check_for_value(n):
    # Dsiplay whether or not the key is in the dictionary
    while True:
        if n in d.values():
            print('True! {} is a value in the dictionary'.format(n))
            break
        
        print('False! {} is not a value in the dictionary.'.format(n))
        break    

def main():
    
    # Add keys and values to the dictionary
    add_to_d()
    
    # Display the dictionary
    print(d)

    # Delete the entry cake
    d.pop('cake')

    # Display the dictionary
    print(d)

     # Add an entry for “fruit” with “Mango” and display the dictionary
    d['fruit'] = 'Mango'

    # Display the dictionary keys
    print(d.keys())

    # Display the dictionary values
    print(d.values())
    
    # check if n is a key in the dictionary
    check_for_key('cake')
    
    # check if n is a value in the dictionary
    check_for_value('Mango')
    
    
if __name__ == '__main__':
   main()
   
   