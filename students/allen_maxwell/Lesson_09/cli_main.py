#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 1/20/2020
# cli_main.py


import os
from donor_models import *


def menu():
    '''Prompts for a user menu selection'''

    while True:
        response = input('\n'.join((
            '\n',
            'Please choose from the following '
            'options:',
            '1) Create a Report',
            '2) Send a Thank You letter to a donor',
            '3) Send a Thank You letter to all donors',
            '4) Quit',
            'Please enter your selection > ')))
        message = check_menu_response(response)
        if message is not None:
            print(message)


def check_menu_response(response):
    '''Checks user menu selection'''

    try:
        menu_dict.get(int(response))()
    except TypeError:
        return '\nPlease enter a number 1 - 4'
    except ValueError:
        return '\nPlease enter a number 1 - 4'


def thank_you():
    '''Creates a thank you letter for a single donor'''

    print()
    name = get_donor_name(donors)
    donation = get_donation_amount(name)
    DonorCollection.add_donation(donors, name, donation)
    print(get_letter_text(name, donation))


def get_donor_name(donors):
    '''Gets the name of the donor'''

    while True:
        response = input("Please enter the full name of the donor, 'List' for "
                         "a list of donors, or 'Quit' to exit to the menu > ")
        answer = check_donor_name(response)
        if answer == response.title():
            return answer
        else:
            print(answer)


def check_donor_name(response):
    '''Checks the donor is in the dict'''

    try:
        if response.lower() == 'quit':
            menu()
        elif response.lower() == 'list':
            return '\n'.join(sorted(DonorCollection.get_donors_names(donors)))
        else:
            response.split()[1]
            return check_new_donor(response.title())
    except IndexError:
        return 'Please enter a full name'


def check_new_donor(name):
    if donors.is_donor_present(name):
        return name
    else:
        response = input('Donor does not exist on file. Do you want to add {} '
                         'to the donor list? Y/N : '.format(name))
    if response.upper() == 'Y':
        return name
    else:
        return "Please enter another donor's name."


def get_donation_amount(name):
    '''Gets the amount of the donation'''

    while True:
        donation = input("Please enter the amount of the donation for {} or "
                         "'Quit' to exit to the main menu > $ ".format(name))
        if donation.lower() == 'quit':
            menu()
        donation_float = check_donation_amount(donation)
        if (type(donation_float) == float) and (donation_float <= 0):
            print('Please enter a positive numeric value, greater than zero')
        elif type(donation_float) == float:
            return donation_float
        else:
            print(donation_float)


def check_donation_amount(donation):
    '''Checks the donation is a numeric value'''

    try:
        result = float(donation)
    except ValueError:
        result = 'Please enter a positive numeric value'
    return result


def get_letter_text(name, donation):
    '''Formats an email thanking the donor for their donation'''

    donor = {'first_name': name.split()[0],
             'last_name': name.split()[1].strip(','),
             'amount': donation}
    letter = '''\n
        Dear {first_name} {last_name},\n
        Thank you so much for your generous gift of ${amount:,.2f}!\n
        Your donation will go far in helping so many orphaned kittens
        and puppies find a new home.\n
        Thank You,\n
        Paws'''.format(**donor)
    return letter


def display_report():
    '''Prints report to screen'''

    print()
    header = ('{:<19}{:3}{:12}{:3}{:10}{:3}{:<10}'.format(
        'Donor Name', '|',
        'Total Given', '|',
        'Num Gifts', '|',
        'Average Gift'))
    header += ('\n' + '-'*62)
    print(header)
    for donor in DonorCollection.get_report(donors):
        print('{:<21}${:>11,.2f}{:^16}${:>11,.2f}'.format(*donor))


def thank_all():
    '''Formats and saves a letter thanking all the donor for their donations'''

    save_thank_all(donors)
    print('\nTask Complete')


def save_thank_all(donors):
    '''Saves a letter thanking all the donor to file'''

    for donor in donors.donors.values():
        Donor.save_donor_file(donor, get_letter_text(donor.name,
                              donor.total_donations))


def quit():
    '''Exit the program'''

    print('\nGood Bye!\n\n')
    exit()


d1 = Donor('William Gates', [653784.49, 2])
d2 = Donor('Mark Zuckerberg', [16396.10, 3])
d3 = Donor('Jeff Bezos', [877.33, 1])
d4 = Donor('Paul Allen', [708.42, 3])
d5 = Donor('Steve Jobs', [10000.00, 1])
donors = DonorCollection(d1, d2, d3, d4, d5)


menu_dict = {
    1: display_report,
    2: thank_you,
    3: thank_all,
    4: quit, }


if __name__ == "__main__":

    menu()
