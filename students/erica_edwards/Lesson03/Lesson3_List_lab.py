#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

response = input("Please enter a new fruit. ")
fruit.append(response)
print(fruit)

response = int(input("Please enter a number. "))
number = response - 1
#print(number)
print(f'{response}  {fruit[number]}')

fruit = ['Bananas'] + fruit
print(fruit)

fruit.insert(0, 'Cherries')
print(fruit)

for fruit in fruits:
    print(fruit)
    if fruit[0].upper() == 'P':
        print(fruit)