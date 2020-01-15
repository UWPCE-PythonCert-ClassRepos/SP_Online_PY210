#!/usr/bin/env python3

"""
cli_main.py
By David Baylor on 12/31/19
uses python 3

the comand prompt UI for mail_room_oo.
"""

import sys
from operator import itemgetter
import Mail_Room_oo as mail_room

def write_email(name, donation):
    return f"""Dear {name.title()},

Thank you for your generous donnation of ${donation}.

                    -The Team"""

def send_thank_you(donors):
    name = input("Enter a full name or type 'list' to vew current donors: ").title()
    if name.upper() == "LIST":
        for i in donors.donor_dict.keys():
            print(i)
    else:
        if donors.check_donor_in_db(name) == False:
            if input(f"Selected name is not alredy in donor list. Type 'y' to continue and add {name} to the list.").upper() != "Y":
                return
        while True:
            try:
                donation = float(input(f"How much did {name.title()} donate: $"))
            except ValueError:
                print("Please enter a number") 
            else:
                if donation > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
        donors.add_donation(name, donation)
        print(write_email(name,donation))

def make_table(donors):
    table = """
Donor Name                | Total Given | Num Gifts | Average Gift
--------------------------|-------------|-----------|-------------"""
    for i in donors.sort_lst():
        table += "\n{:26}|${:12}|{:11}|${:12}".format(i.name, 
                                                      i.total_donated, 
                                                      i.donations, 
                                                      i.average_donation)
    return table

def create_report(donors):
    print(make_table(donors))

def send_all(donors):
    for i in donors.donor_dict:
        file_name = f'letter_to_{i}.txt'
        with open(file_name, "w") as file:
            file.write(write_email(donors.donor_dict[i].name, donors.donor_dict[i].total_donated))

def exit_program(data):
    sys.exit()

if __name__ == "__main__":

    donors = mail_room.DonorCollection()
    donors.add_donation("Jeff Bezos", 200, 2)
    donors.add_donation("Elon Musk", 600, 3)
    donors.add_donation("Bill Gates", 50, 1)
    donors.add_donation("Mark Zuckerberg", 75, 5)

    dispatch_dict = {"1":send_thank_you, "2":create_report, "3":send_all, "4":exit_program}
    while True:
        choice = input("""
What would you like to do?

1) Send a Thank You 
2) Create a Report
3) Send a Thank You to all donors
4) Quit
""")
        
        if choice in dispatch_dict:
            dispatch_dict[choice](donors)

