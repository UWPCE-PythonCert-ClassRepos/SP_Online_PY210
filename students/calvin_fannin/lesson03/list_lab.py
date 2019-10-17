#!/usr/bin/env python3

#series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response = input("Input another fruit > ")
#add fruit to end of list
fruits.append(response)
print(fruits)
response = input("Enter a number for a fruit > ")
#Display fruit from input number
print (response + " " + fruits[int(response) - 1])
#add fruit to start of list using "+""
fruits = ['Banna'] + fruits
print(fruits)
fruits.insert(0, 'Pineapple')
print(fruits)
#display all fruits that begin with p
for item in fruits:
    if 'P' in item[0:1]:
        print(item)

#series 2
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
#remove last fruit from list
fruits.pop(len(fruits)-1)
print(fruits)
response = input("Enter a fruit to delete > ")
#delete fruit entered from input if fruit not found double list
while not response in fruits:
      fruits = fruits * 2
      response = input("Enter a fruit to delete > ")
else:
    #remove all occurences of found fruit
    while response in fruits:
        fruits.remove(response)

#series 3
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
for i, item in enumerate(fruits):
    response = input("Do you like " + item + " yes or no > ")
    while not (response == 'yes' or response == 'no'):
        response = input("Please enter only yes or no > ")
    if response == 'no':
        #delete fruit on no
        fruits.pop(i)
    elif response == 'yes':
        #lower case fruit on yes
        fruits[i] = item.lower()
print(fruits)

#series 4
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
#copy the list to new list
copy_fruits = fruits[:]
#reverse each item in list
for i,item in enumerate(fruits):
    copy_fruits[i] = item[-1::-1]
#delete the last item in the list
fruits.pop(i)














