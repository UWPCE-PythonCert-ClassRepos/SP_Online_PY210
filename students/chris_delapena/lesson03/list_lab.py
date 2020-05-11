#!/usr/bin/env python3

#Chris Dela Pena
#UW PCE PY210
#Lesson 3.2 List Lab

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

#Ask user for another fruit and add to list
addFruit = input("Enter a new fruit to the list: ")
fruit.append(addFruit)
print(fruit)
