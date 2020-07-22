#!/usr/bin/env python3
"""
Purpose: Mailroom Part 1 python certificate from UW
Author: Pirouz Naghavi
Date: 07/03/2020
"""

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]


def main_menu():
    """"This function makes the menu portion of the program work."""
    while True:
        option = input('Please select of the three options: Send a Thank You, Create a Report or Quit.\n'
                       'Type 1 and hit enter if you wish to Send a Thank You\n'
                       'Type 2 and hit enter if you wish to Create a Report\n'
                       'Type 3 and hit enter if you wish to Quit\n'
                       'Please make your selection:\n')
        if option == '1':
            send_thank_you()
        elif option == '2':
            create_report()
        elif option == '3':
            break
        else:
            print('Please only type 1 or 2 or 3 and hit enter. Any other option will not be acceptable.')


def sort_donors(db_list):
    """"This function will sort donors according to their maximum historical donations."""
    db_list.sort(key=lambda item: sum(item[1]), reverse=True)


def create_report():
    """"This function will create a report."""

    # Sort database first
    sort_donors(donor_db)

    # Printing table
    print('{:<30.30s}\t|{:^16.16s}\t|{:^12.12s}\t|{:^16.16s}'
          .format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('------------------------------------------------------------------------------------------------')

    # printing donor table
    for donor in donor_db:
        # printing donor table
        print(
            '{:<30.30s}\t ${:>15.15s}\t{:>12.12s}\t ${:>15.15s}'
            .format(donor[0], format(float(sum(donor[1])), '.2f'), str(len(donor[1])),
                    format(float(sum(donor[1]) / len(donor[1])), '.2f')))
    print('\n')


def print_list_of_donors():
    """"This function will print list of donors."""
    print('{:<30.30s}\t'.format('Donor Name'))
    print('---------------------------------')

    # printing donor names
    for donor in donor_db:
        # printing donor name
        print('{:<30.30s}\t'.format(donor[0]))
    print('\n')


def ask_donation_write_thank_you(donerindex):
    """"This function will write a thank to a donor.

    Args:
        donerindex: Is the index of the donor thank you card will be written to.
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
            donor_db[donerindex][1].append(amount_float)
            print('Dear {},\n'.format(donor_db[donerindex][0]))
            print('Thank you for your latest donation of ${:0.2f}. With this donation your overall donation has reached'
                  ' ${:0.2f}. We are very grateful for all your {} donations, and we appreciate all your support. '
                  'Please do not forget us in future we need because there is still more work that needs to be done and'
                  ' we need your help to accomplish them.\n'.format(amount_float,
                                                                    float(sum(donor_db[donerindex][1])),
                                                                    len(donor_db[donerindex][1])))
            print('Best Regards')
            print('Pirouz Naghavi')
            break


def send_thank_you():
    """"This function will type a thank card to the selected donor."""
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
            donor_names_list = [item[0] for item in donor_db]
            if option in donor_names_list:
                ask_donation_write_thank_you(donor_names_list.index(option))
            else:
                print('The new donor name you entered will be added to the donor table.')
                donor_db.append((option, []))
                ask_donation_write_thank_you(len(donor_names_list))
            break


if __name__ == "__main__":
    # run some unit tests on everything
    main_menu()
