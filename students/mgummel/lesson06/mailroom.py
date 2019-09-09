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

    donor = validate(
        "Please type a donor's full name or type 'list' to view donors\n>>> ").title()

    while donor == "List":
        # Prints a list of donors for the user to view
        print(generate_list(donor_db))
        donor = validate(
            "Type donor's name or 'list' to print names again\n>>>").title()

    donor_db.setdefault(donor, list())
    new_donation = get_donation_amt()
    email_names = add_donation(donor, new_donation)
    single_email = build_template(email_names)

    # Print out template that will be emailed to donor.
    print(single_email)


def generate_list(db_dict):
    names = [key for key in db_dict.keys()]
    name_selection = "\n".join(["{}"] * len(donor_db)).format(*names)
    return name_selection


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


def add_donation(sponsor, donation_amt):
    """
    Finds the donor in the database, adds the donation amount
    to the database. Returns an email string built with the
    turns the donation amount 
    
    :param sponsor: string used to find tuple in database 
    :type sponsor: string
    :param donation_amt: New donation amount to be added
    :type donation_amt: float
    """

    for donor_key in donor_db.keys():
        if sponsor == donor_key:
           donor_db[donor_key].append(donation_amt)
    return (sponsor, donor_db[sponsor])


def build_template(donor_info):
    """
    Builds the email template that will be used to send out to 
    donors. 

    :param d_key: donor key in the donor database for each donor
    :type d_key: string

    """

    past_donations = 0
    donor_values = donor_info[1]
    template_dict = {'donor': donor_info[0], 'donation': donor_info[1][-1]}

    # Build the email template
    email_template = '\n'.join(('\n\nDear {donor},\n',
                                'Thank you for your very kind donation of ${donation:.2f}.\n',
                                'It will be put to very good use.\n',
                                '           Sincerely,',
                                '             -The Team\n'))

    # Add a sentence to the template if the donor has previously donated money
    if len(donor_values) > 1:
        for i in range(len(donor_values) - 1):
            past_donations += donor_values[i]

        donation_string = '\n'.join((f'\nYour past donation amount of ${past_donations:.2f}\n',
                                     'has helped our organization tremendously.\n'))

        line_end = email_template.index(",") + 2

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

    # Compute rows to display in report table
    report_rows = compute_sorted(donor_db)

    # Print out report header
    header = "{:<26}|{:^15}|{:^13}|{:>14}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))

    # Print the rows to the report table
    for sorted_item in report_rows:
        print("{:<27}${:>12.2f}{:>14}   ${:>13.2f}".format(*sorted_item))


def compute_sorted(db):
    """
    Uses the Donor database to generate the rows of data
    that will be printed as a report.
    
    :param db: Database of donors and donations
    :type db: dictionary
    """

    computed_list = [(k, sum(db[k]), len(db[k]), avg(db[k]))
                     for k in db.keys()]
    sorted_list = sorted(computed_list, key=itemgetter(1), reverse=True)
    return sorted_list


def avg(donation_list):
    """
    Calculates the average donation amount per donor.

    :param sum_list: list of donations per donor
    :type sum_list: list
    """

    agg = 0.0
    for single_donation in donation_list:
        agg += single_donation
    return round(agg / len(donation_list), 2)


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
