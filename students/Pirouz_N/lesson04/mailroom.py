#!/usr/bin/env python3
"""
Purpose: Mailroom Part 2 python certificate from UW
Author: Pirouz Naghavi
Date: 07/07/2020
"""

# imports
import datetime

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
    global continue_loop
    continue_loop = False


def main_menu():
    """"This function makes the menu portion of the program work."""
    global continue_loop
    continue_loop = True
    option_dict = {'1': send_thank_you_after_donation, '2': create_report, '3': send_thank_you_to_all, '4': exit_loop}
    while continue_loop:
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
            print('Please only type 1 or 2 or 3 or 4 and hit enter. Any other option will not be acceptable.')


def create_report():
    """"This function will create a report."""
    # Printing table
    print('{:<30.30s}\t|{:^16.16s}\t|{:^12.12s}\t|{:^16.16s}'
          .format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('------------------------------------------------------------------------------------------------')

    # printing donor table
    for donor in donor_db:
        # printing donor table
        print(
            '{:<30.30s}\t ${:>15.15s}\t{:>12.12s}\t ${:>15.15s}'
            .format(donor, format(float(sum(donor_db[donor])), '.2f'), str(len(donor_db[donor])),
                    format(float(sum(donor_db[donor]) / len(donor_db[donor])), '.2f')))
    print('\n')


def print_list_of_donors():
    """"This function will print list of donors."""
    print('{:<30.30s}\t'.format('Donor Name'))
    print('---------------------------------')

    # printing donor names
    for donor in donor_db:
        # printing donor name
        print('{:<30.30s}\t'.format(donor))
    print('\n')


def write_thank_you(donername):
    """"This function will write a thank to a donor.

    Args:
        donername: Is the name of the donor thank you card will be written to.

    """
    letter = 'Dear {},\n\n'.format(donername)
    letter += 'Thank you for your latest donation of ${:0.2f}. With this donation your overall donation has reached'\
        .format(donor_db[donername][len(donor_db[donername]) - 1])
    letter += ' ${:0.2f}. We are very grateful for all your {} donations, and we appreciate all your support. '\
        .format(float(sum(donor_db[donername])), len(donor_db[donername]))
    letter += 'Please do not forget us in future we need because there is still more work that needs to be done and'
    letter += ' we need your help to accomplish them.\n\n'
    letter += 'Best Regards\n'
    letter += 'Pirouz Naghavi'
    return letter


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
            donor_names_list = [item for item in donor_db]
            if option in donor_names_list:
                write_thank_you_with_donation(option)

            else:
                print('The new donor name you entered will be added to the donor table.')
                donor_db[option] = []
                write_thank_you_with_donation(option)

            # Updating the database
            write_db_to_file()
            break


def write_thank_you_with_donation(donername):
    """"This function will write a thank to a donor after a donation.

    Args:
        donername: Is the name of the donor thank you card will be written to.
    """
    while True:

        amount = input('Please enter your donation amount:')

        try:
            amount_float = float(amount)

        except TypeError:
            print('Entered amount cannot be accepted. Please enter a number.')
        except ValueError:
            print('Entered value cannot be accepted. Please enter a number.')
        except:
            print('Entered value cannot be accepted. Please try again.')
        else:
            donor_db[donername].append(amount_float)
            print(write_thank_you(donername))
            break


def send_thank_you_to_all():
    """"This function will type a thank card to all the donors."""
    for db_key in donor_db:
        with open('letters/' + db_key + '_on_' +
                  str(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")) + '.txt', 'w') as output_file:
            output_file.writelines(write_thank_you(db_key))


if __name__ == "__main__":

    # Global main loop condition
    continue_loop = True

    # Populating the dictionary from database
    populate_db_from_file()

    # Running main menu
    main_menu()

    # Updating the database
    write_db_to_file()
