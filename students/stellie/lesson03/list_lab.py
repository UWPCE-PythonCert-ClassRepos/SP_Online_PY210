#!/usr/bin/env python3

# Series 1
# Displays list of fruits to user
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruit list:', fruit_list, '\n')

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

#Series 2
# Displays list of fruits to user
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruit list:', fruit_list, '\n')

# Removes last fruit from list and displays list to user
fruit_list.pop()
print('The last item on the list has been removed.\n', fruit_list, '\n')

# Prompts the user to delete a fruit from the list and displays the list
user_delete = input('Choose a fruit to delete from the list: ')
for item in fruit_list:
    if item == user_delete:
        fruit_list.remove(item)
    else:
        continue
print(fruit_list)

# Bonus: Multiplies the list times two, keeps asking until a match is found then deletes all occurrences

# Series 3
# Displays list of fruits to user
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruit list:', fruit_list, '\n')
favorites_list = []

# Prompts the user to answer which fruit they like/dislike on the list
for item in fruit_list:
    user_favorites = input('Do you like {}? y/n '.format(item.lower()))
    while user_favorites != 'n' and user_favorites != 'y':
        user_favorites = input('Please answer y or n ')
    if user_favorites == 'y':
        favorites_list.append(item)
    else:
        continue   
print(favorites_list)

# Series 4
# Displays list of fruits to user
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print('Fruit list:', fruit_list, '\n')

# Displays reversed list with reversed items to user
reversed_list = []
for item in fruit_list:
    reversed_list.append(item[::-1])
print('Original list with item letters reversed:', reversed_list, '\n')

# Removes the last item on the original list and displays to user
fruit_list.pop(-1)
print('Original list (with last item removed):', fruit_list, '\n')
print('Copy:', reversed_list, '\n')