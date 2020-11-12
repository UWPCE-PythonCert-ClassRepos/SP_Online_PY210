#!/usr/bin/env python3
import sys
from donor_models import *

dc = DonorCollection()

# Main options menu for user to pick from
def main():
    while True:
        menu()  # Display each option to the user
        options()

# Menu of options for the user in the script
def menu():
    print("Mailroom Program started...", "\n")
    print("You have 4 options to choose from: ", "\n"
        "1) Send Thank you", "\n"
        "2) Create Report", "\n"
        "3) Send a Thank you note to all donors", "\n"
        "4) Exit", "\n"
          )

def options():
    try:
        choice = int(input("What would you like to do? "))
        # Using a dictionary for a switch case
        switch_func_dict = {
            1: thank_you,
            2: get_report,
            3: all_letters,
            4: quit
        }
        switch_func_dict.get(choice)()
    except ValueError as error_message:
        print(error_message)
    except TypeError:
        print("Not a valid option, please select again.")

# Ask for a donor name and donation amount, send an email to that donor once completed
def thank_you():
    name = input("Enter a first and last name (type 'list' to see existing donors): ").title()
    if name.lower() == "list":
        print(dc.list_donors())
        return thank_you()
    elif name.lower() in ("quit", 'q'):
        return
    try:
        gift = float(input("Enter a donation amount: "))
    except ValueError as error_message:  # Catch if the user doesn't input a number
        print(error_message)
    # If donor is in the list, append the donation to the donor's history
    if name == dc.check_donor(name):
        dc.add_donation(name, gift)
    else:
        dc.add_donor(name, gift)

    d = Donor(name)  # Instantiate the Donor Class for a single donor
    # Thank you email to the donor sent to console
    print(d.thank_you_letter(name, gift))

# Show a list of current donor's in the list and sorted by total number of donations
def get_report():
    report = dc.create_report()
    for line in report:
        print(line)

# Create a text file thank you letter named after all donors in the list
def all_letters():
    dc.all_letters()
    print("All Thank You letters created for Donors.")

# Exit the program
def quit():
    print("Ending Program...")
    sys.exit()

# Start the program with the main menu for the user to interact with
if __name__ == "__main__":
    main()