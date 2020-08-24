#!/usr/bin/env python3

# Dominic Divakaruni
# Lesson03 - List Lab

""" Series 1
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
"""


print(" ## Series 1 ## \n\n")
fruit = [ "Apples", "Pears", "Oranges", "Peaches" ]

#Display the list
print("Here's the list of fruit: \n ", fruit, " \n ")

#Ask the user for another fruit and add it to the end of the list. Display the list.
new = input("Add another fruit to the list:")
fruit.append(new)
print("Great! Here's the list of fruit \n", fruit, " \n")

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
item_num = int(input("Use a number to choose a fruit out of the list: "))
if item_num != False:
    if item_num in range(len(fruit)+1):
        print("OK! Here's what you choose: \n" + str(item_num) + " -- " + fruit[item_num-1] + "\n")
    else:
        print("poor choice try again later! \n")
else:
    print("poor choice try again later \n")
    continue
    
#Add another fruit to the beginning of the list using + and display the list.
fruit = ["Mangoes"] + fruit
print("The store now has Mangoes! Here's the list \n", fruit, "\n")

#Add another fruit to the beginning of the list using insert() and display the list.
fruit.insert(0, "Papayas")
print("The store now has Papayas! Here's the list \n\n", fruit)

#Display all the fruits that begin with P, using a for loop.
for i in fruit:
    if i[0] == "P":
        print("here's a fruit in the list that starts with the letter P: ", i)
        
print ("\n")

""" Series 2
Using the list created in series 1 above:

Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""

print("## Series 2 ## \n\n")
# Display the list. Remove the last fruit from the list. Display the list
print("Here's the list of fruit", fruit, "\n\n")

series2fruit = list.copy(fruit)
series2fruit.pop()
print("Removed the last item on the menu. Here's the new list:", series2fruit, "\n\n")

#Ask the user for a fruit to delete, find it and delete it.
removefruit = input("what fruit would you like to remove from the list:")
removefruit
if removefruit in fruit:
    series2fruit.remove(removefruit)
    print("Here's the list of fruit for Series 2", series2fruit, "\n\n")
else: 
    print("poor choice try again later. Here's the list of fruit for Series 2", series2fruit, "\n\n")
    continue

""" Series 3
Again, using the list from series 1:

Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
"""
series3fruit = list.copy(fruit)
print("## Series 3 ## \n\n")
length = len(series3fruit)
counter =0
while counter < length:
    rm = input("do you like {}?".format(series3fruit[counter]))
    if rm == "no":
        series3fruit.remove(series3fruit[counter])
        length -= 1
    elif rm == "yes":
        counter += 1
    else:
        print("Your answer has to be a yes or no")

print("Here's the list of fruit for Series 3", series3fruit, "\n\n")


"""Series 4
Once more, using the list from series 1:

Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy. """

print("## Series 4 ## \n\n")

series4fruit = [i[::-1] for i in fruit]
fruit.pop()

print("Series 1 fruit list:", fruit)
print("Series 4 fruit list:", series4fruit)

