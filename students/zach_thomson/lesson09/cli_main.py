#!/usr/bin/env python3

from donor_models import *
import sys


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))


#Initialize donor database
eddie = Donor('Eddie Vedder',[10000.00, 20000.00, 4500.00])
chris = Donor('Chris Cornell', [100.00, 500.00])
kurt = Donor('Kurt Cobain', [25.00])
daveM = Donor('Dave Matthews', [100000.00, 50000.00, 125000.00])
daveG = Donor('Dave Grohl', [50.00])

donor_db = DonorCollection(eddie, chris, kurt, daveM, daveG)


#send a thank you tasks
def initial_input():
    '''Prompt user to query a name or ask for a list of the donors'''
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    return ty_prompt


def add_donor_prompt(name):
    add_prompt = input('Do you want to add {} to the donor list? (Yes/No)'.format(name))
    if add_prompt.lower() == 'yes':
        return True
    elif add_prompt.lower() == 'no':
        return False
    else:
        return add_donor_prompt(name)


def donation_prompt():
    '''Prompt user to enter a donation amount'''
    donation = input('Please enter a donation amount: ')
    try:
        donation = float(donation)
    except ValueError:
        print('Please enter an integer for the donation amount.')
    else:
        try:
            assert donation > 0
        except AssertionError:
            print('Donation should be greater than zero!')
        else:
            return donation


def thank_you():
    thank_you_logic(initial_input())


def donor_list():
    print(donor_db.donors.keys())


def thank_you_logic(name):
    if name.lower() == 'list':
        donor_list()
    else:
        if name not in donor_db.donors.keys():
            add = add_donor_prompt(name)
            if add == True:
                donation_amt = donation_prompt()
                donor_db.new_donation(name, donation_amt)
            else:
                print('Donor not added!')
        else:
            donation_amt = donation_prompt()
            donor_db.new_donation(name, donation_amt)


#Create a report tasks
def create_report():
    '''formats get_report into the create_report format'''
    header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}")
    print(table_header)
    table = donor_db.get_report()
    for entry in table:
        print(line_format.format(*entry))


#make a function to exit the program
def exit_program():
    print('Have a nice day!')
    sys.exit() # exit the interactive script


switch_dict = {1: thank_you,
               2: create_report,
               3: exit_program,
               }


def main():
    while True:
        response = input(prompt)
        try:
            response = int(response)
        except ValueError:
            print('Please input a valid response')
        else:
            try:
                switch_dict.get(int(response))()
            except TypeError:
                print('Please input a valid response')


if __name__ == "__main__":
    main()
