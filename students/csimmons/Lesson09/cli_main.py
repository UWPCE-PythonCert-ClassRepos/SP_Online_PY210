#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom_oo.py assignment
# CLI and Main program
# Created 1/17/2021 - csimmons


import pytest
import sys
from operator import itemgetter
from donor_models import *
from data import *

dc = DonorCollection()

def add_new_donor():
    print('Craig is a new donor')
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    dc.add_donor(donor = 'Craigo', donations = gift)
    print(dc.donors_db)

def updated_donor():
    print('Update Mary')
    while True:
        gift = input(text_dict.get('gift_prompt'))
        try:
            gift = float(gift)
            break
        except ValueError as error:
            print(text_dict.get('donation_err'))
    dc.add_donor(donor = 'Mary Newcomer', donations = gift)
    print(dc.donors_db)
    #print(text_dict.get('letter').format(donor, gift))

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

def exit_program():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

menu_dict = {
            '1' : add_new_donor,
            '2' : run_donor_report,
            '3' : list_donors,
            '4' : updated_donor,
            '5' : exit_program,
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