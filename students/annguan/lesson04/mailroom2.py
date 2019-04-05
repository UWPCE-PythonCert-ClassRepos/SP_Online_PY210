#!/usr/bin/env python3

### Lesson 4 Mailroom, Part 2, uses dict

from textwrap import dedent
import os
import sys
import math

# a data structure holds a list of donors and a history of the amounts they have donated.
def get_donor_db():
    return {'Abraham Lincoln': ("Abraham Lincoln", [145674.32, 23465]),
            'Barack Obama': ("Barack Obama", [3456324.11, 3495, 323]), 
            'Charlie Brown':("Charlie Brown",[453.67]),
            'Doctor Who': ("Doctor Who", [5600, 42]),
            'Eve WallE': ("Eve WallE",[2.22])
            }

OUT_PATH = "thank_you_letters"

def ready_run ():
    if not os.path.isdir(OUT_PATH):
        os.mkdir(OUT_PATH)

# Write thank you letters to disk as a text file
def write_letters_disk():
    for donor in donor_db.values():
        letter = comp_letter(donor)
        filename = donor[0].replace(" ", "_") + ".txt"
        print("writing letter to:", donor[0])
        filename = os.path.join(OUT_PATH, filename)
        with open(filename, 'w') as file:
            file.write(letter)

# prompt user to choose from a menu of 4 actions: "send letters to all", Send a Thank you", "Create a Report", or "quit"
def menu_selection():
    action = input(dedent('''
        Choose an action:

        1 - Send letters to all
        2 - Send a Thank You
        3 - Create a Report
        4 - Quit

        >'''))
    return action.strip()

# Thank You Letter Composition
def comp_letter(donor):
    return dedent('''Dear {0:s},

        Thank you for your donation of ${1:.2f}.

        See you soon.

        '''.format(donor[0], donor[1][-1]))

#Validate donation inputs by user

def receive_donation(name):
    while True:
        donation_amount = input ("Enter a donation amount or Menu to exit > ").strip()
        if donation_amount == "menu":
            return
        try:
            amount = float(donation_amount)
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("invalid donation amount\n")
        else:
            break

    donor = find_donor(name)
    if donor is None:
        donor = add_donor(name)

    donor[1].append(amount)
    print(comp_letter(donor))

# Sending a Thank You

def add_donor(name):
    name = name.strip()
    donor = (name,[])
    donor_db[name.lower()] = donor
    return donor

def find_donor(name):
    key = name.strip().lower()
    return donor_db.get(key)

def list_donors():
    l1 = ["Donor List:"]
    for donor in donor_db.values():
        l1.append(donor[0])
    return "\n".join(l1)

def send_thank_you():
    while True:
        name = input ("Enter the donor's name "
                        "or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(list_donors())
        elif name == "menu":
            return
        else:
            receive_donation(name)


# Create a Report
def sort_key(item):
    return item[1]

def create_donor_report():
    report_lines = []
    for name,donation in donor_db.values():
        total_donation = sum(donation)
        num_donation = len(donation)
        avg_donation = total_donation/num_donation
        report_lines.append((name,total_donation,num_donation,avg_donation))
    
    report_lines.sort(key=sort_key)
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Donation",
                                                            "Num Donation",
                                                            "Average Donation"))

    report.append("-" * 70)
    for line in report_lines:
        report.append("{:25s}   ${:11.2f}   {:9d}   ${:20.2f}".format(*line))
    return "\n".join(report)

def print_donor_report():
    print(create_donor_report())

def quit():
    sys.exit(0)

# main interaction
if __name__ == "__main__":

    ready_run()

    donor_db = get_donor_db()

    selection_dict = {"1": write_letters_disk,
                      "2": send_thank_you,
                      "3": print_donor_report,
                      "4": quit
                      }

    while True:
        selection = menu_selection()
        try:
            selection_dict[selection]()
        except KeyError:
            print("invalid selection")
