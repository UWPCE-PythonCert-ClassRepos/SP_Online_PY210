"""Lesson 03 | List Lab"""
# Goal: Learn the basic ins and outs of Python lists.
#
# Hint: to query the user for info at the command line, you use:
# response = input("a prompt for the user > ")
# response will be a string of whatever the user types (until a <return>).


#!/usr/bin/env python3

"""Series 1: Create a list of fruit."""

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

# Ask the user for another fruit and add it to the end of the list.
response = input('Enter a fruit to add > ')
fruit.append(response)
# Display the list.
print(fruit)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
response = input('Pick a number between 1 and ' + str(len(fruit)) + ' > ')
print(int(response), ' | ', fruit[int(response)-1])


# Add another fruit to the beginning of the list using “+” and display the list.
fruit = ["Banana"] + fruit
print(fruit)

# Add another fruit to the beginning of the list using insert() and display the list.
fruit.insert(0,"Kiwi")
print(fruit)

# Display all the fruits that begin with “P”, using a for loop.
fruit_with_p = []
for item in fruit:
    if item.upper().startswith('P'):
        fruit_with_p.append(item)
print(fruit_with_p)
