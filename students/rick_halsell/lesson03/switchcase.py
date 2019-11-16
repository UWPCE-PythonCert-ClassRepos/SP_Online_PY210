#!/usr/bin/env python3
def my_zero_func():
    print('1')
    return "I'm zero"

def my_one_func():
    print(2)
    return "I'm one"

switch_func_dict = {
    0: my_zero_func,
    1: my_one_func,
}

switch_func_dict.get(1)()




# Function to list donor in dictionary or to add new donor to dictionary
def full_name_func():
    selection = input('Enter Your Selection: ') # prompt user for selection
    if selection == 'list': #options for list selection
        list_donors_func()
    elif selection == '3':
        thank_you_note_func()
    elif len(selection) == 0: # returns to main menu if input is blank
        main_menu_func()
    elif selection in donors_dictionary.keys(): # calls function if the donor is in the dictionary
        donor_in_dict_func(selection)
    elif selection not in donors_dictionary.keys(): # calls function if the donor is NOT in the dictionary
        donor_not_in_dict_func(selection)
    else: # return to main menu
        main_menu_func()
    return


def full_name_func():

    return

# creating default function to catch any selection variable entries that are not found
def full_name_func_default():
    main_menu_func()
    return
# creating a switch case function dictionary
full_name_func = {
        selection == 'list' : list_donors_func(),
        len(selection) == 0 : main_menu_func(),
        selection in donors_dictionary.keys() : donor_in_dict_func(selection),
        selection not in donors_dictionary.keys() : donor_in_dict_func(selection),
        selection not in donors_dictionary.keys() : donor_not_in_dict_func(selection)
}
# passing the condtion to the full_name_func dictionary and calling function (), setting default condition
full_name_func.get(selection, full_name_func_default)()
