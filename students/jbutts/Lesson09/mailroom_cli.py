#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tempfile
import mailroom_oo as mr



def switcher(arg):
    #  Use a switcher dictionary as a way to present a menu-driven interface for users

    # Use a dictionary as a switch statement!
    switcher = {
        1: record_contribution,
        2: donors.show_donors,
        3: donors.send_letter_to_all,
        4: exit,
    }
    func = switcher.get(arg, lambda: print("Invalid Entry"))
    func()





def print_menu():
    '''
    Print a menu to the user's screen
    '''
    return ''.join((
        "\nMain Menu",
        "\n======================",
        "\n1. Send Thank You",
        "\n2. Create a Report",
        "\n3. Send letters to all donors"
        "\n4. Quit",
        "\n\nEnter Selection (1-4) >>> "
    ))

def record_contribution():
    '''
    Prompt user for new contribution for a new or existing donor. Return dictionary with any updates

    add_contribution() actually updates the dictionary, it's called from here if we have valid data.
    '''


    donor_name = ""
    amount = ""

    while donor_name == "" or donor_name == 'list':
        donor_name = input("Please enter donor full name or type 'list': ")
        if donor_name == 'list':
            print(donors.list_donors())
        else:
            amount = float(input("Please enter donation amount: "))
    else:
        if donors.donor_db.get(donor_name):
            donors.add_contribution(donor_name, amount)  # Add the contribution
            print(donor.format_email(donor_name, amount, sum(donors.donor_db[donor_name])))  # print mail
            #  to terminal
        else:
            response = str(input("Donor {} doesn't exist, add them (y/n)?:".format(donor_name)))
            if response.lower() == 'y':
                donors.add_contribution(donor_name, amount)
                print(donor.format_email(donor_name, amount, sum(donors.donor_db[donor_name])))
    # return donor_db

def main():
    '''
    main loop, continually present users with menu options
    '''


    while True:
        switcher(int(input(print_menu())))



if __name__ == '__main__':
    # We're not getting imported, run main():
    # donor_db = {}  # dict that contains user/donation records
    donors = mr.Donors()
    donor = mr.Donor()
    donors.populate_data
    main()
else:
    # donor_db = {}
    donors = mr.Donors()
    donor = mr.Donor()
    donors.populate_data