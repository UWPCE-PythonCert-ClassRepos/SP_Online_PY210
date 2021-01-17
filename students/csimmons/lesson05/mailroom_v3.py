#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons
# Edited 12/3/2020 - v1.1 - csimmons
# Edited 12/10/2020 - v1.2 - csimmons
# edited 12/11 - 12/13 2020 - v2.0 -csimmons
# edited 12/30 - 12/31/2020 - v3.0 -csimmons

import os, sys
import pathlib
from operator import itemgetter

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

menu_prompt = '\n'.join(('\nPlease choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Send thank you letters to all donors',
          '4 - Quit',
          '\n>>> '))

thanks_prompt = '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '>>>  '))

gift_prompt = '\n'.join(('Please enter the donation amount: ',
                '>>>  '))

donation_err = '\nError: Please enter a number or decimal ("$" and commas not needed).'

letter_err = '\nError: The letter for {} not generated. Please check the destination folder'

letter = (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands, perhaps\n'
        'even millions, enjoy the wonders of the Emerald city!\n\n'
        'Sincerely,\n\n'
        'H.P. Lovecraft \n'))

def print_donors(donors):
    print('\nMaster List of Donors:\n')
    for donor in donors:
        print(donor)
    print('\n')

def exist_donor(response, donors):
    response = response.title()
    while True:
        gift = input(gift_prompt)
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(donation_err)
    for donor in donors:
        if response == donor:
            donorlist_dict.setdefault(donor, []).append(gift)
    print(letter.format(response, gift))

def new_donor(response):    
    response = response.title()
    print(('\n{} is a new donor!\n').format(response))
    while True:
        gift = input(gift_prompt)
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(donation_err)
    donorlist_dict[response] = [gift]
    print(letter.format(response, gift))

def print_donorlist(all_info):
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 32) +'\n'
    info_row = '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format
    print(header1)
    print(header2)
    for name, total, gifts, avg in all_info: 
        print(info_row(dname=name, total=total, gifts=gifts, avg=avg))
    print('\n')
  
def send_thankyou():
    donors = donorlist_dict.keys()
    response = input(thanks_prompt)
    if response.lower() == 'list':
        print_donors(donors)
    elif response.lower() == 'exit': 
        return
    elif response.title() in donors:
        exist_donor(response, donors)
    else:
        new_donor(response)

def generate_letters():
    isdir = os.path.isdir('letters')  
    if isdir == True:
        pass
    else:
        os.mkdir('letters')
    for key, value in donorlist_dict.items():
        donor = str(key.replace(' ', '_'))
        gift = (list(value))[-1]
        filename = 'letters/' + donor + '.txt'
        try:
            with open(filename, 'w') as output:
                output.write(letter.format(donor, gift))
            output.close
        except IOError:
            print(letter_err.format(donor))
    print('\nThank You letters were generated for all donors\n')

def display_report():
    all_info = []
    for key, value in donorlist_dict.items():
        donor_info = []
        donor_info.append(key)
        donor_info.append(sum(value))
        donor_info.append(len(value))
        donor_info.append(sum(value)/len(value))
        all_info.append(donor_info)
    all_info = sorted(all_info, key=itemgetter (1), reverse=True)
    print_donorlist(all_info) 

def program_exit():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

menu_prompt = '\n'.join(('Please choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Send thank you letters to all donors',
          '4 - Quit',
          '>>> '))

menu_dict = {
            '1' : send_thankyou,
            '2' : display_report,
            '3' : generate_letters,
            '4' : program_exit
            }

def menu_select(menu_prompt, menu_dict):
    selection = ['1', '2', '3', '4']
    while True:
        response = input(menu_prompt)
        try:
            if response not in selection:
                print('\nNot a valid selection. Please try again!')
            elif menu_dict[response]() == 'exit menu':
                break
        except KeyError:
            print('\nNot a valid selection. Please try again!')

if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!\n')
    menu_select(menu_prompt, menu_dict)