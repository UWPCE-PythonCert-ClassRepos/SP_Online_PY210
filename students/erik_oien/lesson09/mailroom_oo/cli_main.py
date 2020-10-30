#!/usr/bin/env python3

import sys 
import os

from donor_models import Donor, DonorCollection

donor_dict = {
    "Nathan Explosion": [39595, 35081, 93295], 
    "Skwisgaar Skwigelf": [37198], 
    "Toki Wartooth": [20037, 32892, 99788],
    "William Murderface": [87470, 86870, 4397],
    "Pickles": [87838, 60282, 26653],
}

donors = DonorCollection.initialize_donor_dict(donor_dict)

def menu():
    while True:
        welcome_input = input(opening_promt)
        try:
            menu_switch[welcome_input]()
        except KeyError:
            print("Invalid option, please choose a number from the list below:")

def thank_you():
    while True:
        donor_name = input(f"Please choose a donor or type list to see previous donors.\n{sub_menu_prompt}")
        past_donor = False
        if donor_name.lower() in ["menu", "quit"]:
            sub_menu_switch[donor_name.lower()]()
        elif donor_name.lower() == 'list':
            print(donors.list_donors())
        else:
            if donors.check_donors(donor_name):
                donation_amount = input("How much was the most recent donation from {}? >>> ".format(donor_name))
                donor = donors.donors[donor_name]
            else:
                print("Looks like this is a new donor, lets add them!")
                donation_amount = input("How much did {} donate? >>> ".format(donor_name))
                donor = Donor(donor_name)
                donors.add_donor(donor)
            donor.add_donation(int(donation_amount))
            print(donors.donors[donor_name].thank_you_letter())
            return False

def create_report():
    donors.report_of_donors()

def thank_all_donors():
    pass

def quit_program():
    print("Bye!")
    sys.exit()  

# using dictionaries for switch satement to go between menus

menu_switch = {
    "1": thank_you,
    "2": create_report,
    "3": thank_all_donors,
    "4": quit_program,
    "quit": quit_program,
}

sub_menu_switch = {
    "menu": menu,
    "quit": quit_program,
}

# prompts for main menu and sub menu

opening_promt = "\n".join(("Welcome to the mailroom!",
                "Please choose from the below options",
                "1 - Send a Thank You",
                "2 - Create a Report",
                "3 - Send letters to all donors",
                "4 - Quit",
                ">>> "))

sub_menu_prompt = "\n".join(("If you would like to return to the menu type menu.",
                    "If you would like to quit please type quit.",
                    ">>> "))


if __name__ == "__main__":
    menu()