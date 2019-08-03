#! /usr/bin/env python3

import sys
from operator import itemgetter

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Marc Benioff", [45023.15, 442.30])
            ]


prompt = "\n".join(("Welcome to the Mailroom App!",
          "Please choose from below options:",
          "(*) - Send a Thank You",
          "(*) - Create a Report",
          "(*) - Quit",
          ">>> "))

def quit_program():
    print("The program will now exit.")
    sys.exit()  

def send_thank_you():
    donor = "List"
    while donor == "List":
        donor = input("Please type a donor's full name or type 'list' to view donors. \n >>> ").title()
        names = []
        for row in donor_db:
            names.append(row[0])

        if donor == "Quit":
            quit_program()
        elif donor == "List":
            print("\n".join(["{}"] * len(donor_db)).format(*names))
        elif donor not in names:
            donor_db.append((donor, []))

    new_donation = find_tuple(donor)
    print(f"Thank you {donor} for your generous donation of ${new_donation}.", end = " ")
    print("Your contribution will help our organization do good out in the community.\n")

def find_tuple(donor_tuple):
    donation = float(input("What's the new donation amount? \n >>> "))
    if donation <= 0:
        quit_program()
    
    for index in donor_db:
        if donor_tuple == index[0]:
            index[1].append(donation)
    return donation 

def create_report():
    create_header()

def create_header():
    print("{:<20}|{:^15}|{:^13}|{:>14}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 65)
    
def find_average(donations):
    pass


def main():

    while True:
        response = input(prompt).title()
        if response == "Quit":
            quit_program()
        elif response == "Send A Thank You":
            send_thank_you()
        elif response == "Create A Report":
            create_report()
        else:
            print("Not a valid option!")



if __name__=='__main__':
    main()
    