#!/usr/bin/env python3

# Stella Kim
# Assignment 1: Mailroom Part 1

"""
This program lists donors and their donation amounts.  A user is able to 
choose from a menu of 3 donation-related actions: send a thank you, create 
a report or quit the program.
"""

import sys

# Lists donors and their contributions
donor_db = [['John Smith', [10000, 5000, 1000]],
            ['Mary Johnson', [50000]],
            ['David Carlton', [2500, 500]],
            ['James Wright', [500, 500, 500]],
            ['Caroline Baker', [1000]]
            ]

# Displays menu options to user
prompt = '\n'.join(('\nWelcome to the mail room.',
          'Please choose from below options:',
          '1 - Send a Thank You',
          '2 - Create a Report',
          '3 - Quit',
          '>>> '))

def send_thank_you():
    # Prompts user to choose a thank you note option
    user_response = input('\nPlease enter your full name or type "list" to view the list of donors: ')
    if user_response == 'list':
        view_donors()
        send_thank_you()
    else:
        donor = search_db(user_response)  # calls function to search for already existing donor
        if donor:
            print('\nThis donor already exists in our database.')
            donation = donation_amount()  # calls function to obtain donation amount made
            donor[1].append(donation)  # adds donation amount to existing donor in database
            thank_you_email(donor[0], donation)
        else:
            print('\nThis is a NEW donor and will be added to the database.')
            donation = donation_amount()  # calls function to obtain donation amount made
            new_donor = [user_response, [donation]]
            donor_db.append(new_donor)  # adds new donor to database
            thank_you_email(new_donor[0], donation)

# Displays list of donors
def view_donors():
    print('\nThe following is the list of donors:')
    for donor in donor_db:
        print(donor[0])

# Searches database to see if user already exists
def search_db(donor_name):
    for record in donor_db:
        if record[0] == donor_name:
            return record
    return None

# Prompts user to enter a donation amount
def donation_amount():
    user_donation = input('Please enter the amount you would like to donate: $')
    return float(user_donation)

# Sends donor a thank you email
def thank_you_email(donor_name, amount):
    print(f'\nThank you {donor_name} for your generous donation amount of ${amount:.2f}.  We hope to see you again soon.')

# Creates a report for user to see list of all donors and donations made
def create_report():
    print('\n{:<20} | {:<12} | {:<10} | {:<15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('=' * 65)
    sorted_db = sorted(donor_db, key = sum_total, reverse = True)  # sorts database by sum amounts in descending order
    for item in sorted_db:
        total = sum(item[1])  # sum of all donations
        count = len(item[1])  # total number of donations
        average = total/count  # average of all donations
        print(f'{item[0]:<20} | {total:<12.2f} | {count:<10} | {average:<15.2f}')

# Sums donation amounts for each donor record and returns amounts for sorted database
def sum_total(donor_record):
    return sum(donor_record[1])

# Exits the program
def exit_program():
    print('\nThank you for visiting!')
    sys.exit()

# Main menu options for user to choose for mail program
def main():
    while True:
        response = input(prompt)
        if response == '1':
            send_thank_you()
        elif response == '2':
            create_report()
        elif response == '3':
            exit_program()
        else:
            print('\nThat is not a valid option.  Please choose one of the three options above.')

if __name__ == "__main__":
    main()