# ------------------------------------------#
# !/usr/bin/env python3
# Title: List_Lab.py
# Desc: Learn the basic ins and outs of Python lists..
# Tian Xie, 2020-04-05, Created File
# ------------------------------------------#

# Series 1
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
my_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Display the list
print(my_list)

# Ask the user for another fruit and add it to the end of the list
response = input("Please enter a name for a fruit:")
my_list.append(response)

# Display the list
print(my_list)

# Ask the user for a number and display the number back to the user and the fruit corresponding to that number.

for i,item in enumerate(my_list):
    i = int(input("Please enter a number:"))-1
    print(i+1, item)
    break

# Add another fruit to the beginning of the list using “+” and display the list.
another_fruit = ['Lemon']
my_list = another_fruit + my_list
print(my_list)

# Add another fruit to the beginning of the list using insert() and display the list.
another_fruit2 ='Strawberry'
my_list.insert(0,another_fruit2)
print(my_list)

# Display all the fruits that begin with “P”, using a for loop.
for item in my_list:
    if 'P' in item:
        print(item)

# Series 2
my_list2 =['Apples', 'Pears', 'Oranges', 'Peaches']
#Display the list.
print(my_list2)
#Remove the last fruit from the list.
my_list2 = my_list2[:-1]
#Display the list.
print(my_list2)
#Ask the user for a fruit to delete, find it and delete it.
fruit_to_del = input('Please enter a fruit to delete')
my_list2.remove(fruit_to_del)
print(my_list2)


# Series 3
my_list3 = ['Apples', 'Pears', 'Oranges', 'Peaches']
liked_list = []
for i in my_list3:
    response = input("Do you like " + i + "? ").lower()
    while response != 'yes' and response != 'no':
        response = input('Please answer yes or no ')
    if response == "yes":
       liked_list.append(i)
    else:
        pass
print(liked_list)
