#!/usr/bin/env python3

# Series 1
print('===========================')
print('Series 1')
fruits = ["Apples","Pears","Oranges","Peaches"]

print('fruits = {}'.format(fruits))

new_fruit = input("Add another fruit: ")

fruits.append(new_fruit.title())

print('fruits = {}'.format(fruits))

NumInvalid = 1
while NumInvalid:
    number = input("Type a number between 1 and {:d}: ".format(len(fruits)))
    number = int(number)
    if number > 0 and number < (len(fruits)+1):
        NumInvalid=0

print("{:d} {}".format(number,fruits[number-1]))

new_fruit2 = input("Add another fruit: ")

fruits = fruits + [new_fruit2.title()]

print('fruits = {}'.format(fruits))

new_fruit3 = input("Add another fruit: ")

fruits.insert(0,new_fruit3.title())

print('fruits = {}'.format(fruits))

for fruit in fruits:
    if fruit[0] == "P":
        print(fruit)



print('End Series 1')
print('===========================')

# Series 2
print("Series 2")

fruits2 = fruits[:]

print('fruits2 = {}'.format(fruits2))

fruits2.pop()

print('fruits2 = {}'.format(fruits2))

Del_fruit = input("Choose a fruit to delete: ")

while (Del_fruit.title() in fruits2):
    fruits2.remove(Del_fruit.title())

print('fruits2 = {}'.format(fruits2))

print('End Series 2')
print('===========================')

#Series 3
print('Series 3')

fruits3 = fruits[:]

response = "default"

for fruit in fruits3[:]:
    while response.lower() not in ["yes","no"]:
        response = input('Do you like {}?\n'.format(fruit.lower()))

    if response.lower() == "no":
        fruits3.remove(fruit)

    response = "default"

print('End Series 3')
print('===========================')

# Series 4
print('Series 4')

fruits4 = fruits[:len(fruits)-1]

for Idx, fruit in enumerate(fruits4):
    fruits4[Idx] = fruit[::-1]
    print(fruit)

print('fruits4 = {}'.format(fruits4))
print('fruits = {}'.format(fruits))