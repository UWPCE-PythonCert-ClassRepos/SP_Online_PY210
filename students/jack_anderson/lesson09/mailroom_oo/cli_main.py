#!/usr/bin/env python

from donor_models import *
import sys
import datetime


def quit():
    print("Exiting program")
    sys.exit()


def check_input(x):
    prompt = ""
    while len(prompt) < 1:
        prompt = input(x)
        if prompt.lower() == 'q':
            start()
        else:
            return prompt


def prompt_info(name=None, amount=None):
    list_donors = DonorCollection().list_donors()
    while name is None:
        name = check_input(
            "Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors): ")
        if name.lower() == 'list':
            print(list_donors)
            name = None
        else:
            while amount is None:
                amount = check_input("Please enter a donation amount: \n")
                try:
                    amount = [float(amount)]
                except ValueError:
                    print("You must enter a numerical value")
                    amount = None

    return name, amount


def send_thanks():
    dc = DonorCollection()
    name, amount = prompt_info()
    d = Donor(name.title(), amount).thanks_template()
    dc.add_donor(name.title(), amount)
    print()
    print(d)

def create_report():
    dc = DonorCollection()
    header = dc.report_header()
    report = dc.create_report()
    print(header)
    for donors in report:
        print(donors)
    print("=" * 70)


def send_emails():
    dc = DonorCollection()
    dc.send_email_all()
    print("Created emails are stored in the 'outgoing_emails_{date}' folder".format(date=date.today()).replace("-", "_"))

def start():
    """
    Action to prompt user to select various menu items or to close the program. Checks in place to ensure user
    enters a numerical key.
    """
    while True:
        mailroom_start = {1: send_thanks, 2: create_report, 3: send_emails, 4: quit}
        line = "-" * 60
        try:
            print()
            print(line)
            action = input("Select a number to perform one of the following actions... |\n"
                "1 -- Send a Thank You to a single donor                    |\n"
                "2 -- Create a Report.                                      | \n"
                "3 -- Send a Thank You to all donors                        |\n"
                "4 -- Quit                                                  |\n" \
                           + line + '\n:')

            x = int(action)
            try:
                mailroom_start.get(x)()
            except ValueError:
                print("Not a valid option: Please enter a number from 1 to 4")
        except KeyboardInterrupt:
            print()
            return quit()


if __name__ == '__main__':
    start()