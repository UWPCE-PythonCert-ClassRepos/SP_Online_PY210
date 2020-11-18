#!/usr/bin/env python3
# PY210 Lesson 09 MailRoom 4 Interactive Client - Chase Dullinger

import sys
import donor_models
donor_collection = donor_models.DonorCollection()


def get_send_thank_you_prompt():
    """Display menu and return selection for send thank you screen.
        :param: None
        :return: Input object
    """
    return input("Enter name of donor or type 'list' for list of current donors.\
'back' returns to main menu'> ")


def show_donor_list(*args):
    """Displays the list of current donors to the console
    :param: None, *args is an unused dummy param
    """
    print(donor_collection.get_donor_list_text())


def get_send_thank_you_selection():
    """Returns a selection dictionary for send thank you screen"""
    return {"list": show_donor_list}


def send_thank_you():
    """Selection to enter a donation and/or add a donor and then generate a
    thank you letter.
        :param: None
        :return: None
    """
    while True:
        user_input = get_send_thank_you_prompt()
        if user_input == "back":
            break
        get_send_thank_you_selection().get(user_input,
                                           get_donation_info)(user_input)


def get_donation_info(donor):
    """Gets the donation amount for a donor"""
    if donor not in donor_collection.donor_names:
        add_response = input(f"{donor} is not in the database - add? Y/N> ")
        if add_response.lower() == "y" or add_response.lower() == "yes":
            donor_collection.add_donor(donor)
        else:
            send_thank_you()  # Retry adding with the same donor

    response = input(f"Enter donation amount for {donor} .\
     'back' returns to main menu> ")
    if response == 'back':
        return

    try:
        response = float(response)
    except ValueError:
        print("Please enter a numeric value for donation amount")
        get_donation_info(donor)  # Retry adding with the same donor
        return

    if response < 0:
        print("Please enter an positive amount")
        get_donation_info(donor)  # Retry adding with the same donor

    donor_collection.add_donation_to_donor(donor, response)

    email_text = donor_collection.get_donor_by_name(donor).compose_email()
    print(email_text)


def display_report():
    """Print out the donor report"""
    print(donor_collection.create_report())


def create_all_letters():
    """Writes letters for all donors and saves them to disk"""
    donor_collection.create_all_letters()


def save_donor_db():
    """Saves all donor information to disk"""
    donor_collection.save_donor_db()


def read_donor_db():
    """Reads all donor information from disk"""
    donor_collection.read_donor_db()


def quit_program():
    """Cleanly exit the program"""
    sys.exit()


def get_main_prompt():
    """Display menu and return selection.
        :param: None
        :return: Input object
    """
    return input("Select an action:\n\
    1) Send a thank you\n\
    2) Create a report\n\
    3) Send letters to all donors\n\
    4) Save donor database to disk\n\
    5) Read donor database from disk\n\
    6) Quit the program\n\
    \n\
Enter number you wish to choose > ")


def get_main_selection():
    return {"1": send_thank_you,
            "2": display_report,
            "3": create_all_letters,
            "4": save_donor_db,
            "5": read_donor_db,
            "6": quit_program}


def invalid_entry():
    """Informs user of invalid menu selection"""
    print("\nInvalid Entry\n")


def create_menu(prompt, selection_dict):
    """Creates a menu given a prompt and a selection dictionary
    :param prompt: input object with get_prompt
    :param selection_dict: dictionary object user input as keys and methods as
                           values
    """
    user_input = prompt()
    selection_dict.get(user_input, invalid_entry)()


def main():
    """ Main menu
        :param: None
        :return: None
    """
    while True:
        create_menu(get_main_prompt, get_main_selection())


if __name__ == "__main__":
    main()
