# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:49:53 2020

@author: miriam
"""

# Part 1
import sys
donors = [('Miriam Pintor', [100, 300]),
          ('Waleed Alvarez', [500, 200, 800]),
          ('Ricardo Gallegos', [50, 75, 100]),
          ('Dina Sayury', [125, 120]),
          ('Urias Gramajo', [1000]),
          ]

prompt = "\n".join(("Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - quit",
                    ">>> "))


def finder(type_name):
    for name in donors:
        if type_name == name[0]:
            return name
    return None


def sort_key(entry):
    return sum(entry[1])


def send_thankyou():
    recipient = input ("Enter the donor's Full Name or 'list' for current" 
                       "donors ")

    while recipient == "list":
        for name in donors:
            print(name[0])
        recipient = input ("Please enter a  Full Name ")        
    donor = finder(recipient)
    if donor is None:
        donor = (recipient, [])
        donors.append(donor)
    donation = float(input ("Enter the amount for donation "))
    donor[1].append(float(donation))
    print_thankyou(recipient, donation)


def print_thankyou(name, amount):
    print(f'\nDear {name.title()},')
    print(f'Thank you for your generous donation of ${amount:,.2f}')


def create_report():
    header = '\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donors, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(entry[1])
        num = len(entry[1])
        average = total/num
        print('{:<18} ${:>12,.2f}{:>8}        ${:>12,.2f}'.format(entry[0],
              total, num, average))
    print('')


def quit_action():
    print("Bye")
    sys.exit()


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thankyou()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_action()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()