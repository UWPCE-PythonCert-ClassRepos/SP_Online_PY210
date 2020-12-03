#!/usr/bin/env python

# ------------------------------------------------------------------------ #
# Title: mailroom.py
# Description: Updated for Lesson06
# KODonnell,10.25.2020,created script
# KODonnell,11.05.2020 added switch dict menu
# KODonnell,11.07.2020 added function to generate letters
# KODonnell,11.10.2020 split file writing functions into multiple funcs
# KODonnell,11.14.2020 updated to *actually* have a dictionary database
# KODonnell,11.22.2020 updated exception handling
# KODonnell,11.29.2020 refactor for unit testing
# KODonnell,12.02.2020 update for unit testing
# ------------------------------------------------------------------------- #

import sys

# Data -------------------------------------------------------------------- #

# Dictionary database for donor information
donor_dict = {
    "William Gates, III": [653784.49, 2, 326892.24],
    "Mark Zuckerberg": [16396.10, 3, 5465.37],
    "Jeff Bezos": [877.33, 1, 877.33],
    "Paul Allen": [708.42,  3, 236.14],
    "Elon Musk": [50.00, 2, 25.00]
}


# Processing  ------------------------------------------------------------- #
def add_donation_amount(name, donation, donor_db):  # Add new donation to database
    """
    Add new donation to database
    :param name: (string) with name of donor:
    :param donation: (float) amount of donation:
    :param donor_db: (dictionary) with donor information:
    :return: dictionary
    """
    success = False
    try:
        total_update = donation + donor_db[name][0]
        num_update = donor_db[name][1] + 1
        average_update = round(total_update/num_update, 2)
        donor_db[name] = [total_update, num_update, average_update]
        success = True
    except KeyError:
        donor_db[name] = [donation, 1, donation]
    except ValueError:
        print("Entry failed: Donations must be entered as a number!")
    return donor_db, success


def format_report(donor_db):  # Format data in database
    """
    Format report of donor database
    :param donor_db: (dictionary) with donor information
    :return: string
    """
    report_list = []
    # Sort by total donated
    sorted_donor_db = sorted(donor_db.items(), key=lambda x: x[1], reverse=True)
    # Format table header
    heading = "| {dn:<20s}\t| {tg:<15s}\t| {ng:<10s} | {ag:<15s}   |".format
    report_list.append(heading(dn="Donor Name", tg="Total Given",
                               ng="Num Gifts", ag="Average Gift"))
    report_list.append("-" * 78)
    # Format Table rows
    row = "{dn:<20s} \t {ds:<1s} {tg:>14.2f} \t " \
          "{ng:>10d} \t {ds2:<1} {ag:>14.2f} ".format
    for i in sorted_donor_db:
        name = i[0]
        report_list.append(row(dn=name, ds="$", tg=donor_db[name][0],
                           ng=donor_db[name][1], ds2="$", ag=donor_db[name][2]))
    return report_list


def send_letters(donor_db):  # Create letter file for all donors
    """
    Generate letter files for donors in database
    :param donor_db: (dictionary) with donor information
    :return: nothing
    """
    for i, v in donor_db.items():
        name_list = (i.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(i.title(), v[0]))


def letter_text(name, value):  # Format string for thank you letter
    """
    Generate thank you letter text
    :param name: (string) with name of donor
    :param value: (float) with donation amount
    :return: string
    """
    letter = """
    Dear {},
    Thank you for your collective contributions of ${:.2f} over the years.
    Your generous donations have been put to good use!
    Sincerely,
    Kyle at Kelby Doggo, Inc\n""".format(name, value)
    return letter


# Presentation (Input/Output)  -------------------------------------------- #
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
    Option 1: Write Letter for New Donation
    Option 2: Send Letters to Donors
    Option 3: Create a Report
    Option 4: Exit \n''')


def prompt_menu_option():  # Elicit main menu option
    """
    Prompt menu option
    :return: string
    """
    menu_option = input("Please select an option from the menu (1-4): ")
    return menu_option


def enter_name():  # Elicit donor name
    """
    Prompt donor name
    :return: string
    """
    name = input("Please enter a donor's full name: ")
    return name


def display_names(donor_db):  # Display list of donor names
    """
    Print list of donor names
    :param donor_db: (dictionary) with donor information
    :return: nothing
    """
    count = 1
    for i, v in donor_db.items():
        print("{}. Donor Name: {}".format(count, i))
        count += 1


def enter_donation(name):  # Elicit donation amount
    """
    Prompt donation amount for donor
    :param name: (string) with name of donor:
    :return: float
    """
    donation = round(float(input("Please enter the donation amount from {}: ".format(name))), 2)
    return donation


def print_report(donor_db):
    """
    Print formatted report
    :param donor_db: (dictionary) with donor information
    :return: dictionary
    """
    formatted_report = format_report(donor_db)
    for row in formatted_report:
        print(row)
    press_enter_to_continue()
    return donor_db


def close_app(donor_db):
    """
    Print goodbye message and exit
    :param donor_db: (dictionary) with donor information:
    :return: nothing
    """
    print("Closing the Mailroom Program...Goodonor_dbye!")
    sys.exit()


def write_letter(donor_db):  # Update database
    """
    Prompt new donation info and print letter
    :param donor_db: (dictionary) with donor information:
    :return: dictionary
    """
    while True:
        name_string = enter_name()
        # Cancel task
        if name_string.lower() == "cancel":
            print("Cancelling task...")
            break
        # Print list of donors
        elif name_string.lower().strip() in ["list", "go to list", "show list"]:
            display_names(donor_db)
        else:
            # Prompt donation amount
            donation_amount = enter_donation(name_string)
            # Add entry to database
            donor_db, success = add_donation_amount(name_string.strip(" "),
                                                    donation_amount, donor_db)
            # Print letter
            if success:
                print(letter_text(name_string, donation_amount))
                break
            else:
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


def send_letter_choice(donor_db):
    """
    Process choice to send one letter or all letters
    :param donor_db: (dictionary) with donor information:
    :return: dictionary
    """
    letter_choice = send_letter_menu()
    if letter_choice == 1:
        name = input("What donor would you like to write to? ")
        try:
            amount = donor_db[name.title()][0]
            donor_data = {name: [amount]}
            send_letters(donor_data)
            print("Check your local directory for a letter to {}!".format(name))
        except KeyError:
            print("{} is not in your database!".format(name))
    else:
        send_letters(donor_db)
        print("Check your local directory for letter files!")
    press_enter_to_continue()
    return donor_db


def press_enter_to_continue():
    """ Prompt user to press enter to continue
    :return: nothing
    """
    input("Press 'Enter' to Continue\n")


# Switch function dictionary for main menu
switch_func_dict = {
    1: write_letter,
    2: send_letter_choice,
    3: print_report,
    4: close_app
}


# Main Body of Script  ---------------------------------------------------- #
if __name__ == '__main__':
    welcome_message()
    while True:
        menu_options()
        try:
            choice = int(prompt_menu_option())
            donor_dict = switch_func_dict.get(choice)(donor_dict)
        except ValueError:
            print("Please choose a number from the menu")
            press_enter_to_continue()
        except TypeError:
            print("Please enter a choice between 1-4")
            press_enter_to_continue()
