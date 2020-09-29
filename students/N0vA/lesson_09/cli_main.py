#!/usr/bin/env python

from donor_models import *
import sys


donors = {'Bill Gates': Donor('Bill Gates', [2000000, 250000000]), 
            'Jeff Bezos': Donor('Jeff Bezos', [2000000]),
            'Elon Musk': Donor('Elon Musk', [50000000, 10000000]), 
            'Howard Schultz': Donor('Howard Schultz', [1000000]), 
            'Paul Allen': Donor('Paul Allen',[450000000])}

database = DonorCollection(**donors)

def donation_amount(name): # User inputs donation
    
    # Enter donation amount
    while True:
        try:
            amount = int(input('How much was their donations? '))
        except ValueError:
            print('Sorry that is an invalid')
            continue
        else:
            break

    return amount

def thank_you(): # Send a thank you
    
    # Set up inputs for appending database
    name = 'list'
    while name == 'list':
        name = input("Alright.  Which donor would you like to send a thank you card?\nType 'list' to see a list of past donors >>>")   
        if name == 'list':
            print(list(donors.keys()))
    
    donation = donation_amount(name)

    # Add new donation to database
    if database._database.get(name):
        database._database.get(name).add_donation(donation)
    else:
        database.add_donor(name, donation)
    
    # Print thank you email
    print(database._database.get(name).text_thank_you())
    
def report():
    """Print a report of the existing donors"""

    database.display_report()
    
    # Exit to main menu
    exit = 'none'
    while exit != 'quit':
        exit = input('Type quit to return to the menu... ')

# Execute file when running
if __name__ == '__main__':
    
    arg_dict = {'1': thank_you,
                '2': report,
                '3': exit}

    while True:
    # Opens up the mailroom
        task = 0
        task = input("\n".join(("What do you need to do?",
              "Please choose from the options below:",
              "1 - Send Thank You Card",
              "2 - Print A Report",
              "3 - Exit",
              ">>> ")))

        # Run functions for tasks based on user's response
        while True:
            try:
                arg_dict.get(task)()
            except (ValueError, TypeError, KeyError) as e:
                task = input('Please enter a valid option from 1-3: ')
                continue
            else:
                break