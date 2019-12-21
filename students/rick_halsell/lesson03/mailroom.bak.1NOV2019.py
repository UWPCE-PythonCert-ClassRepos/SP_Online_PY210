#!/usr/bin/env python3
import os
import time
import sys
import contextlib
# Mailroom (Part 1)

donors_dictionary = {'Jonny Gill': [3.00, 15.00, 25.00], 'Bobby Brown': [11.00, 45.01], 'Michael Bivins': [345.00], 'Ricky Bell': [232.00, 35.00, 123.00], 'Ronnie DeVoe': [456.00, 789.00]}

def listdonorsfullfunc():
    print('\n***** Printing Donors and Donations *****')
    for key, value in donors_dictionary.items(): # prints all donors (key) and donation (value)
        print(key, '->', value)
        time.sleep(0.5) # slows program for processing
    print()
    mainmenufunc() # returns to main menu
    return

# Prints exact keys and values
def exactselection(selection):
    print(selection, (donors_dictionary[selection])) # prints key and value of donor
    print() # newline for screen formatting
    donation = float(input('Enter new donation amount: ')) # prompts user to add new donation
    donors_dictionary[selection].append(donation) # add new donation to the donor's list
    print(selection, (donors_dictionary[selection])) # prints out donor and donation
    return

def listdonorsfunc():
    #print('You selected \"Create a Report\"')
    print()
    print('***** Printing Donors *****')
    for key in donors_dictionary.keys():
        print(key)
        time.sleep(0.5)
    print('*'*25) # formatting
    print()
    thankyoufunc()
    return

# Function to Show a Donor that is in the database and add new donation amount
def donorindictfunc(selection):
    founddonordonations = donors_dictionary.get(selection) # getting key from dictionary
    try:
        cleaneddonations = " ".join(founddonordonations) # join to clean up the list output
    except TypeError:
        pass
    exactselection(selection) # prints out exact selection from database
    selection = selection.replace(" ", "") # more cleaning up options
    thankyounotefunc(selection) # provides selection as input for thank you note
    thankyoufunc() # sends user back to the thank you note sub-menu
    return

# function to add not found donor to the dictionary
def donornotindictfunc(selection):
    print(f"\nDonor Name \'{selection}\' Not Found -- Adding to List of Donors")
    donors_dictionary[selection] = selection # adding not found donor to the dictionary as a key
    donation = float(input('\nEnter donation amount: ')) #prompting user for donation
    donors_dictionary[selection] = [donation] # adding new value/donation as a list to dictionary
    thankyoufunc()
    return

# Function to list donor in dictionary or to add new donor to dictionary
def fullnamefunc():
    selection = input('Enter Your Selection: ') # prompt user for selection
    if selection == 'list': #options for list selection
        listdonorsfunc()
    elif len(selection) == 0: # returns to main menu if input is blank
        mainmenufunc()
    elif selection in donors_dictionary.keys(): # calls function if the donor is in the dictionary
        donorindictfunc(selection)
    elif selection not in donors_dictionary.keys(): # calls function if the donor is NOT in the dictionary
        donornotindictfunc(selection)
    else: # return to main menu
        mainmenufunc()
    return

# Funtion to provide Thank you note options
def thankyoufunc():
    global selection
    #print('You selected \"Send a Thank You\"')
    print ("""
    ****** Thank You Note Options ***************
    1. Type 'List' to see a full list of donors
    2. Type in a donor's full name
    3. Press Enter Key to return to the Main Menu
    *********************************************
    """)
    fullnamefunc()
    return

# Function to Generate Thank you note printed to screen
def thankyounotefunc(selection):
    print (f"""
    To: {selection}@email.com
    From: mailer-auto@donations.com
    Subject: Recent Donation

    Dear {selection},

    Thank you for your generous donation.

    Sincerely,

    The Donation Collection Staff

    ***********************************
    """)
    time.sleep(5)
    return

# Function to exit the program
def exitfunc():
    print('Exiting Program!')
    time.sleep(1)
    sys.exit()
    return

# Restart or Exit Program Function
def executeAgainfunc():
    while True:
        RunAgain = input('Would you like to execute this script again? (Y/N): ').lower()
        if not (RunAgain in ('yes', 'y')):
            exitfunc()
        if (RunAgain in ('yes', 'y')):
            mainmenufunc()
    return

def reportfunc():
    # assigns variables for easy formatting
    left_aligned = "Donor Name"
    center = "Total Given"
    mid_right_aligned = "Num Gifts"
    right_aligned = "Average Gift"

    # formatting and printing report header
    print(f"{left_aligned:<15} | {center:^10} | {mid_right_aligned:>10} | {right_aligned:>13}")
    print('-'*60)
    for selection, value in donors_dictionary.items():
        totaldonationsgiven = len(value) # gives the total number of donations in dictionary associated with donor
        donationtotal = sum(value) # gives total sum of all donations
        donationtotal = float(donationtotal) # turns sun into a float
        avgdonation =  round(donationtotal / totaldonationsgiven, 2) # round answer to the second decimal place
        avgdonation = (f"{avgdonation:.2f}") # format string to print 2 decimal places
        donationtotal = (f"{donationtotal:.2f}") # format string to print 2 decimal places
        print(f"{selection:<15}{donationtotal:^24}{totaldonationsgiven:>3}{avgdonation:>18}") # format string for report
        time.sleep(0.5) # slow down terminal printing for user
    mainmenufunc() # back to main menu
    return

# main menu function
def mainmenufunc():
    print ("""
    ***** Main Menu **********
    1. Generate Thank You Note
    2. Create a Report
    3. Restart Program
    4. Exit Program
    **************************
    """)
    answer = input('Enter A Number: ')
    print()
    print(f"You selected: {answer}")
    print()
    while True:
        if answer == '1':
            thankyoufunc() # takes user to thank you list
            break
        elif answer == '2':
            reportfunc() # generates a report for the user
            break
        elif answer == '3':
            executeAgainfunc() # gives the option to restart the program
            break
        elif answer == '4':
            exitfunc() # exits the program cleanly
            break
        else:
            mainmenufunc() # catch all for all invalid entries

if __name__ == "__main__":
    mainmenufunc()
