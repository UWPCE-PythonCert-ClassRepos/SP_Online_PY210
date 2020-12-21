#!/usr/bin/env python3

from donor_models import Donor, DonorCollection
import donor_data

""" Mailroom Program
    The Last Laugh Program
    https://simpsons.fandom.com/wiki/Last_Laugh_Program
"""
import datetime


def prompt_for_donation(name):
    """Prompt user for donation and add to donor data."""
    while True:
        amount = input('Enter donation amount in dollars: ')
        try:
            # Value checking is handled by the Donor Class
            return Donor(name, amount)
        except ValueError:
            print('Value must be a number greater than zero.')


def send_thanks():
    """Generate a thank you note. """
    # Prompt for name to send thank you
    name = input('\nWho would you like to send a thank you to?\n(Tip: type \'list\' for possible names)\n')
    if name == 'list':
        print('Current Donors:')
        for d in donors.donor_names:
            print(d)
        # Repeat question for donor email
        send_thanks()
    elif name.lower() == 'quit':
        print('Returning to main menu.')
        return
    else:
        #Add donation by adding a donor object.  The DonorCollection checks for existing donor and if present adds the
        #donation amount, otherwise a new donor instance is added.
        donors.add_donor(prompt_for_donation(name))
        print(donors.donors[name].generate_email)


def create_report():
    print('\n'.join(donors.create_report()))


def letters_all():
    """Generage all the latest donation letter"""
    print('\nGenerating donations letters:')
    dl = donors.letters_all()
    for name, fname in dl:
        print(f'{name:20} --> {fname}')


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
            i = int(response)
            a = enumerate_actions[int(response)]
            #return int(response), enumerate_actions[int(response)]
            return i, a
        except (ValueError, KeyError) as e:
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

if __name__ == '__main__':
    #Intialize the donor data
    donors = DonorCollection.donorDict(donor_data.donors)

    # Begin the script by asking the user what they want to do
    # program will continue to loop until the user selects the Quit option
    while True:
        resp_num, resp_str = prompt_actions()
        main_actions.get(resp_str)()



