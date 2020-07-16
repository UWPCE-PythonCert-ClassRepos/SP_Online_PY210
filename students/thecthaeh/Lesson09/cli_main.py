#!/usr/bin/env python3

import sys
from operator import itemgetter
from donor_models import *

"""This module handles the user interaction for mailroom_oo and the main flow.

"""

f = Donor('Frank Miller', 320.00, 100.00, 570.50)
t = Donor('Tess Baker', 1000.00, 540.00)
g = Donor('Grant Hugh', 5000.00)
s = Donor('Sarah Piper', 40.00)
j = Donor('Jim Newton', 1350.00, 1500.00, 5.50)

data = Donor_Collection(f, t, g, s, j)

#the main menu
def options():
    prompt = input("Choose one of the following menu options: \n"
            "1. Send a Thank You letter to a single donor \n"
            "2. Create a Report \n"
            "3. Send letters to all donors \n"
            "4. Quit \n"
            ">>> ")
    return prompt

#exit the program
def quit_program():
    print("Goodbye")
    sys.exit()

#Send a thank you letter to a donor
def send_thanks():
    name = input("If you would like to see a list of current donors, type 'list'.\n"
                "Otherwise, enter the donor's full name.\n>> ")
    
    while name.lower() == 'list':
        print(data.list_all_donors())
        name = input("\nEnter the donor's full name.\n>> ")
        
    if name.lower() == 'quit':
        return
    
    input_donation = input("\nEnter the donation amount.\n>> $")
    while input_donation != 'quit':
        try:
            donor = Donor(name)
            donor.new_donation = float(input_donation)
            break
        except ValueError:
            input_donation = input("\nInvalid entry, try again. \n"
                            "Using only numbers, enter the donation amount. \n>> $")
    
    if input_donation.lower() == 'quit':
        return

    data.add_donor_object(donor)
    print(donor.thank_you)

#display a report
def display_report():
    print(data.report_header())
    print(data.report_data())

#create an update letter for each donor
def send_letters():
    data.donor_letters()
    print("Sending letters to all donors.\n")

def switch_menu():
    menu = {
            '1': send_thanks, 
            '2': display_report,
            '3': send_letters,
            '4': quit_program,
            'quit': quit_program
        }
    
    while True:
        try:
            choice = options()
            menu.get(choice)()
        except TypeError:
            print("\n That is not a valid option.\n"
                  "Please enter a valid option from the menu.\n")

if __name__ == "__main__":
    switch_menu()