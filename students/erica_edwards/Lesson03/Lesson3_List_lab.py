#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

response = input("Please enter a new fruit. ")
fruits.append(response)
print(fruits)

response = int(input("Please enter a number. "))
number = response - 1
#print(number)
print(f'{response}  {fruits[number]}')

fruits = ['Bananas'] + fruits
print(fruits)

fruits.insert(0, 'Cherries')
print(fruits)

for fruit in fruits:
    #print(fruit)
    if fruit[0].upper() == 'P':
        print(fruit)