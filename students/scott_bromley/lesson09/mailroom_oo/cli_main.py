#!/usr/bin/env python3

from donor_models import Donor, DonorCollection
import sys


def main():
    main_prompt = ("\nPlease enter an option from the following menu\n"
                   "1 - Send a Thank You\n"
                   "2 - Create a Report\n"
                   "3 - Quit\n>> ")
    dispatch = {"1": thank_you, "2": display_report, "3": quit_mailroom}
    menu_selection(main_prompt, **dispatch)


def menu_selection(prompt, **dispatch_dict):
    """
    prompts user for input and calls function object in dispatch_dict
    :param prompt: user input prompt
    :param dispatch_dict: dict of dispatch functions
    :return:
    """
    while True:
        try:
            response = safe_input(f"{prompt}")
        except (TypeError, ValueError) as menu_err:
            print(f"Invalid option {response}\n")
            raise menu_err
        if dispatch_dict[response]() == 3:
            sys.exit()


def safe_input(prompt):
    """
    Prompt user for input; handle forced exit of mailroom
    :param prompt: user prompt
    :return: response
    """
    try:
        response = input(prompt).strip()
    except KeyboardInterrupt:
        print('\nExiting mailroom...')
        sys.exit()
    except EOFError:
        print('\nExiting mailroom...')
        sys.exit()
    else:
        return response


def thank_you():
    """
    prompt user for a donor name; if name exists, prompts for donation, otherwise add name to DonorCollection object;
    'list' displays a list of donors
    print thank you to donor
    :return: None
    """
    donor_name = safe_input("Please enter the name of a donor: ")
    if donor_name == 'list':
        print(f"List of donors: {', '.join([donor for donor in donors.donors])}")
    elif donor_name not in donors.donors:
        add_donor(donor_name)
        add_donation(donor_name)
    else:
        while True:
            add_donation(donor_name)
            continue
        print(f"{donors[donor_name].thank_you()}")


def add_donor(donor_name: str):
    """
    if donor not in DB, add donor; prompt user for initial donation
    :param donor_name:
    :return:
    """
    donor_response = safe_input(f"Donor {donor_name} does not exist, add donor to database (Y/N)?: ").lower().strip()
    if donor_response and donor_response[0] == "y":
        donors.append(Donor(donor_name))
        print(donors)
    else:
        exit()


def add_donation(donor_name: str):
    """
    Prompts user for donation amount; adds to Donor's donations
    :param donor_name:
    :return:
    """
    donation = float(safe_input("Please enter the donation amount: ").strip('$'))
    try:
        donors[donor_name].add_donation(donation)
        print(donors)
    except ValueError as donation_err:
        raise donation_err


def display_report():
    """
    prints formatted report of Donor objects sorted by Donor.total_donations in descending order
    :param collection: collection of Donor objects
    :return: None
    """
    if not donors.donors:
        raise ValueError("DonorCollection is empty")
    donors.report()


def quit_mailroom():
    """
    quit the mailroom
    :return:  (quit option)
    """
    return 3


if __name__ == "__main__":
    print("Running", __file__)
    donors = DonorCollection()
    main()
else:
    print("Running as imported module", __file__)












