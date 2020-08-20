#!/usr/bin/env python3
'''

'''

# Series 1

print("Series 1")
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

# Series 2

print("")
print("Series 2")
print(fruits)
fruits.pop()
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
