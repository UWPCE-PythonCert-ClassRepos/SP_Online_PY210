#!/usr/bin/env python3

# Series 1
print('===========================')
print('Series 1')
Fruits = ["Apples","Pears","Oranges","Peaches"]

print('Fruits = {}'.format(Fruits))

New_Fruit = input("Add another fruit: ")

Fruits.append(New_Fruit.title())

print('Fruits = {}'.format(Fruits))

NumInvalid = 1
while NumInvalid:
    number = input("Type a number between 1 and {:d}: ".format(len(Fruits)))
    number = int(number)
    if number > 0 and number < (len(Fruits)+1):
        NumInvalid=0

print("{:d} {}".format(number,Fruits[number-1]))

New_Fruit2 = input("Add another fruit: ")

Fruits = Fruits + [New_Fruit2.title()]

print('Fruits = {}'.format(Fruits))

New_Fruit3 = input("Add another fruit: ")

Fruits.insert(0,New_Fruit3.title())

print('Fruits = {}'.format(Fruits))

for fruit in Fruits:
    if fruit[0] == "P":
        print(fruit)



print('End Series 1')
print('===========================')

# Series 2
print("Series 2")

Fruits2 = Fruits[:]

print('Fruits2 = {}'.format(Fruits2))

Fruits2.pop()

print('Fruits2 = {}'.format(Fruits2))

Del_fruit = input("Choose a fruit to delete: ")

while (Del_fruit.title() in Fruits2):
    Fruits2.remove(Del_fruit.title())

print('Fruits2 = {}'.format(Fruits2))

print('End Series 2')
print('===========================')

#Series 3
print('Series 3')

Fruits3 = Fruits[:]

response = "default"

for fruit in Fruits3[:]:
    while response.lower() not in ["yes","no"]:
        response = input('Do you like {}?\n'.format(fruit.lower()))

    if response.lower() == "no":
        Fruits3.remove(fruit)

    response = "default"

print('End Series 3')
print('===========================')

# Series 4
print('Series 4')

Fruits4 = Fruits[:len(Fruits)-1]

for Idx, fruit in enumerate(Fruits4):
    Fruits4[Idx] = fruit[::-1]
    print(fruit)

print('Fruits4 = {}'.format(Fruits4))
print('Fruits = {}'.format(Fruits))