#!/usr/bin/env python3

"""
List Lab 
Goal - Learn the basic ins and outs of Python lists.
Author: Clifford Butler
"""

"""
Series 1
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]

for item in (fruit_list):
    """Display each item in the list """
    print(item)

#ask the user for another fruit 
response = input("Enter the fruit you would like to add to the list: ")

if response not in fruit_list:
    """Add user input to the end of fruit_list """
    fruit_list.append(response)
else: print("Already in list!")
    
print(fruit_list)

#ask the user for a number
response2 = input("Enter a number: ")

for i, item in enumerate(fruit_list):
    """Display the number the user input and the fruit corresonding to that number """
    i += 1
    print(response2, fruit_list[int(response2) - 1])
    break    