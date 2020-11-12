#!/usr/bin/env python """
import sys
import tempfile
import os

from datetime import date
today = date.today()

"""Mailroom Part 4"""
""" Updates from Part 3
1. Refactored for testing
"""


# Prompt user to choose from menu of 4 actions:
# Send a Thank You, Create a Report, Send thanks to all donors or quit.

assert_donor_db = {"Cher": [1000.00, 245.00],
            "Drew Barrymore": [25000.00],
            "Charlie Brown": [25.00, 50.01, 100.00],
            "Jack Black": [256.00, 752.50, 10101.00],
            "Sam Smith": [5500.00, 24.00],
            }

donor_db = {"Cher": [1000.00, 245.00],
            "Drew Barrymore": [25000.00],
            "Charlie Brown": [25.00, 50.01, 100.00],
            "Jack Black": [256.00, 752.50, 10101.00],
            "Sam Smith": [5500.00, 24.00],
            }

default_folder = "thank_you_cards"


def get_input(prompt):
    response = input(prompt)
    return response


def sort_key(donors):
    #  sort by total donations
    return sum(donors[1])


def list_donors():
    return list(donor_db)


def add_donor(donator, donation):
    """      Add new donor with donation
    """

    donor_db[donator] = []
    donor_db[donator] = donor_db[donator] + [donation]


def update_donor(donator, donation):
    """      update donor with new donation
    """

    donor_db[donator] = donor_db[donator] + [donation]


def get_letter_text(donation_dict):
    """Get letter text for file content"""

    formatted = 'Dear {name},\
    \n\n\tThank you for your very kind donation of ${donation:,.2f}.\
    \n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\
    \n\t\t\t   -The Team'.format(**donation_dict)

    return formatted


def create_card(donator, amount, fldr):
    """
    Create thank you note for passed user
    """

    donation_dict = {}
    donation_dict['name'] = donator
    donation_dict['donation'] = float(amount)

    ty_text = get_letter_text(donation_dict)

    file_name = donation_dict['name'].replace(' ', '_') + '.txt'
    file_path = os.path.join(fldr, file_name)

    try:
        with open(file_path, 'w+') as f:
            f.write(ty_text)
            print(ty_text)
    except IOError:
        print(f"IOError: Error writing to file: {write_path}")

    print(f"\n** Thank you note to {donation_dict['name']} for ${donation_dict['donation']:,.2f} written to {write_path}.  **\n")


def get_donor_name():
    donor_prompt = "\n".join(("\nEnter Full name of donor",
                        "  or Enter list to show current donors",
                        "  or 'q' to return to main menu",
                        "  Please enter donor name:"
                        " > "))
    in_name = get_input(donor_prompt)
    return in_name.title()


def send_ty(donors):
    ''' Send thank you to selected donor '''

    donation = []

    while True:
        donor_name = get_donor_name()

        if donor_name.lower() == 'list':
            donor_names = list_donors()
            print('\n')
            for donor_name in donor_names:
                print(f'   * {donor_name}')
            print('\n')
        elif donor_name.lower() == "q":
            break
        elif donor_name == '':
            continue
        else:
            donation = get_donation()
            if donor_exists(donor_name):
                update_donor(donor_name, donation)
                create_card(donor_name, donation, write_path)
                break
            else:
                add_donor(donor_name, donation)
                create_card(donor_name, donation, write_path)
                break

    return


def donor_exists(name):
    if donor_db.get(name):
        return True
    else:
        return False


def get_donation():
    while True:
        prompt = "Please enter a valid amount to donate >"
        donation = get_input(prompt)
        if donation == "q":
            return

        try:
            donation = float(donation)
        except ValueError:
            print('ValueError: Please enter a numeric value')
        else:
            if donation > 0:
                break
            else:
                continue

    return donation


def get_report(data_passed):

    report = []
    sorted_donors = dict(sorted(data_passed.items(), key=sort_key, reverse=True))
    for donor in sorted_donors.items():
        count = len(donor[1])
        total = sum(donor[1])
        avg = total/count
        write_row = ('{:25}  ${:13,.2f}   {:11}  ${:12,.2f}'.format(
            donor[0], total, count, avg))
# belarsonQ:  how to get this format converted to string
#        write_row = ('f'{donor:25}  ${total:13,.2f}   {count:11}  ${avg:12,.2f}')
        report.append(write_row)

    return report


def display_report():
    for row in get_report(donor_db):
        print(row)


def display_report_header():
    header = []
    col1 = 'Donor Name'
    col2 = 'Total Given'
    col3 = 'Num Gifts'
    col4 = 'Average Gift'
    # print(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    # print('-'*70)
    header.append(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    header.append('-'*70)
    return header


def create_report(donors):
    """
    Print formatted report of donors and donations
    Sort report by total donations
    """
    report = []

    report_header = [display_report_header()]
    report_body = [display_report()]
    print(report_header)
    print(report_body)


def ask_for_folder():
    global user_folder

    # as creating folders is platform specific, end if not Windows. 
    import platform 

    if not platform.system().lower() == 'windows':
        print(f'Sorry, future development requested but not currently enabled for {platform.system()} platform')
        exit_program(0)

    text = "\n".join(("\n\n\nEnter folder Name or hit enter for default",
                      " >"))
    folder_prompt = get_input(text)

    if folder_prompt:
        user_folder = folder_prompt.replace(" ", "_")
    else:
        user_folder = default_folder

    temp_path = tempfile.gettempdir()
    folder_name = user_folder + '_' + today.strftime("%b_%d_%Y")

    folder_path = os.path.join(temp_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def send_all_ty(donors):
    '''
    Create cards for all donor in dictionary
    Note: revised code to use comprehension in Mailroom Part 3
    '''

    [create_card(donor, donations[-1], write_path) for donor, donations in donor_db.items()]    
    '''
    for donor, donations in donor_db.items():
        donation_current = donations[-1]
        create_card(donor, donation_current, write_path)
    '''
    return


def exit_program(donors):
    print('Thank you')
    sys.exit()


def get_selection():

    menu_prompt = "\n".join(("**  Please Select Valid Option Listed:  **",
                        "       1: Send a Thank You",
                        "       2: Create a Report",
                        "       3: Thanks to All Donors",
                        "       4: Quit",
                        f"       (Folder: {user_folder})",
                        "       Please enter your choice:"
                        " > "))

    response = get_input(menu_prompt)

    return response


if __name__ == '__main__':

    try:
        response = ''
        write_path = ask_for_folder()
        print(f'writing to file: {write_path}')

        switch_func_dict = {
            '1': send_ty,
            '2': create_report,
            '3': send_all_ty,
            '4': exit_program
        }

        while True:
            response = get_selection()
            try:
                # if response in switch_func_dict:
                # switch_func_dict.get(response, "nothing")()
                # switch_func_dict.get(response, "nothing")(donor_db)
                switch_func_dict[response](donor_db)
                # else:
                #    print("Please enter valid option")
            except KeyError:
                print('Please select a value 1-4')
 
    except KeyboardInterrupt:
        print('\n\nKeyboardInterrupt: Interrupted and Exiting')
        sys.exit(0)
