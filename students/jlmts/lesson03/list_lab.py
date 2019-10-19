#!/usr/bin/env python3

"""
exercise 3.2: list lab
joli umetsu
"""

#---series 1---
print("\n---SERIES 1---")

# create list with specified fruits and display the list
list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Display the list:",list) 

# make copy of original list
list1 = list[:]

# prompt user for another fruit
response1 = input("Please enter another fruit > ")

# add user input to the list and print the new list 
list1.append(response1)
print("Display the list:",list1)

# ask the user for a number 
num_input = input("Enter a number > ")
item_num = int(num_input)  # change input string into integer
print("Entered number and corresponding fruit:",item_num, list1[item_num-1])  # print the number and corresponding fruit

# add another fruit to the beginning of the list using "+" and display the list
fruit_1 = ['Bananas']
list1 = fruit_1 + list1
print("Display the list with additional fruit:",list1)

# add another fruit to the beginning of the list using "insert()" and display list
list1.insert(0,'Pineapples')
print("Display the list with additional fruit:",list1)

# display fruits that begin with "p" using a for loop
print("Fruits that begin with 'P':")
for itm in list1:
    if itm[0] == 'P':
        print(itm)


#---series 2---
print("\n---SERIES 2---")

# display the list
list2 = list[:]
print("Display the list:",list2)

# remove last fruit from list; display list
list2.pop()
print("Display the list with last fruit deleted:",list2)

# prompt user for a fruit to delete; find and delete occurences of it (works if list is multiplied by 2)
response2 = input("Enter fruit to delete > ")
for itm in list2:
    if itm == response2:
        list2.remove(itm)
        
print("Display the list:",list2)


#---series 3---
print("\n---SERIES 3---")

# make copy of original list 
list3 = list[:]
print("Display the list:",list3)

# create list of items to remove
pop_list = []

for i, fruit in enumerate(list3):
    response3 = input("Do you like {}? > ".format(fruit.lower()))
    # for answers that aren't yes or no, prompt user to answer with one of those values 
    while response3.lower() != 'yes' and response3.lower() != 'no':
        response3 = input("Please answer 'yes' or 'no'\n")
    # if response is yes, don't do anything
    if response3.lower() == 'yes':
        pass 
    # if response is no, add to list to be deleted later 
    elif response3.lower() == 'no':
        pop_list.append(i)

# reverse order so that subsequent items aren't re-indexed and deleted
pop_list.reverse()        
for j in pop_list:
    list3.pop(j)

print("Display the list:",list3)


#---series 4---
print("\n---SERIES 4---")

# make a copy of original list 
list4 = list[:]
new_list4 = []
print("Display original list:",list4)

# create new list with letters of original items backwards 
for j, fruits in enumerate(list4):
    letters = []
    letters.extend(fruits)
    letters.reverse()
    backwards = []
    for all in letters:
        backwards.append(all)
        new_fruit = "".join(backwards)
    new_list4.append(new_fruit) 

print("Display new list:",new_list4)    
    
# create copy of the new list and remove last item    
last_item = new_list4[len(new_list4)-1]
copy_list4 = new_list4[:]
copy_list4.remove(last_item)
print("Display copy of list with last item removed:",copy_list4)

