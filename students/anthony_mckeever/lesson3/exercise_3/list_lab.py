#!/usr/bin/env python3

"""
Programming In Python - Lesson 3 Exercise 3: List Lab
Code Poet: Anthony McKeever
Start Date: 07/30/2019
End Date: 07/30/2019
"""

def get_fruit():
    return input("Give me another fruit! > ")

def print_fruit(fruits_list, msg="Current Fruit:"):
    print(msg,  fruits_list, "\n")

print("Series 1: Fun with Fruit!\n")

fruits_list = ["Apples", "Pears", "Oranges", "Peaches"]
print_fruit(fruits_list)

fruits_list.append(get_fruit())
print_fruit(fruits_list)

fruit = input(f"Choose a number between 1 and {len(fruits_list)} > ")
print(f"You chose {fruit}: {fruits_list[int(fruit) - 1]}")

fruits_list = [get_fruit()] + fruits_list
print_fruit(fruits_list)

fruits_list.insert(0, get_fruit())
print_fruit(fruits_list)

for fruit in fruits_list:
    if fruit[0] == "P":
        print(fruit)

print("\nSeries 2: Deleting Fruit!\n")
fruits_list2 = fruits_list[:]
print_fruit(fruits_list2)

fruits_list2 = fruits_list2[:-1]
print_fruit(fruits_list2)

# Bonus - Multiple the list times two and delete all instances of a fruit
fruits_list2 = fruits_list2 * 2

while fruit != "" and fruit != "exit":
    fruit = input("Delete a fruit?  (leave empty or send \"exit\" to stop) > ")
    for del_fruit in fruits_list2:
        if fruit == del_fruit:
            fruits_list2.remove(fruit)

print_fruit(fruits_list2, "Remaining fruit:")

print("\nSeries 3: Do you like this fruit?\n")
fruits_list3 = fruits_list[:]

for fruit in fruits_list:
    choice = input(f"Do you like {fruit}? > ")
    
    if choice.lower() not in ["yes", "no"]:
        while choice.lower() not in ["yes", "no"]:
            choice = input("A simple \"yes\" or \"no\" please... > ")
    elif choice.lower() == "yes":
        fruits_list3.remove(fruit)
else:
    print_fruit(fruits_list3, "So you like:")

print("\nSeries 4: tiurF esreveR (Reverse Fruit)\n")
fruits_list4 = [x[::-1] for x in fruits_list]
fruits_list = fruits_list[:-1]

print_fruit(fruits_list, "Original Fruit: ")
print_fruit(fruits_list4, "Reversed Fruit: ")
