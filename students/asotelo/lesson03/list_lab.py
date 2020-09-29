#!/usr/bin/env python3

'''
Author: Alex Sotelo
Exercise 3.2
Python 3 required
Requirement: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html
Tasks:

Series 1

    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
'''

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

#Display the list (plain old print() is fine…)
print(fruits)

#Ask the user for another fruit and add it to the end of the list.
ask = input("Y u no add more fruit? ")
if ask in fruits:
    print("In the list, the fruit already is.")
else:
    fruits.append(ask)

#Display the list.
print(fruits)

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
#Remember that Python uses zero-based indexing, so you will need to correct.
number = input("Y u no choose number? ")
print('You chose the number ' + number + ', the corresponding fruit is', fruits[int(number)-1]+'.')

#Add another fruit to the beginning of the list using “+” and display the list.
another = input("Y u no add more fruit? ")
if another in fruits:
    print("In the list, the fruit already is.")
else:
    fruits = [another] + fruits
    print("The new list of fruits is ", fruits)

#Add another fruit to the beginning of the list using insert() and display the list.
yetAnother = input("Y u no add more fruits? ")
if yetAnother in fruits:
    print("In the list, the fruit already is.")
else:
    fruits.insert(0, yetAnother)
    print("The new list of fruits is ", fruits)

#Display all the fruits that begin with “P”, using a for loop.
for p in fruits:
    if p[0] is "P":
        print("This fruit in the list starts with the letter P:", p)

'''
Series 2

Using the list created in series 1 above:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    
'''

#Display the list.
print(fruits)
#Remove the last fruit from the list.
fruits.pop()
#Display the list.
print(fruits)
#Ask the user for a fruit to delete, find it and delete it.
delete = input("Y u no delete fruit? ")
if delete not in fruits:
    print("Cannot delete fruit that is not in the list. ")
else:
    fruits.remove(delete)
    print("The new list is ", fruits)

'''
Series 3

Again, using the list from series 1:

    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.
'''

#Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).

for fruit in fruits[:]:
    answers = ['yes','no','Yes','No','YES','NO']
    ask = 'Do you like {}?'.format(fruit.lower())
    while True:
        response = input(ask)
        if response not in answers:
            print('Y u no answer with either yes or no? ')
        else:
            break
    if response in ['No','no','NO']:
        fruits.remove(fruit)

#Display the list.
print("The new list of fruits is", fruits)

'''
Series 4

Once more, using the list from series 1:

    Make a new list with the contents of the original, but with all the letters in each item reversed.
    Delete the last item of the original list. 
    Display the original list and the copy.
'''
#Make a new list with the contents of the original, but with all the letters in each item reversed.
newList = []
for fruit in fruits:
    newList.append(fruit[::-1])

#Delete the last item of the original list.
fruits.pop(-1)

#Display the original list and the copy.
print(fruits)
print(newList)