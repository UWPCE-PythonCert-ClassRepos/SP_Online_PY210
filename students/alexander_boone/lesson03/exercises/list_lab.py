#!/usr/bin/env python3


# --------------------------------------------------- SERIES 1 -----------------------------------------------------
l = ["Apples", "Pears", "Oranges", "Peaches"]
print(l)

l.append(input("Enter the name of another fruit: "))
print(l)

# ask user for number and display corresponding list element (starting index of 1)
user_choice = int(input("Enter a number: ")) - 1
print(l[user_choice])

# add item to beginning of list
l = [input("Enter the name of another fruit: ")] + l[:]
print(l)

# add another item to beginning of list
l.insert(0, input("Enter the name of another fruit: "))
print(l)

# display items that begin with a p
for fruit in l:
    if fruit[0] == "P" or fruit[0] == "p":
        print(fruit)

# --------------------------------------------------- SERIES 2 -----------------------------------------------------

# display list
print(l)

# remove last element from list
l.pop()
print(l)

# prompt user for element to delete
fruit_delete = input("Enter the name of a fruit to remove from the list: ")
l.remove(fruit_delete)
print(l)

# --------------------------------------------------- SERIES 3 -----------------------------------------------------

