#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:53:34 2019

@author: humberto gonzalez
"""

import sys  


donor_db = [("Tyrod Taylor", [1000.00, 45.50]),
            ("Jarvis Landry", [150.25]),
            ("Philip Rivers", [650.23, 40.87, 111.32]),
            ("Melvin Gordon", [1677.25, 4300.23, 10532.00]),
            ("Mike Williams", [230.56, 12.45, 11.00]),
            ("Antonio Brown", [100.00, 88.88])
            ]

donors = []

for donor_info in donor_db:
    donors.append(donor_info[0])

main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a Report",
              "3 - Exit",
              ">>> "))

    

def send_thank_you():
    '''Prompts user for a donor and donation amount, and then prints out a thank you email'''
    donor_name = input('What is the full name of the donor you would like to thank? ')
    if donor_name.lower() == "quit":
        main()
    if donor_name not in donors:
        donor_db.append((donor_name,[]))
    donation = input('What was the donation amount? ')
    if donation.lower()=="quit":
        main()
    for donor_info in donor_db:
        if donor_info == donor_name:
            donor_info[1].append(donation)
    print()
    print()
    print(f'Dear {donor_name}, Thank you for your generous donation of ${donation}')
    main()


def create_report():
    '''Creates a report of the current donor database'''
    print('{:20} | {:^10} | {:^10} | {:^10} |'.format("Donor Name",
          "Total Given","Num Gifts","Average Gift"))
    print('-'*64)
    formatter = "{:20}   ${:>10}   {:>10}   ${:>10}"
    for donor_info in donor_db:
        donor = donor_info[0]
        donations = donor_info[1]
        total = round(sum(donations),2)
        num = len(donations)
        average = round(total/num,2)
        print(formatter.format(donor,total,num,average))
    main()
    
def exit_program():
    print("Bye!")
    sys.exit()

def main():
    response = input(main_prompt)  # continuously collect user selection
    # now redirect to feature functions based on the user selection
    if response == "1":
        send_thank_you()
    elif response == "2":
        create_report()
    elif response == "3":
        exit_program()
    else:
        print()
        print("Not a valid option!")
        print("Returning to the main menu")
        main()


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()


















