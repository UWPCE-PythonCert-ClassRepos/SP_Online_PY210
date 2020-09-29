#!/usr/bin/env python
"""
Command line interface code for mailroom assignment.
"""
import os
from donor_model import Donor, DonorCollection

# Mailroom functions
def prompt_user():
    prompt = "\n".join(('What would you like to do?',
                        '1: Send thank you note to a single donor.',
                        '2: Create report.',
                        '3: Send thank you letters to all donors.',
                        '4: Quit.',
                        '>>> '))
    UserAction = input(prompt)
    return UserAction


def send_letters(DonorRecord):
    DonorRecord.send_letters()


def print_report(DonorRecord):
    if DonorRecord.donors:
        lines = DonorRecord.create_report()
        report = "\n".join(lines)
        print(report)
        print("\n")
    else:
        print('\nNo donor data available.\n')


def send_thank_you_note(DonorRecord):
    donor_name = input('Enter the donors full name: ')
    donor_name = donor_name.strip().title()
    donation_amount = input('Enter donation amount: ')
    DonorRecord.add_donation(donor_name, donation_amount)
    donor = DonorRecord.get_donor(donor_name)
    thank_you = donor.create_thank_you_note()
    print(thank_you)


def quit(DonorRecord):
    print('Goodbye')
    os.sys.exit()


def mail_room():
    print('------------Welcome to the Mailroom :)------------')

    options_dict = {
        '1': send_thank_you_note,
        '2': print_report,
        '3': send_letters,
        '4': quit}

    DonorRecord = DonorCollection()

    while True:
        UserAction = prompt_user()

        try:
            options_dict.get(UserAction)(DonorRecord)
        except TypeError:
            print('Not a valid option....\n')

    return None


# Main Interaction
if __name__ == "__main__":
    mail_room()