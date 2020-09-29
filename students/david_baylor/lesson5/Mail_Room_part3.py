#!/usr/bin/env python3

"""
Mail_room_part1.py
By David Baylor on 12/3/19
uses python 3

Automates writing an email to thank people for their donations.
"""

import sys
from operator import itemgetter

def send_thank_you(data):
    name = input("Enter a full name or type 'list' to vew current donors: ")
    if name.upper() == "LIST":
        for i in data:
            print(i.capitalize())
        return data
    else:
        while True:
            try:
                donation = float(input(f"How much did {name.capitalize()} donate: $"))
            except ValueError:
                print("Please enter a number") 
            else:
                if donation > 0:
                    break
                else:
                    print("Please enter a number greater than 0")
        if name in data:
            data[name][0] += donation
            data[name][1] += 1
        else:
            data[name] = [donation, 1]
        write_email(name, donation)
        return data

def create_report(data):
    print("""        
Donor Name                | Total Given | Num Gifts | Average Gift
--------------------------|-------------|-----------|-------------""")
    for i in sorted([[i, data[i][0], data[i][1]] for i in data], reverse=True, key=itemgetter(1)):
        make_row(i[0], data[i[0]][0], data[i[0]][1], data[i[0]][0]/data[i[0]][1])

def make_row(name, total, num_gift, ave_gift):
    print("{:26}|${:12}|{:11}|${:12}".format(name, total, num_gift, ave_gift))

def send_all(data):
    for i in data:
        write_all(i, data[i][0])


def write_email(name, donation):
    print("Here is the email:") 
    print(f"""
Dear {name.capitalize()},

Thank you for your generous donnation of ${donation}.

                    -The Team""")

def write_all(name, donation):
    file_name = f'letter_to_{name}.txt'
    with open(file_name, "w") as file:
        file.write(f"""Dear {name.capitalize()},

Thank you for your generous donnation of ${donation}.

                    -The Team""")
    print(f"Sent to {name}")

def exit_program(data):
    sys.exit()

if __name__ == "__main__":
    data = {"Bill" : [100, 2], 
            "John" : [75, 3], 
            "Joe"  : [150, 3], 
            "Fred" : [3.5, 1]}

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
            dispatch_dict[choice](data)

