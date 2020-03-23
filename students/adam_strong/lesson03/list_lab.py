#!/usr/bin/env python3
##Lists##
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruits_original = fruits[:]


## Series 1 ##
print('')
print('Begin Series 1')
print('')
print(fruits)
response1 = input("Please add another fruit to my fruit list > ")
fruits.append(response1)
print(fruits)

response2 = input("Type a number and I will return that fruit's number")
#response2 = int(response2)
print('Fruit number: ', response2, ' ', fruits[int(response2)-1])

response3 = input("Please add another fruit to the beginning of my fruit list > ")
fruits = [response3] + fruits
print(fruits)


response4 = input("Please add another fruit to the beginning of my fruit list > ")
fruits.insert(0, response4)
print(fruits)

print('All the fruits that begin with "P"')
for fruit in fruits:
    if fruit[0] == "P":
        print(fruit)

##Series 2 ##
print('')
print('Begin Series 2')
print('')
print(fruits)

fruits = fruits[:-1]
print(fruits)

response5 = input("Please type a fruit to remove from the list > ")
fruits.remove(response5)
print(fruits)

##Series 3
print('')
print('Begin Series 3')
print('')
fruits2 = fruits[:]
for fruit in fruits:
    while True: 
        yn = input("Do you like " + fruit.lower() + '?. Type yes or no.')
        if yn == 'no':
            fruits2.remove(fruit)
            break
        elif yn == 'yes':
            break
        else:
            input("Please type only yes or no in response.")
print(fruits2)

##Series 4 ##
print('')
print('Begin Series 4')
print('')
fruits_backwards = []
for fruit in fruits_original:
    fruits_backwards.append(fruit[::-1])

fruits_original_minus = fruits_original[:-1]

print(fruits_backwards)
print(fruits_original)
print(fruits_original_minus)
