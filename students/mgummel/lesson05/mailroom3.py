#! /usr/bin/env python3

import pathlib
import sys
from operator import itemgetter

donor_db = {
    "William Gates, III": [653772.32, 12.17],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Marc Benioff": [45023.15, 442.30]
}

prompt = "\n".join(("Please choose a number corresponding to the options below:",
                    "1 - Send a Thank You.",
                    "2 - Create a Report.",
                    "3 - Send letters to all donors.",
                    "4 - Quit.",
                    ">>> "))


def validate(user_input):
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
    donor = "List"
    names = list()

    while donor == "List":
        donor = validate(
            "Please type a donor's full name or type 'list' to view donors. \n >>> ").title()

        # Prints a list of donors for the user to view
        if donor == "List":
            names = [key for key in donor_db.keys()]
            print("\n".join(["{}"] * len(donor_db)).format(*names))

        # If the user isn't a past donor, the donor gets added
        elif donor not in names:
            donor_db.setdefault(donor, list())

    single_email = single_thank_you(donor)

    # Print out template that will be emailed to donor.
    print(single_email)


def single_thank_you(sponsor):
    """
    Accepts user input for a donation amount, adds the amount
    to the donor database and returns the donation amount 
    in a formatted string.

    :param sponsor: string used to find tuple in database 
    :type sponsor: string
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

    # Append donation amount to the donor's donation list

    for donor_key in donor_db.keys():
        if sponsor == donor_key:
           donor_db[donor_key].append(donation)
    email = build_template(sponsor, donor_db[sponsor])
    return email


def build_template(d_key, all_donations):
    """
    Builds the email template that will be used to send out to 
    donors. 

    :param d_key: donor key in the donor database for each donor
    :type d_key: string

    :param all_donations: all donations a donor has made
    :type all_donations: list
    """

    past_donations = 0
    template_dict = {'donor': d_key, 'donation': all_donations[-1]}

    # Build the email template
    email_template = '''Dear {donor},\n
Thank you for your very kind donation of ${donation:.2f}.\n
It will be put to very good use.\n
                Sincerely,
                   -The Team\n\n'''

    # Add a sentence to the template if the donor has previously donated money
    if len(all_donations) > 1:
        for i in range(len(all_donations) - 1):
            past_donations += all_donations[i]

        donation_string = f'''\nYour past donation amount of ${past_donations:.2f} \n
has helped our organization tremendously.\n'''
        line_end = email_template.index("\n") + 1

        # Insert new sentence regarding past donations
        email_template = email_template[:line_end] + \
            donation_string + email_template[line_end:]

    return email_template.format(**template_dict)


def create_report():
    """
    Prints a table in a nice formatted way that contains the 
    donor name, the total amount they have donated, the number
    of donations, and their corresponding average gift amount.
    """

    create_header()
    computed_list = [(k, sum(donor_db[k]), len(donor_db[k]),
                      avg(donor_db[k])) for k in donor_db.keys()]
    sorted_list = sorted(computed_list, key=itemgetter(1), reverse=True)

    for sorted_item in sorted_list:
        print("{:<27}${:>12.2f}{:>14}   ${:>13.2f}".format(*sorted_item))


def create_header():
    """
    Prints a table in a nice formatted way that contains the 
    table/titles that will organize  donor name, the total amount 
    they have donated, the number of donations, and their 
    corresponding average gift amount in a neat formatted manner.
    """

    header = "{:<26}|{:^15}|{:^13}|{:>14}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))


def avg(donation_list):
    """
    Calculates the average donation amount per donor.

    :param sum_list: list of donations per donor
    :type sum_list: list
    """

    agg = 0
    for single_donation in donation_list:
        agg += single_donation
    return agg / len(donation_list)


def sum(sum_list):
    """
    Calculates the total amount of donations per donor.

    :param sum_list: list of donations per donor
    :type sum_list: list
    """

    total_amount = 0
    for donation in sum_list:
        total_amount += donation
    return total_amount


def write_letters():
    """
    Accepts user input for a directory to write templatized
    email documents for each donor.
    """

    translate_dict = {ord(" "): "_", ord(","): None}
    directory = pathlib.Path("")

    while True:
        location = validate("\n".join(("Please type the directory you want files to be generated.",
                                       "(Hit \'Enter\' to default to the current working directory)",
                                       ">>> ")))
        directory = pathlib.Path(location)
        filepth_dict = {key_item: directory /
                        key_item.translate(translate_dict) for key_item in donor_db.keys()}
        for key, value in filepth_dict.items():
            # Verify that the directory exists for each file before writing to disk
            try:
                with open(f'{value}.txt', 'w', encoding='utf-8') as email:
                    email_template = build_template(key, donor_db[key])
                    email.write(email_template)
            except FileNotFoundError:
                print("That's not a valid directory. Please type a valid location.\n")
                directory = pathlib.Path("")
                break
        else:
            break


def main():
    menu = {
        "1": send_thank_you,
        "2": create_report,
        "3": write_letters,
        "4": quit_program
    }

    print("Welcome to the Mailroom App!")

    while True:
        response = validate(prompt)
        if response in menu:
            menu[response]()
            print("\n")
        else:
            print("Not a valid option!\n\n")


if __name__ == '__main__':
    main()