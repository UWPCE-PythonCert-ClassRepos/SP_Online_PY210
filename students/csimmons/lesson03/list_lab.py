#!/usr/bin/env python3
# Craig Simmons
# Python 210
# list_lab.py: List Lab Exercises
# Created 11/21/2020 - csimmons

# list data for all exercises
fruits = ['Apples', 'Pears', 'Oranges', 'Blueberries']

def series_one(fruits):
    print('Series One Exercises ************')
    # Display the list of fruits
    print('We have the following fruits available: ' + str(fruits))
    # Ask user for another fruit and add to end of the list
    add_fruit = input('What kind of fruit do you want to add?  ')
    fruits.append(add_fruit)
    # Display the list of fruits again
    print('The following fruits are now available: ' + str(fruits))
    # Ask user to select one of the fruits in above list by position
    print('Select one of the above fruits by its position in the list')
    fruit_idx = input('Please enter a number: ')
    print(fruits[(int(fruit_idx)-1)] + ' are in position ' + str(fruit_idx))
    # add additional fruit to list via concatenation and insert()
    fruits = ['Pineapples'] + fruits
    print(str(fruits) + ' Pineapples added to list')
    fruits.insert(0, 'Bananas')
    print(str(fruits) + ' Bananas added to list')
    #Display all fruits that begin with 'P' using for loop
    for fruit in fruits:
        if fruit.startswith("P"):
            print(fruit)
    return fruits


def series_two(fruits):
    print('\nSeries Two Exercises ************')
    #using the list from series_one, display it
    print(fruits)
    #Remove last fruit from list and display
    fruits.pop(-1)
    print(fruits)
    #Ask user for fruit to delete. Find the fruit and delete
    user_remove = input("Please select a fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in fruits:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    else:
        fruits.remove(user_remove)
    print(fruits)
    # Bonus Section - Multiply list times two. Keep asking until match is found
    # Once found, delete all occurences
    print('\nSeries Two Bonus Code ************')
    double_fruit = fruits * 2 
    print(double_fruit)
    user_remove = input("Please select another fruit to delete from the list (using the fruit's name):  ")
    while user_remove not in double_fruit:
        user_remove = input('Oh no! The fruit you entered is not in the list. Please try again:  ')
    for fruit in double_fruit:
        while user_remove in double_fruit:
            double_fruit.remove(user_remove)
    print(double_fruit)
    #return(double_fruit)
    #return(fruits)

def series_three(fruits):
    print('\nSeries Three Exercises ************')
    #using the list from series_one, display it
    print(fruits)
    #Ask for user input with a line like “Do you like apples?” for each fruit in the list 
    #Display the fruit name in all lowercase.
    for fruit in fruits:
        #Handle Yes/No answers For Yes, leave it. For No remove it
        # if answer is something else, remind user to enter Yes or No until she does
        while True:
            fruit_lower = fruit.lower()
            user_answer = input('Do you like ' + fruit_lower + '? Yes or No: ')
            if user_answer == 'Yes':
                break
            elif user_answer == 'No':
                fruits.remove(fruit)
                break
            else:
                print('Please enter "Yes" or "No"')
    #Display list of fruit the user likes
    print('You like the following fruits: ' + str(fruits))

def series_four(fruits):
    print('\nSeries Four Exercises ************')
    #using the list from series_one, display it
    print(fruits)
    # Make new list with the contents of original, but all the letters in each item reversed.
    new_fruits = []
    for fruit in fruits:
        new_fruits.append(fruit[::-1])
    print(new_fruits)
    #Delete last item of new and original lists
    del new_fruits[-1]
    del fruits[-1]
    print(new_fruits)
    print(fruits)
    print('\nAll List Exercises Complete!')

#series_one(fruits)
#series_two(fruits)
#series_three(fruits)
series_four(fruits)