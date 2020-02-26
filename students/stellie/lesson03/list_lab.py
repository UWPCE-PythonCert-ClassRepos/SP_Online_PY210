#!/usr/bin/env python3

# Series 1
"""
# Displays list of fruits to user
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list, '\n')

# Prompts user to add a fruit to the list and displays list to user
user_choice = input('Enter another fruit of your choice: ')
fruit_list.append(user_choice)
print('Your fruit has been added to the list.\n', fruit_list, '\n')

# Prompts user to enter a number and display that numbered item on the list
user_number = input('Enter a number: ')
print('The fruit at that list number is:', fruit_list[int(user_number) - 1], '\n')

# Adds another fruit to the list using '+' and displays the list
fruit_list = ['Pineapples'] + fruit_list
print('Pineapples have been added to the list of fruits\n', fruit_list, '\n')

# Adds another fruit to the list using 'insert()' and displays the list
fruit_list.insert(0, 'Strawberries')
print('Strawberries have been added to the list of fruits\n', fruit_list, '\n')

# Displays all fruits that begin with the letter 'P'
print('Below are fruits in the list that start with "P"\n')
for item in fruit_list:
    if item[0] == 'P':
        print(item)
    else:
        continue
"""

#Series 2

