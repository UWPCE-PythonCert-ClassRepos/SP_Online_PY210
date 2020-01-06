#!/usr/bin/env python3


# Series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruits)

useradd = input("Please enter another fruit: ")

useradd = useradd.capitalize()

fruits.append(useradd)

print(fruits)

i = str(len(fruits))

userindex = int(input("Please enter a number between 1 and " + i + ": ")) - 1

while userindex <= len(fruits) - 1:
    userindex = int(input("Please enter a number between 1 and " + i + ": ")) - 1

print(fruits[userindex])
