#!/usr/bin/env python3
'''
This Script is meant to be a practice in manipulating lists.  It starts
with a list of fruits, upon which copies are made, and modifications are
made to either the original list, the copy, or even both.
'''

# Series 1

print("Series 1")
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
new_fruit = input("Please enter a fruit to add to the end of the list: ")
fruits.append(new_fruit)
print(fruits)
fruit_index = int(input("Please enter the number place of a fruit in the "
                        "list: "))
print(str(fruit_index) + ": " + fruits[fruit_index - 1])
fruits = ["Mangoes"] + fruits
print(fruits)
fruits.insert(0, "Blueberries")
print(fruits)
temp_fruits = []
for fruit in fruits:
    if fruit.lower()[0] == "p":
        temp_fruits.append(fruit)
print(temp_fruits)

# Series 2

print("")
print("Series 2")
print(fruits)
fruits2 = fruits[:]
fruits2.pop()
print(fruits)
found_fruit = False
while not found_fruit:
    fruit_to_remove = input("what fruit (case sensitive) should be removed?: ")
    if fruit_to_remove in fruits:
        for i in range(fruits.count(fruit_to_remove)):
            fruits.remove(fruit_to_remove)
        found_fruit = True
    else:
        fruits = fruits * 2
print(fruits)

# Series 3

print("")
print("Series 3")
yes_no_input = ""
fruits_copy = fruits[:]
for fruit in fruits_copy:
    yes_no_input = ""
    while yes_no_input not in ("yes", "no"):
        yes_no_input = input("Do you like " + fruit.lower() + "?: ")
        if yes_no_input not in ("yes", "no"):
            print("answer must be 'yes' or 'no'")
        elif yes_no_input == "no":
            fruits.remove(fruit)
print(fruits)

# Series 4

print("")
print("Series 4")
fruits_reversed = []
for fruit in fruits:
    fruits_reversed.append(fruit[::-1])
fruits.pop()
print(fruits)
print(fruits_reversed)
