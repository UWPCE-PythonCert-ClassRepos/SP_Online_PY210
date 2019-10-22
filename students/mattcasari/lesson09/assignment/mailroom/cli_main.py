#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 9, Exercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-oo.html

Description:
    Mailroom - Object Oriented

"""
import pathlib
import sys
import donor_models as dm

donors = dm.DonorCollection()

PROMPT_TEXT = (
    "\nSelect an option:\n"
    "1. Send a Thank You to a single donor.\n"
    "2. Create a Report.\n"
    "3. Send letters to all donors.\n"
    "4. Quit\n"
    "> "
)

def main():
    """ 
    Main Run Loop 
    """
    initialize_donors()

    while True:
        prompt_user()

def initialize_donors():
    """
    Populate the donor list with the initial donors
    """
    donors.add_donor(dm.Donor("Neil Armstrong",[15000.00, 15000.00]))
    donors.add_donor(dm.Donor("Buzz Alrid",[23021.10, 25020.30, 28999.29]))
    donors.add_donor(dm.Donor("Sally Ride",[42917.42, 38281.28]))
    donors.add_donor(dm.Donor("Al Shepard",[2387.00, 2321.42, 3700.00]))
    donors.add_donor(dm.Donor("Alan Bean",[28477.13, 727.1]))
    donors.add_donor(dm.Donor("Mae Jemison",[23185.22, 17271.55, 1372.34]))
    donors.add_donor(dm.Donor("Chris Hadfield",[17325.42, 13823.83, 0.99]))

def prompt_user():
    """ 
    Prompts the user for menu option 
    """
    switch_func_dict = {
        1: add_donor,
        2: generate_report,
        3: send_letters,
        4: quit_program,
    }
    try:
        result = input(PROMPT_TEXT)
        result = int(result)
        switch_func_dict.get(result)()
    except (ValueError, TypeError) as e:
        print("\nInvalid Entry")
        print(e)


def add_donor():
    """ 
    Adds new donor or new donation to existing donor 
    """
    valid_donor = False
    while not valid_donor:
        donor_name = input("Enter Full Name (or list): ")
        if donor_name == "list":
                print(donors.donor_list)
        else:
            amount = input("Enter donation amount ($): ")

            try:
                amount = float(amount)
                
            except ValueError:
                print("Invalid Entry")

            donor = dm.Donor(donor_name, [amount])
            donors.add_donor(donor)
            print(donor.thank_you_letter())
            valid_donor = True
    
def generate_report():
    """
    Creates the report of all donors and donation history
    """
    print(donors.generate_report())


def quit_program():
    """ 
    Exits out of program
    """
    print("Exiting Program")
    sys.exit()


def print_donor_list(values):
    """ 
    Prints the list of donors passed to function
    """
    print("\nList of donors:".upper())
    for value in values:
        print(value)


def send_letters():
    """
    Create file(s) in user specified directory for each donor.
    """
    directory = input("Enter save directory name: ")
    path = create_directory(directory)
    save_letters(donors, path)

def create_directory(directory):
    """
    Create a directory to save letters to.
    Args:
        directory: Path to create
    Returns:
        directory: Path created
    """
    path = pathlib.Path("./")
    path = path / directory
    try:
        if not path.exists():
            path.mkdir()
    except OSError:
        print("Error creating directory")

    return path

def save_letters(donors, path):
    """
    Generate and save letters to donors

    Args: 
        donors: Dictionary of donors and donations
        path: Directory to save letters to
    """
    path = pathlib.Path("./") / path
    for donor in donors.donor_list:
        filename = donor.name.replace(" ", "_") + ".txt"
        filename = path / filename
        try:
            with open(filename, "w+") as temp:
                temp.write(donor.thank_you_email())
        except OSError:
            print("File failure")

if __name__ == "__main__":
    main()
