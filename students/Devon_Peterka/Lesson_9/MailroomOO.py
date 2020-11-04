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
    pass

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
    first = input('Donor First Name: ')
    last = input('Donor Last Name: ')
    if 'Donor(first, last)' in donors:
        different_person = False if input(f'Has {first} {last} donated before? (y/n): ').lower() == 'y' else True
    amount = input('Donation Amount: ')
    donors.new(first, last, amount)

def donor_list():
    os.system('clear')
    print('Current Donors:')
    for i in range(len(donors.list)):
        print('\t' + donors.list[i].full_name)
    print()
    
# Initial donor data for script
donors = DonorCollection([Donor('Bill', 'Turner', [1500.99, 3500, 800.25]), Donor('Jack', 'Yelb', [145.72, 1350.25]), Donor('Kelly', 'Jones', [250.00, 57.00]), Donor('Mark', 'Tomles', [600.00]), Donor('Guido', 'Roccio', [1153.90, 47.15]), Donor('Mary', 'Jaco', [27500.00])])

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
