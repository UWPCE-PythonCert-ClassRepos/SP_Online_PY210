#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/16/2019
# Part 4
# mailroom.py

import os


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


def display_report():
    '''Prints report to screen'''

    print()
    for data in get_report(donors):
        print(data)


def get_report(donors):
    '''Gets a sorted list of donors, sorted by historical donation amount'''

    report = []
    report.append('{:<19}{:3}{:12}{:3}{:10}{:3}{:<10}'.format(
        'Donor Name', '|',
        'Total Given', '|',
        'Num Gifts', '|',
        'Average Gift'))
    report.append('-'*62)
    for name, data in sorted(donors.items(), key=sort_key, reverse=True):
        report.append('{:<21}${:>11,.2f}{:^16}${:>11,.2f}'.format(name, *data))
    return report


def sort_key(values):
    '''Sorts the dictionary by historical value'''

    return values[1][0]


def thank_you():
    '''Creats a thank you letter for a single donor'''

    print()
    name = get_donor_name(donors)
    donation = get_donation_amount(name)
    print(add_donation(name, donation, donors))


def get_donor_name(donors):
    '''Gets the name of the donor'''

    while True:
        response = input("Please enter the full name of the donor, 'List' for "
                         "a list of donors, or 'Quit' to exit to the menu > ")
        answer = check_donor_name(response, donors)
        if answer == response.title():
            return answer
        else:
            print(answer)


def check_donor_name(response, donors):
    '''Checks the donor is in the dict'''

    try:
        if response.lower() == 'quit':
            menu()
        elif response.lower() == 'list':
            donor_list = '\n'.join([donor for donor in sorted(donors)])
            return donor_list
        elif donors.get(response.title()):
            return response.title()
        else:
            response.split()[1]
            donors.update({response.title(): [0, 0, 0]})
            return response.title()
    except IndexError:
        return 'Please enter a full name'


def get_donation_amount(name):
    '''Gets the amount of the donation'''

    while True:
        donation = input("Please enter the amount of the donation for {} or "
                         "'Quit' to exit to the main menu > $ ".format(name))
        if donation.lower() == 'quit':
            menu()
        donation_float = check_donation_amount(donation)
        if type(donation_float) == float:
            return donation_float
        else:
            print(donation_float)


def check_donation_amount(donation):
    '''Checks the donation is a float value'''

    try:
        result = float(donation)
    except ValueError:
        result = 'Please enter a numeric value'
    return result


def add_donation(donor, donation, donors):
    '''Appends donor donation data and prints thank you letter'''

    donor_data = donors.get(donor)
    sum_donations = donor_data[0] + donation
    num_donations = donor_data[1] + 1
    avg_donation = sum_donations / num_donations
    donors.update({donor: [sum_donations, num_donations, avg_donation]})
    return get_letter_text(donor, donation)


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


def thank_all():
    '''Formats and saves a letter thanking all the donor for their donations'''

    save_thank_all(donors)
    print('\nTask Complete')


def save_thank_all(donors):
    '''Saves a letter thanking all the donor to file'''

    for donor in donors:
        first_name = donor.split()[0]
        last_name = donor.split()[1].strip(',')
        file_path = os.path.join("./{}_{}.txt".format(first_name, last_name))
        with open(file_path, 'w+') as new_file:
            new_file.write(get_letter_text(donor, donors.get(donor)[0]))


def quit():
    '''Exit the program'''

    print('\nGood Bye!\n\n')
    exit()


donors = {
    'William Gates, III': [653784.49, 2, 326892.24],
    'Mark Zuckerberg': [16396.10, 3, 5465.37],
    'Jeff Bezos': [877.33, 1, 877.33],
    'Paul Allen': [708.42, 3, 236.14],
    'Steve Jobs': [10000.00, 1, 10000.00]}

menu_dict = {
    1: display_report,
    2: thank_you,
    3: thank_all,
    4: quit, }

if __name__ == "__main__":

    menu()
