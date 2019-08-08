#!/usr/bin/env python3

import sys
from donor_models import *

# Initialize a global collection
donor_list = DonorCollection()

def main_menu(prompt, prompt_actions):
    """ Prompt a user to select an action to take, 
    and call the appropriate function """

    # Build a prompt message based on prompt and actions
    prompt_message = prompt
    for item in prompt_actions:
        prompt_message += "\n" + item[0] + " - " + prompt_actions[item]['message']
    prompt_message += "\n> "
    
    # Prompt the user and set the selection
    while True:
        try:
            selection = input(prompt_message)
            if prompt_actions[selection]['action']() == 'quit':
                print("Quitting...")
                quit_program()
        except KeyError:
            print("Please select a valid number...")

def prompt_for_donor():
    """ Prompt for a donor name, list if needed, add if not found """

    while True:
        # Prompt the user for the full name
        full_name = input("Please enter the full name of a donor (type 'list' for current donor names) > ")

        # If the name is 'list' print the full list of names
        if not full_name:
            print("Unable to proceed with input, please enter a donor name...")
        elif full_name.lower() == "list":
            print(donor_list.list_donors())
        else:
            new_donor = Donor(full_name)
            return new_donor

def prompt_for_donation_amount(new_donor):
    """ Prompt for a donation amount and add it for the donor """
    
    while True:
        # Prompt for the amount
        donation_amount = input("Please enter the donation amount > ")
        try:
            float_amount = float(donation_amount)
            zero_check = 1 / float_amount
            break
        except ValueError:
            print("Invalid donation amount, please try again...")
        except ZeroDivisionError:
            print("Donation amount can't be zero, please try again...")

    # Add the donation to the donor's list of donations
    new_donor.add_donation(float_amount)
    #return float_amount

def send_a_thank_you():
    """ Generate a thank you letter for a given donor and amount """

    # Prompt for donor's full name
    new_donor = prompt_for_donor()

    # Prompt for the donation amount
    prompt_for_donation_amount(new_donor)

    # Add donor to collection
    donor_list.add_donor(new_donor)

    # Print out a letter customized for the donor and amount
    print(new_donor.format_thank_you())

def display_report():
    """ Display a summary report """

    # Print the header row
    header_row = "{0:<20} | {1} | {2} | {3}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header_row)
    print("-" * len(header_row))

    # Print the list
    donor_report = donor_list.create_report()
    for donor in donor_report:
        print(f"{donor[0]:<20} ${donor[1]:>13,.2f} {donor[2]:>11} {donor[3]:>13,.2f}")

def send_thank_you_to_all():
    """ Create letters for all donors for their latest donation and save to disk """

    # Loop through the donors, create, and save letters
    temp_dir = "/tmp/"
    for donor in donor_list.donors:
        file_name = temp_dir + donor.full_name + ".txt"
        # Open a file named for the full_name and write the letter
        try:
            with open(file_name, "w") as f:
                f.write(donor.format_thank_you())
                print("Saved letter for {} to {}".format(donor.full_name, file_name))
        except IOError:
            print("Unable to save letter for {} to {}, please check the file path...".format(donor.full_name, file_name))

def quit_program():
    sys.exit



# Run the main program
if __name__ == '__main__':
    # Define dictionary of menu prompt messages and actions
    main_menu_prompt_actions = {
        "1": {"message": "Send a Thank You", "action": send_a_thank_you},
        "2": {"message": "Create a Report", "action": display_report},
        "3": {"message": "Send Thank You to All Donors", "action": send_thank_you_to_all},
        "4": {"message": "Quit", "action": quit}
    }

    # Define the main menu prompt
    main_menu_prompt = """Please enter a number to select the action:"""

    # Initialize the donor list
    initial_donors = {
        "Lana Kane": [2999.99],
        "Cheryl Tunt": [150.20, 98192.10],
        "Cyril Figgis": [819.25, 998.62, 10.50],
        "Pam Poovey": [74926.10, 2675.87, 3289.33],
        "Ray Gillette": [3820.90]
    }
    for donor in initial_donors:
        new_donor = Donor(donor)
        for donation in initial_donors[donor]:
            new_donor.add_donation(donation)
        donor_list.add_donor(new_donor)

    # Display the main menu
    main_menu(main_menu_prompt, main_menu_prompt_actions)