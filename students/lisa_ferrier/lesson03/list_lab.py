#!/usr/bin/env python
# list_lab.py
# Lisa Ferrier, Python201, Lesson 03 exercise

# ------------------------------- Series 01 -------------------------------- #
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
# ask the user to add another fruit to the list
response = input('Name another type of fruit: ')
# add response to fruit list
fruit.append(response)
print(fruit)
# ask the user to provide a number in range of list indices, on a 1-is-first
# basis..
number = int(input('Provide a number 1 and ' + str(len(fruit)) + ':    '))
# correct the input number to reference the true index position
print(fruit[number-1])

# create a second 'fruit' list
fruit2 = ['Mangoes']
# merge the fruit2 and fruit list. items in fruit2 appear first in the list.
fruit = fruit2 + fruit
print(fruit)

# add another fruit to the beginning of the list using the insert function
fruit.insert(0, 'Coconuts')
print(fruit)

# display all fruits that begin with "P", using a for loop
# note that capitalization matters. Items that begin with a lower case 'p' will
# not be printed. Could add an or statement to the if line: 'or i[0] == "p"'
for i in fruit:
    if i[0] == "P":
        print(i)

# ------------------------------- Series 02 -------------------------------- #
fruit = ["Apples", "Pears", "Oranges", "Peaches", "Bananas"]
print(fruit)
# remove last item from list
del fruit[-1]
print(fruit)
# ask the user to name a fruit in the list above to remove.
response2 = input('Look at the last printed list. Choose a fruit to remove. ')

# check that fruit supplied by user is in list. If not, try again.
if response2 not in fruit:
    print('That fruit is not in the list. Try again.')
    response2 = input('Choose a fruit to remove.')
else:
    # if fruit is in the list, remove it and print the new list.
    for i in fruit:
        if i == response2:
            fruit.remove(i)
    print(fruit)

# BONUS
# multiply the list *2
fruit2 = fruit*2
print(fruit2)
# ask user to specify another fruit to remove.
response3 = input('Look at the last printed list. Choose a fruit to remove.')
# remove all occurences.
if response3 not in fruit2:
    print('That fruit is not in the list. Try again.')
    response3 = input('Choose a fruit to remove.')
else:
    # if fruit is in the list, remove all occurences and print the new list.
    for i in fruit2:
        while i == response3:
            fruit2.remove(i)
            break
    print(fruit2)


# ------------------------------- Series 03 -------------------------------- #
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

for i in fruit[:]:
    while True:
        response = str(input("Do you like %s? " % i))
        response = response.lower()
        if response == 'no':
            print("Removing %s." % i)
            fruit.remove(i)
            break
        if response == 'yes':
            print("%s remains in the list." % i)
            break
        if response != 'no' and response != 'yes':
            print("Please enter yes or no")
print(fruit)


# ------------------------------- Series 04 -------------------------------- #
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit = []

for i in fruit[:]:
    fruit2.append(i[::-1])
    if i == fruit[-1]:
        fruit.remove(i)

print(fruit)
print(fruit2)
