#!/usr/bin/env python3

from operator import itemgetter

donation_table = [["Bill Gates", [40000.0, 50000.0, 9000.0]],
                  ["Mark Zuckerberg", [10000.0, 6500.00]],
                  ["Jeff Bezos", [1000.0, 40000.0, 7500]],
                  ["Paul Allen", [100000.0, 2000.0]],
                  ["Jack Ma", [15000.0, 77000.0]]
                 ]
def main():
    while True:
        user_choice = print_menu()
        if (user_choice == '1'):
            send_thank_you(donation_table)
        elif (user_choice == '2'):
            create_report(donation_table)
        elif (user_choice == '3'):
            input('Press [Enter] key to exit...')
            break
        else:
            print('Invalid choice; try again...')

def print_menu():
    """
    Print a menu of choices to the user and ask for the user selection

    :return: string: user selection
    """
    print('''
    Main Menu
    
    1) Send a Thank You
    2) Create a Report
    3) Quit
    ''')
    choice = str(input('Which option? [1 to 3] - ')).strip()
    return choice

def send_thank_you(table):
    """
    send a thank you to donors

    :param table: (list) donation table
    :return: the list is passed by reference and will be
             updated automatically; no explicit return is necessary
    """

    while True:
        donor_name = input("Enter the donor's full name or 'list' to show current donors: ").strip()

        if (donor_name.lower() == 'list'): # list current donors
            print('\nThese are the current list of donors:')
            for row in table:
                print(row[0], end=" || ")
            print("\n")
        else: # name entered
            donation_amount = float(input('How much to donate? - '))

            new_donor = True
            for row in table: # for exisitng donor
                if (row[0].lower() == donor_name.lower()):
                    row[1].append(donation_amount)
                    new_donor = False
                    print(donor_name, 'is in the list: updated the record.')
                    break

            if (new_donor): # for new donor
                new_row = [donor_name, [donation_amount]]
                donation_table.append(new_row)
                print(donor_name, 'is a new donor: donation is added in the list.')

            send_email(donor_name, donation_amount)
            break

def create_report(table):
    """
    create a summary report of the donation

    :param table: (list) donation table
    :return: none
    """

    summary_table = []
    for row in table:
        total_given = sum(row[1])
        average_gift = total_given / len(row[1])
        summary_table_row = [row[0], total_given, len(row[1]), average_gift]
        summary_table.append(summary_table_row)

    # sort the summary table by the index 1 field: total_given
    sorted_summary_table = sorted(summary_table, key=itemgetter(1), reverse=True)

    print()
    print('{:20}| {:>12} |{:>10} |{:>15}'.format('Donor Name', 'Total Given',
                                                 'Num Gifts', 'Average Gift'))
    print('-'*63)
    for row in sorted_summary_table:
        print('{:20} ${:12.2f}  {:>10d}  ${:14.2f}'.format(*row))

def send_email(name, amount):
    print('\n----------- Email -----------')
    print('Dear', name.title(), ',',
          '\n\nThank you for your generous donation of', f"$ {amount:.2f}.",
          '\n\nSincerely,',
          '\nThe ABC Organization')
    print('----------- Email -----------')

if __name__ == "__main__":
    main()