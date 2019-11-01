#!/usr/bin/env python3

"""
Steve Morehouse
Lesson 03

"""

print('Series 1')

print('Current fruit are:')
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

print('What fruit would you like to add?')
fruit.append(input())

print('The list of fruit is now:')
print(fruit)

formatter1 = 'The fruit selected is {:s}'
formatter2 = 'You chose {:d}'
fruit_selected = input('Which number fruit do you want (first is one)?')
print(formatter2.format(int(fruit_selected)))
print(formatter1.format(fruit[int(fruit_selected) - 1]))

print('Enter a fruit to add to the beginning of the list')
fruit = [input()] + fruit
print(fruit)

print('Enter another fruit to add to the beginning of the list')
fruit.insert(0, input())
print(fruit)

print('Fruit that begin with P')
for f in fruit:
    if f[0] == 'P':
        print(f)

print('\nSeries 2')
print(fruit)
print('Deleting the last fruit')
fruit2 = fruit[:-1]
print(fruit2)
fruit_to_del = input('Which fruit do you want to delete? ')
for f in fruit2:
    if fruit_to_del == f:
        fruit.remove(f)
print('The current fruit list:')
print(fruit2)

print('\nSeries 3')
print(fruit)
fruit3 = fruit[:]

for f in fruit3:

    print('The current fruit list:')
    print(fruit3)

    print('Do you like ' + f.lower() + '? ')
    response = input()

    if response.lower() not in ['yes', 'no']:
        while response.lower() not in ['yes', 'no']:
            response = input('try again, enter \'yes\' or \'no\'\n')

    # there is a bug here which skips over the next item
    if response.lower() == 'no':
        print(f + ' removed.')
        fruit3.remove(f)

print('\nSeries 4')
print('Original list')
print(fruit)
fruit4 = []

for f in fruit:
    fruit4.append(f[::-1])
fruit4 = fruit4[:-1]
print('Fruit4 list')
print(fruit4)
