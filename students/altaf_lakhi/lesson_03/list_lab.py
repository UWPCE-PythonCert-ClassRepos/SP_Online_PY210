#!/usr/bin/env python3

#series 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

#append new input item to list
new = input('Enter a fruit: ')
fruit.append(new)
print(fruit)

#ask user for a number and display corresponding item
num = int(input('Enter a number: '))
print(num, fruit[num-1])

#add new item with '+'
fruit = ['Cherries'] + fruit
print(fruit)

#add new item with 'insert'
fruit.insert(0, 'Guava')
print(fruit)

#display all items that start with 'P'
for i in fruit:
    if i.startswith('P'):
        print(i)


#series 2
fruit_list = fruit.copy()
print(fruit_list)

#remove last fruit
fruit_list.pop()
print(fruit_list)

#ask user for a fruit to remove
def delete_fruits(fruit_list):    
    delete_fruit = str(input('Delete a fruit: '))
    for i in fruit_list:
        if delete_fruit in i:
            fruit_list.remove(i)
    return fruit_list

delete_fruits(fruit_list)

#bonus
print(fruit_list + fruit_list)


#series 3
fruit_list_2 = fruit.copy()
print(fruit_list_2)
for i in fruit_list_2:
    answer = input('Do you like ' + i.lower() + '?')
    while answer.lower() not in ('yes', 'no'):
        answer = input("Please enter 'yes' or 'no' only: ")
    if answer.lower() == 'no':
        fruit_list_2.remove(i)
    else:
        continue
print(fruit_list_2)

#series 4
fruit_list_3 = fruit.copy()
fruit_list_4 = []
for i in fruit_list_3:
    fruit_list_4.append(i[::-1])
fruit_list_3.pop()

print(fruit_list_3, fruit_list_4)





# for i in fruit_list_3:
#     answer = input('Do you like ' + i.lower() + '?')
#     while answer.lower() not in ('yes', 'no'):
#         print("Please enter only yes or no")
#         answer = input("Do you like " + i.lower() + "? Enter yes or no only?")
#     if  answer.lower() == "no":
#         fruit_list_3.remove(i)
# print(fruit_list_3)









#options to turn list into dict

#1) fruit_dicty = {i:j for i,j in enumerate(fruit)}

#2) enum = enumerate(fruit)
# for i,j in enum:
# fruit_dicty = {i,j}
# fruit_dict = dict((i,j) for i,j in enum)