#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:47:58 2020

@author: jaked

**Series 1**
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.

**Series 2**
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

**Series 3**
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.

**Series 4**
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.

"""
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruit_num = 0

#Series_1
print("Series 1:")
print()
fruits_series_1 = fruits

print(fruits_series_1)

new_fruit = input("Please add another fruit: ")

fruits_series_1.append(new_fruit)

print(fruits_series_1)

fruit_num = int(input("Please select a fruit by number: "))

print("User selection: " + str(fruit_num))
print("Selected Fruit: " + fruits_series_1[fruit_num - 1])

print()
print("Add Grapes:")
fruits_series_1  = ["Grapes"] + fruits
print(fruits_series_1)

print()
print("Add Watermellon:")
fruits_series_1.insert(0, "Watermellon")
print(fruits_series_1)
print()

print("Fruits starting with 'P'")
for i in fruits_series_1:
    if i[0] == "P":
       print(i)
print()

#Series_2
print("Series 2:")
print()
fruits_series_2 = fruits_series_1
print(fruits_series_2)
fruits_series_2.pop()
print(fruits_series_2)
del_fruit = input("Input a fruit to delete: ")
fruits_series_2.remove(del_fruit)
print(fruits_series_2)
print()

#Series 3
print("Series 3:")
print()
print(fruits_series_1)
fruits_series_3 = fruits_series_1[:]
fruit_ans = ""

for i in fruits_series_3[:]:
    fruit_ans = input("Do you like " + i.lower() + " ? ")
    while fruit_ans not in ['yes', 'no']:
        fruit_ans = input ("Please input yes or no. ")
    if fruit_ans == 'no':
        fruits_series_3.remove(i)

print(fruits_series_3)
print()

#Series 4
fruits_series_4 = []

for i in fruits_series_1[:]:
    fruits_series_4.append(i[::-1])
fruits_series_1.pop()
print(fruits_series_4)
print(fruits_series_1)
