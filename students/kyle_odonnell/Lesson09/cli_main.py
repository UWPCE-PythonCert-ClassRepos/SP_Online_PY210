#!/usr/bin/env python3

""""
Title: cli_main.py (Py210: Introduction to Python - Lesson09 - Assignment 8)
Description: Refactoring of Mailroom.py to use custom classes in donor_models.py
KODonnell, 01-17-2021, updated code to use Donor nad DonorCollections
"""

import sys
from donor_models import Donor
from donor_models import DonorCollections


# Data -------------------------------------------------------------------- #
# Dictionary with Donor Data
donor_dict = {
    "William Gates, III": [653784.49, 2, 326892.24],
    "Mark Zuckerberg": [16396.10, 3, 5465.37],
    "Jeff Bezos": [877.33, 1, 877.33],
    "Paul Allen": [708.42, 3, 236.14],
    "Elon Musk": [50.00, 2, 25.00]
}


# Presentation (Input/Output)  -------------------------------------------- #
# Convert dictionary to DonorCollections object
def render_donor_collections(donor_data):
    """
    Render DonorCollections object from dictionary
    :param donor_data: (dictionary) with donor information:
    :return: DonorCollections
    """
    donor_objects = DonorCollections()
    for x in donor_data.items():
        d = Donor(x[0], amount=x[1][0], number=x[1][1])
        donor_objects.add_donor(d)
    return donor_objects


def welcome_message():  # Display welcome message
    """
    Print welcome message when program is launched
    :return: nothing
    """
    print("\nWelcome to the Mailroom Program!")


def menu_options():  # Display menu options
    """
    Print menu options for users
    :return: nothing
    """
    print('''
    ******MENU OPTIONS*******
    Option 1: Generate Report
    Option 2: Update Database
    Option 3: Write Letter
    Option 4: Send Letters
    Option 5: Exit \n''')


def prompt_menu_option():  # Elicit main menu option
    """
    Prompt menu option
    :return: string
    """
    menu_option = input("Please select an option from the menu (1-5): ")
    return menu_option


def enter_name():  # Elicit donor name
    """
    Prompt donor name
    :return: string
    """
    name = input("Please enter a donor's full name: ").title()
    return name


def display_names(donor_db):  # Display list of donor names
    """
    Print list of donor names
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: nothing
    """
    for name in donor_db.get_names():
        print(name)


def enter_donation(name):  # Elicit donation amount
    """
    Prompt donation amount for donor
    :param name: (string) with name of donor:
    :return: float
    """
    try:
        donation = round(float(input("Please enter the donation amount "
                                     "from {}: ".format(name))), 2)
        if donation >= 0:
            return donation
        else:
            raise ValueError
    except ValueError:
        print("Donations must be entered as a positive number!")
        return ValueError


def print_report(donor_db):
    """
    Print formatted report
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: DonorCollections
    """
    formatted_report = DonorCollections.format(donor_db)
    for row in formatted_report:
        print(row)
    press_enter_to_continue()
    return donor_db


def close_app(donor_db):
    """
    Print goodbye message and exit
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: nothing
    """
    print("Closing the Mailroom Program...Goodbye!")
    sys.exit()


def lookup_donor(donor_name, donor_db):
    """
    Returns donor object in databse
    :param donor_name: (string) name of Donor object
    :param donor_db: (DonorCollections) database of Donor objects
    :return:
    """
    if donor_name in donor_db.get_names:
        for x in donor_db.list:
            if x.name == donor_name:
                return x
    else:
        return None


def write_letter(donor_db):  # Write letter to donor
    """
    Prompt new donation info and print letter
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: DonorCollections
    """
    while True:
        print("(Enter 'list' to see names or 'cancel' to cancel task)")
        name_string = enter_name()
        # Cancel task
        if name_string.lower().strip() in ["cancel", "stop", "never mind", "nm"]:
            print("Cancelling task...")
            break
        # Print list of donors
        elif name_string.lower().strip() in ["list", "go to list", "show list"]:
            print("\nHere are the names of all donors in your database:")
            for x in donor_db.get_names:
                print(x)
            print("\n")
        # Find donor in database
        else:
            donor = lookup_donor(name_string, donor_db)
            if donor:
                print(donor.write_letter)
            else:
                print("{} is not in your database. "
                      "Select Option 2 from the menu to add them".format(name_string))
            break
    press_enter_to_continue()
    return donor_db


def send_letter_menu():  # Prompt for letter writing options
    """
    Prompt option to send one or all letters
    :return: integer
    """
    file_option = int(input("""
    Okay, let's generate some letter files! You can:
    1. Create a letter for a specific donor
    2. Create letters for all donors
    Please select an option (1 or 2): """))
    return file_option


def send_letter(donor_db):
    """
    Process choice to send one letter or all letters
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: DonorCollections
    """
    letter_choice = send_letter_menu()
    if letter_choice == 1:
        name = input("What donor would you like to write to? ")
        donor = lookup_donor(name, donor_db)
        if donor:
            donor.send_letter()
            print("Check your local directory for a letter to {}!".format(name))
        else:
            print("{} is not in your database!".format(name.title()))
    else:
        donor_db.send_letters()
        print("Check your local directory for letter files!")
    press_enter_to_continue()
    return donor_db


def press_enter_to_continue():
    """ Prompt user to press enter to continue
    :return: nothing
    """
    input("Press 'Enter' to Continue ")


def add_donation(donor_db):
    """
    Add new donation to DonorCollections
    :param donor_db: (DonorCollections) database of Donor objects:
    :return: DonorCollections
    """
    donor_name = enter_name()
    try:
        # add donation for existing donor
        donor = lookup_donor(donor_name, donor_db)
        if donor:
            donation = enter_donation(donor_name)
            donor.add_donation(donation)
            print("{} has been added for {}!".format(donation, donor_name))
        # add new donor to database
        else:
            confirm_add = input("{} is not in the database. "
                                "Would you like to add them? ".format(donor_name))
            if confirm_add.lower() in ["y", "yes", "yeah"]:
                donation = enter_donation(donor_name)
                new_donor = Donor(donor_name, amount=donation, number=1)
                donor_db.add_donor(new_donor)
                print("{} has been added to your database".format(donor_name))
            else:
                print("{} will not be added to the database!".format(donor_name))
    except ValueError:
        pass
    press_enter_to_continue()
    return donor_db


# Switch function dictionary for main menu
switch_func_dict = {
    1: print_report,
    2: add_donation,
    3: write_letter,
    4: send_letter,
    5: close_app
}


# Main Body of Script  ---------------------------------------------------- #
if __name__ == '__main__':

    welcome_message()
    donors = render_donor_collections(donor_dict)
    while True:
        menu_options()
        try:
            choice = int(prompt_menu_option())
            donors = switch_func_dict.get(choice)(donors)
        except ValueError:
            print("Please choose a number from the menu")
        except TypeError:
            print("Please enter a choice between 1-5")
