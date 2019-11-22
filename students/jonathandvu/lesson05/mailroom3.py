#!/usr/bin/env python
# PY210 Lesson 5 Mailroom Assignment
# Jonathan Vu
#
# Properties
import os
from datetime import date

donor_donations = {"Bill Gates": [85, 100],
                   "Jeff Bezos": [65, 25, 55],
                   "Elon Musk": [15, 25],
                   "The Rock": [250, 125, 55],
                   "Kevin Hart": [30]}


# Support Functions
def get_donor_names():
    for x in donor_donations:
        print('{}'.format(x))

def send_a_thank_you():
    print('\n----- Send a Thank You -----')
    prompt = "\n".join(('Please select from the options:',
                        '1: Type in the full name of a donor.',
                        '2: Type in ''list'' to see donors.',
                        '3: Type in a new donor name',
                        '>> '))
    user_action_TY = input(prompt)
    donor_name_list = list(donor_donations.keys())

    if user_action_TY == 'list':
        get_donor_names()
        send_a_thank_you()
    else:
        donation = input('Donation Amount ($): ')
        try:
            donation = int(donation)
        except ValueError:
            print('Enter a numeric value!')
            donation = int(donation)

        if user_action_TY in donor_name_list:
            [donor_donations[user_action_TY].append(donation) for donor in donor_name_list if donor == user_action_TY]
        elif user_action_TY not in donor_donations.keys():
            donor_donations[user_action_TY] = [donation]

        Email_Thanks = '{}, your donation of ${:.2f} is greatly appreciated.'
        print('\n----- Thank YOU! -----')
        print(Email_Thanks.format(user_action_TY, donation))


def create_a_report():
    sorted_keys = sorted(donor_donations.keys())
    report = ["\nDonor Name        | Total Given | # Gifts | Average Gift\n" +
              "------------------------------------------------------------------"]
    for donor in sorted_keys:
        sumation = sum(donor_donations[donor])
        length = len(donor_donations[donor])
        report.append(f"{donor:<15}   ${sumation:>9.2f}   {length:>9d}     ${sumation / length:>10.2f}")
    report = '\n'.join(report)
    print(report)
    return report


def quit_program():
    os.sys.exit()

def send_all_letters():
    for donor, data in donor_donations.items():
        name = donor
        total_donation = sum(data)
        my_date = date.today()
        with open(f"{name}.txt", 'w+') as fileout:
            fileout.write(f"\nToday's Date: {my_date}")
            fileout.write(f"\n------------------------------------\n\n")
            fileout.write(f"Hello {name},\n\n")
            fileout.write(f"Thank your for your kind donation of ${total_donation}. We will use this money for good "
                          f"use! We hope to hear from you soon.\n\n")
            fileout.write(f"Yours Truly, \n\nJon's Team")
        fileout.close()


# User Choices for Main Function
switch_action_dict = {'1': send_a_thank_you,
                      '2': create_a_report,
                      '3': send_all_letters,
                      '4': quit_program}

# Main Function
if __name__ == '__main__':
    var = True
    while var:
        print('\n----- Welcome to the Mailroom -----')
        user_prompt = "\n".join(('Please select from the options:',
                                 '1: Send thank you note',
                                 '2: Create report',
                                 '3: Send letters to ALL donors.',
                                 '4: Quit',
                                 '>> '))
        # Assign value to user input
        user_action = input(user_prompt)
        try:
            # Checks dictionary and gets value for running function
            switch_action_dict.get(user_action)()
        except TypeError:
            print('\n\nThat was an invalid entry. Try again!')
