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

DONORS = {}

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
    DONORS["Neil Armstrong"] = [15000.00, 15000.00]
    DONORS["Buzz Aldrin"] = [23021.10, 25020.30, 28999.29]
    DONORS["Sally Ride"] = [42917.42, 38281.28]
    DONORS["Al Shepard"] = [2387.00, 2321.42, 3700.00]
    DONORS["Alan Bean"] = [28477.13, 727.1]
    DONORS["Chris Hadfield"] = [17325.42, 13823.83, 0.99]


def calculate_stats(donations):
    """
    Calculates the sum, average and number of donations for a donor 

    Args:
        donations: list of all donations

    Returns:
        result: dict of sum, length and average   
    """
    results = {'sum':sum(donations),
                'len':len(donations),
                'average':sum(donations)/len(donations)}
    
    return results


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


def create_files():
    """
    Create file(s) in user specified directory for each donor.
    """
    directory = input("Enter save directory name: ")
    path = pathlib.Path("./")
    path = path / directory
    if not path.exists():
        path.mkdir()

    for donor in DONORS:
        filename = donor.replace(" ", "_") + ".txt"
        filename = path / filename
        try:
            with open(filename, "w+") as temp:
                donor_dict = {
                    "name": donor,
                    "last": DONORS[donor][-1],
                    "sum": sum(DONORS[donor]),
                    "number": len(DONORS[donor]),
                }

                temp.write(EMAIL_TEMPLATE.format(**donor_dict))
                temp.close()
        except OSError:
            print("File failure")

def sort_donors_by_total(donors):
    print(type(donors))
    """ Function used to sort donors by total contributions """
    return sum(donors)

def generate_report(donors):
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    names = donors.keys()
    print("donors=", donors)
    print("names=", names)
    result = []


    column_donor_length = max([len(name)+5 for name in names]) 
    
    f_str = " {" + f":<{column_donor_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    result.append(title_str)
    result.append("-" * len(title_str))

    
    for name in names:
    names = sorted(donors.values(), key=sort_donors_by_total, reverse=True)
    # names = sorted(sum(donors.iterkeys()))
    print(names)

    # for name in names:
    #     f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
    #     (d_sum, d_num, d_ave) = calculate_stats(DONORS[name])
    #     v_str = f_str.format(name, d_sum, d_num, d_ave)
    #     result.append(v_str)
    #     # print(v_str)

    # return result

def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value)


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


def add_donor():
    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        try:
            donor = input("Enter Full Name (or list): ")
        except ValueError:
            print("Invalid entry")
        else:
            for idx, value in enumerate(DONORS):
                if value[0] == donor:
                    valid_donor = True
                    break
            else:
                if donor == "list":
                    print_donor_list(DONORS)
                    continue
                else:
                    DONORS.setdefault(donor, [])

                    idx += 1
                    valid_donor = True
                    break
    try:
        amount = input("Enter donation amount ($): ")
        amount = float(amount)
    except ValueError:
        print("\nInvalid amount entered")
    else:
        # Add amount to data
        DONORS[donor].append(amount)
        donor = {"name": donor, "amount": amount}
        txt = thank_you_email(donor)
        print(txt)


def main():
    """ Main Run Loop """
    initialize_donors()

    while True:
        prompt_user()


if __name__ == "__main__":
    main()
