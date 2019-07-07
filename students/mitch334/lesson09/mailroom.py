"""Lesson 09 | Mailroom Part 5"""

"""You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts.
You are tired of doing this over and over again, so you’ve decided to let Python help
you out of a jam and do your work for you."""

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

# Add a full suite of unit tests.
# The Program: Part 4
# “Full suite” means all the code is tested. In practice, it’s very hard to test the user interaction, but you can test everything else. Therefore you should make sure that there is as little logic and untested code in the user interaction portion of the program as possible.
# This is a big step; you may find that your code is hard to test. If that’s the case, it’s a good sign that you should refactor your code.
# I like to say: “If it’s hard to test, it’s not well structured.”
# Put in the tests before you make the other changes below. That’s much of the point of tests. You can know that you haven’t broken anything when you refactor!

# The Program: Part 5
# Goal: Refactor the mailroom program using classes to help organize the code.


import os
import tempfile
import datetime

# Class responsible for donor data encapsulation
class Donor:
    def __init__(self, name, donations=None):
        self.name = name

        if donations == None:
            self._donations = []
        else:
            self._donations = list(donations)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def donations(self):
        return self._donations


# Class responsible for donor collection data encapsulation
class DonorCollection:
    def __init__(self, donors=None):
        if donors == None:
            donors = []
        else:
            self._donors = donors

    @property
    def donors(self):
        return self._donors

    def donors_list(self, list_output):
        list = '\n'

        for donor in self.donors:
            if list_output == 'list':
                list += f'{donor.name}' + '\n'
            elif list_output == 'db':
                list += f'{donor.name:26}{donor.donations}' + '\n'
            else:
                list = ''
        return list


    def add_donor(self, name):
        donor_exists = False

        for donor in self.donors:
            if donor.name == name:
                donor_exists = True
                break

        if not donor_exists:
            donor = Donor(name)
            self.donors.append(donor)

        return donor

""" Initial donor list"""
donors = DonorCollection([
    Donor("William Gates, III", [100.00, 50.00]),
    Donor("Jeff Bezos", [1000.00, 10.00, 500.00]),
    Donor("Mark Zuckerberg", [200.00, 20.00, 50.00]),
    Donor("Warren Buffet", [600.00, 300.00]),
    Donor("Paul Allen", [1000.00])
    ])


def send_thankyou():

    donor_name = ''
    while donor_name != 'exit':
        donor_name = input('Thank-You Menu:\n'
                            '\tOptions:\n'
                            "\t\tEnter 'list' for donor list\n"
                            "\t\tEnter 'exit' to return to the main menu\n"
                            '\tEnter full name of donor: ')

        if donor_name.lower() == 'list':
            print(donors.donors_list('list'))
        elif donor_name.lower() == 'db':
            print(donors.donors_list('db'))
        elif donor_name.lower() == 'exit' or donor_name.lower() == '4':
            break
        else:
            donor = donors.add_donor(donor_name.title())

            amount = verify_donation()
            print('verify_donation amount: ', amount)

            donor.donations.append(amount)

def verify_donation():
    amount_input = input('Enter donation amount: $')

    try:
        amount = round(float(amount_input),2)

        print('return amount: ', amount)
        return amount

    except ValueError:
        print('Error. Enter a valid donation amount.')
        verify_donation()


def quit():
    print('Enjoy! :)')


def invalid_menu():
    print('Invalid option. Select 1, 2, 3, or 4.')

send_thankyou()
# create_report()
# send_letters()

if __name__ == '__main__':

    option = None
    # main_menu = {'1': send_thankyou, '2': create_report, '3': send_letters, '4': quit }
    main_menu = {'1': send_thankyou, '2': quit, '3': quit, '4': quit }

    while option != '4':
        option = input('Main Menu:\n'
                    '\t1: Send a Thank You\n'
                    '\t2: Create a Report\n'
                    '\t3: Send Letters\n'
                    '\t4: Quit\n'
                    '\tSelect an option: ')

        main_menu.get(option, invalid_menu)()
