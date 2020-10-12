#!/usr/bin/env python3

# belarson - add check if donor exists
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
Methods: List Donors, Add donor, Create report of donors Sorted by total donations
Static Method: create DonorCollection instance from dict
"""


def main():
    main_prompt = ("\Select Next Step\n"
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
    :return:
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
    :return: None
    """
    donor_prompt = "\n".join(("\nEnter Full name of donor",
                        "  or Enter list to show current donors",
                        "  or 'q' to return to main menu",
                        "  "
                        " > "))
    donor_name = safe_input(donor_prompt)

    if donor_name.lower() == 'list':
        print(f"List of donors: {', '.join([donor for donor in donors.donors])}")
    elif donor_name not in donors.donors:
        add_donor(donor_name)
        add_donation(donor_name)
    else:
        while True:
            add_donation(donor_name)
            continue
        print(f"{donors[donor_name].send_ty()}")


def add_donor(donor_name: str):
    """
    if donor not in DB, add donor; prompt user for initial donation
    :param donor_name:
    :return:
    """
    donor_response = safe_input(f"Donor {donor_name} does not exist, do you want to add donor to database (Y/N)?: ").lower().strip()
    if donor_response and donor_response[0] == "y":
        donors.append(Donor(donor_name))
    else:
        exit()


def add_donation(donor_name: str):
    """
    Prompts user for donation amount; adds to Donor's donations
    :param donor_name:
    :return:
    """
    donation = float(safe_input("Please enter the donation amount: ").strip('$'))
    if donation == "q":
        return

    try:
        donors[donor_name].add_donation(donation)
    except ValueError as donation_err:
        raise donation_err


def create_report():
    """
    Print formatted report of donors and donations. Sort report by total donations
    :param collection: collection of Donor objects
    :return: None
    """
    if not donors.donors:
        raise ValueError("No Donors in Data Collection")
    donors.report()


def exit_program():
    """
    :return:  (quit option 3)
    """
    print('Thank you')
    return 3

 
if __name__ == "__main__":
    donors = DonorCollection()
    main()
