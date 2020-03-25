#!/usr/bin/env python3

# Stella Kim
# Assignment 1: Mailroom Part 1

"""
This program lists donors and their donation amounts.  A user is able to 
choose from a menu of 3 actions: send a thank you, create a report or quit.
"""

import sys

# Lists donors and their contributions
donor_db = [('John Smith', [10000, 5000, 1000]),
            ('Mary Johnson', [50000]),
            ('David Carlton', [2500, 500]),
            ('James Wright', [500, 500, 500]),
            ('Caroline Baker', [1000])
            ]

# Displays options to user
prompt = '\n'.join(('Welcome to the mail room.',
          'Please choose from below options:',
          '1 - Send a Thank You',
          '2 - Create a Report',
          '3 - Quit',
          '>>> '))

def send_thank_you():
    user_response = input('Please enter your full name: ')
    if user_response == 'list':
        view_donors()
    #elif user_response == :


#def create_report():

def view_donors():
    print(donor_db)

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