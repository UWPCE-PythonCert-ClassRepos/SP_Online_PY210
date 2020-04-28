# -*- coding: utf-8 -*-
"""
Created on Mon April 27 2020

@author: cliff
"""

#!/usr/bin/env python3
'''
Use dicts where appropriate.
Part 1 of this assignment used these basic data types: numbers, strings, 
ists and tuples.

However, using dictionaries, covered in Lesson 4, will let you re-write 
your program a bit more simply and efficiently.

Update your mailroom program to:

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
See if you can use a dict to switch between the users selections. 
see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the letter 
as one big template, rather than building up a big string that 
produces the letter in parts.
'''

import sys
import operator

# dictionary with donor names and donation amounts
donor_list = {"William Gates, III": [653772.32, 12.17],
              "Jeff Bezos":  [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
              "Alexandra Butler": [777.77, 44.44]}

def main_menu():
    # display the main menu
    print("\n".join(("Welcome to the MailRoom!",
        "Please choose from below options:",
        "1 - Send a Thank You",
        "2 - Create a Report",
        "3 - Send letters to all donors",
        "4 - Quit",
        ">>> ")))
    return input()

def prompt_amount(full_name):
    # request user input for donation amount
    try:    
        amount = input("What's the donation amount? \n >>")
        amount = int(amount)
        add_amount(full_name,amount) 
    except ValueError:
        print("Input must be a number. Donor information not entered. Try again! ")
    return amount

def add_amount(full_name,amount):
    # add donation amount to the dictionary
    donor_list[full_name].append(amount)

def prompt_name():
    # request user to input a full name
    try:
        full_name = input("Type the donors full name or type list to display donor names.")
        if full_name == 'list':
            for key in donor_list:
                print(key)
            prompt_name()
        elif full_name == "":
            raise TypeError
        else:
            add_name(full_name)
    except TypeError:
            print("\nNot a valid answer. Please enter a name.\n>>>")
    return full_name

def add_name(full_name):
    # update add name to the dictionary
    for donor in donor_list:
        if full_name == donor:
            break
    else:
        donor_list[full_name] = []

def thank_you_text(full_name,amount):
    # display thank you letter with donor name and donation amount
    print ("\n\nHi {}:\n Thank you for the generous donation of ${:2d}, Sincerely, \n Clifford Butler\n".format(full_name,amount))

def send_thank_you():
    # send thank you email based on user input information
    full_name = prompt_name()
    amount = prompt_amount(full_name)
    thank_you_text(full_name, amount)
    main()

def create_report():
    # Generate and display a report of the donors in donor_dict
    report = []
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)

    for donor, value in sorted(donor_list.items(), key=operator.itemgetter(1)):
        if len(value) != 0:
            report.append((donor, round(sum(value),2), len(value),round(sum(value)/len(value))))
            print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(donor, '$', round(sum(value),2), len(value), '$',round(sum(value)/len(value),1))))
    print (report)
    return report
    
def letter_to_all():
    # send thank you letter to all donors
    for full_name in donor_list:
        with open(f"{full_name}.txt","w+") as donor_letter:
            donor_letter.write(f"Hi {full_name},\n\nThank you for the generous donation of ${sum(donor_list[full_name]):.2f}.\n\nSincerely,\nClifford Butler")
    print("Thank you letters sent!")

def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit() 

def main():
    #dict with the user options and the functions
    switch_dict = {
        '1': send_thank_you,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    }

    while True:
        try:
            response = main_menu()
            switch_dict[response]()
        except KeyError:
            print("\n'{}'  is not a valid option, please enter 1, 2, 3, or 4!. \n >> ".format(response))

if __name__ == "__main__":
    main()