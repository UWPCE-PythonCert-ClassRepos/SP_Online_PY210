#!/usr/bin/env python3

from donor_models import Donor
from donor_models import DonorCollection
import os
import sys

"""
Steve Morehouse
Lesson 09
"""

prompt = "\n".join(("Welcome to the Mailroom!",
          "Please choose from below options:",
          "1 - Enter a Donation",
          "2 - Send a Thank You",
          "3 - Create Report",
          "4 - Send letters to all",
          "5 - Exit",
          ">>> "))

first_usage = False

def get_max_lengths(seq, header):

    name_len = len(header[0])
    total_len = len(header[1])
    count_len = len(header[2])
    avg_len = len(header[3])

    for item in seq:
        total = f"${item[1]:.02f}"
        count = str(item[2])
        avg = f"${item[3]:.02f}"

        name_len = len(item[0]) if len(item[0]) > name_len else name_len
        total_len = len(total) if len(total) > total_len else total_len
        count_len = len(count) if len(count) > count_len else count_len
        avg_len = len(avg) if len(avg) > avg_len else avg_len

    return [name_len, total_len, count_len, avg_len]


def sort_key(item):
    return item[1]


"""
Return a formatted string that will fit in the donor summary table.
"""
def format_line(item, lengths):
    total = f"{item[1]:.02f}"
    avg = f"{item[3]:.02f}"
    return f"{item[0]:<{lengths[0]}}  ${total:>{lengths[1]}}   {item[2]:>{lengths[2]}}  ${avg:>{lengths[3]}}"


def get_donation_amount(donor):
    while True:
        try:
            donation_amount = input("Enter the donation amount")
            if float(donation_amount) > 0:
                donor.add_donation(float(donation_amount))
                print(donor.compose_thank_you())
                return
            else:
                print("The number you enter must be greater than 0.")
                continue
        except ValueError:
            print('Invalid input. You must enter an amount')


def enter_a_donation(donors):
    while True:
        name = input("Type 'list' to see a list of names, 'quit' to quit, or enter a name: ")
        if name == "list":
            print (donors.list_donors())
            continue
        elif name == "quit":
            return
        else:
            result = donors.donor_exists(name)
            if result is False: # new donor
                donor = Donor(name)
                get_donation_amount(donor)
                donors.add(donor)
            else:
                get_donation_amount(donors.donors[name])
            return


def send_a_thank_you (donor):
    print (donor.compose_thank_you ())


def create_report (donors):
    donor.create_report()


def print_report (donors):
    pass


def exit_program(ignore):
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    prompt_action = {"1" : enter_a_donation,
                     "2" : send_a_thank_you,
                     "3" : create_report,
                     "4" : print_report,
                     "5" : exit_program }

    donors = DonorCollection()
    donors.add (Donor('Bill Gates',[1,2]))
    donors.add (Donor('Warren Buffet',[12,22]))
    donors.add (Donor('Jeff Bezos',[199]))
    donors.add (Donor('Mark Zuckerberg',[10.12,20.30,40.44]))
    donors.add (Donor('Melinda Gates',[99.00]))

    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        try:
            prompt_action[response](donors)
        except KeyError:
            print ("try again")

if __name__ == "__main__":

    main()

