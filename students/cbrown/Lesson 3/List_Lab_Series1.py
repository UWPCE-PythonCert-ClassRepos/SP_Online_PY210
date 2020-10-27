#!/usr/bin/#!/usr/bin/env python3

#List Lab Excercise. Lesson 3, series 1

fruits = ['Apples','Pears','Oranges','Peaches']
print(fruits)

fruit = input("What Fruit Do You Like? ")

fruits.append(fruit)
print(fruits)

number = int(input("What's Your Favorite Number? "))
print('Your Number is ',number)

try:
    print('Your Fruit is ',fruits[number + 1])

except:
    print("Oops! That number doesn't match a fruit!")

fruits = fruits + ['Blackberries']
print(fruits)

fruits.insert(0,"Grapes")
print(fruits)

for item in fruits:
    if item[0] == 'P':
        print(item)
