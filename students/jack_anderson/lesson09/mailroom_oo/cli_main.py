#!/usr/bin/env python

"""
Jack Anderson
03/10/2020
UW PY210
Lesson 09

Client for the mailroom program. Handles all user-interactions and sends them to the Donor and DonorCollection classes
"""

from donor_models import *
import sys
import datetime


# Menu options
action = input("Select a number to perform one of the following actions... |\n"
               "1 -- Send a Thank You to a single donor                    |\n"
               "2 -- Create a Report.                                      | \n"
               "3 -- Send a Thank You to all donors                        |\n"
               "4 -- Quit                                                  |\n" \
               + line + '\n:')


# Text for name prompt
name_prompt = "Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors): "

# Text for donation amount prompt
amount_prompt = "Please enter a donation amount: \n"



def quit():
    # Action to exit program gracefully when the quit menu item is selected
    print("Exiting program")
    sys.exit()



def check_input(x):
    """
    Action to validate user input and continually prompt if no response returned by user
    :param x: Text to prompt user
    :return: 'q' directs user to start menu else return input entered by user
    """
    prompt = ""
    while len(prompt) < 1:
        prompt = input(x)
        if prompt.lower() == 'q':
            start()
        else:
            return prompt



def prompt_info(name=None, amount=None):
    """
    Action to continually prompt user for a name and amount until params are not none.
    Action also lists donors if name='list' and checks for valid input of donation.
    :param name: None by default = leave this to continually prompt user name until valid name is entered
    :param amount: None by default = leave this to continually prompt user amount until valid amount is entered
    :return: name == 'list': list of donors, else return user input of donor name and donation amount
    """
    list_donors = DonorCollection().list_donors()
    while name is None:
        name = check_input(name_prompt)
        if name.lower() == 'list':
            print(list_donors)
            name = None
        else:
            while amount is None:
                amount = check_input(amount_prompt)
                try:
                    amount = [float(amount)]
                except ValueError:
                    print("You must enter a numerical value")
                    amount = None
    return name, amount



def send_thanks():
    """
    Send Thanks option calls Donor and DonorCollection classes after prompting user for name and donation.
    Calls to classes will add donor and donation to the donors_dict file, then print a 'thank you'
    letter onscreen displaying donor name and donation amount
    :return: Print out of Thank You letter for a single donor
    """
    dc = DonorCollection()
    name, amount = prompt_info()
    d = Donor(name.title(), amount).thanks_template()
    dc.add_donor(name.title(), amount)
    print()
    print(d)




def create_report():
    """
    Create Report option calls DonorCollection class to list all donors in the donors_dict file in report format, sorted
    by most donated
    :return: Print out of Donor names, total donations, num of donations and avg donation
    """
    dc = DonorCollection()
    header = dc.report_header()
    report = dc.create_report()
    print(header)
    for donors in report:
        print(donors)
    print("=" * 70)




def send_emails():
    """
    Action to call the send_email_all function in the DonorCollection class
    :return: txt files of emails stored in a folder, print out of name of folder emails are stored
    """
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