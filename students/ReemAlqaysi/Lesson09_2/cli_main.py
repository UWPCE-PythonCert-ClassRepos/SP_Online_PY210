#!/usr/bin/env python3

import sys, os
from datetime import datetime
from donor_models import Donor, DonorCollection

# Mailroom functions
def prompt_user():
    prompt = "\n".join(("Welcome to the MailRoom!",
        "Please Choose an action:",
        "1 - Send a Thank You to a single donor.",
        "2 - Create a Report.",
        "3 - Send letters to all donors.",
        "4 - Quit",
        ">>> "))
    response = input(prompt)
    return response


def thank_you_text():
    #Ask for donor name
    while True:
        donor_name = input("Enter the donor name.'list' to get list of donors, or 'q' to quit) ")
        if donor_name.lower() == 'q':
            exit_program()
        # If user types list print donors
        elif donor_name.lower() == "list":
            print('\nCurrent list of donors:\n')
            print('\n'.join(dc.donor_names))
            continue
        else:
            if donor_name not in dc.donor_names:
                answer = input("The donor name is not in the list of donors. "
                               "Do you want to add the donor? Yes or No ")
                if answer.lower() == "yes":
                    name = donor_name
                else:
                    exit_program()
    #Ask for donation amount
        donation_amount = input("Enter the donation amount (or q to quit) ")
        if donation_amount.lower() == 'q':
            exit_program()
        elif float(donation_amount) > 0:
            amount = float(donation_amount)
            dc.update_donor(name,amount)
        else:
            print("The number you enter must be greater than 0.")

        dc.update_donor(name,amount)
        # Generate & print email to screen, return to main program
        email = dc.get_donor(name).generate_email()
        print(email)
        return

def print_formatted_report(report):
    formatted_report = ['',
    'Donor Name                    | Total Donation | Num Donations | Avg Donation |',
    '-------------------------------------------------------------------------------']
    for donor in report:
        donor_name, total, number, average = donor
        formatted_report.append(f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}')
    formatted_report.append('')
    print('\n'.join(formatted_report))

def create_report():
    # Generate, format, and print report data
    report = dc.generate_report_data()
    print_formatted_report(report)


def letter_to_all():
    #send letter to all donors in the current directory
    for name in dc.donor_names:
        filename = name.replace(' ', '_').replace(',', '') + ".txt"
        filename = filename.lower()
        filetext = dc.get_donor(name).generate_email()
        with open(filename,'w+') as output:
            output.write(filetext)
        print("\nLetters {} have been printed and are saved in the current directory".format(filename))

def exit_program():
    #exit the program
    print('Goodbye')
    os.sys.exit()

def main():

    options = {
        '1': thank_you_text,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    }
    while True:
        #if response in options:
        try:
            response = prompt_user()
            options[response]()
        except KeyError:
            print("\n'{}'  is not a valid answer, please select option from 1-4 !. \n >> ".format(response))

if __name__ == "__main__":
    # Create some donor data for running the program from the command line
    dc = DonorCollection()
    donors = ['Charlie Puth', 'Demi Lovato', 'Meghanr Tainor']
    amounts = [[50.00,25.00,100.00], [100.00,50.00,80.00], [200.00,100.00,300.00]]
    for donor, amount in zip(donors,amounts):
        for donation in amount:
            dc.update_donor(donor, donation)
    # Driver for main function
    main()
