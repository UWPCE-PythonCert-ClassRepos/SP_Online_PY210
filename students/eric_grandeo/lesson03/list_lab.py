#!/usr/bin/env python3

#Series 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

#Ask the user for another fruit and add it to the end of the list.
response = input("Please enter in a new fruit > ")
fruits.append(response)

print(fruits)

#Ask the user for a number and display the number back to the user
#and the fruit corresponding to that number (on a 1-is-first basis)
num = int(input("Please enter a number > "))
print("You selected number {}, which is {}".format(num, fruits[num-1]))

#Add another fruit to the beginning of the list using “+” and display the list.
strawberry = ['Strawberry']
fruits = strawberry + fruits

print("Added new fruit with +: {}".format(fruits))

#Add another fruit to the beginning of the
#list using insert() and display the list.

fruits.insert(0, 'Banana')
print("Added new fruit with insert: {}".format(fruits))

#Display all the fruits that begin with “P”, using a for loop.
letter_p = []
for i in fruits:
    if i[0] == "P":
        letter_p.append(i)

print("Fruits that begin with 'P': {}".format(letter_p))

#Series 2
print("Here is the fruits list: {}".format(fruits))

#Remove the last fruit from the list.
fruits.pop(-1)
print("Removed the last fruit: {}".format(fruits))







    