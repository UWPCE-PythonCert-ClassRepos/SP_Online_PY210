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
#Series 3
#
#############################################
print('\n\nSeries 3')

print(fruit)

#Ask the user if they like each fruit, if no delete the fruit from the list
#Create a copy of fruit as you should not iterate on the list that we are going to modify
fruit3 = fruit[:]
for f in fruit:
    response = input(f'Do you like {f.lower()}?')
    while response not in ['yes','no']:
        response = input(f'Please answer \'yes\' or \'no\'.  Do you like {f}?')
    if response == 'yes':
        continue
    else:
        fruit3.remove(f)
        print(f'Removed {f} from list.')
        
print(f'You like the following fruit: {fruit3}')


#
#Series 4
#
#############################################
print('\n\nSeries 4')

print(fruit)

#Copy fruit list and but reverse the letters of each item
fruit4 = []
for f in fruit:
    fruit4.append(f[::-1])
print('Reversed letters...')
print(fruit4)

#Delete the last item of the original list.  Display the original list and the copy
fruit4a = fruit[:-1]
print(f'Original list:                 {fruit}')
print(f'Original list minus last item: {fruit4a}')








