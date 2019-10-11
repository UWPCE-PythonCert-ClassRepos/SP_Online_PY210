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

fruits_series_one = fruits[:]

#Series 2
print("Series 2{}".format('-' * 25))
print("Here is the fruits list: {}".format(fruits))

#Remove the last fruit from the list.
fruits.pop(-1)
print("Removed the last fruit: {}".format(fruits))

#Ask the user for a fruit to delete, find it and delete it.
del_fruit = input("Please enter a fruit you would like to delete > ")
fruits.remove(del_fruit)
print("Removed the fruit per your request: {}".format(fruits))

#Series 3
print("Series 3{}".format('-' * 25))
print("Here is the list of fruits: {}".format(fruits))

#Ask the user for input displaying a line like “Do you like apples?”
#for each fruit in the list (making the fruit all lowercase).

#updated per instructors recommendations
for x in fruits[:]:
    while True:
        user_like = input("Do you like {} ? ".format(x.lower()))
        if user_like not in ("yes", "no"):
            print("Please answer yes or no")
        else:
            break
        
    if user_like.lower() == "no":
        fruits.remove(x)    

print("Here is the udpated list based on your answers: {}".format(fruits))

#Series 4
print("Series 4{}".format('-' * 25))
print("Here is the fruits list from Series 1: {}".format(fruits_series_one))

#Make a new list with the contents of the original,
#but with all the letters in each item reversed.


#Delete the last item of the original list.
# Display the original list and the copy.

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits1 = []
for y in fruits:
    fruits1.append(y[::-1])

del fruits[-1:]
print(fruits)
print(fruits1)






    