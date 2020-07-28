#!/usr/bin/env python3

from donor_models import *


donor = Donor("Bill Gates", [40000.00, 50000.00, 9000.00])
donation_list = [donor]
donor = Donor("Mark Zuckerberg", [10000.00, 6500.00])
donation_list.append(donor)
donor = Donor("Jeff Bezos", [1000.00, 40000.00, 7500.00])
donation_list.append(donor)
donor = Donor("Paul Allen", [100000.00, 2000.00])
donation_list.append(donor)
donor = Donor("Jack Ma", [15000.00, 77000.00])
donation_list.append(donor)

donor_list = DonorCollection(donation_list)

print(repr(donor_list))


def main():

    dispatch_dict = {
        "1": send_thank_you,
        "2": create_report,
        "3": quit
    }
    while True:
        user_choice = print_menu()

        if user_choice not in dispatch_dict:
            print('Invalid choice; try again...')
        elif dispatch_dict[user_choice]() == "exit menu":
            break


def print_menu():
    """
    Print a menu of choices to the user and ask for the user selection

    :return: string: user selection
    """
    print('''
    Main Menu

    1 - Send a Thank You to a single donor
    2 - Create a report
    3 - Quit
    ''')
    choice = str(input('Which option? [1 to 3] - ')).strip()
    return choice


def send_thank_you():
    """ send a thank you to donors """
    dispatch_dict = {
        "list": print_list_donors,
        "1": new_donation,
        "2": to_main_menu
    }

    while True:
        print('''
        <Send Thank you> Sub-Menu

        list - List current donors
        1 - Add a new donation and send email
        2 - Back to main menu
        ''')
        user_input = str(input('Which option? - ')).strip()

        if user_input not in dispatch_dict:
            print('Invalid choice; try again...')
        elif dispatch_dict[user_input]() == "main menu":
            break


def print_list_donors():
    print('\nThese are the current donors:')
    name_list = donor_list.list_donors()
    for name in name_list:
        print(name, end=" || ")
    print()


def new_donation():

    while True:
        donor_name = input("Enter the donor's full name: ").strip()
        existing_donor = donor_list.search_donor(donor_name)
        if existing_donor is None:
            response = input(donor_name + " is not in the database: new donor! "
                                        + "Please confirm (y/n): ")
            if response.lower() == 'y':
                break
        else:
            break

    while True:
        try:
            donation_amount = float(input('How much to donate? - ').strip())
        except ValueError:
            print("Donation amount must be a number; please try again...")
        else:
            if donation_amount > 0:
                break
            else:
                print("Donation must be a positive number; please try again...")

    if existing_donor is not None:  # existing donor
        existing_donor.add_donation(donation_amount)
        print('\n' + existing_donor.email_text())
    else:  # new donor
        new_donor = Donor(donor_name.title(), donation_amount)
        donor_list.add_donor(new_donor)
        print('\n' + new_donor.email_text())


def to_main_menu():
    return "main menu"


def create_report():
    """ create a summary report of the donation """
    print()
    for row in donor_list.get_report():
        print(row)


def quit():
    input('Press [Enter] key to exit...')
    return "exit menu"


if __name__ == "__main__":
    main()
