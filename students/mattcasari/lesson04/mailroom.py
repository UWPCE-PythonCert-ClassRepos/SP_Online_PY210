#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 4, Exercise 3

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part2.html

Description:
    The Program: Part 2
    Update the program from Lesson 3 (Part 1) by using dicts where appropriate.

    Also, add file writing.

"""
import pathlib

donors = {}

PROMPT_TEXT = (
    "\nSelect an option:\n"
    "1. Send a Thank You to a single donor.\n"
    "2. Create a Report.\n"
    "3. Send letters to all donors.\n"
    "4. Quit\n"
    "> "
)


def prompt_user():
    """ Prompts the user for menu option """
    switch_func_dict = {
        1: add_donor,
        2: generate_report,
        3: create_files,
        4: quit_program,
    }

    result = input(PROMPT_TEXT)
    result = int(result)
    switch_func_dict.get(result)()


def initialize_donors():
    """
    Populate the donor list with the initial donors
    """
    donors["Neil Armstrong"] = [15000.00, 15000.00]
    donors["Buzz Aldrin"] = [23021.10, 25020.30, 28999.29]
    donors["Sally Ride"] = [42917.42, 38281.28]
    donors["Al Shepard"] = [2387.00, 2321.42, 3700.00]
    donors["Alan Bean"] = [28477.13, 727.1]
    donors["Chris Hadfield"] = [17325.42, 13823.83, 0.99]


def calculate_stats(donations):
    """
    Calculates the sum, average and number of donations for a donor 

    Args:
        donations: list of all donations

    Returns:
        donor_sum: Sum of all donations
        donor_num: Number of donations
        donor_average: Average of all donations    
    """
    donor_sum = sum(donations)
    donor_num = len(donations)
    donor_average = donor_sum / donor_num
    return (donor_sum, donor_num, donor_average)


def sort_donors_by_total(name):
    """ Function used to sort donors by total contributions """
    return sum(donors[name])


def quit_program():
    """ 
    Exits out of program
    """
    print("Exiting Program")
    quit()


def create_files():
    """
    Create file(s) in user specified directory for each donor.
    """
    directory = input("Enter save directory name: ")
    path = pathlib.Path("./")
    path = path / directory
    if not path.exists():
        path.mkdir()

    for donor in donors:
        filename = donor.replace(" ", "_") + ".txt"
        filename = path / filename

        with open(filename, "w+") as temp:
            name = donor
            donation_last = donors[donor][-1]
            donation_sum = sum(donors[donor])
            donation_number = len(donors[donor])
            EMAIL_TEMPLATE = (
                f"Dear {name},\n\n"
                f"Thank you for your last donation of ${donation_last:.2f}.\n"
                f"You have contributed a total of ${donation_sum:.2f} over {donation_number} donation(s).\n"
                f"Your generosity is appreciated.\n"
                f"\nSincerely,\n"
                f"-The Team\n\n"
            )

            temp.write(EMAIL_TEMPLATE)
            temp.close()


def generate_report():
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    values = donors
    print("\n")
    column_donor_length = 0
    for value in values:
        column_donor_length = max(len(values), column_donor_length) + 5

    f_str = " {" + f":<{column_donor_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(title_str)
    print("-" * len(title_str))

    values = sorted(donors, key=sort_donors_by_total, reverse=True)

    for value in values:
        f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
        (d_sum, d_num, d_ave) = calculate_stats(donors[value])
        v_str = f_str.format(value, d_sum, d_num, d_ave)

        print(v_str)


def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value)


def thank_you_email(name, amount):
    """
    Create the email from a template.
    
    Args:
        name: Name of donor
        amount: Amount donated (this time)
    Return:
        email: Contents of email
    """

    txt = (
        f"""\nDear {name},\n"""
        f"""Thank you for your recent donation of ${amount:.2f}. """
        f"""Your donation will help us purchase a taxidermied seagull.\n"""
        f"""Please consider donating again at your earliest convenience.\n\n"""
        f"""Sincerely,\n"""
        f"""The Human Fund\n"""
    )

    return txt


def add_donor():
    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        donor = input("Enter Full Name (or list): ")

        if donors.get(donor):
            valid_donor = True
            break
        else:
            if donor == "list":
                print_donor_list(donors)
                continue
            else:
                donors[donor] = []
                valid_donor = True
                break

    amount = input("Enter donation amount ($): ")
    amount = float(amount)

    # Add amount to data
    donors[donor].append(amount)

    txt = thank_you_email(donor, amount)
    print(txt)


def main():
    """ Main Run Loop """
    initialize_donors()

    while True:
        prompt_user()


if __name__ == "__main__":
    main()
