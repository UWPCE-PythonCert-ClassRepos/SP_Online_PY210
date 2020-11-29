# ------------------------------------------------------------------------ #
# Title: mailroom.py
# Description: Assignment for Lesson04
# KODonnell,10.25.2020,created script
# KODonnell,11.05.2020 added switch dict menu
# KODonnell,11.07.2020 added function to generate letters
# KODonnell,11.10.2020 split file writing functions into multiple funcs
# KODonnell,11.14.2020 updated to *actually* have a dictionary database
# KODonnell,11.22.2020 updated exception handling
# KODonnell,11.29.2020 refactor for unit testing
# ------------------------------------------------------------------------- #
import sys
import os

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
    try:
        total_update = donation + donor_db[name][0]
        num_update = donor_db[name][1] + 1
        average_update = round(total_update/num_update, 2)
        donor_db[name] = [total_update, num_update, average_update]
    except KeyError:
        donor_db[name] = [donation, 1, donation]
    return donor_db


def format_report(donor_db):  # Format data in database
    """
    Format report of donor database
    :param donor_db: (dictionary) with donor information
    :return: donor_db
    """
    report_list = []
    sorted_donor_db = sorted(donor_db.items(), key=lambda x: x[1], reverse=True)  # Sort by total donated
    heading = "| {dn:<20s}\t| {tg:<15s}\t| {ng:<10s} | {ag:<15s}   |".format
    report_list.append(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    report_list.append("-" * 78)
    row = "{dn:<20s} \t {ds:<1s} {tg:>14.2f} \t {ng:>10d} \t {ds2:<1} {ag:>14.2f} ".format
    for i in sorted_donor_db:
        name = i[0]
        report_list.append(row(dn=name, ds="$", tg=donor_db[name][0],
                  ng=donor_db[name][1], ds2="$", ag=donor_db[name][2]))
    return report_list


def generate_one_letter(donor_db):  # Create letter file for one donor
    """
    Write letter for one donor to file
    :param donor_db: (dictionary) with donor information
    :return: donor_db
    """
    name = input("What donor would you like to write to? ")
    try:
        name_list = (name.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(name.title(), donor_db[name.title()][0]))
        print("Check your local directory for a letter to {}".format(name))
    except KeyError:
        print("{} is not in your database!".format(name))
    press_enter_to_continue()
    return donor_db


def generate_all_letters(donor_db):  # Create letter file for all donors
    """
    Generate letter files for all donors in database
    :param donor_db: (dictionary) with donor information
    :return: donor_db
    """
    for i, v in donor_db.items():
        name_list = (i.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(i.title(), v[0]))
    print("Check your local directory for letter files!")
    press_enter_to_continue()
    return donor_db


def generate_letter_choice(donor_db):  # Prompt for letter writing options
    """
    Write letters to text files for every donor in database
    :param donor_db: (dictionary) with donor information:
    :return: donor_db
    """
    file_option = int(input("""
    Okay, let's generate some letter files! You can:
    1. Create a letter for a specific donor
    2. Create letters for all donors \n
    Please select an option (1 or 2): """))
    donor_db = switch_func_letter_dict.get(file_option)(donor_db)
    return donor_db



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
    Option 2: Generate Letters for Donors
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


def print_report(donor_db):  # Generate report based on database
    """
    Print formatted
    :param donor_db: (dictionary) with donor information
    :return: donor_db
    """
    formatted_report = format_report(donor_db)
    for row in formatted_report:
        print(row)
    press_enter_to_continue()
    return donor_db


def close_app(donor_db):
    """
    Print goodonor_dbye message and exit
    :param donor_db: (dictionary) with donor information:
    :return: nothing
    """
    print("Closing the Mailroom Program...Goodonor_dbye!")
    sys.exit()


def new_donation_letter(donor_db):  # Update database
    """
    Add new donation to database and print letter
    :param donor_db: (dictionary) with donor information:
    :return: donor_db
    """
    while True:
        name_string = enter_name().title()
        if name_string.lower() == "cancel":  # Cancel task
            print("Cancelling task...")
            break
        elif name_string.lower().strip() in ["list", "go to list", "show list"]:  # display names
            display_names(donor_db)
        else:
            try:
                donation_amount = enter_donation(name_string)  # Prompt donation amount
                donor_db = add_donation_amount(name_string.strip(" "), donation_amount, donor_db)
                print(letter_text(name_string, donation_amount))
                break
            except ValueError:
                print("Entry failed: Donations must be entered as a number!")
                break
    press_enter_to_continue()
    return donor_db




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


def press_enter_to_continue():
    """ Prompt user to press enter to continue
    :return: nothing
    """
    input("Press 'Enter' to Continue\n")


# Switch function dictionary for main menu
switch_func_dict = {
    1: new_donation_letter,
    2: generate_letter_choice,
    3: print_report,
    4: close_app
}


# Switch function dictionary for letter writing choice
switch_func_letter_dict = {
    1: generate_one_letter,
    2: generate_all_letters
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