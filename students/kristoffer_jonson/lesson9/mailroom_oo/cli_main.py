#!/usr/bin/env python3
'''
cli main.py
Module handles user interaction functions and main program flow.
'''

from donor_models import DonorCollections
from donor_models import Donor
import sys
import math

#Initialize default donor database.
donorcollection = DonorCollections()
donorcollection.add_donor("William", [653772.32, 12.17])
donorcollection.add_donor("Jeff", [877.33])
donorcollection.add_donor("Paul", [663.23, 43.87, 1.32])
donorcollection.add_donor("Mark", [1663.23, 4300.87, 10432.0])
donorcollection.add_donor("Elon", [234.25, 2764.87, 9783.0])

def main(donorcollection):
    """
    Prompts user for navigation of donor database
    :param donor_db: Database of donations and donors
    """
    response = ''

    switch_func_dict = {
        '1':thank_you,
        '2':create_report,
        '3':all_thank_you,
        '4':exit_program
    }

    while True:
        response = initial_prompt()
        try:
            switch_func_dict.get(response,"nothing")(donorcollection)
        except TypeError:
            print('Invalid selection, try again.')

def initial_prompt():
    prompt = "\n".join(("","Welcome to the Donor Database",
              "Please choose from below options (i.e. 2):",
              "1 - Send a Thank You",
              "2 - Create a Report",
              "3 - Send letters to all donors",
              "4 - Quit",
              ">>> "))
    response = input(prompt)
    return response

def thank_you(donorcollection):
    """
    Add donor if not in database and/or add donation
    :param donorcollection donor collection object of donors and donations
    """
    prompt = "\n".join(("Enter full name of donor",
                        "(Type list to diplay current donors):"))
    response = input(prompt)
    if response.lower() == 'list':
        donor_list = donorcollection.list_donors()
        print(donor_list)
    elif response in donorcollection.list_donors():
        donor = response
        donation = enter_donation()
        donorcollection.add_donation(donor, donation)
        card_text = donorcollection.create_card(donor,donation)
        print(card_text)
    else:
        confirm_add = input(response + ' not in database.  Type yes to add.')
        if confirm_add.lower() == 'yes':
            donor = response
            donation = enter_donation()
            donorcollection.add_donor(donor, [donation])
            card_text = donorcollection.create_card(donor,donation)
            print(card_text)
        else:
            print(response + ' not added to database.')
    return True

def enter_donation():
    '''
    Ensure donation can be converted to a number
    '''
    try:
        donation = float(request_donation())
        math.sqrt(donation)
    except ValueError:
        print('\n\nDonation entry not valid. Zero logged.'+'\n')
        donation=0
    return donation

def request_donation():
    '''
    Request donation amount from user
    '''
    prompt = "\n".join(("Enter amount of donation",
                "(No leading $ required):"))
    donation_in = input(prompt)
    return donation_in


def create_report(donorcollection):
    """
    Print formatted report of donors and amounts donated
    :param donorcollect donor collection object of donors and donations
    """
    report_text = donorcollection.create_report()
    print(report_text)
    return report_text


def all_thank_you(donorcollection):
    '''
    Print thank you cards to disk in cards folder.
    :param donorcollect donor collection object of donors and donations
    '''
    for donor in donorcollection.donor_list:
        letter_text = donorcollection.create_card(donor.donor,donor.donations[-1])
        with open('./cards/' + donor.donor + '.txt', 'w+') as f:
            f.write(letter_text)

def exit_program(donors):
    sys.exit()

if __name__ == '__main__':
    main(donorcollection)
