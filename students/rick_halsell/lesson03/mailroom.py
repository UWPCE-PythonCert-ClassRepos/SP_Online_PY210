#!/usr/bin/env python3
import os
import sys
import operator
from operator import itemgetter

# Mailroom (Part 2)
donors_dictionary = {'Jonny Gill' : [3.00, 15.00, 25.12], 'Bobby Brown' : [11.75, 45.01], 'Michael Bivins' : [345.99], 'Ricky Bell' : [232.33, 35.03, 123.78], 'Ronnie DeVoe' : [456.00, 789.00]}

def list_donors_full_func():
    print('\n***** Printing Donors and Donations *****')
    for key, value in donors_dictionary.items(): # prints all donors (key) and donation (value)
        print(key, '->', value)
    print()
    entry_function() # returns to main menu
    return

# Prints exact keys and values
def exact_selection_func(selection):
    print(selection, (donors_dictionary[selection])) # prints key and value of donor
    print() # newline for screen formatting
    donation = float(input('Enter new donation amount: ')) # prompts user to add new donation
    donors_dictionary[selection].append(donation) # add new donation to the donor's list
    print(selection, (donors_dictionary[selection])) # prints out donor and donation
    return

def list_donors_func():
    #print('You selected \"Create a Report\"')
    print()
    print('***** Printing Donors *****')
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
    selection = input('Search For Donor -> Enter Name: ') # prompts to enter donor name
    if selection in donors_dictionary.keys(): #donor_in_dict_func(selection)
        founddonordonations = donors_dictionary.get(selection) # getting key from dictionary
        try:
            cleaneddonations = " ".join(founddonordonations) # join to clean up the list output
        except TypeError:
            pass
        exact_selection_func(selection) # prints out exact selection from database
        selection = selection.replace(" ", "") # more cleaning up options
        thank_you_note_func() # provides selection as input for thank you note
        thank_you_func() # sends user back to the thank you note sub-menu
    else:
        donor_not_in_dict_func(selection) # sends user to function that will add the donor to dictionary
    return

# function to add not found donor to the dictionary
def donor_not_in_dict_func(selection):
    if selection not in donors_dictionary.keys():
        print(f"\nDonor Name \'{selection}\' Not Found -- Adding to List of Donors")
        donors_dictionary[selection] = selection # adding not found donor to the dictionary as a key
        donation = float(input('\nEnter donation amount: ')) #prompting user for donation
        donors_dictionary[selection] = [donation] # adding new value/donation as a list to dictionary
        thank_you_func()
    else:
        thank_you_func()
    return

# Function to Generate Thank you note printed to screen
# Goal: Write a full set of letters to all donors to individual files on disk.
# for loop to print thank you note
def thank_you_note_func(): # I need help with aligning text when written to a file
    global thankyoutoutputfile
    #print(f"{left_aligned:<15} | {center:^10} | {mid_right_aligned:>10} | {right_aligned:>13}")
    numberofdonors = (len(donors_dictionary.items()))
    print(f"\n Generating {numberofdonors} Thank You Letters:")
    for key, value in donors_dictionary.items():
        cleanedvalue = ", ".join(map(str, value)) # cleaning up donation amounts from dictionary
        totaldonationsgiven = len(value) # gives the total number of donations in dictionary associated with donor
        donationtotal = sum(value) # gives total sum of all donations
        donationtotal = float(donationtotal) # turns sun into a float
        donationtotal = (f"{donationtotal:.2f}") # limiting float to second decimal place
        # assigns local variables for formatting letter
        left_aligned_to_line = (f"Dear {key}") # aligned opening
        mid_left_aligned_body = (f"\n\nThank you for your very kind donation of ${donationtotal}.") # aligned body
        mid_right_aligned = (f"\n\nIt will be put to very good use.") # aliged body
        right_aligned_ending = (f"\n\nSincerely, \n-The Team") # aligned ending
        thankyoutoutputfile = (f"{key}_Thank_You_Letter.txt") # create an empty file to write all thank you letters
        thankyoutoutputdata = open(thankyoutoutputfile, 'w+') # opens the file for writing data
        # writes letter to files
        thankyoutoutputdata.write(f"{left_aligned_to_line:<15},{mid_left_aligned_body:^20}{mid_right_aligned:>10}{right_aligned_ending:>10}") # prints thank you letter to screen
        thankyoutoutputdata.close() # closing file
    print('\nThank you letters created...') # giving user feedback
    print(f"Thank you letters location: {os.getcwd()}") # telling user where files are located
    thank_you_func() # taking user back to menu

# creating default function to catch any selection variable entries that are not found
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
        selection = int(selection) # changed to int to pass to dictionary .get
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
    full_name_func.get(selection, thank_you_func)()# switch case dict .get with error handle default
    return

# Function to exit the program
def exit_func():
    print('Exiting Program!')
    time.sleep(1)
    sys.exit()
    return

# Restart or Exit Program Function
def execute_again_func():
    while True:
        RunAgain = input('Would you like to execute this script again? (Y/N): ').lower()
        if not (RunAgain in ('yes', 'y')):
            exit_func()
        if (RunAgain in ('yes', 'y')):
            entry_function()
    return

def report_func():
    # assigns variables for easy formatting
    left_aligned = "Donor Name"
    center = "Total Given"
    mid_right_aligned = "Num Gifts"
    right_aligned = "Average Gift"

    # formatting and printing report header
    print(f"{left_aligned:<15} | {center:^10} | {mid_right_aligned:>10} | {right_aligned:>13}")
    print('-'*58) # line for terminal output
    x_list = [] # list to hold donor data extracted from dictionary
    #for loop to
    for selection, value in sorted (donors_dictionary.items()):
        specificdonorlist = [] # list to hold data from the specific donor selected
        totaldonationsgiven = len(value) # gives the total number of donations in dictionary associated with donor
        donationtotal = sum(value) # gives total sum of all donations
        donationtotal = float(donationtotal) # turns sun into a float
        avgdonation =  round(donationtotal / totaldonationsgiven, 2) # round answer to the second decimal place
        avgdonation = (f"{avgdonation:.2f}") # format string to print 2 decimal places
        donationtotal = (f"{donationtotal:.2f}") # format string to print 2 decimal places
         # adding all values to list
        sublistvalues = [selection, donationtotal, totaldonationsgiven, avgdonation]
        # for loop to append items to specificdonorlist list
        for item in sublistvalues:
            specificdonorlist.append(item) # adding item to donor's list
        x_list.append(specificdonorlist) # nesting sub list into comprehensive donors list
    numofthingitems = 0 # initializing numofthingitems at 0
    numofthingitems = len(x_list) - 1 # determining the number of items in list minus 1 to start at 0
    # loop using lamda to sort list by list index position [3]
    for thing in sorted(x_list, reverse=True, key=lambda x: float(x[3])):
        selection = x_list[numofthingitems][0] # assigning list [numofthingitems][0] to selection
        donationtotal = x_list[numofthingitems][1] # assigning list [numofthingitems][1] to donationtotal
        totaldonationsgiven = x_list[numofthingitems][2] # assigning list [numofthingitems][2] to totaldonationsgiven
        avgdonation = x_list[numofthingitems][3] # assigning list [numofthingitems][3] to avgdonation
        #print(f"{selection:<15}{donationtotal:^24}{totaldonationsgiven:>3}{avgdonation:>18}") # format string for report
        numofthingitems -= 1 # decrementing numofthingitems
        # I need help with aligning text when written to a file
        print(*thing, sep=" ") # printing out values
        #print(f"Thank you {selection} for your donations of {donationtotal}.")
        #print(f"{selection:<15}{donationtotal:^24}{totaldonationsgiven:>3}{avgdonation:>18}") # format string for report
    print('-'*58)  # line for terminal output
    entry_function() # back to main menu after loop completes
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
    switch_main_menu_dict.get(answer, full_name_func_default)()# switch case dict .get with error handle default
    return answer

# Using switch case for main menu prompt
switch_main_menu_dict={
    0: entry_function,
    1: thank_you_func,
    2: report_func,
    3: execute_again_func,
    4: exit_func}

if __name__ == "__main__":
    entry_function()
