# Author: Brian Minsk

# This module contains the sample data, the command line interface code, and
# the main function.

from mailroom_oo import *

donor_data = (("Dee Zaster", (10000.00, 1500.00)),
              ("Owen Money", (7000.00)),
              ("Shanda Lear", (100.00, 900.00, 1500.00)),
              ("Joe King", (500.00, 700.00, 500.00)),
              ("Artie Choke", (1600.00, 1800.00)))

main_prompt = "\n".join(("Please choose an option:",
                         "1 - Send a Thank You",
                         "2 - Create a Report",
                         "3 - Quit",
                         ">>> "))

thank_you_prompt = "\n".join(("Please type a donor name or type 'list' to "
                              "show all the donor names:", ">>> "))

donation_amount_prompt = "\n".join(("Please type the donation amount:",
                                    ">>> "))


def populate_objects():
    """ Load the donor_data into the DonorCollection class.
    """
    dc = DonorCollection()

    for donor in donor_data:
        dc.add_donor(donor[0], donor[1])

    return dc


def create_report(donor_collection):
    try:
        print(donor_collection.report())
    except AssertionError as error:
        print(error.args)


def send_thank_you(donor_collection):
    """ Prompt the user to type a name or type 'list'.
    - If the user types 'list' show a list of the donor names and re-prompt.
    - Check if the donor name the user typed is already in the db.
    - If the user types a name not in the list, add that name to the donor
        db and use it.
    - If the user types a name in the list, use it.
    - Get the donation amount for the donor.

    Compose an email thanking the donor for their generous donation.
    Print the email to the terminal and return to the original prompt.
    """
    donation_amount = None
    donor = None

    while True:
        response = input(thank_you_prompt)
        if response.lower() == "list":
            show_donor_list(donor_collection)
        else:
            donor = process_donor_name_input(donor_collection, response)
            if not donor:
                continue

            donation_amount = add_donation(donor)
            print(donor.thank_you_message())
            break


def show_donor_list(donor_collection):
    """ Print a list of donor names from a DonorCollection object.

    Keyword arguments:
    donor_collection - a DonorCollection object
    """
    donor_list = donor_collection.get_donor_names()
    print("\n".join(donor_list))


def process_donor_name_input(donor_collection, donor_name):
    """ If there is a donor with donor_name already in the db return it.
    If not already in the db:
    - check for a valid name.
    - If the name is not valid inform the user and return None.
    - If the name is valid add a donor with donor_name and return the donor.

    Keyword arguments:
    donor_collection - DonorCollection object
    donor_name - string representing a donor name
    """
    donor = donor_collection.is_existing_donor(donor_name)
    if not donor:  # Donor does not exist
        try:
            Donor.test_name(donor_name)
        except ValueError:
            print('Name should be of the form "Firstname Lastname"')
            return None
        donor = donor_collection.add_donor(donor_name)

    return donor


def add_donation(donor):
    """ Prompt the user for a donation amount and add the donation to the
    matching donor in the donor db. Return the donation amount.

    Keyword arguments:
    donor - item in the donor_db.
    """
    donation_amount = get_donation_amount_from_user()

    donor.donations.add_donation(donation_amount)

    return float(donation_amount)


def get_donation_amount_from_user():
    """ Prompt user for a donation amount, check to see that it is a number,
    and return the amount. If it is not a number, inform the user and prompt
    again.
    """
    while True:
        donation_amount = input(donation_amount_prompt)
        try:
            float(donation_amount)
        except ValueError:
            print("Donation amount should be a plain number and not formatted "
                  "as currency.")
        else:
            return float(donation_amount)


def quit_app(dc=None):
    return "quit"


def main():
    """ Prompt the user to select an option (send a thank you, create a
    report, or quit), which invokes the appropriate function. Except for the
    "quit" response, the others will return to this prompt after finishing.
    """
    dc = populate_objects()

    switch_main_dict = {"1": send_thank_you, "2": create_report,
                        "3": quit_app, "q": quit_app}

    while True:
        response = input(main_prompt)
        response_result = None
        try:
            response_result = switch_main_dict.get(response)(dc)
        except TypeError:
            print("Please type '1', '2', or '3' to select one of the "
                  "available options.")
        if response_result == "quit":
            break


if __name__ == "__main__":
    main()
