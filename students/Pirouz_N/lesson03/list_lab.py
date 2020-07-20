#!/usr/bin/env python3
"""
Purpose: Lessen 3 homework two, list lab, python certificate from UW
Author: Pirouz Naghavi
Date: 06/26/2020
"""


# Series 1
# Creating a list that contains 'Apples', 'Pears', 'Oranges' and 'Peaches'.
series1_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

# Printing series one
print('Current fruit list is:')
print(series1_list)

# Asking for another fruit
response_fruit = input("Please add another fruit to add to the list: ")

# Adding new fruit to the list
series1_list.append(response_fruit)

# Printing series one
print(series1_list)

input_not_acceptable = True

while input_not_acceptable:

    # Asking for a number between 1 and 5
    response_number = input("Please provide a number between 1 and {}: ".format(len(series1_list)))

    # Checking input
    try:
        int(response_number)

    except ValueError:
        print('Input was not a number. Please try again.')

    except:
        print('Input could not be converted to a number.')

    else:
        if int(response_number) > len(series1_list) or int(response_number) < 1:
            print('The number that was inputted  was {} which is not in range of 1 to 5 inclusively.'
                  .format(int(response_number)), 'Please try again.')
        else:
            input_not_acceptable = False

# Printing fruit number response_number on the list
print("Fruit number {} on the list is {}.".format(response_number, series1_list[int(response_number) - 1]))

# Printing task to accomplish
print('Adding bananas to the list.')

# Adding banana to the list
series1_list = ['Bananas'] + series1_list

# Printing series one
print('Current fruit list is:')
print(series1_list)

# Printing task to accomplish
print('Adding pineapples to the list.')

# Adding pineapple to the list
series1_list.insert(0, 'Pineapples')

# Printing series one
print('Current fruit list is:')
print(series1_list)

series1_list_starting_with_P = []

# Printing the list of all the fruits that start with p or P
for fruit in series1_list:
    if fruit[0] == 'P':
        series1_list_starting_with_P.append(fruit)

# Printing series one
print('Current fruit list of fruits starting with letter p is:')
print(series1_list_starting_with_P)


# Series 2
# Copying list from series one to series two
series2_list = series1_list[:]

# Printing series 2 list
print('Current fruit list is:')
print(series2_list)

# Removing last fruit from list
series2_list.pop()
# Or del series2_list[len(series2_list) - 1:]

# Printing series 2 list
print(series2_list)

# Multiplying list by two
series2_list = series2_list * 2

# Informing user of plan
print('List has been doubled to show complete remove where every instance will be removed.')
print('Displaying current list after doubling operation.')
print(series2_list)

# Asking the user for a fruit to delete
input_not_acceptable = True

while input_not_acceptable:

    # Asking the user to select a fruit from the list
    selected_fruit = input("Please select a fruit from the list: ")

    # Checking list for match
    match_found = False
    try:
        for item in series2_list:
            if item == str(selected_fruit):
                match_found = True
                del series2_list[series2_list.index(selected_fruit)]

    except ValueError:
        print('Input was not text. Please try again.')

    except:
        print('Run time error has occurred due to your input. Please try a different input.',
              'Please try again.')

    else:
        if not match_found:
            print('Your selection could not be found on the list.', 'Please try again.')
        else:
            input_not_acceptable = False

# Displaying current doubled list
print('Displaying current list after removing an element, but still doubled.')
print(series2_list)

# Displaying current not doubled list
print('Displaying current list after removing an element. Elements are no longer doubled.')
print(list(set(series2_list)))

# Series 3
# Copying list from series one to series three
series3_list = series1_list[:]
print('New series.', 'New series fruit list contains.')
print(series3_list)

# Copying list to avoid iteration issues during deletion
modified_series3_list = series3_list[:]

# Iterating through list
for fruit in series3_list:
    input_not_acceptable = True
    while input_not_acceptable:
        reply_on_deletion = input('Please respond by typing yes or no. Do you like {}? '.format(fruit.lower()))
        try:
            if str(reply_on_deletion) == 'no':
                del modified_series3_list[modified_series3_list.index(fruit)]
                input_not_acceptable = False
            elif str(reply_on_deletion) == 'yes':
                input_not_acceptable = False
            else:
                print('Your response was not yes or no. Please respond only yes or no.')

        except ValueError:
            print('Input was not text. Please try again.')

        except:
            print('Run time error has occurred due to your input. Please try a different input.',
                  'Please try again.')

# Printing new and modified list
print('Printing new list, which is a copy of series one list')
print(modified_series3_list)

# Series 4
# Copying list from series one to series four
series4_list = series1_list[:]

# Reversing letters of each element
for i, fruit in enumerate(series4_list):
    series4_list[i] = fruit.lower()[:: -1]

# Removing last element
series4_list.pop()

# Printing new and modified list
print('Printing new and modified list.', 'This list has very fruit with letters reversed and last item is removed.')
print(series4_list)

print('Printing original list.')
print(series1_list)
