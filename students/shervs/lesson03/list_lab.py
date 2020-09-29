#!/usr/bin/env python

#Series 1
print('Series 1\n')

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(f'Fruit List:{fruit_list}')

#Ask the user for another fruit and add it to the end of the list.
fruit_list.append(input("Name a fruit to add to the list > ").title())
print(fruit_list)

#Ask the user for a number and display the number back to the user and
#    the fruit corresponding to that number
fruit_num = input(f"Pick a number between 1 and {len(fruit_list)}> ")
print(fruit_list[int(fruit_num)-1], "corresponding to",fruit_num )
   
#Add another fruit to the beginning of the list using “+”
new_fruit = input("Name a fruit to add to the beginning of the list> ").title()
fruit_list = [new_fruit] + fruit_list
print(fruit_list)

#Add another fruit to the beginning of the list using insert()
fruit_list.insert(0,input("Name a fruit to add to the beginning of the list>"
                          ).title())
print(fruit_list)

#Display all the fruits that begin with “P”, using a for loop.
for fruit in fruit_list:
    if fruit[0] == "P":
         print(fruit)


#Series 2
print('\nSeries 2\n')

#Reload the fruit list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(f'Fruit List:{fruit_list}')

#Remove the last fruit from the list.
fruit_list.pop(-1)
print(fruit_list)

#remove selected fruit from the list
fruit_gone = input("select a fruit to be removed >").title()
for fruit in fruit_list:
    if fruit == fruit_gone:
        fruit_list.remove(fruit)
print(fruit_list)

#bonus
print('\nSeries 2 bonus\n')

#Reload the fruit list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(f'Fruit List:{fruit_list}')
     
fruit_list = fruit_list*2
print(fruit_list)
while True:
    fruit_gone = input("select a fruit to be removed >").title()
    if fruit_gone in fruit_list:
        for fruit in fruit_list:
            if fruit == fruit_gone:
                fruit_list.remove(fruit)
        print(fruit_list)
        break


#Series 3
print('\nSeries 3\n')

#Reload the fruit list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(f'Fruit List:{fruit_list}')

#Remove the fruits that user doesn't like
i = 0
while i < len(fruit_list):
    response = input(f"Do you like {fruit_list[i].lower()}? (yes or no) >")
    if response.lower() == 'no':
        fruit_list.remove(fruit_list[i])
    elif response.lower() == 'yes':
        i += 1
    else:
        print("Please respond with yes or no.")
print(fruit_list)


#Series 4
print('\nSeries 4\n')

#Reload the fruit list
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(f'Fruit List:{fruit_list}')

# Make a new list with the contents of the original, but with all the letters
#    in each item reversed.
new_fruit_list=[]
for fruit in fruit_list:
    new_fruit_list.append(fruit[::-1])

#Delete the last item of the original list. Display the original
#     list and the copy.
fruit_list.pop(-1)
print(fruit_list)
print(new_fruit_list)