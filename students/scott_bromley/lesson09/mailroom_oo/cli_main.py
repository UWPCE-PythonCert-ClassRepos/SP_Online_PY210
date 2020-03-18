#!/usr/bin/env python3

from donor_models import Donor, DonorCollection
import sys


def main():
    main_prompt = ("\nPlease enter an option from the following menu\n"
                   "1 - Send a Thank You to a single donor\n"
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
        print('CTRL-C pressed. Exiting mailroom...')
        sys.exit()
    except EOFError:
        print('CTRL-Z pressed. Exiting mailroom...')
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
        print(f"List of donors: {
    else:
        while True:
            try:
                donation = float(get_user_input("Please enter the donation amount: ").strip('$'))
                if bool(donation) is True:
                    break
                else:
                    print(f"Invalid donation, please enter a valid donation.\n")
            except ValueError as donation_err:
                raise donation_err
                continue
        donor_info = (donor_name, donation)
        update_donor(donor_info)
        print(f"{format_thank_you(donor_info)}")

















