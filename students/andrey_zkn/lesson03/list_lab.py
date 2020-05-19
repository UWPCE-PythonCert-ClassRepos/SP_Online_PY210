#!/usr/bin/env python3

# SERIES 1

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
another_fruit = input("Please enter another fruit ...")
fruits.append(another_fruit)
print(fruits)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number 
# (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
fruit_number = input("Please enter a number for a fruit ...")
print (fruit_number + " " + fruits[int(fruit_number) - 1])

# Add another fruit to the beginning of the list using “+” and display the list.
fruits = ['Cherries'] + fruits
print(fruits)

# Add another fruit to the beginning of the list using insert() and display the list.
fruits.insert(0, 'Lemon')
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for item in fruits:
    if item[0] == 'P':
        print(item)



# SERIES 2

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list created in series 1 above:
print(fruits)

# Remove the last fruit from the list.
fruits = fruits[:-1]
print(fruits)
 
# Ask the user for a fruit to delete, find it and delete it.
fruit_delete = input("Please enter a fruit name to delete ...")
if fruit_delete in fruits:
    fruits.remove(fruit_delete)
else:
    print(fruit_delete, "not in list")
print(fruits)
        



# SERIES 3

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list
# (making the fruit all lowercase). For each “no”, delete that fruit from the list.
# For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
# (a while loop is good here)
for fruit in fruits:
        answer = input("Do you like " + fruit.lower() + "?")
        while  answer.lower() not in ("yes", "no"):
            print("Please enter only Yes or No")
            answer = input("Do you like " + fruit.lower() + "? Enter yes or no only?")
        if  answer.lower() == "no":
            fruits.remove(fruit)
print(fruits)




# SERIES 4

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Make a new list with the contents of the original, but with all the letters in each item reversed.
fruits_new = []
for fruit in fruits:
        fruits_new.append(fruit[::-1])

# Delete the last item of the original list. Display the original list and the copy.
fruits.pop()

print (fruits_new)
print (fruits)


