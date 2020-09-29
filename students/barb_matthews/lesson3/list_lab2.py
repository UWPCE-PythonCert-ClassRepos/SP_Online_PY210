#!/usr/bin/env python3

## Lesson 3.2 List Lab
## By: B. Matthews
## 9/15/2020

## Add a fruit to the list
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
yummyfruit = ['something']
delfruit = ['something']
delindex = 0

print("Fruit choices are: ", fruits)
fruits.pop()

print(fruits)
delfruit[0] = input("Enter a fruit to delete >> ")

fruits.remove(delfruit[0])
print(fruits)

#yummyfruit[0] = input("Enter a fruit to add >> ")
#fruits = fruits + yummyfruit
#print("Fruit choices are: ", fruits)

## Ask for a number and display that order of fruit in list
#n = int(input("Enter a number >> "))
#print("You typed: ", n)
#n-=1
#print("Here's your fruit:", fruits[n])

#fruits = ["Lychees"] + fruits
#print("even more fruit!\n", fruits)
#fruits.insert(0,"Watermelons")
#print("so much fruit!\n", fruits)

## Display all fruits beginning with P
#match = "P"
#for i,item in enumerate(fruits):
    #print(item[0][0])
    #if (item[0][0] == match):
        #print("\nFruits with P are found: ", item)