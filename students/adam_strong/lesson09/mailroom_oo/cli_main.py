#!/usr/bin/env python3

""" Command line interface for the mailroom_oo program,
uses classes from donor_models.py
"""

import donor_models as dm
import sys

main_prompt = "\n".join(("", "Welcome to the donors list",
                             "Please choose from below options:",
                             "1 - Send a thank you",
                             "2 - Create a report",
                             "3 - Send a letter to all the donors",
                             "4 - Quit",
                             "Type a number to select >>> "))

ty_prompt = "\n".join(("", "Please type the full name of the donor OR",
                           "type 'list' to see a list of donors",
                           "Type input here >>>"))

data = dm.DonorCollections(dm.Donor('Scrooge McDuck', [8000.00, 70000.00]),
                           dm.Donor('Montgomery Burns', [49.53]),
                           dm.Donor('Richie Rich', [1000000.00, 500000.00]),
                           dm.Donor('Chet Worthington', [200.00, 44387.63, 10200.00]),
                           dm.Donor('Silas Skinflint', [0.25, 1.00, 0.43]))


# Functions
# 1 - Thank you


def thank_you():
    ''' Main thank_you logic'''
    tyname = input(ty_prompt)
    list_invoked(tyname)
    amt = input("Please enter the donation amount >>>")
    amt_logic(tyname, amt)


def list_invoked(tyname):
    '''Checks if list is entered'''
    if tyname == 'list':
        report()
    else:
        return tyname


def amt_logic(tyname, amt):
    '''Validates the amount entered'''
    try:
        amt = float(amt)
        assert amt > 0
    except (ValueError, AssertionError):
        print('\n--->Not a valid amount, please try your submission again')
    else:
        message = data.add_donor(tyname, amt)
        print(message)


# 2 - Make Report


def report():
    '''Main report logic - prints the returned report'''
    rep = data.make_report()
    for item in rep:
        print(item)

    if __name__ == '__main__':
        main()
    else:
        return


# 3 - Send Letter


def send_letter():
    '''Executes the send_letter code in the donor_models module'''
    data.send_letter()


# 4 - Exit Program


def exit_program():
    '''Exits the program'''
    print('\nShutting down the program\n')
    sys.exit()


# Main interface

def main_switch(response):
    '''Main code logic - Handling input response'''
    try:
        switch_func_dict.get(int(response))()
    except (ValueError, TypeError):
        print('\n----> Invalid Selection: Please input a number 1-4')


switch_func_dict = {
    1: thank_you,
    2: report,
    3: send_letter,
    4: exit_program,
}


def main():
    '''Main code logic'''
    while True:
        response = input(main_prompt)
        main_switch(response)

# Main Code Block --------------------------------------------------------------


if __name__ == '__main__':
    # Guards against running automatically if this script is imported
    main()
