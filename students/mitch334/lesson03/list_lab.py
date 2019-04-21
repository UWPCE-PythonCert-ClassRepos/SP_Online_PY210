"""Lesson 03 | List Lab"""
# Goal: Learn the basic ins and outs of Python lists.
#
# Hint: to query the user for info at the command line, you use:
# response = input("a prompt for the user > ")
# response will be a string of whatever the user types (until a <return>).


#!/usr/bin/env python3

"""Series 1: Create a list of fruit."""

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
# Display the list (plain old print() is fine…).
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

# Ask the user for another fruit and add it to the end of the list.
response = input('Enter a fruit to add > ')
fruit.append(response.title())
# Display the list.
print(fruit)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
response = input('Pick a number between 1 and ' + str(len(fruit)) + ' > ')
print(int(response), ' | ', fruit[int(response)-1])


# Add another fruit to the beginning of the list using “+” and display the list.
fruit = ["Bananas"] + fruit
print(fruit)

# Add another fruit to the beginning of the list using insert() and display the list.
fruit.insert(0,"Kiwis")
print(fruit)

# Display all the fruits that begin with “P”, using a for loop.
fruit_with_p = []
for item in fruit:
    if item.upper().startswith('P'):
        fruit_with_p.append(item)
print(fruit_with_p)
fruit_series1 = fruit.copy()

"""Series 2: Play with Series 1 fruit list."""
# Using the list created in series 1 above:
# Display the list.
print(fruit)

# Remove the last fruit from the list.
# Display the list.
del fruit[-1]
print(fruit)

# Ask the user for a fruit to delete, find it and delete it.
response = input('Enter a fruit to remove > ')
if response.title() in fruit:
    fruit.remove(response.title())
else:
    print(response, 'not in list.')
print(fruit)

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruit = fruit*2
print(fruit)

fruit_match = False
while not fruit_match:
    response = input('Enter a fruit to remove > ')
    while response.title() in fruit:
        fruit.remove(response.title())
        fruit_match = True
    else:
        print(response, 'not in list.')
print(fruit)

"""Series 3: Play with Series 1 fruit list again."""
# Again, using the list from series 1:
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.

fruit = fruit_series1.copy()
print(fruit)

for item in fruit_series1:
    response = input('Do you like ' + item.lower() + '? > ')

    while response.lower() not in ['yes','no']:
        print(response, 'is invalid. Enter yes or no.')
        response = input('Do you like ' + item.lower() + '? > ')

    if response.lower() == 'no':
        fruit.remove(item)
print(fruit)
