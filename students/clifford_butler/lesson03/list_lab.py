#!/usr/bin/env python3

"""
List Lab 
Goal - Learn the basic ins and outs of Python lists.
Author: Clifford Butler
"""

"""
Series 1
    Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    Display the list (plain old print() is fine…).
    Ask the user for another fruit and add it to the end of the list.
    Display the list.
    Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    Add another fruit to the beginning of the list using “+” and display the list.
    Add another fruit to the beginning of the list using insert() and display the list.
    Display all the fruits that begin with “P”, using a for loop.
"""

print ("Series 1 exercise:" + "\n")

# Create a list and display the list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
for item in (fruit_list):
    print ("A list has been created \
with the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1])
    break


# Ask the user for another fruit and add it to the end of the list
response = input("Enter the fruit you would like to add to the list: ")
if response not in fruit_list:
    fruit_list.append(response)
else: print("Already in list!")
print(response,"has been added to the end of the list. Here is the new list:")
print(str(fruit_list)[1:-1])


# Ask the user for a number and display the number back to the user 
# and the fruit corresponding to that number (on a 1-is-first basis)
response2 = int(input("What fruit would you like to display? \
Enter the number corresonding with the fruit: "))
for i, item in enumerate(fruit_list):
    if 0 <= response2 <= len(fruit_list):
        i += 1
        print(str(response2), fruit_list[int(response2) - 1], "\n")
        break
    else:
        print ("That number is out of range!")
    print ("The list has the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1])
    break
       
# Add another fruit to the beginning of the list using “+” and display the list
new_fruit = "Mangoes"
fruit_list = [new_fruit] + fruit_list
print(new_fruit, "has been added to the beginning of the list using +.")
print("Here is the new list:",str(fruit_list)[1:-1], "\n")
    
# Add another fruit to the beginning of the list using insert() and display the list
new_fruit2 = "Watermelons"
fruit_list.insert(0, new_fruit2)
print(new_fruit2, "has been added to the beginning of the list using insert().")
print("Here is the new list:",str(fruit_list)[1:-1], "\n")

# Display all the fruits that begin with “P”, using a for loop
print("The following fruit start with P:")
for fruit in fruit_list:
    if fruit[0].upper() == "P":
        print(fruit)
        

"""
Series 2
Using the list created in series 1 above:

    Display the list.
    Remove the last fruit from the list.
    Display the list.
    Ask the user for a fruit to delete, find it and delete it.
    (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
"""

print ("\n" + "Series 2 exercise:" + "\n")

# Display items in fruit_list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print ("The list contains the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1],"\n")
    
#remove the last fruit from the list
deleted_fruit = fruit_list[-1]
fruit_list = fruit_list[:-1]
print(deleted_fruit, "has been deleted from the list.")

# Display items in fruit_list
print ("The list has the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1], "\n")    
   
# Ask the user for a fruit to delete, find it and delete it    
response3 = input("Enter the fruit you would delete from the list: ")
if response3 in fruit_list:
    fruit_list.remove(response3)
    print(response3, "has been deleted.")
else:
    print (response3, " cannot be deleted because it is not in the fruit list.")   
print ("The list has the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1])

"""
Series 3
Again, using the list from series 1:

    Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    For each “no”, delete that fruit from the list.
    For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    Display the list.)
"""

print ("\n" + "Series 3 exercise:" + "\n")

'''
while loop identifying which fruit the users likes
displays what fruit the user likes once the while loop
passes through all of the fruit in the list.
'''

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
hated_fruit = []

for i in fruit_list:
    response4 = ""
    #response4 = input("Do you like {}? ".format(i.lower()))
    while response4.lower() != "yes" and response4.lower() != "no":
        response4 = input("Do you like {}? ".format(i.lower()))
    if response4.lower() == "no":
        hated_fruit.append(i)
    elif response4 == "yes":
        continue
    else:
        print("Please answer with 'yes' or 'no'")
        
print("")

for x in hated_fruit:
    fruit_list.remove(x)

if len(fruit_list) == 0:
    print("The list contains", len(fruit_list), "fruit in the list.")
        
else:
    print("The list has the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1])

"""
Series 4
Once more, using the list from series 1:

    Make a new list with the contents of the original, but with all the letters in each item reversed.
    Delete the last item of the original list. Display the original list and the copy.

"""

print ("\n" + "Series 4 exercise:" + "\n")

# Make a new list with the contents of the original, but with all the letters in each item reversed.
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
series_four_list = fruit_list[:]
series_four_list2 = [x[::-1] for x in series_four_list][:]

#Delete the last item of the original list. Display the original list and the copy.
fruit_list = fruit_list[:-1]
print("The original list has the following", len(fruit_list), "fruit:", str(fruit_list)[1:-1])  
print("The copied list has the following", len(series_four_list2), "fruit:", str(series_four_list2)[1:-1])