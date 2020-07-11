#!/usr/bin/env python3

from operator import itemgetter

donation_table = {"Bill Gates": [40000.00, 50000.00, 9000.00],
                  "Mark Zuckerberg": [10000.00, 6500.00],
                  "Jeff Bezos": [1000.00, 40000.00, 7500.00],
                  "Paul Allen": [100000.00, 2000.00],
                  "Jack Ma": [15000.00, 77000.00]
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
    for name in list_donors(donation_table):
        print(name, end=" || ")
    print()


def list_donors(dic):
    return list(dic.keys())


def new_donation():
    donor_name = input("Enter the donor's full name: ").strip()
    while True:
        try:
            donation_amount = float(input('How much to donate? - '))
        except ValueError:
            print("donation amount must be a number; please try again...")
        else:
            break

    update_donation_table(donor_name, donation_amount)
    print(email_text(donor_name, donation_amount))


def update_donation_table(donor, amount):
    new_donor = True
    for name in donation_table:  # for exisitng donor
        if (name.lower() == donor.lower()):
            donation_table[name].append(amount)
            new_donor = False
            print(donor, 'is in the list: updated the record.')
            break

    if (new_donor):  # for new donor
        donation_record = []
        donation_record.append(amount)
        donation_table[donor.title()] = donation_record
        print(donor, 'is a new donor: donation is added in the list.')


def email_text(name, amount):
    return('Dear ' + name.title() + ',' +
           '\n\nThank you for your generous donation of' + f" ${amount:.2f}." +
           '\n\nSincerely,' +
           '\nThe Team')


def to_main_menu():
    return "main menu"


def create_report():
    """ create a summary report of the donation """
    print()
    for row in get_report():
        print(row)


def get_report():
    summary_table = [[donor, sum(record), len(record), sum(record) / len(record)]
                     for donor, record in donation_table.items()]

    # sort the summary table by the index 1 field: total_given
    sorted_summary_table = sorted(summary_table, key=itemgetter(1), reverse=True)

    report = []
    report.append('{:20}| {:>12} |{:>10} |{:>15}'.
                  format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    report.append('-' * 63)
    for row in sorted_summary_table:
        report.append('{:20} ${:12.2f}  {:>10d}  ${:14.2f}'.format(*row))

    return report


def send_letters_to_all():
    """ generate thank you letters for all donors """
    for donor in donation_table:
        file_name = donor.replace(" ", "_") + ".txt"
        total_given = sum(donation_table[donor])
        with open(file_name, 'w') as file_obj:
            file_obj.write(get_letter_text(donor, total_given))


def get_letter_text(name, amount):
    letter_content = []
    letter_content.append('Dear ' + name + ',\n\n')
    letter_content.append(' ' * 8 + 'Thank you for your kind donation of ' +
                           f"${amount:.2f}.\n\n")
    letter_content.append(' ' * 8 + 'It will be put to good use.\n\n')
    letter_content.append(' ' * 25 + 'Sincerely\n' + ' ' * 28 + '-The Team')
    return "".join(letter_content)


def quit():
    input('Press [Enter] key to exit...')
    return "exit menu"


if __name__ == "__main__":
    main()
