#!/usr/bin/env python3
#
#Series 1
#
#######################################

print('Series 1')
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

#Ask the user for another fruit
response = input('Please add another fruit to the list:')
fruit.append(response)
print(fruit)

#Ask user for a number and return which fruit
response = input('Select a number between 1 and {}:'.format(len(fruit)))
print(response,fruit[int(response)-1])

#Add another fruit to beginning of list using "+"
fruit = ['Pineapple'] + fruit
print(fruit)

#Add another fruit to the beginning of list using insert
fruit.insert(0,'Strawberries')
print(fruit)

#Display all the fruit that begins with "P" using for loop
print('\nFruit in list that start with "P"')
for f in fruit:
    if f.startswith('P'):
        print(f)

#        
#Series 2
#
##########################################
print('\n\nSeries 2')

print(fruit)
#Remove the last fruit from the list
fruit.pop()
print(fruit)

#copy fruit list and double
print('Double the list')
fruit2 = fruit[:] *2
print(fruit2)

#Ask the user for a fruit to delete
del_success = False
while not del_success:
    response = input('Enter a fruit to delete:')
    if response in fruit2:
        while response in fruit2:
            fruit2.remove(response)
            print('Removing response')
            print(fruit2)
        del_success = True
    else:
        print('{} not found in fruit list.  Please retry.'.format(response))

print(fruit2)        
#
#
#





