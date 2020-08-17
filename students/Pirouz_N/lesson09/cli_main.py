#!/usr/bin/env python3
"""
Purpose: OO Mailroom Part 1 python certificate from UW
Author: Pirouz Naghavi
Date: 08/14/2020
"""
from donor_models import DonorCollection
import sys

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]


def main_menu_option_one(donors):
    """"Function that will be called for menu option one. Sends thank you."""
    send_thank_you(donors)


def main_menu_option_two(donors):
    """"Function that will be called for menu option two. Prints donor report. """
    print(donors.report_all_donors())


def main_menu_option_three(donors):
    """"Function that will be called for menu option three. Records data in the donor table and exits main menu."""
    global donor_db
    donor_db = donors.create_donor_table()
    sys.exit()


def main():
    """"This function makes the menu portion of the program work."""
    global donor_db
    donors = DonorCollection(donor_db)
    option_dict = {'1': main_menu_option_one, '2': main_menu_option_two, '3': main_menu_option_three}
    while True:
        option = input('Please select of the three options: Send a Thank You, Create a Report or Quit.\n'
                       'Type 1 and hit enter if you wish to Send a Thank You\n'
                       'Type 2 and hit enter if you wish to Create a Report\n'
                       'Type 3 and hit enter if you wish to Quit\n'
                       'Please make your selection:\n')
        try:
            option_dict[option](donors)
        except KeyError:
            print(f"Please choose from following options: {', '.join(map(str, option_dict))}")


def ask_donation_write_thank_you(name, donors):
    """"This function will write a thank to a donor.

    Args:
        donors: Is the donors collection object.
        name: Name of the donor.
    """
    while True:
        amount = input('Please enter your donation amount:')
        try:
            amount_float = float(amount)
        except ValueError:
            print('Entered value cannot be accepted. Please enter a number.')
        else:
            try:
                new_donor, letter = donors.add_donor_or_donation(name, amount_float)
                if new_donor:
                    print("{} has been added to the list of donors.".format(name))
                print(letter)
            except ValueError as err:
                print(err)
            else:
                break


def send_thank_you(donors):
    """"This function will type a thank card to the selected donor."""
    while True:
        option = input('Please type in the name of the donor you wish to thank.\n'
                       'If you wish to see the list of all the donors, please type list.\n'
                       'If you wish to add a new donor to the list, please type in their name.\n'
                       'If you wish to return to the main menu please type exit and hit enter.\n'
                       'Please type in your desired option and hit enter:\n')

        if option == 'list':
            print(donors.list_of_donor_names())

        elif option == 'exit':
            break
        elif option == '':
            print('Name is required for every donor.')
        else:
            if option not in donors:
                response = input("Entered name in not amongst the donors. Are you sure you want to add this donor to"
                                 " the list of donors. If so please type yes and hit enter otherwise hit enter and the"
                                 "program will return to previous state.\n")
                if response != "yes":
                    continue
            ask_donation_write_thank_you(option, donors)
            break


if __name__ == "__main__":
    # run some unit tests on everything
    main()
