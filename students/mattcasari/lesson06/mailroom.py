#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 5, Exercise 2

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part2.html

Description:
    The Program: Part 3
    - Add Exceptions to inputs (and file handling)
    - Use comprehensions where appropriate

"""
import pathlib
import sys

donors = {}

THANK_YOU_TEMPLATE = (
    """\nDear {name},\n"""
    """Thank you for your recent donation of ${amount:.2f}. """
    """Your donation will help us purchase a taxidermied seagull.\n"""
    """Please consider donating again at your earliest convenience.\n\n"""
    """Sincerely,\n"""
    """The Human Fund\n"""
)
EMAIL_TEMPLATE = (
    "Dear {name},\n\n"
    "Thank you for your last donation of ${last:.2f}.\n"
    "You have contributed a total of ${sum:.2f} over {number} donation(s).\n"
    "Your generosity is appreciated.\n"
    "\nSincerely,\n"
    "-The Team\n\n"
)

PROMPT_TEXT = (
    "\nSelect an option:\n"
    "1. Send a Thank You to a single donor.\n"
    "2. Create a Report.\n"
    "3. Send letters to all donors.\n"
    "4. Quit\n"
    "> "
)


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
        result: dict of sum, length and average   
    """
    results = {
        "sum": sum(donations),
        "len": len(donations),
        "average": sum(donations) / len(donations),
    }

    return results


def thank_you_email(donor_dict):
    """
    Create the email from a template.
    
    Args:
        name: Name of donor
        amount: Amount donated (this time)
    Return:
        email: Contents of email
    """

    return THANK_YOU_TEMPLATE.format(**donor_dict)


def update_donation_dict(name, amount):
    """
    Updates the donors dictionary with new amount
    
    Args:
        name: Full donor name
        amount: Donation amount ($)

    Returns:
        None
    """
    donors.setdefault(name, []).append(amount)


def sort_donors_by_total(donors):
    print(type(donors))
    """ Function used to sort donors by total contributions """
    # return sum(donors)

def create_report_header(max_name_length):
    result = []
    f_str = " {" + f":<{max_name_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    result.append(title_str)
    result.append("-" * len(title_str))

    return result

def create_report_body(name_length, donors):
    result = []
    f_str = " {name" + f":<{name_length}" + "}  ${sum:11.2f}   {len:9}  ${average:12.2f}"
    for donor in donors.keys():
        stats = calculate_stats(donors[donor])
        stats['name']=donor
        v_str = f_str.format(**stats)
        result.append(v_str)

    return result

def generate_report(donors):
    names = donors.keys()
    column_donor_length = max([len(name) for name in names])+5

    header = "\n".join(create_report_header(column_donor_length))

    body = "\n".join(create_report_body(column_donor_length, donors))

def generate_report2(donors):
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    names = donors.keys()
    print("donors=", donors)
    print("names=", names)
    result = []

    column_donor_length = max([len(name) + 5 for name in names])
    report_header = create_report_header(column_donor_length)
    report_body = create_report_body()
    

    # for name in names:
    names = sorted(donors.values(), key=sort_donors_by_total, reverse=True)
    # names = sorted(sum(donors.iterkeys()))
    print(names)

    # for name in names:
    #     f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
    #     (d_sum, d_num, d_ave) = calculate_stats(donors[name])
    #     v_str = f_str.format(name, d_sum, d_num, d_ave)
    #     result.append(v_str)
    #     # print(v_str)

    # return result


"""
NO TESTS FOR THE FOLLOWING FUNCTIONS
All following functions require inputs or print statements
"""


def add_donor():
    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        try:
            donor = input("Enter Full Name (or list): ")
            amount = input("Enter donation amount ($): ")
            amount = float(amount)
            if donor == "list":
                print_donor_list(donors)
            else:
                valid_donor = True
        except ValueError:
            print("Invalid entry")
    try:
        update_donation_dict(donor, amount)
        donor = {"name": donor, "amount": amount}
        txt = thank_you_email(donor)
        print(txt)
    except ValueError:
        print("\nInvalid amount entered")


def prompt_user():
    """ Prompts the user for menu option """
    switch_func_dict = {
        1: add_donor,
        2: generate_report,
        3: create_files,
        4: quit_program,
    }
    try:
        result = input(PROMPT_TEXT)
        result = int(result)
        switch_func_dict.get(result)()
    except (ValueError, TypeError):
        print("\nInvalid Entry")


def quit_program():
    """ 
    Exits out of program
    """
    print("Exiting Program")
    sys.exit()


def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value)


def create_directory():
    try:
        directory = input("Enter save directory name: ")
        path = pathlib.Path("./")
        path = path / directory
        if not path.exists():
            path.mkdir()
    except OSError:
        print("Error creating directory")

    return directory


def create_files():
    """
    Create file(s) in user specified directory for each donor.
    """
    path = input("Enter save directory name: ")

    for donor in donors:
        filename = donor.replace(" ", "_") + ".txt"
        filename = path / filename
        try:
            with open(filename, "w+") as temp:
                donor_dict = {
                    "name": donor,
                    "last": donors[donor][-1],
                    "sum": sum(donors[donor]),
                    "number": len(donors[donor]),
                }

                temp.write(EMAIL_TEMPLATE.format(**donor_dict))
                temp.close()
        except OSError:
            print("File failure")


def main():
    """ Main Run Loop """
    initialize_donors()

    while True:
        prompt_user()


if __name__ == "__main__":
    main()
