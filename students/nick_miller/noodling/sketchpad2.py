#!/usr/bin/env python3

print("Begin series 3:")
print()

fruits = ["Oranges", "Peaches", "Apples", "Pineapples"]
delfruits = []
for fruit in fruits:
    question = "Do you like " + fruit + "? (y/n): "
    yesorno = input(question)
    drop = fruits.index(fruit)
    while yesorno != "y" and yesorno != "n":
        yesorno = input("Please enter y or n: ").lower()
    if yesorno == "n":
        delfruits.append(drop)
for i in delfruits:
    fruits[i] = '!'
for i in range(0, fruits.count('!')):
    fruits.remove('!')
print(fruits)
