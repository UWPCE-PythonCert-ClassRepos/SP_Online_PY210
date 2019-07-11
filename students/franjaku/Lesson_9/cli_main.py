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


def send_letters(DonorCollection):
    pass


def print_report(DonorCollection):
    lines = DonorCollection.create_report()
    report = "\n".join(lines)
    print(report)


def send_thank_you_note(DonorCollection):
    pass


def quit(DonorCollection):
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
            print('Nota a valid option....\n')

    return None


# Main Interaction
if __name__ == "__main__":
    mail_room()