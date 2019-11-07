#!/usr/bin/env python
# PY210 Lesson 3 List_Lab Activity
# Jonathan Vu

# List 1
print('\n\n PART 1')
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
new_fruit = input('\nPlease add another fruit to the list: \n>> ')
fruit_list.append(new_fruit)
print(fruit_list)
num_select = input('\nPlease enter a number for the fruit you want: \n>> ')
print(fruit_list[int(num_select) - 1])
fruit_list = ['Pineapple'] + fruit_list
fruit_list.insert(0, 'Banana')
for i in range(len(fruit_list)):
    if fruit_list[i][0] == 'P':
        print(fruit_list[i])

# List 2
print('\n\n PART 2')
fruit_list_copy = fruit_list.copy()
print(fruit_list_copy)
fruit_list_copy.pop(len(fruit_list_copy)-1)
print(fruit_list_copy)
remove_fruit = input('\nPlease provide a fruit in the list to remove: ')
fruit_list_copy.remove(remove_fruit)
print(fruit_list_copy)

# List 3
print('\n\n PART 3')
fruit_list_copy3 = fruit_list.copy()
for i in range(len(fruit_list_copy3)):
    response = input("\nDo you like " + fruit_list[i].lower() + "? > ")
    while response != 'no' and response != 'yes':
        response = input("\nPlease enter yes or no > ")
    if response == 'no':
        fruit_list_copy3.remove(fruit_list[i])
print(fruit_list_copy3)

# List 4
print('\n\n PART 4')
fruit_list4 = fruit_list.copy()
for i in range(len(fruit_list4)):
    fruit_list4[i] = fruit_list4[i][::-1]
fruit_list4.pop(len(fruit_list)-1)
print(fruit_list4)
print(fruit_list)