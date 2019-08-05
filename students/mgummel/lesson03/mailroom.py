#! /usr/bin/env python3

import sys
from operator import itemgetter

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Marc Benioff", [45023.15, 442.30])
            ]


prompt = "\n".join(("Please choose from below options:",
          "- Send a Thank You",
          "- Create a Report",
          "- Quit",
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
    sorted_list = []
    computed_list = []

    for donor_tuple in donor_db:
        total_donation, avg_donation, num_of_donations = compute_donation(donor_tuple[1])
        computed_list.append((donor_tuple[0], total_donation, num_of_donations, avg_donation))
    sorted_list = sorted(computed_list, key=itemgetter(1), reverse=True)

    for sorted_item in sorted_list:
        print("{:<27}${:>12.2f}{:>14}   ${:>13.2f}".format(*sorted_item))

def create_header():
    header = "{:<26}|{:^15}|{:^13}|{:>14}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))
    
def compute_donation(donations):
    total_amount = 0 
    donation_num = 0 
    avg_amount = 0

    for amount in donations:
        donation_num += 1
        total_amount += amount

    total_amount = round(total_amount, 2)
    avg_amount = round(total_amount / donation_num, 2)
    
    return total_amount, avg_amount, donation_num


def main():

    print("Welcome to the Mailroom App!")

    while True:
        response = input(prompt).title()
        if response == "Quit":
            quit_program()
        elif response == "Send A Thank You":
            send_thank_you()
            print("\n\n")
        elif response == "Create A Report":
            create_report()
            print("\n\n")
        else:
            print("Not a valid option!\n\n")



if __name__=='__main__':
    main()
    