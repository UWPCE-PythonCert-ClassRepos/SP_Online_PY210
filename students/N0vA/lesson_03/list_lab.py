#!/usr/bin/env python3

#### List Lab Exercises ####

# Series 1 #
# Creat original list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruit_list)

print('Please add a fruit to the list')
your_fruit = input('> ')
fruit_list.append(your_fruit)
print(fruit_list)

print('Now pick a number from to see what fruit you get.')
your_num = int(input('> '))
print('Your number is ', your_num)
x = your_num - 1
print(fruit_list[x])

# Add item at beginning of list
print('Now enter another fruit')
fruit_2 = [input('> ')]
fruit_list = fruit_2 + fruit_list
print(fruit_list)

# Use insert to add item at beginning of list
print('Add one more fruit')
fruit_3 = input('> ')
fruit_list.insert(0, fruit_3)
print(fruit_list)

# Display any fruits that start with a P
print('These are the fruits that start with the letter P')
for fruit in fruit_list:
    if fruit[0] == 'P' or fruit[0] == 'p':
        print(fruit)

series_1 = fruit_list[:]

# Series 2

series_2 = series_1[:]
print(series_2)

# Remove last item in the list
print('Removing last item...')
series_2.pop()
print(series_2)

# Ask user for a fruit and delete it from the list
print('Please list a fruit you would like to be deleted from the list')
del_fruit = input('> ')
series_2.remove(del_fruit)
print(series_2)

# Bonus
list_2 = series_2 + series_2


# Series 3

print(series_1)
series_3 = series_1[:]

user_answers = ['Yes', 'No', 'yes', 'no']

# Ask user if they like each fruit item
def fav_fruits(list):
    for f in list:
        response = ''
        liked_fruits = []

        while response not in user_answers:
            response = input('Do you like {}? [Yes/No]'.format(f.lower()))

        if response == 'Yes' or response == 'yes':
            liked_fruits.append(f)
            print('Perfect.  Next item...')
        elif response == 'No' or response == 'no':
            list.remove(f)
    return list

print(series_3)

# Series 4

series_4 = series_1[:]

# Make every item spelled backwards is new list
def flip_flop(list):
    for item in list:
        list[list.index(item)] = item[::-1]

flip_flop(series_4)
series_1.pop()
print('This is the original list', series_1)
print('This is the new copy where each item is backwards', series_4)
