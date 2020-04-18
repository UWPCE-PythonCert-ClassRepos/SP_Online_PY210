#!/usr/bin/env python3

import sys
from datetime import date
today = date.today()

donor_db = {"William": [653772.32, 12.17],
            "Jeff": [877.33],
            "Paul": [663.23, 43.87, 1.32],
            "Mark": [1663.23, 4300.87, 10432.0],
            "Elon": [234.25, 2764.87, 9783.0],
            }
response = ''

def main(donor_db):
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
        switch_func_dict.get(response,"nothing")(donor_db)


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

def thank_you(donors):
    """
    Enter donor data
    :param donor_db: Database of donations and donors
    """

    prompt = "\n".join(("Enter full name of donor",
                        "(Type list to diplay current donors):"))
    response = input(prompt)
    donation = []

    if response.lower() == 'list':
        donor_list()
    elif response in donors:
        donation = enter_donation(donors, response)
        create_card(response,donation)
    else:
        donors[response] = []
        donation = enter_donation(donors, response)
        create_card(response,donation)

    return donors

def donor_list(donors):
    for donor,donations in donors.items():
        print(key)
    return (donors)

def enter_donation(donors, donator):
    """
    Add donation data to donor
    :param donor: Name of donator
    :param donor: Amount of donation
    """
    prompt = "\n".join(("Enter amount of donation",
                        "(No leading $ required):"))
    donation = input(prompt)
    donation = float(donation)
    donors[donator] = donors[donator] + [donation]

    return donation

def create_card(donator, amount):
    """
    Create thank you card text
    :param donor: Name of donator
    :param donor: Amount of donation
    """

    donation_dict = {}
    donation_dict['name'] = donator
    donation_dict['donation'] = float(amount)

    card_text = 'Dear {name}: \n\n\tThank you for your generosity of your recent gift of ${donation:.2f}.  It will go long way in supporting this charity. \n\n\t\tSincerely,\
    \n\n\n\n\t\tKristoffer Jonson'.format(**donation_dict)

    with open('./cards/' + donation_dict['name'] + '_' +  today.strftime("%b_%d_%Y") + '.txt', 'w+') as f:
        f.write(card_text)

    print(card_text)
    return True

def create_report(donors):
    """
    Print formatted report of donors and amounts donated
    :param donor_db: Database of donations and donors
    """
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    format_string = '{:<26} $ {:>11.2f}{:>12d} $ {:>11.2f}'
    donors = dict(sorted(donors.items(),key=sort_key,reverse=True))
    for donor, donations in donors.items():
        print(format_string.format(donor,sum(donations),len(donations),sum(donations)/len(donations)))

def all_thank_you(donors):
    for donor, donations in donors.items():
        donation_current = donations[-1]
        create_card(donor,donation_current)
    return donors

def sort_key(donors):
    return sum(donors[1])

def exit_program(donors):
    sys.exit()

if __name__ == '__main__':
    main(donor_db)
