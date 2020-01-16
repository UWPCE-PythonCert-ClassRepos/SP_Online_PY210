#!/usr/bin/env python3

"""PY210_SP - exercise 3.2 - list_lab
author: Nick Miller"""

# Begin series 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.

fruits = ["Oranges", "Peaches", "Apples", "Pineapples"]

# Display the list (plain old print() is fine…).

print(fruits)
print()

# Ask the user for another fruit and add it to the end of the list.

userAdd = input("Enter a fruit: ")

userAdd = userAdd.capitalize()

fruits.append(userAdd)

# Display the list.

print(fruits)
print()

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number
# (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.

while True:
    try:
        userPick = int(input("Pick a number between 1 and 5: "))
        if userPick in range(6):
            break
    except:
        pass
    print('\nIncorrect input, try again')

userPick = userPick - 1

print((userPick + 1), fruits[userPick])
print()

# Add another fruit to the beginning of the list using “+” and display the list.

userAdd = input("Enter another fruit: ")

userAdd = [userAdd.capitalize()]

fruits = userAdd + fruits

print(fruits)
print()

# Add another fruit to the beginning of the list using insert() and display the list.

userAdd = input("Enter another fruit: ")

userAdd = userAdd.capitalize()

fruits.insert(0, userAdd)

print(fruits)
print()

# Display all the fruits that begin with “P”, using a for loop.

pfruits = []

for i in range(len(fruits)):
    if fruits[i][0] == "P":

        pfruit = fruits[i]
        pfruits.insert(0, pfruit)

print("Here are all the fruit in the list that start with 'P'.")
print(pfruits)
print()

print("That was the end of series 1.")
print()

# End series 1

# Begin series 2

# Display the list.

print("Begin series 2:")
print()

print(fruits)

# Remove the last fruit from the list.

del fruits[-1]

# Display the list.

print(fruits)
print()

# Ask the user for a fruit to delete, find it and delete it.
usrChoose = input("Enter a fruit to remove from the list: ")

usrChoose = usrChoose.strip()
usrChoose = usrChoose.capitalize()

while usrChoose not in fruits:
    usrChoose= input("Sorry, that fruit is not in the list, enter a fruit to remove from the list: ")
    usrChoose = usrChoose.strip()
    usrChoose = usrChoose.capitalize()

while usrChoose in fruits:
    fruits.remove(usrChoose)

print(fruits)
print()

# Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.

print("Bonus: ")
fruits = fruits * 2

usrChoose = input("Enter a fruit to remove from the list: ")

usrChoose = usrChoose.strip()
usrChoose = usrChoose.capitalize()

while usrChoose not in fruits:
    usrChoose = input("Sorry, that fruit is not in the list, enter a fruit to remove from the list: ")
    usrChoose = usrChoose.strip()
    usrChoose = usrChoose.capitalize()

while usrChoose in fruits:
    fruits.remove(usrChoose)

print(fruits)
