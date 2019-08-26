#!/usr/bin/env python3

"""
Module responsible for main program flow (CLI - Command Line Interface).
"""

import sys
from donor_models import *

def send_thankyou(donor_db):
    """Compose an email thanking the donor for their generous donation."""
    # Ask for donor's full name
    name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Continue asking for donor's full name
    while name == "list":
        # Display list of donor names
        print_donor(donor_db)
        # Ask for donor's full name
        name = input("Enter donor's full name (or 'list' to list all donor' names): ")
    # Prompt for a donation amount
    response = input("Enter donation amount: $")
    # Convert user's prompt in string to float
    try:
        amount = float(response)
    except ValueError:
        print("amount must be a number")
        exit_program()
    # Add new amount to the donation history of the selected donor
    donor_db.add_donor(name, amount)
    # Compose thank you email to the donor
    index = donor_db.search_donor(name)
    prompt = donor_db.donors[index].send_thankyou()
    print(prompt)

def create_report(donor_db):
    """
    Print a list of donors, sorted by total historical donation amount.

    Sample:
    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

    """
    # Sort the donor's list by total historical donation amount
    donor_db.sort_by_donations(reverse=True)
    # Print header
    fheader = "\n{:<26}|{:^13}|{:^11}|{:>13}"
    print(fheader.format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print('-' * 66)
    # Get body format
    fbody = "{:<27}${:>11.2f}{:>12}  ${:>12.2f}"
    # Get report content of all donors
    contents = donor_db.create_report()
    for content in contents:
        # Print report
        print(fbody.format(*content))

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script
  
def print_donor(donor_db):
    """
    Print all donor names.
    """
    for donor in donor_db.donors:
        print(donor.name)

def main():

    # Initialize list of donors with their names and the amounts they have donated
    donor_db = DonorCollection([
                    Donor("William Gates, III", [653772.32, 12.17]),
                    Donor("Jeff Bezos", [877.33]),
                    Donor("Paul Allen", [663.23, 43.87, 1.32]),
                    Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
                    Donor("Bill Nordstrom", [2013.25, 23456.78]),
                ])

    prompt = "\n".join(("\nWelcome to the mail room!",
            "Please choose from below options:",
            "1 - Send a Thank You",
            "2 - Create a Report",
            "3 - quit",
            ">>> "))

    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_thankyou(donor_db)
        elif response == "2":
            create_report(donor_db)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
