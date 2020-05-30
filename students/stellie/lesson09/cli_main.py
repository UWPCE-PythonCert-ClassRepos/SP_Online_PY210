#!/usr/bin/env python3

# Stella Kim
# Assignment 8: Object Oriented Mailroom

"""
This program lists donors and their donation amounts.  A user is able to choose
from a menu of 3 donation-related actions: send a thank you, create a report or
quit the program.
"""

import sys
from donor_models import *

# List donors and their contributions
donor_db = {'John Smith': [10000, 5000, 1000],
            'Mary Johnson': [50000],
            'David Carlton': [2500, 500],
            'James Wright': [500, 500, 500],
            'Caroline Baker': [1000]
            }

# Set variable to call DonorCollection class with DB data
data = DonorCollection(**donor_db)

# Display menu options to user
prompt = '\n'.join(('\nWelcome to the mail room.',
                    'Please choose from the below options:',
                    '1 - Send a Thank You',
                    '2 - Create a report',
                    '3 - Quit',
                    '>>> '))


def invalid_option():
    print('\nThat is not a valid option.  Please choose one of the three '
          'options above.')


def send_thank_you():
    # Prompt user to choose a thank you note option
    user_response = input('\nPlease enter your full name or type "list" to '
                          'view the list of donors.\nIf you would like to see '
                          'the main menu type "menu": ')
    if user_response == 'list':
        view_donors()
        send_thank_you()
    elif user_response == 'menu':
        return
    else:
        # Search for already existing donor
        if data.search_db(user_response.title()):
            print('\nThis donor already exists in our database.')
            donation = donation_amount()  # obtain donation amount made
            Donor(user_response.title(),
                  data.data.get(user_response.title())).add_donation(donation)
        else:
            print('\nThis is a NEW donor and will be added to the database.')
            donation = donation_amount()  # obtain donation amount made
            # Add new donor and donation to the DB
            data.add_new_donor(user_response.title(), donation)
        print(Donor(user_response.title(), donation).thank_you_email())


# Display list of donors
def view_donors():
    print('\nThe following is the list of donors:')
    for donor in data.data.keys():
        print(donor)


# Prompt user to enter a donation amount
def donation_amount():
    while True:
        prompt_amount = input('Please enter the amount you would '
                              'like to donate: $')
        try:
            user_donation = float(prompt_amount)
        except ValueError:
            print('That is an invalid amount value.')
        if user_donation <= 0:
            print('Please enter a valid amount.')
        else:
            return user_donation


# Display a report of all donors and donations made
def display_report():
    print('\n{:<20} | {:<12} | {:<10} | {:<15}'.format('Donor Name', 'Total '
          'Given', 'Num Gifts', 'Average Gift'))
    print('=' * 65)
    # Call create_report class to display donor report
    print('\n'.join(data.create_report()))


# Exit the program
def exit_program():
    print('\nThank you for visiting!')
    sys.exit()


# Main menu options for user to choose for mail program
def main():
    switch_dict = {
        1: send_thank_you,
        2: display_report,
        3: exit_program
    }
    while True:
        try:
            response = int(input(prompt))
            switch_dict.get(response, invalid_option)()
        except ValueError:
            print('Input is invalid, please enter a number from the menu.')


if __name__ == "__main__":
    main()
