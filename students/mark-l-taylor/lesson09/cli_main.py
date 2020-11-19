#!/usr/bin/env python3

from donor_models import Donor, DonorCollection

""" Mailroom Program Part 1
    The Last Laugh Program
    https://simpsons.fandom.com/wiki/Last_Laugh_Program
"""
import datetime


def prompt_for_donation(name):
    """Prompt user for donation and add to donor data."""
    while True:
        amount = input('Enter donation amount in dollars: ')
        try:
            # convert the amount to a float
            return float(amount)
        except ValueError:
            print('Value must be a number!')


def send_thanks():
    """Generate a thank you note. """
    # Prompt for name to send thank you
    name = input('\nWho would you like to send a thank you to?\n(Tip: type \'list\' for possible names)\n')
    if name == 'list':
        print('Current Donors:')
        for d in get_donor_names():
            print(d)
        # Repeat question for donor email
        send_thanks()
    elif name.lower() == 'quit':
        print('Returning to main menu.')
        return
    else:
        amount = prompt_for_donation(name)
        add_donation(name, amount)
        print(generate_email(name, amount))


def add_don():
    if name not in get_donor_names():
        print('\n{} is a new donor! Adding to donor database.'.format(name))
        # Add new donor with empty donation
        donors[name] = []

def quit_program():
    """Quit the program"""
    print('Exiting Script.')
    exit()


def prompt_actions():
    """ Prompt user for action they would like to perform"""

    print('\nWhat would you like to do?')

    # Simplify the input to prompt for a numbered response
    # Create a dictionary from an enumerated list
    enumerate_actions = dict(enumerate(main_actions.keys(), start=1))
    for i, act in enumerate_actions.items():
        print(f'\t({i}) {act}')

    # Get user action
    response = input('Please select an action: ')
    while True:
        try:
            return int(response), enumerate_actions[int(response)]
        except ValueError:
            response = input(f'Select a number between 1 and {len(main_actions)}: ')


#
# Main Action (Dictionary Switch
#
main_actions = {'Send thank you to single donor': send_thanks,
                'Create report': create_report,
                'Send letters to all donors': letters_all,
                'Quit': quit_program,
                }

#
# Data Set
#
donors = {'Homer Simpson': [25.15],
          'Charles Burns': [0.01, 0.05],
          'Kent Brockman': [105.75, 225.76, 387.90],
          'Ned Flanders': [1054.85, 2345.00, 876.50],
          'Barney Gumble': [15.25, 35.75, 12.99],
          }

if __name__ == '__main__':
    # Begin the script by asking the user what they want to do
    # program will continue to loop until the user selects the Quit option
    while True:
        resp_num, resp_str = prompt_actions()
        main_actions.get(resp_str)()



