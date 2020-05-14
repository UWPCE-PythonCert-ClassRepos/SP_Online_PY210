#!/usr/bin/env python3

# Stella Kim
# Assignment 5: Mailroom Part 4

"""
This program lists donors and their donation amounts.  A user is able to choose
from a menu of 3 donation-related actions: send a thank you, create a report or
quit the program.
"""

import sys

# List donors and their contributions
donor_db = {'John Smith': [10000, 5000, 1000],
            'Mary Johnson': [50000],
            'David Carlton': [2500, 500],
            'James Wright': [500, 500, 500],
            'Caroline Baker': [1000]
            }

# Display menu options to user
prompt = '\n'.join(('\nWelcome to the mail room.',
                    'Please choose from the below options:',
                    '1 - Send a Thank You',
                    '2 - Create a report',
                    '3 - Send letters to all donors',
                    '4 - Quit',
                    '>>> '))


def invalid_option():
    print('\nThat is not a valid option.  Please choose one of the four '
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
        if search_db(user_response):
            print('\nThis donor already exists in our database.')
            donation = donation_amount()  # obtain donation amount made
            add_donation(user_response, donation)
        else:
            print('\nThis is a NEW donor and will be added to the database.')
            donation = donation_amount()  # obtain donation amount made
            add_new_donor(user_response, donation)
        print(thank_you_email(user_response, donation))


# Display list of donors
def view_donors():
    print('\nThe following is the list of donors:')
    for donor in donor_db.keys():
        print(donor)


# Search database to see if user already exists
def search_db(donor_name):
    if donor_db.get(donor_name):
        return True
    else:
        return False


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


# Add donation amount to existing donor in database
def add_donation(donor_name, donation_amount):
    donor_db[donor_name].append(donation_amount)


# Add new donor and donation amount to database
def add_new_donor(donor_name, donation_amount):
    donor_db[donor_name] = [donation_amount]


# Send donor a thank you email
def thank_you_email(donor_name, amount):
    return(f'\nThank you {donor_name} for your generous donation amount of $'
           f'{amount:.2f}!')


def display_report():
    print('\n{:<20} | {:<12} | {:<10} | {:<15}'.format('Donor Name', 'Total '
          'Given', 'Num Gifts', 'Average Gift'))
    print('=' * 65)
    # Create list out of database to iterate through
    donor_list = list(donor_db.items())
    print('\n'.join(create_report(donor_list)))  # displays donor report


# Create report for user to see list of all donors and donations made
def create_report(donor_list):
    # Sort database by sum amounts in descending order
    donor_stat = []
    sorted_db = sorted(donor_list, key=sum_total, reverse=True)
    for item in sorted_db:
        total = sum(item[1])  # sum of all donations
        count = len(item[1])  # total number of donations
        average = total/count  # average of all donations
        donor_stat.append((f'{item[0]:<20} | {total:<12.2f} | {count:<10} |'
                           f' {average:<15.2f}'))
    return donor_stat


# Sum donation amounts for each donor record and return amounts for sorted
# database
def sum_total(donor_record):
    return(sum(donor_record[1]))


# Loop through donor database to retrieve name and donations made
def letter_list_looper():
    for record in list(donor_db.items()):
        create_file(record)  # generate letter to donor
    print('All donation letters have been created.')


def create_file(record):
    file_name = f'{record[0]}.txt'  # create file name using name of donor
    with open(file_name, 'w') as new_file:  # create a new file
        new_file.write(compose_letter(record))  # write letter to the text file
    return file_name


# Generate letter for each donor and donations made
def compose_letter(record):
    donor_letter = f'Dear {record[0]},\n\nThank you for your ' + \
                   f'{len(record[1])} donations that total $' + \
                   f'{sum(record[1]):.2f}.\nIt will be put to very ' + \
                   f'good use.\n\n\tSincerely,\n\t-The Team'
    return donor_letter


# Exit the program
def exit_program():
    print('\nThank you for visiting!')
    sys.exit()


# Main menu options for user to choose for mail program
def main():
    switch_dict = {
        1: send_thank_you,
        2: display_report,
        3: letter_list_looper,
        4: exit_program
    }
    while True:
        try:
            response = int(input(prompt))
            switch_dict.get(response, invalid_option)()
        except ValueError:
            print('Input is invalid, please enter a number from the menu.')


if __name__ == "__main__":
    main()
