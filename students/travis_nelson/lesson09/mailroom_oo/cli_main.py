#!/usr/bin/env python

from donor_models import *


def elicit_donor():
    '''Simple input to receive donor name'''
    return input("\nTo whom should we address this Thank You?\n"
                 "(Type 'list' to view existing donors)\n\n").title()


def validate_input_donor(response_str):
    '''Checks response string for certain conditions'''
    try:
        if response_str[0].isalpha():
            if response_str.lower() == "list":
                return "List"
            else:
                return response_str
        else:
            raise TypeError
    except TypeError:
            print("Please enter a correct value.")
            return None


def process_donor(donor_name):
    '''Returns donor name after validating or adding name to donor db'''
    if dc.existing_donor(donor_name):
        print("\nAn existing patron!\n")
        return donor_name
    else:
        print("\nA new donor!\n")
        return donor_name


def list_donors():
    '''Prints names of all donors'''
    print(", ".join(dc.donor_names))


def donor_input_flow():
    '''Continues to ask for valid input until given'''
    while True:
        response = elicit_donor()
        if validate_input_donor(response):
            if response == 'List':
                print("_" * 10 + "\n" + ",\n".join(dc.donor_names))
            else:
                donor_name = process_donor(response)
                return donor_name


def single_thank_you():
    '''Process flow for storing a donation and sending a thank you letter'''
    recipient = donor_input_flow()
    donation = donation_input_flow()
    store_new_donation(recipient, donation)


def elicit_donation():
    '''Simple function to receive donation amount'''
    return input("How much did they donate?\n")


def validate_donation(donation_response_str):
    '''Logic for handling user input donation'''
    while True:
        try:
            if float(donation_response_str):
                print("\nNice!\n")
                return donation_response_str
        except ValueError:
            print("\nJust a number is fine.\n")
            return None


def donation_input_flow():
    '''Asks for valid donation until given'''
    while True:
        response = elicit_donation()
        if validate_donation(response):
            return float(response)


def store_new_donation(donor_name, donation):
    '''Updates donor db with new donation'''
    if dc.existing_donor(donor_name):
        for i in range(dc.number_of_donors):
            if dc.donors[i].name == donor_name:
                old_donor = dc.donors.pop(i)
                old_donor.add_donation(donation)
                print(old_donor.thank())
                dc.add_donor(old_donor)
                return
    else:
        new_donor = Donor(donor_name, donation)
        print(new_donor.thank())
        dc.add_donor(new_donor)


def create_report():
    print(dc.generate_report())


def generate_all_thanks():
    dc.thank_everyone()
    print("Everyone has been thanked!")


def exit_program():
    '''Exits the interactive script'''
    print("\nOk Bye!\n")
    sys.exit()


def launch_user_interface():
    '''Continuously asks the user for next task'''
    prompt = "\n".join(("_________\n",
                        "Welcome to the Donation Station!\n",
                        "Please choose from below options:\n",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit\n\n",))
    arg_dict = {"1": single_thank_you, "2": create_report,
                "3": generate_all_thanks, "4": exit_program}
    while True:
        response = input(prompt)
        try:
            arg_dict[response]()
        except KeyError:
            print("\nNot a valid choice! Try again.\n")

if __name__ == "__main__":
    # kick it off w a pre-populated Donor Collection
    dc = Donor_Collection()
    launch_user_interface()
