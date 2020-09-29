#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 11/9/2019
# list_lab.py

# displays the list or indexed item in standard format
def run_print(fruits, index=0):
    menu=[]

    # if no index is passed print full list
    if index == 0:
        for i in range(len(fruits)):
            menu.append(print_format(i + 1, fruits[i]))

    # else print indexed item
    else:
        menu = print_format(index, fruits[index - 1])
    print(menu)

# format the display item
def print_format(index, item):
    return str(index) + ') ' + item

# standardize the list format
def fruit_format(fruit):

    # if fruit is not plural, pluralize it
    if fruit.endswith('y'): 
        fruit = fruit[0 : len(fruit) - 1]
        fruit += 'ies'
    elif fruit.endswith('ch'): 
        fruit += 'es'
    elif not (fruit.endswith('s') or fruit == ''):  
        fruit += 's'

    # if fruit is not capitalized, capitalize the first letters
    fruit = fruit.title()
    return fruit

# create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = (['Apples', 'Pears', 'Oranges', 'Peaches'])

# display the list
run_print(fruits)

#------------------------------- Series 1 ------------------------------------------------------

# ask the user for another fruit
response = fruit_format(input("Please add a fruit > "))

# add the fruit to the end of the list
fruits.append(response)

# display the list
run_print(fruits)

# ask the user for a number, using a loop to get a valid response 
while True:

    # prompt user for input
    response = input("Enter a number from list > ")

    # if response is not numeric
    if not response.isnumeric():
        response = -1         
    
    # if response is in range
    if int(response) > 0 and int(response) <= len(fruits):
        
        # display the number back to the user and the fruit
        run_print(fruits, int(response))
        break

    # else diplay error and reprompt user input
    else: 
        print('Invalid option, please try again')
 
# Add another fruit to the beginning of the list 
response = fruit_format(input("Please add a fruit > "))
fruits = [response] + fruits

# display the list
run_print(fruits)

# add another fruit to the beginning of the list
response = fruit_format(input("Please add a fruit > "))
fruits.insert(0, response)

# display the list
run_print(fruits)

# create a list of all the fruits that begin with 'P'
p_list=[]
i=0
for fruit in fruits:
    i+=1
    if fruit[0] == 'P': 
        p_list.append(print_format(i, fruit))

# display the 'P' list
print(p_list)

#------------------------------- Series 2 ------------------------------------------------------

# copy the list from series 1
series_2 = []
series_2 += fruits

# display the list
run_print(series_2)

# remove the last fruit from the list
series_2.pop()

# display the list
run_print(series_2)

# ask the user for a fruit to delete, find it and delete it
response = fruit_format(input("Please enter the name of a fruit to delete > "))

# keep asking until a match is found. Once found, delete all occurrences
for fruit in series_2:
    if fruit == response:
        series_2.remove(response) 

# display the results of series 2
run_print(series_2)

#------------------------------- Series 3 ------------------------------------------------------

# copy the list from series 1
series_3 = []
series_3 += fruits

# ask the user for input displaying “Do you like apples?” for each fruit in the list
for fruit in fruits:
    while True:
        response = input("Do you like {}? ".format(fruit.lower()))
        response = response.lower()
        if response == 'yes':
            break
        elif response == 'no':
            series_3.remove(fruit)
            break
        else:
            print("Please answer with a 'yes' or 'no'")

# display the results of series 3
run_print(series_3)

#------------------------------- Series 4 ------------------------------------------------------

# copy the list from series 1
series_4 = []
series_4 += fruits

# make a new list with the contents of the original, but with all the letters in each item reversed
fruits_reverse =[]
for fruit in series_4:
    fruits_reverse.append(fruit[len(fruit) + 1 : : -1])

# delete the last item of the original list. 
fruits.pop()

# display the original list and the copy
run_print(fruits)
run_print(fruits_reverse)