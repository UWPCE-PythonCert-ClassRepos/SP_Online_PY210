#!/usr/bin/env python
# mailroom_pt4.py, Python 210, Lesson 06


import sys
from operator import itemgetter
import time


def gather_all_donors():
    '''Compiles a list of all donors in the database.'''
    donor_name = [name for name, donations in donors.items()]
    send_thank_yous(donor_name)


def summarize_donations():
    '''
    Summarizes contribution total, frequency and average grouped by donor name.
    Output is referenced by the send_thank_you and create_report functions.
    '''
    summary = []
    for name, donation in donors.items():
        total = sum(donation)
        num_of_donations = len(donation)
        average = round((total / num_of_donations), 2)
        summary.append([name, total, num_of_donations, average])
    return summary


def send_thank_yous(donor_name):
    '''
    Generates thank you letter in text file format in current working directory. References the output of summarize_donations to get donor name and total donation amount.
    '''
    for entry in summarize_donations():
        if entry[0] in donor_name:
            print(f'\nGenerating email to {entry[0]}')
            name = entry[0]
            name.replace(' ', '_')
            outfile = (name + '_thank_you.txt')
            with open(outfile, 'w') as f:
                f.write(f"Dear {entry[0]},\n Thank you for your generous donations in the amount of ${entry[1]:.2f} to the Children's Hospital. Many children will benefit from your contribution.\n With gratitude, \n Seattle Childrens.")
        time.sleep(1)
    print('\nReturning to main menu...\n')
    time.sleep(1)
    return


def create_report():
    '''
    Returns a formatted version of the summarize_donation function to the user, sorted in ascending order by name.
    '''
    sort_summary = sorted(summarize_donations(), key=itemgetter(1), reverse=True)
    print("|  {:<26s}|{:^15s}|{:^15s}|{:^15s}|".format("Donor Name", "Total Given",
                                                       "Num Gifts", "Average Gift"))
    print('-' * 78)

    for i in sort_summary:
        print(f'|  {i[0]:26}| ${i[1]:12.2f} |{i[2]:^15}| ${i[3]:12.2f} |')


def verify_donor_info():
    '''
    Triggered by user selection to thank an individual donor.
    Inputs
        donor_name (required)
        donation_amt (optional)
    Input is compared to names in the donor database. If donor does not exist, asks user if they would like to add a donation for the donor. If yes, asks user for donation amount, and appends information to the database. If no, returns user to initial function prompt.
    '''
    while True:
        donor_name = input('''\nEnter the donor's full name. Enter 'list' to see the complete donor list. Enter 'home' to return to the main menu.
            ''')
        donor_name = donor_name.title()

        if donor_name == 'Home':
            print('\nReturning to main menu...\n')
            main_menu()
        elif donor_name == 'List':
            print(list(donors))
        else:
            for name, donations in donors.items():
                if name in donor_name:
                    send_thank_yous(donor_name)
                    return
                else:
                    print('\nDonor not found in donor list. Add donation?')
                    while True:
                        response = input('Enter yes or no\n')
                        response = response.lower()
                        if response == 'yes':
                            add_donation(donor_name)
                        elif response == 'no':
                            verify_donor_info()
                        else:
                            print('Please enter yes or no.\n')
                        return response


def add_donation(donor_name):
    '''
    Adds a donation to the database
    Inputs:
        donor_name (function argument)
        donation_amount (function prompt)
    After donation is entered, generates a thank you letter to donor.
    '''
    while True:
        try:
            donation_amt = float(input('\nEnter a donation amount\n'))
        except ValueError:
            print('\nPlease enter a dollar amount.\n')
        else:
            if donors.get(donor_name):
                donors[donor_name].append(donation_amt)
            else:
                donors[donor_name] = [donation_amt]
            send_thank_yous(donor_name)
            return donor_name


def exit_program():
    ''' Close out of program '''
    sys.exit()


def menu_switch(argument):
    '''
    Main menu switch used to control program flow.
    '''
    switcher = {
        1: verify_donor_info,
        2: gather_all_donors,
        3: create_report,
        4: exit_program,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    return func()


def main_menu():
    '''
    Main menu executes on program launch. Asks the user to select a menu option and action is implemented using the menu_switch function to complete specified action.
    '''

    while True:
        print('''Main Menu, select an option:
              [1] - Thank individual donor.
              [2] - Thank all donors.
              [3] - Create a report summarizing donations.
              [4] - Quit program.
              ''')
        try:
            selection = int(input("Please select an option from above (1-4)\n"))
        except ValueError:
            print('''\nSorry, I didn't understand that. Please enter an integer
            between 1 and 4.\n''')
            # better try again... Return to the start of the loop
        menu_switch(selection)


if __name__ == '__main__':

    donors = {'Bill Gates': [9999.99, 1234.56, 6543.21],
              'Paul Allen': [1500, 1750],
              'Steve Jobs': [5000, 350.75, 4000],
              'Jeff Bezos': [75.75, 25.25, 50.50],
              }

    main_menu()
