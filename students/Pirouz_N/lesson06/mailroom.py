#!/usr/bin/env python3
"""
Purpose: Mailroom Part 4 python certificate from UW
Author: Pirouz Naghavi
Date: 07/13/2020
"""

# imports
import datetime
import sys
from collections import OrderedDict

donor_db = {}


def write_db_to_file():
    """"This function saves donors to the database in donor_db.txt located at current working sub directory data."""
    with open('data/donor_db.txt', 'w') as output_file:
        for db_key in donor_db:
            output_file.write(('{}: ' + '{}, ' * (len(donor_db[db_key]) - 1) + '{}\n')
                              .format(db_key, *donor_db[db_key]))
            # Or using f string
            # output_file.write(f'{db_key}: {str(donor_db[db_key])[1:len(str(donor_db[db_key])) - 1]}\n')


def populate_db_from_file():
    """"This function reads donors from database in donor_db.txt located at current working sub directory data."""
    try:
        with open('data/donor_db.txt', 'r') as input_file:
            for line in input_file:
                colon_sep_list = line.split(':')
                donor_db[colon_sep_list[0]] = [float(item.strip()) for item in colon_sep_list[1].strip().split(',')]
    except TypeError:
        print('Database data has been corrupted. Please restore a previously functioning backup.')
    except FileNotFoundError:
        print('Database file is no available in the current working directory folder.')


def exit_loop():
    """"This function allows the user to exit main menu using global condition."""
    sys.exit()


def main_menu():
    """"This function makes the menu portion of the program work."""
    option_dict = {'1': send_thank_you_after_donation, '2': create_report, '3': send_thank_you_to_all, '4': exit_loop}

    while True:
        option = input('Please select of the three options: Send a Thank You, Create a Report, send letters to all '
                       'donors, or Quit.\n'
                       'Type 1 and hit enter if you wish to Send a Thank You.\n'
                       'Type 2 and hit enter if you wish to Create a Report.\n'
                       'Type 3 and hit enter if you wish to send letters to all donors.\n'
                       'Type 4 and hit enter if you wish to Quit.\n'
                       'Please make your selection:\n')
        try:
            option_dict[option]()
        except KeyError:
            print(f"Please choose from following options: {' ,'.join(map(str, option_dict))}")


def sort_donors(db_list):
    """"This function will sort donors according to their maximum historical donations."""
    db_list.sort(key=lambda item: sum(item[1]), reverse=True)
    return db_list


def get_report():
    """This function generates a report in the form of a list. Where every row is a list."""

    # Sorting database
    global donor_db
    donor_db = OrderedDict(sort_donors(list(donor_db.items())))

    # Adding column row and separator to the list
    report_list = [
        '\n',
        '{:<30.30s}\t|{:^16.16s}\t|{:^12.12s}\t|{:^16.16s}'
        .format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'),
        '------------------------------------------------------------------------------------------------',
    ]
    # Adding donor rows
    for donor in donor_db:
        # Adding donor row
        report_list.append(
            '{:<30.30s}\t ${:>15.15s}\t{:>12.12s}\t ${:>15.15s}'
            .format(donor, format(float(sum(donor_db[donor])), '.2f'), str(len(donor_db[donor])),
                    format(float(sum(donor_db[donor]) / len(donor_db[donor])), '.2f')))

    # Adding final separator
    report_list.append('\n')
    return report_list


def create_report():
    """"This function will print a report."""

    # Printing donor table
    for line in get_report():
        # Printing donor row
        print(line)


def get_donors_list_report():
    """"This function will generate a table formatted as list where each item is a row on the table is a str."""

    # Adding heading to the report list
    report_list = ['\n', '{:<30.30s}\t'.format('Donor Name'), '---------------------------------']

    # printing donor na
    for donor in donor_db:
        # printing donor name
        report_list.append('{:<30.30s}\t'.format(donor))
    report_list.append('\n')

    return report_list


def print_list_of_donors():
    """"This function will print list of donors."""

    # Printing donors table
    for line in get_donors_list_report():
        # Printing table row
        print(line)


def write_thank_you(donorname):
    """"This function will write a thank to a donor.

    Args:
        donorname: Is the name of the donor thank you card will be written to.

    Raises:
        TypeError: If donor name is not of type str.
        KeyError: If provided donor name is not amongst the keys in the dictionary.

    """

    if not isinstance(donorname, str):
        raise TypeError('Donor name must be of type str.')
    if donorname not in donor_db:
        raise KeyError('Provided donor name is not amongst the donors in the database.')

    letter = 'Dear {},\n\n'.format(donorname)
    letter += 'Thank you for your latest donation of ${:0.2f}. With this donation your overall donation has reached'\
        .format(donor_db[donorname][len(donor_db[donorname]) - 1])
    letter += ' ${:0.2f}. We are very grateful for all your {} donations, and we appreciate all your support. '\
        .format(float(sum(donor_db[donorname])), len(donor_db[donorname]))
    letter += 'Please do not forget us in future we need because there is still more work that needs to be done and'
    letter += ' we need your help to accomplish them.\n\n'
    letter += 'Best Regards\n'
    letter += 'Pirouz Naghavi'
    return letter


def update_donors(fullname):
    """"This function will add to donor_db if fullname is not in amongst the keys.

    Args:
        fullname: Is the name of the donor inputted by the user.

    Raises:
        TypeError: If fullname is not a of type str
    """
    if not isinstance(fullname, str):
        raise TypeError('Inputted value must be of type str.')

    if fullname not in donor_db:
        print('The new donor name you entered will be added to the donor table.')
        donor_db[fullname] = []


def add_donation(donorname, amount):
    """"This function will add donation to donor_db if option is not in amongst the keys.

    Args:
        donorname: Is the name of the donor inputted by the user.
        amount: Is the amount of money donor is donating.

    Raises:
        KeyError: If key is not available in the dictionary.
        TypeError: If amount in not of type float.
        ValueError: If amount is less than 0.0.

    """
    if not (isinstance(amount, float) or isinstance(donorname, str)):
        raise TypeError('Provided amount must be of type float and provided donor name must be of type str.')
    if donorname not in donor_db:
        raise KeyError('Provided donor name does not exist.')
    if amount <= 0.0:
        raise ValueError('Zero or negative amount was entered.')

    donor_db[donorname].append(amount)


def send_thank_you_after_donation():
    """"This function will type a thank card to the selected donor after a donation."""
    while True:
        option = input('Please type in the name of the donor you wish to thank.\n'
                       'If you wish to see the list of all the donors, please type list.\n'
                       'If you wish to add a new donor to the list, please type in their name.\n'
                       'If you wish to return to the main menu please type exit and hit enter.\n'
                       'Please type in your desired option and hit enter:\n')

        if option == 'list':
            print_list_of_donors()

        elif option == 'exit':
            break

        else:
            # Add new user if new user is present
            update_donors(option)

            # Write thank you with donation
            write_thank_you_with_donation(option)

            # Updating the database
            write_db_to_file()
            break


def write_thank_you_with_donation(donorname):
    """"This function will write a thank to a donor after a donation.

    Args:
        donorname: Is the name of the donor thank you card will be written to.
    """
    while True:

        amount = input('Please enter your donation amount:')

        try:
            amount_float = float(amount)

        except TypeError as type_er:
            type_er.extra_info = 'Input value {} was not accepted and raised a type error when converting to float.'\
                .format(amount)
            print('Entered amount cannot be accepted. Please enter a number.', type_er.extra_info)
        except ValueError as value_er:
            value_er.extra_info = 'Input value {} was not accepted and raised a value error when converting to float.'\
                .format(amount)
            print('Entered value cannot be accepted. Please enter a number.',  value_er.extra_info)
        except _ as er_unhandled:
            er_unhandled.extra_info = 'Unhandled exception occurred. Please investigate.'
            print('Entered value cannot be accepted. Please try again.')
        else:

            # Donation is negative
            if amount_float <= 0.0:
                print('Donations must be positive and larger than zero.')
                continue

            # Adding new donation to donor_db
            add_donation(donorname, amount_float)

            # Printing thank you to donor
            print(write_thank_you(donorname))
            break


def send_thank_you_to_all():
    """"This function will type a thank card to all the donors."""
    for db_key in donor_db:
        with open('letters/' + db_key + '_on_' +
                  str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")) + '.txt', 'w') as output_file:
            output_file.writelines(write_thank_you(db_key))


def main():
    """"This is the main function.

    The main function reads data from the database, runs the program, and shuts down the program to and updates the
    database when doing so.

    """

    # Populating the dictionary from database
    populate_db_from_file()

    # Running main menu
    main_menu()

    # Updating the database
    write_db_to_file()


if __name__ == "__main__":
    # Running the main function
    main()
