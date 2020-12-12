#!/usr/bin/env python3

from DonorCollection import DonorCollection
from Donor import Donor
import os
import sys

def menu_select(prompt, menu_dict):
    '''
    Provides the menu prompts for the user to select.  Allows flexible
    prompts and actions
    '''
    while True:
        response = clean_inp(prompt, menu_dict)
        if type(response) is str:
            if response == 'invalid':
                print('\nInvalid Input.  Try Again.')
            else:
                break
        else:
            response = response()
        if response == 'back':
            os.system('clear')
            break

def clean_inp(prompt, menu_dict):
    '''
    Grants greater flexibility in user input.  Function reads user input
    then compares it against a list of acceptable inputs for each
    function response, then returns the exact response the calling
    function is looking for.
    '''
    usr_input = str(input(prompt))
    for key, value in menu_dict.items():
        if usr_input.lower() in value:
            return key
    os.system('clear')
    return 'invalid'

def send_thanks():
    '''
    Provides a sub-menu with option to add a donation and draft thank
    you letters to individual/all donors.
    
    added terminal 'clear' to beginning and end to make things cleaner
    '''
    os.system('clear')
    menu_select(send_prompt, send_dict)
    os.system('clear')

def view_report():
    print(DonorCollection.report(donors.list_by_donation))

def exit_program():
    '''
    This function clears the terminal screen, then prints a message
    before exiting the script.  User is left with the program header
    and exit message in the terminal upon exit.
    '''
    os.system('clear')
    print('\nMailroom exited successfully.\n')
    sys.exit()

def write_thanks():
    '''
    Asks user for a Donor's name and donation amount.  Any of the
    "back_out" keywords at any of these inputs will back out to main
    menu.
    
    The donation amount must be a string that is capable of being turned
    to a float type number.  If not, the input is rejected and user is
    re-prompted.
    
    The existing DonorCollection object is searched for a Donor object
    that matches the name of the inputs.  If one is found, user is asked
    to confirm that this donation is made by the same Donor.  If so,
    the new donation is added to the existing Donor object.  If not, a
    new Donor object with the name and amount input is created.
    
    A thank you message is drafted for the donation and printed on the
    screen.
    '''
    first = input('Donor First Name: ').title()
    if first.lower() in back_outs: return 'back'

    last = input('Donor Last Name: ').title()
    if last.lower() in back_outs: return 'back'

    while True:
        amount = input('Donation Amount: ')
        if amount in back_outs: return 'back'
        # Make amount variable a float value
        try:
            amount = float(amount)
            break
        # Throw an error message if amount cannot be made a float value
        except ValueError:
            print('\nERROR:\nDonation amount must be a number.\n')
            continue


    # Check if Donor exists in the collection already
    existing_donor = 'no'
    for i in range(len(donors.list)):
        # Check new donation donor against existing donors one-by-one
        if f'Donor({first}, {last})' == str(donors[i]):
            existing_donor = input(f'Is this the same {first} {last} who made these donations {donors[i].donations}? (y/n) : ').lower()
            if existing_donor in back_outs: return 'back'
            
            # Only accept certain inputs.  Re-try iteration if invalid
            # input received.
            if existing_donor not in ('y','n','yes','no'):
                print('\ninvalid input.  try again.\n')
                i = i-1
                continue

            # If ID'd as an existing donor, append their donation
            # history and break out of loop.
            if existing_donor in ('y', 'yes'):
                donors[i].add_donation(amount)
                break

    # Add to donor list if new donor
    if existing_donor in ('n', 'no'):
        donors.new(first, last, amount)

    # "Send" a thank you regardless of if they're new or existing donor
    print('MESSAGE WILL READ:\n\n---')
    print(Donor.send_thanks(first, last, amount))
    input('---\n\npress ENTER to continue...')
    os.system('clear')
    return 'back'

def donor_list():
    '''
    Prints a list of all the Donor objects in alphabetical order by
    donor's last name.  Leaves list on screen for user reference.
    '''
    os.system('clear')
    print('Current Donors:')
    for i in range(len(donors.list)):
        print('\t' + donors.list[i].full_name)
    print()
    
# Initial donor data for script
#donors = DonorCollection([Donor('Bill', 'Turner', [1500.99, 3500, 800.25]), Donor('Jack', 'Yelb', [145.72, 1350.25]), Donor('Kelly', 'Jones', [250.00, 57.00]), Donor('Mark', 'Tomles', [600.00]), Donor('Guido', 'Roccio', [1153.90, 47.15]), Donor('Mary', 'Jaco', [27500.00])])
donors = DonorCollection()

# List of values that will universally return to menu or quit
back_outs = ['back', 'exit', 'quit', 'q', 'end', 'clear']

# Main menu prompt
main_prompt = ('------Mailroom version 3------\n'
               '\nMAIN MENU:\n'
               '[1] Thank Donor(s)\n'
               '[2] View Donor Report\n'
               '[3] Quit\n'
               '\nYou may input "back" at any \n'
               'input to return here.\n\n'
               'What would you like to do?: '
              )

# dictionary of acceptable inputs for prompt
main_disp = {send_thanks: ['thank',
                           '1',
                           'thank donor',
                           'thank donors',
                           'thank donor(s)'
                           'thank you',
                           'thank yous',
                          ],
             view_report: ['view',
                           'donor',
                           'report',
                           '2',
                           'view report',
                           'view donor report'
                           'donor report'
                          ],
             donor_list: ['list'],
             exit_program: ['3'] + back_outs
            }

# Dispatch disctionary for 'Send Thanks' sub-menu
send_prompt = ('------Mailroom version 3.0------ \n\n'
               'SEND THANKS MENU\n'
               '[1] Record New Donation & Thank\n'
               '[2] View List of Donors\n'
               '[3] Back to Main Menu\n\n'
               'What would you like to do?: '
              )



# Dictionary of acceptable inputs for 'Send Thanks' sub-menu
send_dict = {write_thanks: ['record',
                            'new',
                            'donation',
                            'thank',
                            'record new donation',
                            'new donation',
                            'record new donation and thank',
                            'record new donation & thank',
                            '1'
                           ],
#             letters2all: ['send letter to all donors',
#                           'send letters',
#                           'send to all',
#                           'letters',
#                           'letter',
#                           'send to all',
#                           'send to all donors',
#                           'thank all donors',
#                           '2'
#                          ],
             donor_list: ['view',
                          'list',
                          'donors',
                          'view list',
                          'view list of donors',
                          '2'
                         ],
             'back': ['main',
                      'menu',
                      'main menu',
                      '3',
                     ] + back_outs
             }

if __name__ == '__main__':
    os.system('clear')
    menu_select(main_prompt, main_disp)
