#!/usr/bin/env python3

# Title: List Lab
# Dev: Roslyn Melookaran
# Date: 9/11/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/11/20, created script)
# --------------------------------------------------------------

# -------SERIES 1 -------#
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
list=["Apples", "Pears", "Oranges","Peaches"]
# Display the list (plain old print() is fine…).
print(list)
# Ask the user for another fruit and add it to the end of the list.
input1=input("Please enter a fruit to add to the list: ")
list.append(input1.title())
# Display the list.
print(list)
# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
# Remember that Python uses zero-based indexing, so you will need to correct.
qty=len(list)
n=int(input("Please enter a number from 1-"+str(qty)+": "))
n_mod=n-1
print("You chose "+str(n)+' which corresponds to "' +list[n_mod]+'" in the list')
# Add another fruit to the beginning of the list using “+” and display the list.
input2=input("Please enter a fruit to add to the list: ")
input2=input2.title()
list_add=[input2]
list=list_add+list
print(list)
# Add another fruit to the beginning of the list using insert() and display the list.
input3=input("Please enter a fruit to add to the list: ")
input3=input3.title()
list.insert(0,input3)
print(list)
# Display all the fruits that begin with “P”, using a for loop
print('These are the items in the list that begin with the letter "P": ')
list_p=[]
for item in list:
    if item[0]=="P":
        list_p.append(item)
        print(item)
print(list_p)

# -------SERIES 2 -------#
# Using the list created in series 1 above:
# Display the list.
print(list)
# Remove the last fruit from the list.
list.pop()
# Display the list.
print(list)
# Ask the user for a fruit to delete, find it and delete it.
input_delete=input("Please input a fruit to delete from the list: ")
input_delete=input_delete.title()
for item in list:
    if item==input_delete:
        list.remove(item)
        print(item+" has been deleted from the list.")
print(list)
# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
list_double=list*2
print(list_double)
input_delete=input("Enter a fruit you wish to delete from the list: ")
input_delete=input_delete.title()
while input_delete not in list:
    input_delete=input("That item was not in the list. Please enter a fruit to delete off the list: ")
    input_delete=input_delete.title()
for item in list_double:
    if item == input_delete:
        list_double.remove(item)
        print('"'+item + '" has been deleted from the list.')
    else:
        continue
print(list_double)

# -------SERIES 3 -------#
# Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
for item in list:
    input_preference=input("Do you like "+ item+' ? Please enter "y" or "n": ')
    input_preference=str(input_preference.lower())
    # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    while input_preference != 'y' and input_preference != 'n':
         input_preference = input('Please enter "y" or "n": ')
         input_preference = str(input_preference.lower())
    # For each “no”, delete that fruit from the list.
    if input_preference=="n":
        list.remove(item)
        print(item+" has been removed. the list is now: ")
    elif input_preference=="y":
        continue
    # Display the list.
    print(list)

# -------SERIES 4 -------#
# Make a new list with the contents of the original, but with all the letters in each item reversed.
# Delete the last item of the original list. Display the original list and the copy.
list=["Apples", "Pears", "Oranges","Peaches"]
list_reverse=[]
for item in list:
    item1=item[::-1]
    list_reverse.append(item1)

print("The original list is: " + str(list))
print("The reversed list is:"+ str(list_reverse))
list.pop()
list_reverse.pop()
print("The last item off of the list has been removed. The lists are now: ")
print("Original: " + str(list))
print("Reversed:"+ str(list_reverse))









