#!/usr/bin/env python3

import sys


donor_db = {'Eddie Vedder': [10000.00, 20000.00, 4500.00],
            'Chris Cornell': [100.00, 500.00],
            'Kurt Cobain': [25.00],
            'Dave Matthews': [100000.00, 50000.00, 125000.00],
            'Dave Grohl': [50.00]}

#print(donor_db.keys())
#print(donor_db.values())


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

#send a thank you tasks
def donor_in_list(x):
    result = False
    if x in donor_db.keys():
        result = True
    return result

donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"

def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    while ty_prompt.lower() == 'list':
        print(donor_db.keys())
        ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    else:
        if donor_in_list(ty_prompt) == True:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[ty_prompt].append(donation_amount)
        else:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[ty_prompt] = [donation_amount]
    print(donation_email.format(ty_prompt, donation_amount))

thank_you()
