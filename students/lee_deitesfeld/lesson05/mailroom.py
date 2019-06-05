#!/usr/bin/env python3

import sys
from operator import itemgetter

main_prompt = "\n".join(("Please choose from below mailroom options:",
          "1 - Manage Donors and Donations",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))


sub_prompt = "\n".join(("Please make a selection from the following options",
                        "1 - List the Names of Donors",
                        "2 - Add a New Donation",
                        "3 - Return to Main Menu"
                        ">>> "))

dic_donors = {"Bob Jones": [63.00, 30.00],
             "Sue Smith": [50.00],
             "Joe Grimes": [102.00, 45.00, 70.00],
             "Andrea Funk": [21.00, 21.00],
             "Mickey Mouse": [500.00, 250.00, 100.00]}

def menu_selection(prompt, main_dispatch):
    """Pulls up main menu"""
    while True:
        response = input(prompt)
        try:
            if main_dispatch[response]() == "exit menu":
                break
        except KeyError:
            print("Invalid selection.")

def sub_menu():
    """Pulls up sub menu"""
    menu_selection(sub_prompt, sub_dispatch)

def quit():
    """Quits current menu"""
    print("Quitting this menu")
    return "exit menu"

def report():
    """Creates a report of donors and donation amounts"""
    final_report = [(x, sum(dic_donors[x]), len(dic_donors[x]), (sum(dic_donors[x])/len(dic_donors[x]))) for x in dic_donors]
    final_report.sort(key=itemgetter(1), reverse = True)
    header = ["Name", "Donations Total", "Number of Donations", "Average Donation"]
    print('{:>20} {:>20} {:>25} {:>25}'.format(*header))
    print('---'*35)
    for line in final_report:
        print('{:>20} {:>20.2f} {:>25} {:>25.2f}'.format(*line))

def listof_donors():
    """Corresponds to submenu item List the Names of Donors"""
    for item in dic_donors:
        print(item)

def add_donor():
    """Corresponds to submenu item Add a New Donation"""
    donor_question = input("Please enter the name of a new or existing donor: ")
    donation_amount = input("Please enter donation amount for donor: ")
    try:
        donation_amount = float(donation_amount)
    except ValueError:
        print("Please enter a number.")

    if donor_question in dic_donors:
        dic_donors[donor_question].append(donation_amount)
        email = f'Dear {donor_question}, Thank you for your generous donation of ${donation_amount:.2f}. We hope you will consider donating again!'

    else:
        dic_donors[donor_question] = []
        dic_donors[donor_question].append(donation_amount)
        email = f'Dear {donor_question}, Thank you for your generous donation of ${donation_amount:.2f}. We hope you will consider donating again!'
    print(email)

def email_all():
    """Generates an email to each donor and saves it to a txt file"""
    for donor in dic_donors:
        name_file = donor.replace(' ', '_')
        donation_last = dic_donors[donor][-1]
        donation_last = f'{donation_last:.2f}'
        with open('%s.txt' % name_file, 'w') as f:
            f.write(f"Dear {donor},\n \tThank you for your very kind donation of ${donation_last}.\n \tIt will be put to very good use.\n \t\tSincerely, \n \t\t\t-The Team")
    print("Emails created.")

main_dispatch = {"1" : sub_menu,
                 "2" : report,
                 "3" : email_all,
                 "4" : quit}

sub_dispatch = {"1" : listof_donors,
                "2" : add_donor,
                "3" : quit}

if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
