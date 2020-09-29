#!/usr/bin/env python3

# --------------------------------
# 06/29/19 Jinee Han
# Python Programming Lesson 3
# List Lab
# ---------------------------------

# Series 1
'''
Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
Display the list (plain old print() is fine…).
Ask the user for another fruit and add it to the end of the list.
Display the list.
Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
Remember that Python uses zero-based indexing, so you will need to correct.
Add another fruit to the beginning of the list using “+” and display the list.
Add another fruit to the beginning of the list using insert() and display the list.
Display all the fruits that begin with “P”, using a for loop.
'''

print ("Testing series 1.\n")
fruit_list = ["Apples","Pears","Oranges","Peaches"] # Create a list
print (fruit_list,'\n') # Print the list

ask_user = input ("Would you like to add a fruit? (y/n)") # Ask the user
if ask_user == "y": # Add the fruit to the list
    add_fruit = input ("Which fruit would you like to add\n?")
    fruit_list.append(add_fruit)
    print (fruit_list) # Display the appended list
else:
    print ("\nNo item was added.\n")

fruit_list = ["Apples","Pears","Oranges","Peaches"]
ask_numeber = input("Enter the number to see the fruit from the list\n") #Ask user for a number to display
display_fruit = print(fruit_list[int(ask_numeber)-1]) # Display the fruit

add_another_fruit_with_plus = input("Let's add another fruit. Please type in.\n ") # Add another fruit.
fruit_list = [add_another_fruit_with_plus] + fruit_list# Adding by using '+'
print (fruit_list)

add_another_fruit_with_insert = input("Final addition. What is the fruit name?\n") # Add another fruit.
fruit_list. insert(0,add_another_fruit_with_insert) # Adding by using Insert
print ("Here is the final fruit list.")
print (fruit_list)


# Display all the fruits that begins with 'P'

print ("\nLet's find out fruits start with P\n")
for items in fruit_list:
    if items.startswith('P'):
        print(items)
    else:
        continue

# 2. Series 2
'''
Display the list.
Remove the last fruit from the list.
Display the list.
Ask the user for a fruit to delete, find it and delete it.
(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
'''

print ("\nTesting Series 2\n")
print (fruit_list) # Display the list
print ("\nRemoving the last item\n")
fruit_list.pop() # Remove the last fruit from the list
print (fruit_list) # Display the list
print("\nHere is the list to delete from\n")
fruit_list_2 = fruit_list * 2 #Multiply the list times two to delete all occurrences
print (fruit_list_2)
ask_what_to_delete = input("\nWhich fruit would you want to delete?") # Ask the user what to delete
for item in fruit_list_2:
    print("I am looking for the match.") # Keep asking until a match is found.
    if ask_what_to_delete == item:
        fruit_list_2.remove(item)
    else:
        continue
print (fruit_list_2)

# 3. Series 3
'''
Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
For each “no”, delete that fruit from the list.
For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
Display the list.
'''

print ("\nTesting Series 3.\n")
fruit_list = ["Apples","Pears","Oranges","Peaches"]
removing_list = []
for item in fruit_list:
    do_you_like_fruit = input("Do you like {}? (y/n)".format(item.lower()))
    if do_you_like_fruit == 'n':
        removing_list.append(item)
    else:
        continue
final_list = list(set(fruit_list)-set(removing_list))

print("You want to remove these items: ", removing_list)
print("You deleted fruits you don't like. Here is the left list:\n ", final_list)

# 4. Series 4
'''
Make a new list with the contents of the original, but with all the letters in each item reversed.
Delete the last item of the original list. Display the original list and the copy.
'''
print ("\nTesting series 4.\n")
fruit_list = ["Apples","Pears","Oranges","Peaches"]
new_list = [] # create a new list for a reversed fruit list
for item in fruit_list: # Reverse the fruit name
    item = item[::-1]
    new_list.append(item)
print ("Reversed item list: ", new_list)


copy_list = fruit_list.copy()

fruit_list.pop() # Delete the last item of the original list
print ("Original list, which the last item deleted: ", fruit_list) # Display the original list
print("Copy list: ",copy_list) # Display a copy list