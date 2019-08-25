#! /usr/bin/env python3

import sys, os
from operator import itemgetter
import pathlib

donor_db = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Marc Benioff": [45023.15, 442.30]
}

prompt = "\n".join(("Please choose from below options:",
                    "1 - Send a Thank You.",
                    "2 - Create a Report.",
                    "3 - Send letters to all donors.",
                    "4 - Quit.",
                    ">>> "))


def quit_program():
    print("The program will now exit.")
    sys.exit()


def send_thank_you():
    donor = "List"
    names = []
    while donor == "List":
        donor = input(
            "Please type a donor's full name or type 'list' to view donors. \n >>> ").title()

        if donor == "Quit":
            quit_program()
        elif donor == "List":
            for key in donor_db.keys():
                names.append(key)
            print("\n".join(["{}"] * len(donor_db)).format(*names))
        elif donor not in names:
            donor_db.setdefault(donor, list())

    new_donation = add_donation(donor)
    print(new_donation)


def add_donation(new_sponsor):
    donation = float(input("What's the new donation amount? \n >>> "))
    if donation <= 0:
        quit_program()

    for donor_key in donor_db.keys():
        if new_sponsor == donor_key:
            donor_db[donor_key].append(donation)

    template_dict = {'donor': new_sponsor, 'donation': donation}
    email_template = '''Dear {donor},

        Thank you for your very kind donation of ${donation:.2f}.

        It will be put to very good use.

                       Sincerely,
                          -The Team\n\n'''
    return email_template.format(**template_dict)


def create_report():
    create_header()
    sorted_list = []
    computed_list = []

    for k in donor_db.keys():
        total_donation, avg_donation, num_of_donations = compute_donation(
            donor_db[k])
        computed_list.append(
            (k, total_donation, num_of_donations, avg_donation))
    sorted_list = sorted(computed_list, key=itemgetter(1), reverse=True)

    for sorted_item in sorted_list:
        print("{:<27}${:>12.2f}{:>14}   ${:>13.2f}".format(*sorted_item))


def create_header():
    header = "{:<26}|{:^15}|{:^13}|{:>14}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))


def compute_donation(list_of_donations):
    total_amount = 0
    donation_num = 0

    for amount in list_of_donations:
        donation_num += 1
        total_amount += amount

    total_amount = round(total_amount, 2)
    avg_amount = round(total_amount / donation_num, 2)

    return total_amount, avg_amount, donation_num


def send_letters():
    translate_dict = {ord(" "): "_", ord(","): None}
    directory = pathlib.Path("")

    while True:
            location = input("\n".join(("Please type the directory you want files to be generated.",
                                        "(Hit \'Enter\' to default to the current working directory)",
                                        ">>> ")))
            if location == "quit":
                quit_program()
            directory = pathlib.Path(location)
            if directory.exists():
                break
            else:
                print("That's not a valid directory. Please try again.")
                directory = pathlib.Path("")

    for key_item in donor_db.keys():
        filepath = directory / key_item.translate(translate_dict)

        with open(f'{filepath}.txt', 'w', encoding='utf-8') as email:
            email_template = '''Dear {},

                Thank you for your very kind donation of ${:.2f}.

                It will be put to very good use.

                       Sincerely,
                          -The Team'''.format(key_item, donor_db[key_item][-1])
            email.write(email_template)

def main():
    menu = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_letters,
        "4": quit_program
    }

    print("Welcome to the Mailroom App!")

    while True:
        response = input(prompt)
        if response in menu:
            menu[response]()
        else:
            print("Not a valid option!\n\n")


if __name__ == '__main__':
    main()
