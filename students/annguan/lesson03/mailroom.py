#!/usr/bin/env python3

### Lesson 3 Mailroom, Part 1

from textwrap import dedent
import math

# a data structure holds a list of donors and a history of the amounts they have donated.
donor_db = [("Abraham Lincoln", [145674.32, 23465]),
("Barack Obama", [3456324.11, 3495, 323]), 
("Charlie Brown",[453.67]),
("Doctor Who", [5600, 42]),
("Eve WallE",[2.22]),]

# prompt user to choose from a menu of 3 actions: "Send a Thank you", "Create a Report", or "quit"
def menu_selection():
    action = input(dedent('''
        Choose an action:
        'a' - Send a Thank You
        'b' - Create a Report
        'c' - Quit
        >'''))
    return action.strip()

# Thank You Letter Composition
def comp_letter(donor):
    return dedent('''
        Dear {}

        Thank you for your donation!

        See you soon.

        '''.format(donor[0]))

# Sending a Thank You
def print_donors():
    print("Donar list:\n")
    for donor in donor_db:
        print(donor[0])

def find_donor(name):
    for donor in donor_db:
        if name.strip().lower() == donor[0].lower():
            return donor
    return None

def send_thank_you():
    while True:
        name = input ("Enter the donor's name "
                        "or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print_donors()
        elif name == "menu":
            return
        else:
            break
    while True:
        donamt = input ("Enter the amount being donated (or 'menu' to exit )>").strip()
        if donamt == "menu":
            return
        if math.isnan(float(donamt)) or math.isinf(float(donamt)) or round (float(donamt),2) == 0.00:
            print("invalid donation amount\n")
            continue
        else:
            break

    donor = find_donor(name)
    if donor is None:
        donor = (name,[])
        donor_db.append(donor)

    donor[1].append(float(donamt))
    print(comp_letter(donor))

# Create a Report
def sort_key(item):
    return item[1]

def create_donor_report():
    name_don = []
    for (name,donation) in donor_db:
        total_donation = sum(donation)
        num_donation = len(donation)
        avg_donation = total_donation/num_donation
        name_don.append((name,total_donation,num_donation,avg_donation))
    
    name_don.sort(key=sort_key)

    print("{:25s} |$ {:11s} | {:9s} |$ {:12s}".format(
          "Donor Name", "Total Donation", "Num Donation", "Average Donation"))
    print("-" * 66)
    for row in name_don:
        print("{:25s}   {:11.2f}   {:9d}   {:20.2f}".format(*row))

# main interaction
if __name__ == "__main__":
    running = True
    while running:
        selection = menu_selection()
        if selection == "a":
            send_thank_you()
        elif selection == "b":
            create_donor_report()
        elif selection == "c":
            running = False
        else:
            print("invalid entry!")
