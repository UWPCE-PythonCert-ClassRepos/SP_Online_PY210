#!/usr/bin/#!/usr/bin/env python3

#List Lab Excercise. Lesson 3, Series 1
fruits = ['Apples','Pears','Oranges','Peaches']
print(fruits)

fruit = input("What Fruit Do You Like? ")

fruits.append(fruit)
print(fruits)

number = int(input("What's Your Favorite Number? "))
print('Your Number is ',number)

try:
    print('Your Fruit is ',fruits[number - 1])

except:
    print("Oops! That number doesn't match a fruit!")

fruits = fruits + ['Blackberries']
print(fruits)

fruits.insert(0,"Grapes")
print(fruits)

for item in fruits:
    if item[0] == 'P':
        print(item)

#List Lab Series 2
print(fruits)

#Remove last item
print(fruits.pop())
fruit_del = input('What Fruit Should I delete next? ')

if fruit_del in fruits:
    fruits.remove(fruit_del)
else:
    print('Cannot Find That Fruit! Try Again')

print('This is your current fruit list: ',fruits)

#List Lab Series 3
for fruit in fruits:
    fruit_input = input("Do you like " + fruit.lower() + '? ').lower()

    if fruit_input == 'no' or fruit_input == 'yes':
        if fruit_input == 'no':
            fruits.remove(fruit)
    else:
        while fruit_input != 'no' and fruit_input != 'yes':
            print('Please answer the question!')
            fruit_input = input("Do you like " + fruit.lower() + '? ').lower()
            if fruit_input == 'no':
                fruits.remove(fruit)

print('This is your current fruit list: ',fruits)

#List Lab Series 4
fruits = ['Apples','Pears','Oranges','Peaches']

copy_fruits = []
for fruit in fruits:
    reverse = fruit[::-1]
    copy_fruits.append(reverse)

del fruits[-1]

print(fruits)
print(copy_fruits)
