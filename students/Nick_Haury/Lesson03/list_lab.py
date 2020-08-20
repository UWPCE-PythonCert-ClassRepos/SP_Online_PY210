#!/usr/bin/env python3
'''

'''

# First Series

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)
new_fruit = input("Please enter a fruit to add to the end of the list: ")
fruits.append(new_fruit)
print(fruits)
fruit_index = int(input("Please enter the number place of a fruit in the list: "))
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
