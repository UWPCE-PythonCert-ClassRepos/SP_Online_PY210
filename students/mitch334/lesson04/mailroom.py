'''Lesson 04 | Mailroom Part 2'''

'''You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this over and over again,
so you’ve decided to let Python help you out of a jam and do your work for you.'''

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

import os
import tempfile
import datetime

''' Initial donor list with donation history
    Data: Donor Name: [Donation Amount(s)]'''
donor_db = {"William Gates, III": [100.00, 50.00],
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
def get_donor_names():
    donor_names = []
    for donor in donor_db:
        donor_names.append(donor)

    return donor_names

def create_donation(name):
    donor_names = get_donor_names()

    donation_amount = round(float(input('Enter donation amount: ')),2)
    donor_db[name].append(donation_amount)

    print()
    create_email(name,donation_amount)

def create_email(name,amount):

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

        donor_names = get_donor_names()

        if donor_name.lower() == 'list':
            print('\nDonor List:')
            for donor in donor_db: print('\t',f'{donor}')

        elif donor_name.lower() == 'db':
            print('\nDonor Database:')
            for name, val in donor_db.items(): print('\t',f'{name:26}{val}')

        elif donor_name.lower() == 'exit':
            break

        elif donor_name.title() in donor_names:
            create_donation(donor_name.title())

        else:
            confirm = None
            while confirm != 'no':
                confirm = input("Donor name '"f'{donor_name}'"' was not found.\n"
                                            "\tWould you like to add this donor?\n"
                                            "\tEnter 'yes' or 'no': ")
                if confirm.lower() == 'yes':
                    donor_db[donor_name.title()] = []

                    create_donation(donor_name.title())
                    break
                elif confirm.lower() == 'no':
                    print('Donor not added.')
                    break
                else:
                    print('Invalid entry.')

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
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*66)

    donor_db_stats = {k: [sum(v), len(v), sum(v)/len(v) ] for k, v in donor_db.items()}

    for donor, stat in sorted(donor_db_stats.items(), key=lambda d: d[1][0], reverse=True):
        print(f'{donor:26} ${stat[0]:>11.2f} {stat[1]:>11.0f}  ${stat[2]:>12.2f}')

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

    print('Creating letters for:')
    for name, value in donor_db.items():
        with open(location + '\\' + name.replace(' ','-') + '__' + str(now) + '.txt', 'w') as letter:
            letter.write(create_email(name,value[-1]))
            print(f'\t{name}')
    print(f'Complete. Letters located at: {location}')

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

        main_menu.get(option,invalid_menu)()
