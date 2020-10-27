#!/usr/bin/env python3

"""
Becky Larson
Created 10/5/2020
Updated 10/11/2020
"""

from donor_models import DonorCollection, Donor
import sys

"""Mailroom OO"""

"""
objects:
1) Donor class holds information about a single donor.
Properties: Count of donations, Average donations, Total sum of donations
Methods: Add a donation, Format thank you note to donator
format_ty(self):

2) DonorCollection holds all of the donor objects
Methods: List Donors, Add donor,
         Create report of donors Sorted by total donations
Static Method: create DonorCollection instance from dict
"""


def main():
    main_prompt = ("\nMake Selection\n"
                   "1 - Send Thank You\n"
                   "2 - Create Report\n"
                   "3 - Quit\n>> ")
    dispatch = {"1": send_ty, "2": create_report, "3": exit_program}
    menu_selection(main_prompt, **dispatch)


def menu_selection(prompt, **dispatch_dict):
    """
    prompts user for input and calls function object in dispatch_dict
    :param prompt: user input prompt
    :param dispatch_dict: dict of dispatch functions
    """
    while True:
        try:
            response = safe_input(f"{prompt}")
        except (TypeError, ValueError) as menu_err:
            print(f"Invalid option {response}\n")
            raise menu_err
        if dispatch_dict[response]() == 3:
            sys.exit()


def safe_input(prompt):
    """
    Prompt user for input; handle forced exit of mailroom
    :param prompt: user prompt
    :return: response
    """
    try:
        response = input(prompt).strip()
    except KeyboardInterrupt:
        print('\n\nKeyboardInterrupt: Interrupted and Exiting')
        sys.exit()
    else:
        return response


def send_ty():
    """
    prompt user for a donor name; if name exists, prompts for donation,
        otherwise add name to DonorCollection object;
    'list' displays a list of donors
    print thank you to donor
    """
    donor_prompt = "\n".join(("\nEnter Full name of donor",
                              "  or Enter list to show current donors",
                              "  or 'q' to return to main menu",
                              "  "
                              " > "))
    donor_name = safe_input(donor_prompt).title()

    if donor_name.lower() == 'list':
        print(f"List of donors: {', '.join([donor for donor in donor_collection.donors])}")
    elif donor_name not in donor_collection.donors:
        add_donor(donor_name)
        add_donation(donor_name)
    else:
        add_donation(donor_name)
    print(f"{donor_collection[donor_name].format_ty()}")


def add_donor(donor_name: str):
    """
    if donor not in DB, add donor; prompt user for initial donation
    :param donor_name:
    """
    donor_collection.append(Donor(donor_name))
    print(f'Added new donor: {donor_name}')


def add_donation(donor_name: str):
    """
    Prompts user for donation amount; adds to Donor's donations
    :param donor_name:
    """
    donation_amt = get_donation_amt()
    donor_collection[donor_name].add_donation(donation_amt)


def get_donation_amt():
    """
    Accepts user input for a donation amount and
    returns the donation amount
    """

    donation = 0

    while donation <= 0:
        donation = safe_input("Please enter the donation amount: ").strip('$')
        try:
            donation = float(donation)
        except ValueError:
            print("Not a valid donation amount.")
            donation = 0
        else:
            if donation <= 0:
                print("Not a valid donation amount.")
    return donation


def create_report():
    """
    Print formatted report of donors and donations.
    Sort report by total donations
    """
    if not donor_collection.donors:
        raise ValueError("No Donors in Data Collection")
    print(donor_collection.report())


def exit_program():
    """
    :return:  (quit option 3)
    """
    print('Thank you')
    return 3


donors_data = {Donor("Cher", [1000.00, 245.00]),
               Donor("Drew Barrymore", [25000.00]),
               Donor("Charlie Brown", [25.00, 50.01, 100.00]),
               Donor("Jack Black", [256.00, 752.50, 10101.00]),
               Donor("Sam Smith", [5500.00, 24.00]),
               }

if __name__ == "__main__":

    donor_collection = DonorCollection(donors_data)
    main()
