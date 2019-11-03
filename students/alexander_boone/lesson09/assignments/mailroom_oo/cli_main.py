#!/usr/bin/env python

from donor_models import Donor, DonorCollection
import sys


def load_donors():
    """Load initial donor data into DonorCollection."""
    donors = ['Arnold Schwarzenegger', 'Lebron James', 'Elon Musk',
              'Walter White', 'Gordon Ramsay']
    donations = [100000, 1000000, 2000000, 500000, 1280000]
    donation_count = [1, 1, 1, 1, 1]
    collection = DonorCollection()
    for i in range(len(donors)):
        collection.append(Donor(donors[i], donations[i], donation_count[i]))
    return collection


def thank_you():
    """Send a thank you email to the specified donor."""
    name = input_donor_name()

    # add new name
    if name not in collection.names:
        if should_donor_be_added(name) is False:
            return None

    # enter donation amount
    donation = input_donation(name)
    if donation is None:
        return None

    # Run for new donor
    elif name not in collection.names:
        new_donor = Donor(name, donation, 1)
        collection.append(new_donor)
        print(new_donor.thank_you())

    # Run for existing donor
    else:
        for donor in collection.donors:
            if donor.fullname == name:
                donor.new_donation(donation)
                print(donor.thank_you())


def input_donor_name():
    """Return donor name to update based on user input."""
    print("Who would you like to send a thank you to?")
    name = 'list'
    while name == 'list':
        name = safe_input("Type 'list' for a list of names or enter a name: ")

        # run if user inputs 'list'
        if name == 'list':
            print(collection.names)
    return name


def should_donor_be_added(name):
    """Verify that user wants to add name input to Collection."""
    response = safe_input(name + " not in database. Add? (Y/N)\n")
    if response in ["N", "n"]:
        return False
    return True


def input_donation(name):
    """Return donation amount from safe input."""
    try:
        donation = float(safe_input("\nEnter a donation amount in USD: "))
    except ValueError:
        print("Input must be a number. The donor won't be added.")
        print("Returning to main menu...")
        return None
    if donation <= 0:
        print("Donation input was 0 or negative. No changes will be made.")
        return None
    return donation


def display_report():
    """Display donor report."""
    print(collection.report())


def safe_input(prompt):
    """Handle EOFError and KeyboardInterrupt exceptions."""

    try:
        response = input(prompt)
    except KeyboardInterrupt:
        print('CTRL-C pressed. Exiting the mailroom...')
        sys.exit()
    except EOFError:
        print('CTRL-Z pressed. Exiting the mailroom...')
        sys.exit()
    else:
        return response


def quit_program():
    """Print exit message and quit the program."""

    exit_message = "Closing the mailroom for the day..."
    print(exit_message)
    sys.exit()


if __name__ == '__main__':
    '''Main Code'''
    collection = load_donors()
    response_dict = {1: thank_you, 2: display_report,
                     3: quit_program}
    response = 0
    while True:
        response = 0

        # display main menu with options
        options = ["1. Send a Thank You to a single donor", "2. Create a"
                   + " Report", "3. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}"
              + f"\n{options[2]}")

        # ask for and run user response
        while int(response) not in response_dict:
            try:
                response = int(safe_input("Enter a number: "))
            except ValueError:
                print('Input must be a number. Enter 1, 2, or 3.')
            else:
                if response not in response_dict:
                    print('Invalid Response. Enter 1, 2, or 3.')
        response_dict.get(response)()
