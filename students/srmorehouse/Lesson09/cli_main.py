#!/usr/bin/env python3

from donor_models import Donor
from donor_models import DonorCollection
import os
import sys

"""
Steve Morehouse
Lesson 09
"""

prompt = "\n".join(("Welcome to the Mailroom!",
          "Please choose from below options:",
          "1 - Enter a Donation",
          "2 - Create Report",
          "3 - Send letters to all",
          "4 - Exit",
          ">>> "))

def get_donation_amount(donor):
    while True:
        try:
            donation_amount = input("Enter the donation amount")
            if float(donation_amount) > 0:
                donor.add_donation(float(donation_amount))
                print (donor.compose_thank_you ())
                return
            else:
                print("The number you enter must be greater than 0.")
                continue
        except ValueError:
            print('Invalid input. You must enter an amount')


def enter_a_donation(donors):
    donor=''
    while True:
        name = input("Type 'list' to see a list of names, 'quit' to quit, or enter a name: ")
        if name == "list":
            print (donors.list_donors())
            continue
        elif name == "quit":
            return
        else:
            result = donors.donor_exists(name)
            if result is False: # new donor
                donor = Donor(name)
                get_donation_amount(donor)
                donors.add(donor)
                return
            else:
                get_donation_amount(donors.donors[name])
            return


def create_report (donors):
    print (donors.create_report())


def print_report (donors):
    donors.print_report()
    print ('Letters sent.\n')


def exit_program(ignore):
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    prompt_action = {"1" : enter_a_donation,
                     "2" : create_report,
                     "3" : print_report,
                     "4" : exit_program }

    donors = DonorCollection()
    donors.add (Donor('Bill Gates',[1,2]))
    donors.add (Donor('Warren Buffet',[12,22]))
    donors.add (Donor('Jeff Bezos',[199]))
    donors.add (Donor('Mark Zuckerberg',[10.12,20.30,40.44]))
    donors.add (Donor('Melinda Gates',[99.00]))

    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        try:
            prompt_action[response](donors)
        except KeyError:
            print ("try again")

if __name__ == "__main__":

    main()

