#!/usr/bin/env python3

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list (plain old print() is fine…).
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
new_fruit = input('Please enter a new fruit > ')
fruits.append(new_fruit)

# Display the list.
print(fruits)

# Ask the user for a number and display the number back to the user and the fruit
# corresponding to that number (on a 1-is-first basis). Remember that Python uses 
# zero-based indexing, so you will need to correct.
selected_index = input('Please enter a number to select a fruit from the list > ')
if int(selected_index) <= len(fruits):
    print(fruits[int(selected_index) - 1])
else:
    print("There are only {} fruits in the list".format(str(len(fruits))))

# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ["Cherries"] + fruits
print(fruits)

# Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0, "Lemons")
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in fruits:
    if fruit[0] == "P":
        print(fruit)

# Series 2

# Display the list.
fruits_2 = fruits[:]
print(fruits_2)

# Remove the last fruit from the list.
fruits_2.pop(-1)

# Display the list.
print(fruits_2)

# Ask the user for a fruit to delete, find it and delete it.
fruit_to_delete = input('Please enter a fruit to delete > ')
if fruit_to_delete in fruits_2:
    fruits_2.remove(fruit_to_delete)
else:
    print('{} was not found in the list'.format(fruit_to_delete))
print(fruits_2)

# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
fruits_2 = fruits_2 * 2
fruit_found = False
while fruit_found == False:
    fruit_to_delete = input('Please enter a fruit to delete > ')
    if fruit_to_delete in fruits_2:
        fruit_found = True
        for fruit in fruits_2:
            if fruit == fruit_to_delete:
                fruits_2.remove(fruit_to_delete)
    else:
        print('{} was not found in the list, try again'.format(fruit_to_delete))
print(fruits_2)

# Series 3

fruits_3 = fruits[:]

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
# For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
# Display the list.
for fruit in fruits_3:
    response = ""
    while response.lower() not in ("yes", "no"):
        response = input("Do you like {} > ".format(fruit.lower()))
        if response.lower() == "no":
            fruits_3.remove(fruit)
        elif response.lower() == "yes":
            continue
        else:
            print("Please enter yes or no")
print(fruits_3)

# Series 4

fruits_4 = fruits[:]

# Make a new list with the contents of the original, but with all the letters in each item reversed.
rev_fruits = fruits_4[:]
for i in range(len(rev_fruits)):
    rev_fruits[i] = fruits_4[i][::-1]

# Delete the last item of the original list. Display the original list and the copy.
fruits_4.pop(-1)
print(fruits_4)
print(rev_fruits)