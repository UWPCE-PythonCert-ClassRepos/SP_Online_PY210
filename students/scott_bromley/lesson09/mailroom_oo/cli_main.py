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


    elif name not in collection.names:
        new_donor = Donor(name, donation, 1)
        collection.append(new_donor)
        print(new_donor.thank_you())




def add_donor(donor_name):
    """

    :param donor_name:
    :return:
    """
    response = safe_input(f"{donor_name} does not exist.\nWould you like to add the donor? (Y/N): ").toUpper()
    if response == "Y":
        Donor.add








    def should_donor_be_added(name):
        """Verify that user wants to add name input to Collection."""
        response = safe_input(name + " not in database. Add? (Y/N)\n")
        if response in ["N", "n"]:
            return False
        return True


def display_report():
    """
    prints formatted donor report
    :return: None
    """
    print(f"{collection.report()}")


def quit_mailroom():
    """
    quit the mailroom
    :return: 3 (quit option)
    """
    return 3












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




