#!usr/bin/env python3
# Mailroom OO Exercise created by Niels Skvarch
# This file contains the command line interface

# import modules
from donor_models import Donor, DonorCollections
import os
import sys


menu = ("\n".join(("Welcome to the Mailroom.",
                   "Please choose from below options:",
                   "1 - Add a new contribution and display sample thank you letter",
                   "2 - Display a donor Report",
                   "3 - Create a thank you letter for all donors",
                   "4 - Exit",
                   "--> ")))

"""initialize a "starter" data base of donors"""
data_base = DonorCollections()
d1 = Donor("Bob Johnson")
d1.add_donation(3772.32)
d1.add_donation(512.17)
data_base.add_donor(d1)
d2 = Donor("Fred Billyjoe")
d2.add_donation(877.33)
d2.add_donation(455.50)
d2.add_donation(23.45)
data_base.add_donor(d2)
d3 = Donor("Harry Richard")
d3.add_donation(1.50)
data_base.add_donor(d3)
d4 = Donor("Old Gregg")
d4.add_donation(1663.23)
d4.add_donation(4300.87)
d4.add_donation(10432.0)
data_base.add_donor(d4)
d5 = Donor("Jerry Vars")
d5.add_donation(19.95)
d5.add_donation(653.21)
d5.add_donation(99.45)
data_base.add_donor(d5)


def exit_program():
    """use the sys module to clean-exit the script"""
    print("Good bye")
    sys.exit()


def thanks():
    """Takes input from the user to add an entry to the database of donors and adds a contribution value"""
    while True:
        response = input("\nPlease enter the name of the person donating or type 'List' for a list of donors: ")
        amount = 0
        nl = "\n"
        if response.lower() == "list":
            print_donor_list()
        else:
            normalized_response = response.title()

            target_donor = data_base.get_donor_by_name(normalized_response)
            try:
                amount = float(input("\nPlease enter the amount donated:  "))
            except ValueError:
                print("\nOops! Something went wrong. Please enter a numerical value.")
            target_donor.add_donation(amount)
            if target_donor not in data_base:
                data_base.add_donor(target_donor)
            print(f"Dear {target_donor.name},{nl}" +
                  f"    Thank you for your donation of $ {target_donor.last_donation}. We {nl}" +
                  f"appreciate your contribution.{nl}{nl}    Your total donation amount is now " +
                  f"$ {target_donor.total_donated}.{nl}{nl}" +
                  f"Sincerely,{nl}" +
                  f"Your Charity of Choice"
                  )
            return data_base


def print_donor_list():
    """displays the list of donor objects by name"""
    print(data_base.donor_names)


def run_report():
    """takes in a presorted list and displays it as a grid of information"""
    data_lines = data_base.report_list
    sizes = [0] * len(data_lines[0])
    for line in data_lines:
        for item_index, item in enumerate(line):
            if len(item) > sizes[item_index]:
                sizes[item_index] = len(item)

    for line in data_lines:
        print(line[0].ljust(sizes[0]) + "    $    " + line[1].ljust(sizes[1]) + "    " + line[2].rjust(
            sizes[2]) + "    \t    " + line[3].rjust(sizes[3]))
    print("\n")


def create_thank_you_all():
    """Takes input from the user and runs the create letter module from donor_models.py
    to create thank you letters in the specified directory"""
    custom = input("Press Enter to create the letters in the directory the Mailroom has been run from"
                   " or type 'custom' to specify a directory")
    if custom != "":
        while True:
            custom_dir = input("Please specify a custom directory path:  ")
            if not os.path.exists(custom_dir):
                print("That directory or path does not exist, please specify a valid directory")
            else:
                break
        path = custom_dir
        data_base.create_letters(path)

    elif custom == "":
        path = os.getcwd()
        data_base.create_letters(path)


def main():
    """"main loop for the program to occupy while running, includes the main menu"""
    switch_dict = {"1": thanks, "2": run_report, "3": create_thank_you_all, "4": exit_program}
    while True:
        response = input(menu)
        if response in switch_dict:
            switch_dict[response]()
        else:
            print("Not a valid option!")


# main program name-space
if __name__ == "__main__":
    main()


