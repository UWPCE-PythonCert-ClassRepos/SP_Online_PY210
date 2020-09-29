#!/usr/bin/env python
# list_lab.py
# Lisa Ferrier, Python201, Lesson 03 exercise

# ------------------------------- Series 01 -------------------------------- #
'''
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list; Ask the user for another fruit and add it to the end of the
list; Display the list; Ask the user for a number and display the number back
to the user and the fruit corresponding to that number (on a 1-is-first basis).
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the
list. Display all the fruits that begin with “P”, using a for loop.
'''

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
print(fruit[number - 1])

# create a second 'fruit' list
fruit2 = ['Mangoes']
# merge the fruit2 and fruit list. items in fruit2 appear first in the list.
fruit = fruit2 + fruit
print(fruit)

# add another fruit to the beginning of the list using the insert function
fruit.insert(0, 'Coconuts')
print(fruit)

'''
Display all fruits that begin with "P", using a for loop.
Note that capitalization matters. Items that begin with a lower case 'p' will
not be printed.
Could accomodate this with an additional condition on the if line:
or i[0] == "p"
'''
for i in fruit:
    if i[0] == "P":
        print(i)

# ------------------------------- Series 02 -------------------------------- #
'''
Using the list created in series 1 above:
Display the list; Remove the last fruit from the list; Display the list;
Ask the user for a fruit to delete, find it and delete it.
'''

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

'''
BONUS
Multiply the list times 2. Keeps asking until a match is found. Once found,
delete all occurrences
'''
fruit2 = fruit * 2
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
'''
Asks user if they like each fruit in list. if yes, do nothing, if no remove
item from list. If user inputs a value other than yes or no, question repeats
'''

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
'''
Make a new list with the contents of the original, but with all the letters
in each item reversed. Delete the last item of the original list. Display
 the original list and the copy.
'''

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
fruit2 = []

for i in fruit[:]:
    # add item to fruit2 list, letters reversed for each item.
    fruit2.append(i[::-1])
    # remove the last item in the original fruit list
    if i == fruit[-1]:
        fruit.remove(i)

print(fruit)
print(fruit2)
