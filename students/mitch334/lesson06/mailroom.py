"""Lesson 06 | Mailroom Part 4"""

"""You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again,
so you’ve decided to let Python help you out of a jam and do your work for you."""

# The Program: Part 1
# Write a small command-line script called mailroom.py. This script should be executable. The script should accomplish the following goals:
# 1. It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
#    This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
#    You can store that data structure in the global namespace.
# 2. The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.


# The Program: Part 2
# Update your mailroom program to:
# * Use dicts where appropriate.
# * See if you can use a dict to switch between the users selections. see 'Using a Dictionary to switch' for what this means.
# * Convert your main donor data structure to be a dict.
# * Try to use a dict and the .format() method to produce the letter as one big template, rather than building up a big string that produces the letter in parts.

# The Program: Part 3
# Exceptions
# Now that you’ve learned about exception handling, you can update your code to handle errors better, such as when a user inputs bad data.
# Comprehensions
# Can you use comprehensions to clean up your code a bit?

# The Program: Part 4
# Add a full suite of unit tests.
# “Full suite” means all the code is tested. In practice, it’s very hard to test the user interaction, but you can test everything else. Therefore you should make sure that there is as little logic and untested code in the user interaction portion of the program as possible.
# This is a big step; you may find that your code is hard to test. If that’s the case, it’s a good sign that you should refactor your code.
# I like to say: “If it’s hard to test, it’s not well structured.”
# Put in the tests before you make the other changes below. That’s much of the point of tests. You can know that you haven’t broken anything when you refactor!

import os
import tempfile
import datetime

""" Initial donor list with donation history
    Data: Donor Name: [Donation Amount(s)]"""
donors = {"William Gates, III": [100.00, 50.00],
            "Jeff Bezos": [1000.00, 10.00, 500.00],
            "Mark Zuckerberg": [200.00, 20.00, 50.00],
            "Warren Buffet": [600.00, 300.00],
            "Paul Allen": [1000.00]
            }

# Send a Thank You
# If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
# If the user types list show them a list of the donor names and re-prompt.
# If the user types a name not in the list, add that name to the data structure and use it.
# If the user types a name in the list, use it.
# Once a name has been selected, prompt for a donation amount.
# Convert the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
# Add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
# It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.

def donors_list(list_output):
    if list_output == 'list':
        list = '\nDonor List:\n'
        for donor in donors:
            list += '\t' + f'{donor}' + '\n'

    elif list_output == 'db':
        list = '\nDonor Database:\n'
        for name, val in donors.items():
            list += '\t' + f'{name:26}{val}' + '\n'
    else:
        list = ''

    return list


def add_donation(name, amount = None):
    donor_names = [donor for donor in donors]

    if name not in donor_names:
        donors[name] = []

    if amount == None:
        amount = input('Enter donation amount: ')

    try:
        amount = round(float(amount),2)
        donors[name].append(amount)

        # print()
        # print(create_email(name, amount))

    except ValueError:
        print('Error. Enter a valid donation amount.')
        add_donation(name)


def create_email(name, amount):

    return (f'Dear {name},\n\nThank you for the generous donation of ${amount:.2f}.\n\n'
      'Sincerely,\nMatthew Mitchell')


def send_thankyou():

    donor_name = ''
    while donor_name != 'exit':
        donor_name = input('Thank-You Menu:\n'
                            '\tOptions:\n'
                            "\t\tEnter 'list' for donor list\n"
                            "\t\tEnter 'exit' to return to the main menu\n"
                            '\tEnter full name of donor: ')

        if donor_name.lower() == 'list':
            print(donors_list('list'))

        elif donor_name.lower() == 'db':
            print(donors_list('db'))

        elif donor_name.lower() == 'exit':
            break

        else:
            add_donation(donor_name.title())

# Create a Report
# If the user (you) selected “Create a Report,” print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all of each donor’s donations, just the summary info.
# Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below).
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly.
# Your report should look something like this:
#
# Donor Name                | Total Given | Num Gifts | Average Gift
# ------------------------------------------------------------------
# William Gates, III         $  653784.49           2  $   326892.24
# Mark Zuckerberg            $   16396.10           3  $     5465.37
# Jeff Bezos                 $     877.33           1  $      877.33
# Paul Allen                 $     708.42           3  $      236.14

def create_report():
    report = 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
    report += '-'*66 + '\n'

    donors_stats = {k: [sum(v), len(v), sum(v)/len(v) ] for k, v in donors.items()}

    for donor, stat in sorted(donors_stats.items(), key=lambda d: d[1][0], reverse=True):
        report += f'{donor:26} ${stat[0]:>11.2f} {stat[1]:>11.0f}  ${stat[2]:>12.2f}\n'

    print(report)
    return report

# Update mailroom with file writing.
# Goal: Write a full set of letters to all donors to individual files on disk.
# In the first version of mailroom, you generated a letter to a donor who had just made a new donation, and printed it to the screen.
# In this version of your program, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter for each donor, and writes each letter to disk as a text file.
# The letters should each get a unique file name – you can keep it really simple and just use the donor’s name or add a date timestamp for additional uniqueness.
# You want to avoid specifying a hardcoded file path when creating the files

def send_letters():
    now = datetime.datetime.now()
    now = str(now)[:-7].replace(' ','_').replace(':','')

    location = tempfile.gettempdir()
    files = []

    for name, value in donors.items():
        file = location + '\\' + name.replace(' ','-') + '__' + str(now) + '.txt'
        files.append(file)

        with open(file, 'w') as letter:
            letter.write(create_email(name, value[-1]))

    print(f'Letters created and located at: {location}')

    return files

def quit():
    print('Enjoy! :)')


def invalid_menu():
    print('Invalid option. Select 1, 2, 3, or 4.')

# send_thankyou()
# create_report()
# send_letters()

if __name__ == '__main__':

    option = None
    main_menu = {'1': send_thankyou, '2': create_report, '3': send_letters, '4': quit }

    while option != '4':
        option = input('Main Menu:\n'
                    '\t1: Send a Thank You\n'
                    '\t2: Create a Report\n'
                    '\t3: Send Letters\n'
                    '\t4: Quit\n'
                    '\tSelect an option: ')

        main_menu.get(option, invalid_menu)()
