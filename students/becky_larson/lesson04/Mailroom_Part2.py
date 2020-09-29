#!/usr/bin/env python """
import sys
import tempfile
import os

from datetime import date
today = date.today()

"""Mailroom Part 2"""
""" Updates from Part 1
1. Ask user for temp folder to write notes
2. New option to send cards to all users
3. Tech revision: using dictionary
"""


# Prompt user to choose from menu of 4 actions:
# Send a Thank You, Create a Report, Send thanks to all donors or quit.

donor_db = {"Cher": [1000.00, 245.00],
            "Drew Barrymore": [25000.00],
            "Charlie Brown": [25.00, 50.01, 100.00],
            "Jack Black": [256.00, 752.50, 10101.00],
            "Sam Smith": [5500.00, 24.00],
            }

default_folder = "thank_you_cards"


def sort_key(donors):
    #  sort by total donations
    return sum(donors[1])


def list_donors(donors):
    print(f'\nNumber of Donors found: {len(donors)}\n\n')
    for donor, donations in donors.items():
        print(f'\t{donor}')

    print('\n')
    return (donors)


def add_donation(donors, donator):
    """      Add donation to donor
    """
    prompt = "Please enter an amount to donate >"
    donation = input(prompt)
    donation = float(donation)
    donors[donator] = donors[donator] + [donation]

    return donation


def create_card(donator, amount, fldr):
    """
    Create thank you note for passed user
    """

    donation_dict = {}
    donation_dict['name'] = donator
    donation_dict['donation'] = float(amount)

    ty_text = 'Dear {name},\
    \n\n\tThank you for your very kind donation of ${donation:,.2f}.\
    \n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,\
    \n\t\t\t   -The Team'.format(**donation_dict)

    file_name = donation_dict['name'].replace(' ', '_') + '.txt'
    file_path = os.path.join(fldr, file_name)

    with open(file_path, 'w+') as f:
        f.write(ty_text)

    print(f"\n** Thank you note to {donation_dict['name']} for ${donation_dict['donation']:,.2f} written to {write_path}.  **\n")

    return True


def send_ty(donors):
    ''' Send thank you to selected donor '''

    donation = []

    prompt = "\n".join(("Enter Full name of donor",
                        "  or Enter list to show current donors:",
                        "  Please enter donor name:"
                        " > "))
    response = input(prompt)
    response = response.title()

    if response.lower() == 'list':
        list_donors(donors)
    elif response in donors:
        donation = add_donation(donors, response)
        create_card(response, donation, write_path)
    else:
        donors[response] = []
        donation = add_donation(donors, response)
        create_card(response, donation, write_path)

    return donors


def create_report(donors):
    """
    Print formatted report of donors and donations
    Sort report by total donations
    """

    print("\n** You've selected to create a report.  **\n")
    col1 = 'Donor Name'
    col2 = 'Total Given'
    col3 = 'Num Gifts'
    col4 = 'Average Gift'
    print(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    print('-'*70)

    donors = dict(sorted(donors.items(), key=sort_key, reverse=True))
    for donor, donations in donors.items():
        count = len(donations)
        total = sum(donations)
        avg = total/count
        print(f'{donor:25}  ${total:13,.2f}   {count:11}  ${avg:12,.2f}')
    
    print("\n** Thank you!  **\n")
    return


def ask_for_folder():
    global user_folder

    text = "\n".join(("\n\n\nEnter folder Name or hit enter for default",
                        " >"))
    prompt = input(text)

    if prompt:
        user_folder = prompt.replace(" ", "_")
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
    '''
    
    for donor, donations in donors.items():
        donation_current = donations[-1]
        create_card(donor, donation_current, write_path)
    return donors


def exit_program(donors):
    print('Thank you')
    sys.exit()


def get_selection():

    prompt = "\n".join(("**  Please Select Valid Option Listed:  **",
                        "       1: Send a Thank You",
                        "       2: Create a Report",
                        "       3: Thanks to All Donors",
                        "       4: Quit",
                        f"       (Folder: {user_folder})",
                        "       Please enter your choice:"
                        " > "))

    response = input(prompt)
    
    return response


if __name__ == '__main__':

    response = ''
    write_path = ask_for_folder()    

    switch_func_dict = {
        '1': send_ty,
        '2': create_report,
        '3': send_all_ty,
        '4': exit_program
    }

    while True:
        response = get_selection()
        if response in switch_func_dict:
            switch_func_dict.get(response, "nothing")(donor_db)
        else:
            print("Please enter valid option")
