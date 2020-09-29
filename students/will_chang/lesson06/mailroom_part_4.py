#!/usr/bin/env python

import datetime
import os.path
import pathlib
import sys


initial_donor_list = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
]

def find_max_len_str(list_database):
    max_len_str = [0]*4  # List providing the lengths of the longest items in each column
    for row in list_database:
        for item in range(len(row)):
            if len(str(row[item])) > max_len_str[item]:
                max_len_str[item] = len(str(row[item]))
    return max_len_str


def list_data():
    """Provide formatted and updated list of donors, total donations, number of donations, and average donation"""
    initial_donor_list.sort(key=lambda donor: int(donor[1]), reverse = True)
    
    max_len_str = find_max_len_str(initial_donor_list)
    
    
    format_string = f'{{:<{max_len_str[0]+10}}}${{:<{max_len_str[1]+9}}}{{:<{max_len_str[2]+15}}}${{:<{max_len_str[3]+10}}}' # Format string taking into account the longest item in each column.
    format_string_header = f'{{:<{max_len_str[0]+10}}}{{:<{max_len_str[1]+10}}}{{:<{max_len_str[2]+15}}}{{:<{max_len_str[3]+10}}}'
    print("\n")
    print(format_string_header.format(*("Donor Name", "Total Given", "Num Gifts", "Average Gift")))
    print("-"*(max_len_str[0]+max_len_str[1]+max_len_str[2]+max_len_str[3]+39))
    for row in initial_donor_list:
        print(format_string.format(*row))


def active_names(list_database):
    """Provide a sorted list of names in the donor database"""
    names = []
    for donor in list_database:
        names.append(donor[0])
    return sorted(names)


def name_prompt(list_database):
    """Returns full name of new or existing donor to add to the donor database"""
    ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    while ask_name.lower() == "list":
        print(active_names(list_database))
        ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    return ask_name


def update_donor_list(entry, don_amount):
    entry[1] += don_amount
    entry[2] += 1
    entry[3] = entry[1]/entry[2]
    return entry


def thank_you():
    """Prompt user to input new donor information."""
    ask_name = name_prompt(initial_donor_list)
    
    for donor in initial_donor_list:
        if ask_name == donor[0]:  # Check if the entered name is already in the list
            while True:
                try:
                    ask_donor = float(input("Please enter a donation amount: "))
                    break
                except ValueError:
                    print("Input invalid! Donation amount needs to be a number.")
            donor = update_donor_list(donor, ask_donor)
            print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(donor[0],ask_donor))
            break
    else:  # Check if the entered name is not in the list 
        while True:
            try:
                ask_donor = float(input("Please enter a donation amount: "))
                break
            except ValueError:
                print("Input invalid! Donation amount needs to be a number.")
        initial_donor_list.append([ask_name,ask_donor,1,ask_donor])
        print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(ask_name,ask_donor))


def write_letter():
    """Generate letters for each donor in the list with their total donation amount and stores the letters in a new directory"""
    current = datetime.datetime.now()
    abs_path = pathlib.Path('./').absolute()
    final_path = os.path.join(abs_path, "letter_storage/")
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    for line in initial_donor_list:
        with open("{}{}_{:02}_{:02}_{:02}.txt".format(final_path, line[0], current.month, current.day, current.year), 'w') as thank_you_file:
            thank_you_file.write("Dear {},\n\nThank you for your continuous support over the years\nand for your total donation amount of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(line[0],line[1]))

    
def quit_program():
    """Exit out of the program"""
    print("Exiting the program.")
    sys.exit()


if __name__ == '__main__':
    option_select = {'1': thank_you, '2': list_data, '3': write_letter}
    while True:  # loop until user inputs something other than the keys in option_select
        user_prompt = input("\nPlease choose from the following menu of actions:\n[1] Send a Thank You\n[2] Create a Report\n[3] Send letters to everyone\n[Press any other key to quit.]\n\nInput: ")
        if user_prompt not in option_select:
            quit_program()
        option_select.get(user_prompt)()