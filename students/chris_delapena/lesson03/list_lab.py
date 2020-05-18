#!/usr/bin/env python3

#Chris Dela Pena
#UW PCE PY210
#Lesson 3.2 List Lab

#Series 1
print("***SERIES 1***")
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

#Ask user for another fruit and add to list
add_fruit = input("Enter a new fruit to the list: ")
fruit.append(add_fruit)
print(fruit)

#Ask user for a number and display number and fruit
num_fruit = int(input('Enter a number between 1 and ' + str(len(fruit)) + ': '))
print("#" + str(num_fruit) + " fruit is " + fruit[num_fruit - 1])

#Add fruit to beginning of list using "+" and display list
print("Adding kiwi to the list")
add_fruit_2 = ['Kiwi']
fruit = add_fruit_2 + fruit
print(fruit)

#Add another fruit to the beginning of the list using insert() and display list
print("Adding pineapple to the list")
add_fruit_3 = 'Pineapple'
fruit.insert(0, add_fruit_3)
#Saving configuration of list in fruit_1
fruit_1 = fruit
print(fruit_1)

#Display all fruits that begin with "P" using for loop
print("displaying only fruits beginning with a 'P'")
for n in fruit:
    if n[0] == "P":
        print(n)

#Series 2
print("***SERIES 2***")
#Display list
fruit_2 = fruit_1
print(fruit_2)
#Remove last fruit
del fruit_2[-1]
#Display list
print(fruit_2)
#Ask user for fruit to delete
del_fruit = input('Select a fruit to remove: ')
#Find and delate the fruit.
if del_fruit not in fruit_2:
    print("Fruit not in the list. ")
    del_fruit = input("Select fruit to remove: ")
else:
    for m in fruit_2:
        if m == del_fruit:
            fruit_2.remove(m)
print(fruit_2)

#Series 3
print("***SERIES 3***")
#Display list
print(fruit)
fruit_3 = fruit_1
#Go through list asking if user likes that fruit
for j in fruit_3:
    selection = input("Do you like {}? ".format(j))
    if selection == "yes":
        continue
    elif selection ==  "no":
        #For each no, delete fruit from list
        fruit_3.remove(j)
        continue
    else:
        #For answers not yes/no, prompt user to answer w/ one of those
        print("Enter yes or no")
        continue
#Display list
print(fruit_3)

#Series 4
print("***SERIES 4***")
#Display list
fruit_4 = fruit_1
print(fruit_4)
#Reverse all letters for each item
for k in range (len(fruit_4)):
    fruit_4[k] = fruit_4[k][::-1]
print(fruit_4)
#Delete last item of original list. Display list and copy
fruit_1.pop()
print(fruit_1)
print(fruit_4)
