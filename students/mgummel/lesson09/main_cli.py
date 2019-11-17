#! /usr/bin/env python3

import sys
import pathlib
from donor_models import Donor, DonorCollection

prompt = "\n".join(("Please choose a number corresponding to the options below:",
                    "1 - Send a Thank You.",
                    "2 - Create a Report.",
                    "3 - Send letters to all donors.",
                    "4 - Quit.",
                    ">>> "))

donor1 = Donor("Elliot Spitzer", 1200.00)
donor2 = Donor("Matt Gummel", 512.00)
donor_collection = DonorCollection(donor1, donor2)

def validate(user_input):
    """
    Validates user input and ensures the program can 
    exit gracefully when the user wants to quit.

    :param user_input: user input from the CLI
    :type user_input: string, float, int
    """
    try:
        valid_response = input(user_input)
    except KeyboardInterrupt:
        quit_program()
    except EOFError:
        quit_program()
    else:
        if valid_response.lower() == "quit":
            quit_program()
    return valid_response


def quit_program():
    """
    Informs the user the program will exit and 
    gracefully exits the program.
    """

    print("The program will now exit.")
    sys.exit()


def send_thank_you():
    """
    Prints a in a nicely formatted message that contains the 
    table/titles that will organize  donor name, the total amount 
    they have donated, the number of donations, and their 
    corresponding average gift amount in a neat formatted manner.
    """

    donor = validate(
        "Please type a donor's full name or type 'list' to view donors\n>>> ").title()

    while donor == "List":
        # Prints a list of donors for the user to view
        print(donor_collection.generate_list_of_names())
        donor = validate(
            "Type donor's name or 'list' to print names again\n>>>").title()

    donor_to_thank = donor_collection.find_donor(donor)
    donation_amt = get_donation_amt()
    
    if donor_to_thank:
        donor_to_thank.add_donation(donation_amt)
    else:
        donor_to_thank = Donor(donor, donation_amt)
        donor_collection.add_donor(donor_to_thank)
        
    print(donor_to_thank.__str__())


def get_donation_amt():
    """
    Accepts user input for a donation amount and 
    returns the donation amount 
    """

    donation = 0

    while donation <= 0:
        donation = validate("What's the new donation amount? \n >>> ")
        try:
            donation = float(donation)
        except ValueError:
            print("Not a valid donation amount!")
            donation = 0
        else:
            if donation <= 0:
                print("Not a valid donation amount!")
    return donation

def create_report():
    """
    Prints a table in a nice formatted way that contains the 
    donor name, the total amount they have donated, the number
    of donations, and their corresponding average gift amount.
    """

    # Print out report header
    header = "{:<26}|{:^15}|{:^13}|{:>14}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))

    # Print the rows to the report table
    formatting = "{:<27}${:>12.2f}{:>14}   ${:>13.2f}"
    collection_data = donor_collection.report_data()
    for donor_data in collection_data:
        print("".join(formatting.format(*donor_data)))


def send_letters():
    """
    Accepts user input for a directory to write templatized
    email documents for each donor.
    """

    location = validate("\n".join(("Please type the directory you want files to be generated.",
                                       "(Hit \'Enter\' to default to the current working directory)",
                                       ">>> ")))
    directory = pathlib.Path(location)
    while not directory.exists():
        location = validate("\n".join(("That's not a valid directory. Please type a valid path.\n",
                                       ">>> ")))
        directory = pathlib.Path(location)

    # Write each file to the chosen directory                    
    donor_collection.letters_to_send(directory)

def main():
    menu = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_letters,
        "4": quit_program
    }


    print("\nWelcome to the Mailroom App!")

    # Check to make sure the response is valid and calls
    # the appropriate function
    while True:
        response = validate(prompt)
        if response in menu:
            menu[response]()
            print("\n")
        else:
            print("Not a valid option!\n\n")

if __name__ == '__main__':
    main()