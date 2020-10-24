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

c = DonorCollection()

def send_thank_you():
    """Process donation and send Thank You to individual donor."""
    name = input('\nEnter the full name of the donor > ')
    if name == 'list':
        print('\nPrinting list of current donors :\n')
        for i, donor in enumerate(c.donor_list, start=1):
            print(f"{i:>4d}:  {donor}")
        send_thank_you()
    elif name in ['quit', 'q']:
        return None
    else:
        index = c.check_name(name)
        print(index)
        if index >= 0:
            print(f'Donor {c.donors[index].name} found in donor database\n')
            d = c.donors[index]
        else:
            print(f'Adding {name.upper()} to donor database')
            d = Donor(name)
            c.add_donor(d)
        print(c.donor_list)
        print(c.check_name(name.upper()))
        amt = input('\nEnter a donation amount > $ ')
        while True:
            try:
                d.add_donation(amt)
            except ValueError:
                amt = input('\nPlease enter a valid dollar amount > $ ')
            else:
                break
        print(c.thank_you(d.name))


def create_report():
    pass

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
    while True:
        try:
            menu_selection(main_prompt, main_dispatch)
        except KeyboardInterrupt:
            print("\nPlease use the menu option '3' to Quit.")
        else:
            break
