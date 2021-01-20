#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# CLI and Main program
# Created 1/17/2021 - csimmons


import pytest
import sys, os
from operator import itemgetter
from io import StringIO
from donor_models import *
from data import *

dc = DonorCollection()

def change_donor_info():
    name = input(text_dict.get('donor_prompt'))
    name = name.lower()
    if name == 'list':
        list_donors()
    elif name == 'exit': 
        return
    elif dc.find_donor(name) == True:
        updated_donor(name.title())
    else:
        add_new_donor(name.title())

def add_new_donor(name):
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    dc.edit_donor(donor = name, donations = gift)
    print(text_dict.get('letter').format(name, gift))

def updated_donor(name):
    name = name.title()
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    dc.edit_donor(donor = name, donations = gift)
    print(text_dict.get('letter').format(name, gift))
    
def list_donors():
    print('\nMaster List of Donors:\n')
    for donor in dc.donor_list:
        print(donor)
    print('\n')

def run_donor_report():
    dc.create_report()
    print(text_dict.get('header1'))
    print(text_dict.get('header2'))
    for name, total, gifts, avg in dc.all_info: 
        print(text_dict.get('info_row')(dname=name, total=total, gifts=gifts, avg=avg))
    print('\n')

def create_dir():
    isdir = os.path.isdir('letters')  
    if isdir == True:
        pass
    else:
        os.mkdir('letters')

def write_files(filename, donor, gift):
    with open(filename, 'w') as output:
        output.write(text_dict.get('letter').format(str(donor.replace('_', ' ')), gift))
    output.close

# Need to edit
def batch_thanks():
    create_dir()
    for key, value in dc.donors_db.items():
        donor = str(key.replace(' ', '_'))
        gift = (list(value))[-1]
        filename = 'letters/' + donor + '.txt'
        try:
            write_files(filename, donor, gift)
        except IOError:
            print(text_dict.get(letter_err.format(donor)))
        write_files(filename, donor, gift)
    print('\nThank You letters were generated for all donors\n')

def exit_program():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

menu_dict = {
            '1' : change_donor_info,
            '2' : change_donor_info,
            '3' : list_donors,
            '4' : run_donor_report,
            '5' : batch_thanks,
            '6' : exit_program
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