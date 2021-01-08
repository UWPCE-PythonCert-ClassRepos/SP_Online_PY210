#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons
# Edited 12/3/2020 - v1.1 - csimmons
# Edited 12/10/2020 - v1.2 - csimmons
# edited 12/11 - 12/13 2020 - v2.0 -csimmons
# edited 12/30 - 12/31/2020 - v3.0 -csimmons
# edited 1/4/2020 v4.0 - csimmons

import os, sys
import pathlib
import pytest
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

text_dict = {
    'header1': '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor    Name',  '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift '),
    'header2': ('_ ' * 32) + '\n',
    'info_row': '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format,
    'letter': (('\nDear {},\n\n'
        'We would like to thank you for your recent - and extremely\n'
        'generous - donation of ${:,.2f} to the Famous Charity of Seattle\n'
        'and Greater King County. Your gift will help thousands, perhaps\n'
        'even millions, enjoy the wonders of the Emerald city!\n\n'
        'Sincerely,\n\n'
        'H.P. Lovecraft \n')),
    'gift_prompt': '\n'.join(('Please enter the donation amount: ',
                '>>>  ')),
    'donor_prompt': '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '>>>  ')),
    'donation_err': '\nError: Please enter a number or decimal ("$" and commas not needed).',
    'letter_err': '\nError: The letter for {} not generated. Please       check the destination folder',
    'donor_prompt': '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '\n>>>  ')),
    'menu_prompt': '\n'.join(('Please choose from the options below:\n',
          '1 - Add a new donor',
          '2 - Update existing donor',
          '3 - List current donors',
          '4 - Print donor database',
          '5 - Send thank you letters to all donors',
          '6 - Quit',
          '>>> '))
    }

def create_dir():
    isdir = os.path.isdir('letters')  
    if isdir == True:
        pass
    else:
        os.mkdir('letters')

def write_files(filename, donor, gift):
    with open(filename, 'w') as output:
        output.write(text_dict.get('letter').format(donor.replace('_', ' '), gift))
    output.close

def batch_thanks():
    create_dir()
    for key, value in donorlist_dict.items():
        donor = str(key.replace(' ', '_'))
        gift = (list(value))[-1]
        filename = 'letters/' + donor + '.txt'
        try:
            write_files(filename, donor, gift)
        except IOError:
            print(text_dict.get(letter_err.format(donor)))
        write_files(filename, donor, gift)
    print('\nThank You letters were generated for all donors\n')

def find_donor():
    donor_name = input(text_dict.get('donor_prompt'))
    donor_name = donor_name.title()
    if donor_name.lower() == 'list':
        list_donors()
    elif donor_name.lower() == 'exit': 
        return
    elif donor_name.title() in donorlist_dict.keys():
        update_donor(donor_name)
    else:
        add_donor(donor_name)

def add_donor(donor_name):
    print(('\n{} is a new donor!\n').format(donor_name))
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    donorlist_dict[donor_name] = [gift]
    print(text_dict.get('letter').format(donor_name, gift))
    return (donor_name, gift)

def update_donor(donor_name):
    print(('\n{} is an existing donor!\n').format(donor_name))
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    donorlist_dict.setdefault(donor_name, []).append(gift)
    
    print(text_dict.get('letter').format(donor_name, gift))

def list_donors():
    print('\nMaster List of Donors:\n')
    for donor in donorlist_dict:
        print(donor)
    print('\n')

def create_report():
    all_info = []
    for key, value in donorlist_dict.items():
        donor_info = []
        donor_info.append(key)
        donor_info.append(sum(value))
        donor_info.append(len(value))
        donor_info.append(sum(value)/len(value))
        all_info.append(donor_info)
    all_info = sorted(all_info, key=itemgetter (1), reverse=True)
    print_data(all_info)
    return all_info 

def print_data(all_info):
    print(text_dict.get('header1'))
    print(text_dict.get('header2'))
    for name, total, gifts, avg in all_info: 
        print(text_dict.get('info_row')(dname=name, total=total, gifts=gifts, avg=avg))
    print('\n')

def program_exit():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

menu_dict = {
            '1' : find_donor,
            '2' : find_donor,
            '3' : list_donors,
            '4' : create_report,
            '5' : batch_thanks,
            '6' : program_exit
            }

def menu_select(menu_prompt, menu_dict):
    selection = ['1', '2', '3', '4', '5', '6']
    while True:
        response = input(text_dict.get('menu_prompt'))
        try:
            if response not in selection:
                print('\nNot a valid selection. Please try again!')
            elif menu_dict[response]() == 'exit menu':
                break
        except KeyError:
            print('\nNot a valid selection. Please try again!')

if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!\n')
    menu_select(text_dict.get('menu_prompt'), menu_dict)