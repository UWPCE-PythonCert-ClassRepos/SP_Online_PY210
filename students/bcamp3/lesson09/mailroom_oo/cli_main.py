#!/usr/bin/env python3

"""
Mailroom Object Oriented script.

This script accepts user input to perform the following donation database tasks:
    1 - Display the donor database list or update the donation database with a new donation.
        Then display a 'Thank You' message to the donor of the new donation.
    2 - Display a donation database report
    3 - Quit out of the script
"""

from donor_models import *


def send_thank_you():
    """Process donation and send Thank You to individual donor."""
    name = input('\nEnter the full name of the donor >  ')
    if name == 'list':
        print('\nPrinting list of current donors :\n')
        for i, name in enumerate(db.donor_list, start=1):
            print(f"{i:>4d}:  {name}")
        send_thank_you()
    elif name in ['quit', 'q']:
        return None
    else:
        _name = name.upper()
        if _name in db.donors.keys():
            print(f' ---> Donor {_name} found in donor database\n')
        else:
            print(f' ++++ Adding {_name} to donor database\n')
        amt = input('Enter a donation amount > $ ')
        if amt.lower() in ['quit', 'q']:
            return None
        while True:
            try:
                db.update_donor(_name, amt)
            except ValueError:
                amt = input('\nPlease enter a valid dollar amount > $ ')
            else:
                break
        print(db.donors[_name].send_thank_you)


def create_report():
    """Create a donor database summary report."""
    #       1234567890123456789012345 $12345678901  1234567890  $123456789012
    print(' Donor Name               | Total Given | Num Gifts | Average Gift')
    print(' -----------------------------------------------------------------')
    for row in db.report:
        print(row)


def menu_selection(prompt, dispatch_dict):
    """Menu prompt."""
    while True:
        response = input(prompt)
        if response not in ['1', '2', '3', '4']:
            print("\n!!! INVALID INPUT.  PLEASE PROVIDE A VALID INPUT !!!")
        elif dispatch_dict[response]() == "exit menu":
            break


def quit_msg():
    """Quit menu."""
    print("Quitting...")
    return "exit menu"


main_prompt = ('\nChoose one of the following options:   \n'
               '   1 - Send Thank You. \n'
               '   2 - Create a Report.                  \n'
               '   3 - Quit                              \n'
               )

main_dispatch = {'1': send_thank_you,
                 '2': create_report,
                 '3': quit_msg,
                 }


if __name__ == "__main__":
    """Execute the main menu prompt."""
    # initialize donor collection database
    db = DonorCollection()
    # preallocating donor collection database with some donor info
    donors = [['Katherine elmhurst', 'DAVID Anderson', 'edward Harvik',
               'rebecca manriquez', 'callum zelnick'],
              [[1000., 1500., 1900.], [10865., 5750.], [200., 200., 200.],
              [1750., 1500.], [101.]]]
    for i, donor in enumerate(donors[0]):
        for amt in donors[1][i]:
            db.update_donor(donor, amt)
    # query user input
    while True:
        try:
            menu_selection(main_prompt, main_dispatch)
        except KeyboardInterrupt:
            print("\nPlease use the menu option '3' to Quit.")
        else:
            break
