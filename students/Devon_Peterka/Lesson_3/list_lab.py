#!/usr/bin/env python3

'''
Accomplish the following (4) series of actions:
# 1)  Create a list containing "Apples", "Pears", "Oranges" and "Peaches"
#     - Display the list
#     - Ask the User for another fruit and add to the end of list
#     - Display the new list
#     - Ask the user for a number and display the number and corresponding
#       fruit on a 1-is-first basis.
#     - Add another fruit to the beginning of the list using "+" and display
#     - Add another fruit to the beginning of the list using insert() and
#       display the list
#     - Display all fruits that begin with 'P' in the list
#
# 2)  Using the list from Series 1 above
#     - Display the list
#     - Remove the last fruit from the list
#     - Display the new list
#     - Ask the user for a fruit to delete, find it, and delete it
#     - (Bonus) Multiply the list by 2, keep asking until a match is found,
#       then delete all occurrences.
#
# 3)  Using the list from Series 1 above
#     - Ask the user to input diplaying a line like, "Do you like apples?"
#       for each fruit on the list (making the fruit lowercase)
#     - For each "no" response, delete from the list.
#     - For any answer that is not "yes" or "no" prompt the user to answer "yes"
#       or "no"
#     - Display the new list
#
# 4)  - Make a new list with the contents of the original but with all the
#       letters in each item reversed.
#     - Delete the last item from the original list.
#     - Display the original list and the copy.
'''

# Series #1
print('---Series #1 of Prompt---')
prompt_list = ['Apples', 'Pears', 'Oranges', 'Peaches']    # list given in prompt
list_series1 = prompt_list[:]    # copy prompt list so prompt remains unaltered
print('Starting List: ', list_series1)    # print prompt list as requested
list_series1.append(input('\nName a fruit to add: ').title())    # ask user for a fruit, add to end of list
print('\n Now List is: ', list_series1)    # show the new list as requested
show_num = int(input('Give an integer from 1-' + str(len(list_series1)) + ': '))
while show_num not in range(1, len(list_series1)+1):    # protection from faulty user.  No protection from string input though...
    print('Try again... Maybe follow instructions this time.')
    show_num = int(input('\nGive an integer from 1-' + str(len(list_series1)) + ': '))
print('\nYou Picked: ', list_series1[show_num-1])    # display corresponding fruit from list
list_series1 = [input('\nName another Fruit: ').title()] + list_series1    # ask for input, add to beginning of list with +
print('\nUpdated List: ', list_series1)
list_series1.insert(0, input('\nName another Fruit: ').title())    # ask for input (implied by instructions), add to beginning of list with '.insert()'
print('\nSeries 1 Result: ', list_series1)    # print final list

# Series #2
print('\n---Series #2 of Prompt---')
list_series2 = list_series1[:]
print('Starting List:', list_series2)    # display list created in series 1
list_series2.remove(list_series2[-1])    # remove last item as requested
print('With Last Item Removed: ', list_series2)    # display the new list
to_remove = input('\nName a fruit to remove from list: ')
while to_remove not in list_series2:    # protect from overly imaginative users
    print('\nInvalid Input. Must be one of the following: \n')
    for i, fruit in enumerate(list_series2):    # remind user of their options
        print(fruit)
    to_remove = input('Name a fruit to remove from list: ')    # re-ask the prompt
list_series2.remove(to_remove)
print('\nSeries 2 Result: ', list_series2)    # Not specifically asked, but implied

#Series #2 - BONUS:
list_series2B = 2 * list_series2[:]    # multiply the list by 2
print('\nBONUS LIST: ', list_series2B)
to_remove = input('\nName a fruit to remove from list: ')
while to_remove not in list_series2B:    # protect from overly imaginative users
    print('Invalid Input. Must be one of the following: ', list_series2)    # use original list so there are no doubles in user prompt
    for i, fruit in enumerate(list_series2):
        print(fruit)
    to_remove = input('\nName a fruit to remove from list: ')
while to_remove in list_series2B:    # Remove ALL instances from doubled list
    list_series2B.remove(to_remove)
print('\nModified BONUS LIST: ', list_series2B)

# Series #3
print('\n---Series #3---')
list_series3 = list_series1[:]    # copy series #1 list so it remains unaltered.
print('Starting List: ', list_series3)
idx = 0
while list_series3[idx:idx+1]:    # Will be empty/falsy once list is done.
    rmv_item = input('\nDo you like ' + list_series3[idx].lower() + '?: ').lower()
    while rmv_item != 'yes' and rmv_item != 'no':
        print('Invalid Input')
        rmv_item = input('\nAsking again... Do you like ' + list_series3[idx].lower() + ' (yes/no): ').lower()
    if rmv_item == 'no':
        del list_series3[idx]
        continue    #do not increment idx once item is deleted otherwise will skip the next item.
    idx += 1    #increment only if item was not deleted
print('\nSeries 3 Result: ', list_series3)

# Series #4
list_series4 = prompt_list[:]
for idx in range(len(list_series4)):
    new_item = list_series4 [idx][::-1]
    list_series4 [idx] = new_item
del list_series4[-1]
print('\nSeries #4')
print('\n               Original List: ', prompt_list)
print('\n  List after Series #4 Steps: ', list_series4)
