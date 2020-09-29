#!/usr/bin/env python3
from donor_models import  Donor, DonorCollection
import sys

def select_donor(donors):
    #select the donor for the thank you email

    while True:
        answer = input("Which donor to send Thank You to?\n"
                         "(Type 'list' to show list of donors)\n").title()
        if answer.lower() == "list":
            print(donors.list_donors())
        else:
            break
    return answer

def send_thank_you(donors):
    #send a thank you

    #which donor
    patron_name = select_donor(donors)

    #exception handling for user input
    loop = True
    while loop:
        donation = input("How much is the gift?\n")
        try:
            patron_gift = float(donation)
            break
        except ValueError:
            print("\nNot a good value!\n")

    donors.add_donor(patron_name, patron_gift)
    print(Donor(patron_name, donation).send_thank_you())

def create_report(donors):
    print(donors.report())

def quit(donors):
    #quit the program
    sys.exit()

def main():
    donors = DonorCollection()
    #generate the menu
    menu = "\n".join((">",
                        "Please choose from the following:",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Quit",
                        "> "))

    selections = {"1": send_thank_you, "2": create_report,
            "3": quit}

    while True:
        ans = input(menu)
        try:
            selections.get(ans)(donors)
        except TypeError:
            print("Only 1, 2 or 3 is valid!")
            pass

if __name__ == '__main__':
    main()
