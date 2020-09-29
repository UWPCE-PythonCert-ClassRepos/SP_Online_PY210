#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/7/2019
# Part 3
# mailroom.py

import os


def menu():
    '''
    Prompts for a user menu selection. '''

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
        try:
            menu_dict.get(int(response))()
        except TypeError:
            print('\nPlease enter a number 1 - 4')
        except ValueError:
            print('\nPlease enter a number 1 - 4')


def sort_key(values):
    '''
    Sorts the dictionary by first value.
        Returns: sorted keys '''
    return values[1][0]


def print_report():
    '''
    Prints a sorted list of donors, sorted by historical donation amount. '''

    print('\n{:<19}{:3}{:12}{:3}{:10}{:3}{:<10}'.format('Donor Name', '|',
                                                        'Total Given', '|',
                                                        'Num Gifts', '|',
                                                        'Average Gift'))
    print('-'*62)
    for name, data in sorted(donors.items(), key=sort_key, reverse=True):
        print('{:<21}${:>11,.2f}{:^16}${:>11,.2f}'.format(name, *data))


def thank_you():
    '''
    Creats a thank you letter for a single donor. '''

    print()
    found = False
    while not found:
        response = input("Please enter the full name of the donor, 'List' for "
                         "a list of donors, or 'Quit' to exit to the menu > ")
        if response.lower() == 'quit':
            menu()
        elif response.lower() == 'list':
            print('\n'.join([donor for donor in sorted(donors)]))
        elif donors.get(response.title()):
            add_donation(response.title())
            found = True
        else:
            try:
                response.split()[1]
                donors.update({response.title(): [0, 0, 0]})
                add_donation(response.title())
                found = True
            except IndexError:
                print('Please enter a full name')


def add_donation(donor):
    '''
    Appends donor donation data and prints thank you letter.
        param arg: String: name
        output: Display - Thank You letter'''

    while True:
        donation = input("Please enter the amount of the donation for {} or "
                         "'Quit' to exit to the main menu > $ ".format(donor))
        if donation.lower() == 'quit':
            menu()
        try:
            donation = float(donation)
            break
        except ValueError:
            print('Please enter a numeric value')
    donor_data = donors.get(donor)
    sum_donations = donor_data[0] + donation
    num_donations = donor_data[1] + 1
    avg_donation = sum_donations / num_donations
    donors.update({donor: [sum_donations, num_donations, avg_donation]})
    print(format_letter(donor, donation))


def format_letter(name, donation):
    '''
    Formats an email thanking the donor for their donation.
        param arg1 : String: name(first and last)
        param arg2 : Float: donation
        return: String - Formatted thank you letter'''

    donor = {'first_name': name.split()[0],
             'last_name': name.split()[1].strip(','),
             'amount': donation}

    return('''\n
    Dear {first_name} {last_name},\n
    Thank you so much for your generous gift of ${amount:,.2f}!\n
    Your donation will go far in helping so many orphaned kittens and puppies
    find a new home.\n
    Thank You,
    Paws'''.format(**donor))


def thank_all():
    '''
    Formats and saves a letter thanking all the donor for their donations.
        output: File - Formatted thank you letters '''

    for donor in donors:
        first_name = donor.split()[0]
        last_name = donor.split()[1].strip(',')
        file_path = os.path.join("./{}_{}.txt".format(first_name, last_name))
        with open(file_path, 'w+') as new_file:
            new_file.write(format_letter(donor, donors.get(donor)[0]))
    print('\nTask Complete')


def quit():
    '''
    Exit the program '''

    print('\nGood Bye!\n\n')
    exit()


donors = {
    'William Gates, III': [653784.49, 2, 326892.24],
    'Mark Zuckerberg': [16396.10, 3, 5465.37],
    'Jeff Bezos': [877.33, 1, 877.33],
    'Paul Allen': [708.42, 3, 236.14],
    'Steve Jobs': [10000.00, 1, 10000.00]}

menu_dict = {
    1: print_report,
    2: thank_you,
    3: thank_all,
    4: quit, }

if __name__ == "__main__":

    menu()
