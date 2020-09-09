#!/usr/bin/env python """
import sys
from datetime import date
today = date.today()

"""Mailroom Part 2"""

# Prompt user to choose from menu of 3 actions:
# Send a Thank You, Create a Report, Send thanks to all donors or quit.

donor_db = {"Cher": [1000.00, 245.00],
            "Drew Barrymore": [25000.00],
            "Charlie Brown": [25.00, 50.01, 100.00],
            "Jack Black": [256.00, 752.50, 10101.00],
            "Sam Smith": [5500.00, 24.00],
            }


def sort_key(donors):
    #  sort by total donations
    return sum(donors[1])


def list_donors(donors):
    print(f'\nNumber of Donors found: {len(donors)}\n\n')
    for donor, donations in donors.items():
        print(f'\t{donor}')

    print('\n')
    return (donors)


def add_donation(donors, donator):
    """      Add donation to donor
    """
    prompt = "Please enter an amount to donate >"
    donation = input(prompt)
    donation = float(donation)
    donors[donator] = donors[donator] + [donation]

    return donation


def create_card(donator, amount):
    """
    Create thank you note for passed user
    """

    donation_dict = {}
    donation_dict['name'] = donator
    donation_dict['donation'] = float(amount)

    ty_text = 'Dear {name},\
    \n\n\tThank you for your very kind donation of ${donation:.2f}.\
    \n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\
    \n\t\t\t   -The Team'.format(**donation_dict)

    fn = '_' + today.strftime("%b_%d_%Y") + '.txt'

    with open('./cards/' + donation_dict['name'] + fn, 'w+') as f:
        f.write(ty_text)

    print("Thank you card written!")
    return True


def send_ty(donors):
    ''' Send thank you to selected donor '''

    donation = []

    prompt = "\n".join(("Enter Full name of donor",
                        "  or Enter list to show current donors:",
                        "  Please enter donor name:"
                        " > "))
    response = input(prompt)
    response = response.title()

    if response.lower() == 'list':
        list_donors(donors)
    elif response in donors:
        donation = add_donation(donors, response)
        create_card(response, donation)
    else:
        donors[response] = []
        donation = add_donation(donors, response)
        create_card(response, donation)

    return donors


def create_report(donors):
    """
    Print formatted report of donors and donations
    Sort report by total donations
    """

    print("** You've selected to create a report.  **\n")
    col1 = 'Donor Name'
    col2 = 'Total Given'
    col3 = 'Num Gifts'
    col4 = 'Average Gift'
    print(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    print('-'*70)

    donors = dict(sorted(donors.items(), key=sort_key, reverse=True))
    for donor, donations in donors.items():
        count = len(donations)
        total = sum(donations)
        avg = total/count
        print(f'{donor:25}  ${total:13.2f}   {count:11}  ${avg:12.2f}')
    return


def send_all_ty(donors):
    '''
    Create cards for all donor in dictionary
    '''

    for donor, donations in donors.items():
        donation_current = donations[-1]
        create_card(donor, donation_current)
    return donors


def exit_program(donors):
    print('Thank you')
    sys.exit()


def get_selection():

    prompt = "\n".join(("**  Please Select Valid Option Listed:  **",
                        "       1: Send a Thank You",
                        "       2: Create a Report",
                        "       3: Thanks to All Donors",
                        "       4: Quit",
                        "       Please enter your choice:"
                        " > "))

    response = input(prompt)
    return response


if __name__ == '__main__':

    response = ''

    switch_func_dict = {
        '1': send_ty,
        '2': create_report,
        '3': send_all_ty,
        '4': exit_program
    }

    while True:
        response = get_selection()
        switch_func_dict.get(response, "nothing")(donor_db)
