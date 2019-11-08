#!/usr/bin/env python3
import os
import sys
import operator
import time
from operator import itemgetter

# Mailroom (Part 2)
donors_dictionary = {'Jonny Gill' : [3.00, 15.00, 25.12],
    'Bobby Brown' : [11.75, 45.01], 'Michael Bivins' : [345.99],
    'Ricky Bell' : [232.33, 35.03, 123.78], 'Ronnie DeVoe' : [456.00, 789.00]}

def list_donors_full_func():
        print('\n***** Printing Donors and Donations *****')
        # Prints all donors (key) and donation (value) in dictionary.
        for key, value in donors_dictionary.items():
            print(key, '->', value)
            print()
        entry_function() # returns to main menu
        return


# Prints exact keys and values
def exact_selection_func(selection):
         # prints key and value of donor
        print(selection, (donors_dictionary[selection]))
        print() # newline for screen formatting
        # prompts user to add new donation
        donation = float(input('Enter new donation amount: '))
        # add new donation to the donor's list
        donors_dictionary[selection].append(donation)
        # prints out donor and donation
        print(selection, (donors_dictionary[selection]))
        return


def list_donors_func():
        print('\n***** Printing Donors *****')
        for key in donors_dictionary.keys():
            print(key)
            time.sleep(0.5)
        print('*'*25) # formatting
        print()
        thank_you_func()
        return


# Function to Show a Donor that is in the database and add new donation amount
def donor_in_dict_func():
        global selection
        # prompts to enter donor name
        selection = input('Search For Donor -> Enter Name: ')
        if selection in donors_dictionary.keys(): #donor_in_dict_func(selection)
            # getting key from dictionary
            found_donor_donations = donors_dictionary.get(selection)
            try:
                # join to clean up the list output
                cleaned_donations = " ".join(found_donor_donations)
            except TypeError:
                pass
            # prints out exact selection from database
            exact_selection_func(selection)
            selection = selection.replace(" ", "") # more cleaning up options
            thank_you_note_func() # provides selection as input for thank you note
            thank_you_func() # sends user back to the thank you note sub-menu
        else:
            # sends user to function that will add the donor to dictionary
            donor_not_in_dict_func(selection)
        return


# function to add not found donor to the dictionary
def donor_not_in_dict_func(selection):
        if selection not in donors_dictionary.keys():
            print(f"\nDonor Name \'{selection}\' Not Found -- \
                  Adding to List of Donors")
            # adding not found donor to the dictionary as a key
            donors_dictionary[selection] = selection
            # prompting user for donation
            donation = float(input('\nEnter donation amount: '))
            # adding new value/donation as a list to dictionary
            donors_dictionary[selection] = [donation]
            thank_you_func()
        else:
            thank_you_func()
        return


# Function to Generate Thank you note printed to screen
# Goal: Write a full set of letters to all donors to individual files on disk
# for loop to print thank you note
def thank_you_note_func(): # Need help with aligning text when written to disk
        global thank_you_output_file
        for key, value in donors_dictionary.items():
             # cleaning up donation amounts from dictionary
            cleaned_value = ", ".join(map(str, value))
            # gives the total num of donations in dict associated with donor
            total_donations_given = len(value)
            donation_total = sum(value) # gives total sum of all donations
            donation_total = float(donation_total) # turns sun into a float
            # limiting float to second decimal place
            donation_total = (f"{donation_total:.2f}")
            # assigns local variables for formatting letter
            left_aligned_to_line = (f"Dear {key}") # aligned opening
            # aligned body
            mid_left_aligned_body = (f"\n\nThank you for your very kind \
                                     donation of ${donation_total}.")
            # aliged body
            mid_right_aligned = (f"\n\nIt will be put to very good use.")
            # aligned ending
            right_aligned_ending = (f"\n\nSincerely, \n-The Team")
            # create an empty file to write all thank you letters
            thank_you_output_file = (f"{key}_Thank_You_Letter.txt")

            # opening file to save data
            with open(thank_you_output_file, 'w+') as thank_you_output_data:
                # writes letter to files
                thank_you_output_data.write(f"{left_aligned_to_line:<15}, \
                                            {mid_left_aligned_body:^20} \
                                            {mid_right_aligned:>10} \
                                            {right_aligned_ending:>10}")
        number_of_donors = (len(donors_dictionary.items()))
        # tells user how many letters to expect
        print(f"\n{number_of_donors} - Thank You Letters Generated...")
        # telling user where files are located
        print(f"Thank You Letters Location: {os.getcwd()}")
        thank_you_func() # taking user back to menu
        return


# creating default func to catch any switch case entries that are not found
def full_name_func_default():
        entry_function()
        return


# Funtion to provide Thank you note options
def thank_you_func():
        global selection
        #print('You selected \"Send a Thank You\"')
        print ("""
        *********************************
        *   Please Enter a Number       *
        *********************************
        0. Return to the Main Menu
        1. To see a full list of donors
        2. Search Donor database
        3. Send letters to all donors
        *********************************
        """)
        selection = input('Enter Your Selection: ') # prompt user for selection
        try:
            # changed to int to pass to dictionary .get
            selection = int(selection)
        except ValueError:
            pass
        # creating a switch case function dictionary
        full_name_func = {
                0 : entry_function,
                1 : list_donors_func,
                2 : donor_in_dict_func,
                3: thank_you_note_func
        }
        print(f"You Entered: {selection}") # echo back to user
        # switch case dict .get with error handle default
        full_name_func.get(selection, thank_you_func)()
        return


# Function to exit the program
def exit_func():
        print('Exiting Program!')
        time.sleep(1)
        sys.exit()
        return


def report_func():
        # assigns variables for easy formatting
        left_aligned = "Donor Name"
        center = "Total Given"
        mid_right_aligned = "Num Gifts"
        right_aligned = "Average Gift"
        # formatting and printing report header
        print(f"{left_aligned:<15} | {center:^10} | {mid_right_aligned:>10} \
                 | {right_aligned:>13}")
        print('-'*58) # line for terminal output
        # list to hold donor data extracted from dictionary
        comprehensive_donors_list = []

        # for loop to extract specific donors from dictionary
        for selection, value in sorted (donors_dictionary.items()):
            # list to hold data from the specific donor selected
            specific_donor_list = []
            # gives the total num of donations in dictionary associated with donor
            total_donations_given = len(value)
            donation_total = sum(value) # gives total sum of all donations
            donation_total = float(donation_total) # turns sun into a float
            # round answer to the second decimal place
            avg_donation =  round(donation_total / total_donations_given, 2)
            # format string to print 2 decimal places
            avg_donation = (f"{avg_donation:.2f}")
            # format string to print 2 decimal places
            donation_total = (f"{donation_total:.2f}")
             # adding all values to list
            donor_sub_list_values = [selection, donation_total,
                                     total_donations_given, avg_donation
                                    ]

            # for loop to append items to specific_donor_list list
            for item in donor_sub_list_values:
                specific_donor_list.append(item) # adding item to donor's list
                # nesting sub list into comprehensive donors list
            comprehensive_donors_list.append(specific_donor_list)

        donor_list_index = 0 # initializing donor_list_index at 0
        # determining the number of items in list minus 1 to start at 0
        donor_list_index = len(comprehensive_donors_list) - 1
        # loop using lamda to sort list by list index position [3]
        for thing in sorted(comprehensive_donors_list,
                            reverse=True, key=lambda x: float(x[3])):
            # assigning list [donor_list_index][0] to selection
            selection = comprehensive_donors_list[donor_list_index][0]
            # assigning list [donor_list_index][1] to donation_total
            donation_total = comprehensive_donors_list[donor_list_index][1]
            # assigning list [donor_list_index][2] to total_donations_given
            total_donations_given = comprehensive_donors_list[donor_list_index][2]
            # assigning list [donor_list_index][3] to avg_donation
            avg_donation = comprehensive_donors_list[donor_list_index][3]
            donor_list_index -= 1 # decrementing donor_list_index
            print(*thing, sep=" ") # printing out values
        print('-'*58)  # line for terminal output
        entry_function() # back to main menu after loop completes
        return


# Restart or Exit Program Function
def execute_again_func():
        # try and except to handle non numerical entries
        print ("""
        **************************
        *  Execute Script Again? *
        **************************
        0. Execute Again
        1. Exit Program
        **************************
        """)
        run_again = input('Input: ')
        try:
            answer = int(run_again) # changed to int to pass to dictionary .get
        except ValueError:
            pass
        # switch case dict .get with error handle default
        switch_execute_again_dict.get(answer    , execute_again_func)()
        return

def entry_function():
        print ("""
        ******* Main Menu ********
        *  Please Enter a Number *
        **************************
        1. Thank You Note Menu
        2. Create a Report
        3. Restart Program
        4. Exit Program
        **************************
        """)
        answer = input('Enter a number: ') # prompts user to make a selection
        # try and except to handle non numerical entries
        try:
            answer = int(answer) # changed to int to pass to dictionary .get
        except ValueError:
            pass
        print()
        print(f"You Entered: {answer}") # echos selection to user
        print()
        # switch case dict .get with error handle default
        switch_main_menu_dict.get(answer, full_name_func_default)()
        return answer


# Using switch case for main menu prompt
switch_main_menu_dict={
    0: entry_function,
    1: thank_you_func,
    2: report_func,
    3: execute_again_func,
    4: exit_func
}

# Using switch case for run again prompt
switch_execute_again_dict={
    0: entry_function,
    1: exit_func
}


if __name__ == "__main__":
    entry_function()
