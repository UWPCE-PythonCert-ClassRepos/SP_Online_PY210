#!/usr/bin/env python3
import tempfile
import time
import sys
import donor_models as dm
"""
A  module for handling command line interface for a donor program
"""

donors = dm.DonorCollection()


def thank_you():
    """
    Print menu options for writing a thank you letter.
    If 'list' is provided, launch list_donors function.
    if 'menu' is provided, this function terminates
    If a name is provided, launch write_letter function
    """
    thank_you_options = {
        "MENU": False,
        "LIST": list_donors
    }
    while True:
        user_selection = (
            input("\nPlease provide a full name to send thank you note to (options 'list' and 'menu'): ")
        )
        action = thank_you_options.get(user_selection.upper())
        if action is False:
            break
        elif action is None:  # Write letter to user selection if an action option wasn't selected
            write_letter(user_selection)
        else:
            action()


def list_donors():
    """Go through each donor in public donors object and print to console"""
    for name in donors.list_donor_names():
        print(name)


def write_letter(person):
    """
    Receive the name of a person.
    Look through people in donors object and use that donor if they exist, if they don't asks if user wants to create
    a new donor. Add a new donor to the public donors if desired.
    If a donor existed, or the user wants to create a new donor then ask for the amount donated.
    The donation is then added to the donor within the donors object and the object's generate_recent_thanks() function
    is called.
    """
    current_donor = next((x for x in donors.donor_list if x.name.upper() == person.upper()), None)
    if current_donor is None:
        create_choice = input(person + " doesn't exist in the database, would you like to add them? (yes to add): ")
        if create_choice.upper() == "YES":
            donors.add_new_donor(person)
            current_donor = donors.donor_list[-1]
        else:
            print(person + " was not added")
    if current_donor is not None:
        while True:  # Loop until a valid amount is provided
            donation_amount = input("\nHow much did {} donate?: ".format(person))
            try:
                donation_amount = round(float(donation_amount), 2)
            except ValueError:
                print("Please provide a valid amount without $ symbol")
            else:
                if donation_amount > 0:
                    break
                else:
                    print("Please provide a valid amount without $ symbol")
        current_donor.new_donation(donation_amount)
        print(current_donor.generate_recent_thanks())


def print_report():
    """Print a report of all the donors in the public donors object to the console"""
    the_report = donors.generate_report()
    print(the_report)


def print_all():
    """
    Generate thank you letters for each donor in public donors object and stores them in a temp directory.
    Create files by calling file_creation() function.
    """
    file_location = tempfile.gettempdir()
    print("letters stored at: " + file_location)
    for donor in donors.donor_list:
        file_path_name = "{}{}{}".format(file_location, "\\", donor.name)
        file = file_creation(file_path_name)
        file.write(donor.generate_total_thanks())
        file.close()


def file_creation(file_name):
    """Create and time stamp text files with provided file_name"""
    return open("{}{}{}".format(file_name, time.strftime("%Y%m%d-%H%M%S"), ".txt"), "w")


def menu_input():
    """Print main  menu options and gets user input"""
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Send letters to all donors"
        "\n4. Quit\n"
    )


def main():
    """Main menu that will load an existing hard coded donors and act upon user selection"""
    menu_switch = {
        "1": thank_you,
        "2": print_report,
        "3": print_all,
        "4": sys.exit
    }
    load_donors()
    while True:
        user_selection = menu_input()
        action = menu_switch.get(user_selection)
        try:
            action()
        except TypeError:
            print("Please provide a valid option \n")


def load_donors():
    """Load an existing set of donors to public donors object"""
    donors.add_existing_donor("Jeff Bezos", 877.33, 1)
    donors.add_existing_donor("Paul Allen", 708.42, 3)
    donors.add_existing_donor("Steve Jobs", 1002.40, 2)
    donors.add_existing_donor("Mark Zuckerberg", 16396.1, 3)
    donors.add_existing_donor("Bill Gates", 653784.49, 2)


if __name__ == '__main__':
    main()
