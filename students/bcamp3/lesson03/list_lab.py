#!/usr/bin/env python3

"""
List Lab

"""

"""
Series 1
"""
print('----------\n Series 1\n----------')

fruits = ['Apples','Pears','Oranges','Peaches']

print('\nThe fruits list: \n', fruits)

response = input('\nWhat is another fruit that you like? > ')

if response[-1] != 's':
    response += 's'

fruits.append(response.capitalize())

print(fruits)

response = 0
while response >5 or response <1:
    response = int(input(f'\nPick a number between 1 and {len(fruits)} > '))

print(f'\nFruits list item {response:d} is {fruits[response-1]}')

print('\nAdding Bananas to beginning of fruits list:')
fruits = ['Bananas'] + fruits
print(fruits)

print('\nAdding Melons to beginning of fruits list:')
fruits.insert(0,'Melons')
print(fruits)

print("\nFruits starting with the letter 'P' :")
for fruit in fruits:
    if fruit[0]=='P':
        print('   ', fruit)

"""
Series 2
"""
print('\n----------\n Series 2\n----------')

fruits = ['Apples','Pears','Oranges','Peaches']

print('\nThe fruits list: \n', fruits)

print('\nRemoving the last item in the fruits list:')
fruits.pop()
print(fruits)

fruits = fruits*2
print('\nDoubling the fruits list: \n', fruits)

fruit_del = input('\nWhat fruit would you like to delete? > ')
while fruit_del.capitalize() not in fruits:
    fruit_del = input('\nWhat fruit IN THE LIST would you like to delete? > ')

for fruit in fruits:
    if fruit == fruit_del.capitalize():
        fruits.remove(fruit_del.capitalize())
        
print('\nNew doubled fruits list: \n', fruits)

num=len(fruits)//2
fruits = fruits[:num]
print('\nSingular fruits list: \n', fruits)

"""
Series 3
"""
print('\n----------\n Series 3\n----------')

fruits = ['Apples','Pears','Oranges','Peaches']

print('\nThe fruits list: \n', fruits)
fruits_copy = fruits[:]
print()
for fruit in fruits_copy:
    response = input(f'Do you like {fruit:<8} ? > ')
    while response.lower() not in ['yes','no']:
        print(f"*** Please respond with 'Yes' or 'No' ***")
        response = input(f'Do you like {fruit:<8} ? > ')
    if response.lower() == 'no':
        fruits.remove(fruit)
    
print('\nNew fruits list: \n', fruits)

"""
Series 4
"""
print('\n----------\n Series 4\n----------')

fruits = ['Apples','Pears','Oranges','Peaches']

print('\nThe fruits list: \n',fruits)
new_fruits = []
for fruit in fruits:
    new_fruits.append(fruit[::-1])

fruits.pop()
print('\nRemoving the last item in the fruits list:\n',fruits)

print('\nReversing the order of the fruit names in the fruits list:\n',new_fruits)
