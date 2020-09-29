#!/usr/bin/env python3

from operator import itemgetter

donation_table = {"Bill Gates": [40000.0, 50000.0, 9000.0],
                  "Mark Zuckerberg": [10000.0, 6500.00],
                  "Jeff Bezos": [1000.0, 40000.0, 7500],
                  "Paul Allen": [100000.0, 2000.0],
                  "Jack Ma": [15000.0, 77000.0]
                  }
def main():
    dispatch_dict = {
        "1": send_thank_you,
        "2": create_report,
        "3": send_letters_to_all,
        "4": quit
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
    3 - Send letters to all donors
    4 - Quit
    ''')
    choice = str(input('Which option? [1 to 4] - ')).strip()
    return choice

def send_thank_you():
    """
    send a thank you to donors
    """
    while True:
        donor_name = input("Enter the donor's full name or 'list' to show current donors: ").strip()

        if (donor_name.lower() == 'list'): # list current donors
            print('\nThese are the current list of donors:')
            for name in donation_table:
                print(name, end=" || ")
            print("\n")
        else: # name entered
            donation_amount = float(input('How much to donate? - '))

            new_donor = True
            for name in donation_table: # for exisitng donor
                if (name.lower() == donor_name.lower()):
                    donation_table[name].append(donation_amount)
                    new_donor = False
                    print(donor_name, 'is in the list: updated the record.')
                    break

            if (new_donor): # for new donor
                donation_record = []
                donation_record.append(donation_amount)
                donation_table[donor_name.title()] = donation_record
                print(donor_name, 'is a new donor: donation is added in the list.')

            send_email(donor_name, donation_amount)
            break

def create_report():
    """
    create a summary report of the donation
    """
    summary_table = []
    for donor in donation_table:
        donation_record = donation_table[donor]
        total_given = sum(donation_record)
        average_gift = total_given / len(donation_record)
        summary_table_row = [donor, total_given, len(donation_record), average_gift]
        summary_table.append(summary_table_row)

    # sort the summary table by the index 1 field: total_given
    sorted_summary_table = sorted(summary_table, key=itemgetter(1), reverse=True)

    print()
    print('{:20}| {:>12} |{:>10} |{:>15}'.format('Donor Name', 'Total Given',
                                                 'Num Gifts', 'Average Gift'))
    print('-'*63)
    for row in sorted_summary_table:
        print('{:20} ${:12.2f}  {:>10d}  ${:14.2f}'.format(*row))

def send_letters_to_all():
    """
    generate thank you letters for all donors
    """
    for donor in donation_table:
        file_name = donor.replace(" ", "_") + ".txt"
        total_given = sum(donation_table[donor])
        with open(file_name, 'w') as file_obj:
            file_obj.write('Dear ' + donor + ',\n\n')
            file_obj.write(' '*8 + 'Thank you for your kind donation of ' +
                           f"${total_given:.2f}.\n\n")
            file_obj.write(' '*8 + 'It will be put to good use.\n\n')
            file_obj.write(' '*25 + 'Sincerely\n' + ' '*28 + '-The Team')

def quit():
    input('Press [Enter] key to exit...')
    return "exit menu"

def send_email(name, amount):
    print('\n----------- Email -----------')
    print('Dear', name.title(), ',',
          '\n\nThank you for your generous donation of', f"$ {amount:.2f}.",
          '\n\nSincerely,',
          '\nThe ABC Organization')
    print('----------- Email -----------')

if __name__ == "__main__":
    main()