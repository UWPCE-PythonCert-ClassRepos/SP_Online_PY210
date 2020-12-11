#!/usr/bin/env python3
# Craig Simmons
# Python 210
# mailroom.py# Created 11/23/2020 - csimmons
# Edited 12/3/2020 - v1.1 - csimmons
# Edited 12/10/2020 - v1.2 - csimmons

import sys
from operator import itemgetter

donorlist_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Rutolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

menu_prompt = '\n'.join(('Please choose from the options below:\n',
          '1 - Send a Thank You letter',
          '2 - Create a report',
          '3 - Quit',
          '>>> '))

thanks_prompt = '\n'.join(('\nPlease enter a donor name:',
                '(Enter "List" to see current donors, "Exit" to return to main menu)',
                '\n>>>  '))

gift_prompt = '\n'.join(('\nPlease enter the donation amount ("$" and commas are not needed)',
                '>>>  '))

def print_donors(donors):
    print('\nMaster List of Donors:\n')
    for donor in donors:
        print(donor)
    print('\n')

def exist_donor(response, donors):
    gift = int(input(gift_prompt))
    response = response.title()
    for donor in donors:
        if response == donor:
            donorlist_dict.setdefault(donor, []).append(gift)
    generate_thankyou(response, gift)

def new_donor(response):    
    response = response.title()
    print(('\n{} is a new donor!').format(response))
    gift = int(input(gift_prompt))
    donorlist_dict[response] = [gift]
    generate_thankyou(response, gift)

def print_donorlist(all_info):
    header1 = '{:20}{:1}{:15}{:1}{:10}{:1}{:12}'.format('\n''Donor Name ', '|', ' Total Given ', '|', ' Num Gifts ', '|', ' Average Gift ')
    header2 = ('_ ' * 32) +'\n'
    info_row = '{dname:<20s}$ {total:>13,.2f} {gifts:^10d}  $ {avg:>12,.2f}'.format
    print(header1)
    print(header2)
    for idx, info in enumerate(all_info):
        name1 = all_info[idx][0]
        total1 = all_info[idx][1]
        gifts1 = all_info[idx][2]
        avg1 = all_info[idx][3]
        print(info_row(dname=name1, total=total1, gifts=gifts1, avg=avg1))
    print('\n')

def generate_thankyou(response, gift):
    print(('\nDear {},\n\n'
        'We would like to thank you for your extremely generous donation\n'
        'of ${:,.2f} to the Anonymous Charity of Seattle.\n\n'
        'Sincerely,\n\n'
        'CA Simmons \n'.format(response, gift)))

def send_thankyou(donorlist_dict):
    donors = list(donorlist_dict.keys())
    response = input(thanks_prompt)
    if response.lower() == 'list':
        print_donors(donors)
    elif response.lower() == 'exit': 
        menu()
    elif response.title() in donors:
        exist_donor(response, donors)
    else:
        new_donor(response)

def program_exit():
    print('\nThank You. Exiting the Mailroom Application\n')
    sys.exit()

def display_report(donorlist_dict):
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

menu_options = {
                1: send_thankyou,
                2: display_report,
                3: program_exit
                }

def menu():
    response = input(menu_prompt)
    if response == '1':
        menu_options.get(1)(donorlist_dict)
    elif response == '2':
        menu_options.get(2)(donorlist_dict)
    elif response == '3':
        menu_options.get(3)()
    elif response == '4':
        menu_options.get(4)(donorlist_dict)
    else:
        print('\nSorry, your response was not a valid option')

def main():
    while True:
        menu()

if __name__ == '__main__':
    print('\nWelcome to the Mailroom Application!')
    main()