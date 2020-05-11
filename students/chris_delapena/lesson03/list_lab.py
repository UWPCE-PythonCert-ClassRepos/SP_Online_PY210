#!/usr/bin/env python3

#Chris Dela Pena
#UW PCE PY210
#Lesson 3.2 List Lab

#Series 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

#Ask user for another fruit and add to list
addFruit = input("Enter a new fruit to the list: ")
fruit.append(addFruit)
print(fruit)

#Ask user for a number and display number and fruit
numFruit = int(input('Enter a number between 1 and ' + str(len(fruit)) + ': '))
print("#" + str(numFruit) + " fruit is " + fruit[numFruit - 1])

#Add fruit to beginning of list using "+" and display list
print("Adding kiwi to the list")
addFruit2 = ['Kiwi']
fruit = addFruit2 + fruit
print(fruit)

#Add another fruit to the beginning of the list using insert() and display list
print("Adding pineapple to the list")
addFruit3 = 'Pineapple'
fruit.insert(0, addFruit3)
print(fruit)

#Display all fruits that begin with "P" using for loop
print("displaying only fruits beginning with a 'P'")
for n in fruit:
    if n[0] == "P":
        print(n)
