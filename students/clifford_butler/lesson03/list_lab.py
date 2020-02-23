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

print ("series 1 exercise" + "\n")

# Create a list and display the list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
for item in (fruit_list):
    print(item)

# Ask the user for another fruit and add it to the end of the list
response = input("Enter the fruit you would like to add to the list: ")
if response not in fruit_list:
    fruit_list.append(response)
else: print("Already in list!")
print(fruit_list)


# Ask the user for a number and display the number back to the user 
# and the fruit corresponding to that number (on a 1-is-first basis)
response2 = int(input("Enter a number: "))
for i, item in enumerate(fruit_list):
    if str(response2) in str(i):
        i += 1
        print(str(response2), fruit_list[int(response2) - 1])
        break
        
# Add another fruit to the beginning of the list using “+” and display the list
fruit_list = ["Mangos"] + fruit_list
print(fruit_list)
    
# Add another fruit to the beginning of the list using insert() and display the list
fruit_list.insert(0, "Watermelons")
print(fruit_list)

# Display all the fruits that begin with “P”, using a for loop
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

print ("\n" + "series 2 exercise" + "\n")

# Display items in fruit_list
for item in (fruit_list):
    print(item)
    
#remove the last fruit from the list
fruit_list = fruit_list[:-1]

# Display items in fruit_list
for item in (fruit_list):
    print(item)
   
# Ask the user for a fruit to delete, find it and delete it    
response3 = input("Enter the fruit you would delete from the list: ")  
fruit_list.remove(response3)
  
# Bonus, multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences
print ("\n" + "series 2 exercise bonus" + "\n")
