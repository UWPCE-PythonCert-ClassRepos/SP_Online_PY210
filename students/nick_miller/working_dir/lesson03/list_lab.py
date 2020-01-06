#!/usr/bin/env python3

"""PY210_SP - list_lab
author: Nick Miller"""

# Begin series 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.

fruits = ["Oranges", "Peaches", "Apples", "Pineapples"]

# Display the list (plain old print() is fine…).

print(fruits, "\n")

# Ask the user for another fruit and add it to the end of the list.

userAdd = input("Enter a fruit: ")

userAdd = userAdd.capitalize()

fruits.append(userAdd)

# Display the list.

print(fruits, "\n")

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
# (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.

# still need to do this one

# Add another fruit to the beginning of the list using “+” and display the list.

userAdd = input("Enter another fruit: ")

userAdd = [userAdd.capitalize()]

fruits = userAdd + fruits

print(fruits, "\n")

# Add another fruit to the beginning of the list using insert() and display the list.

userAdd = input("Enter another fruit: ")

userAdd = userAdd.capitalize()

fruits.insert(0, userAdd)

print(fruits, "\n")

# Display all the fruits that begin with “P”, using a for loop.

l = len(fruits)

pfruits = []

for i in range(l):
    if fruits[i][0] == "P":
        pfruit = fruits[i]
        pfruits.insert(0, pfruit)

print(pfruits, "\n that was the end of series 1\n")

# End series 1

# Begin series 2

# Display the list.

print("begin series 2:\n", fruits, "\n")

# Remove the last fruit from the list.

del fruits[-1]

# Display the list.

print(fruits, "\n")

# Ask the user for a fruit to delete, find it and delete it.
