#!/usr/bin/env python3

# Stella Kim
# Assignment 1: Mailroom Part 1

"""
This program lists donors and their donation amounts.  A user is able to 
choose from a menu of 3 actions: send a thank you, create a report or quit.
"""

import sys

# Lists donors and their contributions
donor_db = [['John Smith', [10000, 5000, 1000]],
            ['Mary Johnson', [50000]],
            ['David Carlton', [2500, 500]],
            ['James Wright', [500, 500, 500]],
            ['Caroline Baker', [1000]]
            ]

# Displays options to user
prompt = '\n'.join(('Welcome to the mail room.',
          'Please choose from below options:',
          '1 - Send a Thank You',
          '2 - Create a Report',
          '3 - Quit',
          '>>> '))

def send_thank_you():
    user_response = input('Please enter your full name or type "list" to view the list of donors: ')
    if user_response == 'list':
        view_donors()
        send_thank_you()
    else:
        donor = search_db(user_response)
        if donor:
            print('This donor already exists in our database.')
            donation = donation_amount()
            donor[1].append(donation)
            # print(donor_db)
            thank_you_email(donor[0], donation)
        else:
            print('This is a NEW donor and will be added to the database.')
            donation = donation_amount()
            new_donor = [user_response, [donation]]
            donor_db.append(new_donor)
            # print(donor_db)
            thank_you_email(new_donor[0], donation)

def view_donors():
    print('\nThe following is the list of donors:')
    for donor in donor_db:
        print(donor[0])
    print(donor_db)

def search_db(donor_name):
    for record in donor_db:
        if record[0] == donor_name:
            return record
    return None

def donation_amount():
    user_donation = input('Please enter the amount you would like to donate: $')
    return float(user_donation)

def thank_you_email(donor_name, amount):
    print(f'Thank you {donor_name} for your generous donation amount of ${amount:.2f}.  We hope to see you again soon.')
    return

#def create_report():

def exit_program():
    print('Thank you for visiting!')
    sys.exit()

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
            print('That is not a valid option.')

if __name__ == "__main__":
    main()