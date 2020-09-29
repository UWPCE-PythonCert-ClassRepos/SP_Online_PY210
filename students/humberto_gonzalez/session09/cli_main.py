#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:47:23 2019

@author: humberto
"""

import sys
from donor_models import donorCollection
from donor_models import Donor

#Intializing a donor database
donorA = Donor("Tyrod Taylor")
donorA.add_donation(1000)
donorA.add_donation(50)
donorA.add_donation(15)

donorB = Donor("Philip Rivers")
donorB.add_donation(100)
donorB.add_donation(500)
donorB.add_donation(155)

donorC = Donor("Cam Newton")
donorC.add_donation(200)
donorC.add_donation(540)


mailroom_db = donorCollection()
mailroom_db.add_donor(donorA)
mailroom_db.add_donor(donorB)
mailroom_db.add_donor(donorC)


main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a report",
              "3 - Send letters to all donors",
              "4 - Exit Program",
              ">>> "))

def obtain_donation_info():
    """Prompts user for a donor and donation amount"""
    donor_name = input('What is the full name of the donor you would like to thank? ')
    if donor_name.lower() == "quit":
        main()
    donation = input('What was the donation amount? ')
    try:
        float(donation)
    except ValueError:
        print('Donation amount needs to be a number, please enter a number')
        donation = input('What was the donation amount? ')
    if donation.lower()=="quit":
        main()
    return donor_name, donation

def send_thank_you():
    """Prompts user for a donor and donation amount, and then prints out a thank you email"""
    donor_name, donation = obtain_donation_info()
    new_donor = Donor(donor_name)
    new_donor.add_donation(donation)
    mailroom_db.add_donor(new_donor)
    txt = new_donor.generate_thank_you_note()
    print()
    print()
    print(txt)

def exit_program():
    """
    exits the main program
    """
    print("Bye!")
    sys.exit()

def main():
    while True:
        response = input(main_prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        menu_options = {"1":send_thank_you,
                        "2":mailroom_db.display_report,
                        "3":mailroom_db.send_letters,
                        "4":exit_program}
        try:
            menu_options.get(response)()
        except Exception as e:
            print()
            print("Please select one of the available options")
            print("You will be returned to the main menu")
            continue
        


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
