# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:49:53 2020

@author: miriam
"""

# Part 1
import sys


def donors():
    return {'Miriam Pintor': [100, 300],
            'Waleed Alvarez': [500, 200, 800],
            'Ricardo Gallegos': [50, 75, 100],
            'Dina Sayury': [125, 120],
            'Urias Gramajo': [1000]}


def main_menu():
    print("\n".join(("Please choose from below options:",
                     "1 - Send a Thank You to a single donor.",
                     "2 - Create a Report.",
                     "3 - Send letters to all donors",
                     "4 - quit"
                     ">>> ")))
    option = input('')
    return option


def donors_list():
     ls=[]
     for names in donors_dict:
         ls.append(names)
     return '\n'.join(ls)


def donate(recipient, donation):
    if recipient not in donors_dict:
        donors_dict[recipient] = [donation]
    else:
        donors_dict[recipient] += [donation]


def sort_key(entry):
    return sum(donors_dict.get(entry))


def send_thankyou():
    recipient = input("Enter the donor's Full Name or 'list' for current"
                      "donors ")
    while recipient == "list":
        print(donors_list())
        recipient = input("Please enter a  Full Name ")
    try:
        donation = float(input("Enter the amount for donation "))
    except ValueError:
        print('Please enter a number value')
    else:
        donate(recipient, donation)
        print(print_thankyou(recipient))


def create_report():
    header = '\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donors_dict, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(donors_dict.get(entry))
        num = len(donors_dict.get(entry))
        average = total/num
        print('{:<18} ${:>12,.2f}{:>8}        ${:>12,.2f}'.format(entry,
              total, num, average))
    print('')


def send_letters_all_donors():
    for entry in donors_dict:
        filename = entry + '.txt'
        with open(filename, 'w') as f:
            f.write(print_thankyou(entry))


def print_thankyou(name):
    letter = (f'\nDear {name},'
              f'\nThank you for your very kind donation of ${sum(donors_dict.get(name)):,.2f}'
              '\nIt will be put to very good use.'
              '\n\nSincerely,\n-TheTeam\n')
    return letter


def quit_action():
    print("Bye")
    sys.exit()


def main():
    switch_dict = {1: send_thankyou, 2: create_report, 3: send_letters_all_donors, 4: quit_action}
    while True:
        try:
            option = int(main_menu())
            switch_dict.get(option)()
        except TypeError:
            print('try again\n')


if __name__ == "__main__":
    donors_dict = donors()
    main()