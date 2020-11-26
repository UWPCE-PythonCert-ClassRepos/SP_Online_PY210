#! /usr/bin/env python3

## Lesson 4, Assignment 3, Mailroom Part 2
## By: B. Matthews
## https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part2.html
## update to: use a dict for donor data; use dict for menu switching
## and write letters to files

import sys
#import copy
import os

## Global variables
donors = {'Harry Dresden': [10.00],
          'Queen Mab': [234.10, 1043.50],
          'Molly Carpenter': [1000.00, 25.99, 321.45]}

s_mylist = []
average = 0
total = 0
num_of_donations = 1

prompt = "\n".join(("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nMailroom v.2\n",
                    "Please choose an option:",
                    "1) Send a Thank-you",
                    "2) Create a Report",
                    "3) Send Thank-you letters to all donors (create files)",
                    "4) Quit",
                    "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\a> "))

prompt2 = "\n".join(("**********************************\nThank-You Options\n",
                     "What do you want to do?:",
                     "1) Enter a name",
                     "2) List of donor names",
                     "3) Return to Main Menu",
                     "**********************************\n> "))

def thanks():
    """Prints a donor thank-you to the screen"""

    while True:
        choice = input(prompt2)
        menu2.get(choice)()         # use menu dictionary to select correct function
    return

def report():
    """Prints a report to the screen of donors and amounts"""
    #print("\n" * 100, "\a{:<23} | {:<15} | {:<15} | {:>15}".format("Name", "Total Donated ($)",
                                                                   #"Number of Donations",
                                                                   #"Average Amount ($)"))
    print("-" * 87)

    ## Sort the list of donors in descending total donation amount order
    #s_mylist = sorted(huge_list, key=lambda record : sum(record[1]), reverse=True)

    #for person in s_mylist:
       #total = sum(person[1])
        #number = len(person[1])
        #average = total/number
        #print("{:<24} | {:>17,.2f} | {:>19} | {:>15,.2f}".format(person[0], total, number, average))

    print("\nThe donors and amounts will be printed here soon.\n")
    return

def exit_menu():
    """Exits out of the interactive menu"""
    print("Goodbye")
    sys.exit()

def thank_files():
    """writes a donor thank-you and puts in a file for each donor"""
    cwd = os.getcwd()       # Current working dir
    #number = len(donors)

    for person, amount in donors.items():
        pname = person.replace(' ', '_')
        path = os.path.join(cwd, pname)
        myfile = path + ".txt"

        with open(myfile, 'w') as f:
            f.write("Thanks %s " % (person))
            print("created file: ", myfile)

    return

def name_donors():
    """Ask user for name of donor, add it if new, ask for dontation amount, print thanks.
    If the name is found, just add the new donation to their record"""

    name = input("What name?\n")
    #print("you entered", name)
    what = float(input("How much donated? --> "))

    if name not in donors:
        donors[name] = [what]
        print("\n" * 50, "Dear %s,\n\nThank you for your generous donation of $%.2f. "
                          "We appreciate your support.\n\nSincerely, Grateful Team" % (name, what))
        print("\n" * 5)

    else:
        what_list = donors[name]
        all = sum(what_list) + what
        print("\n" * 50, "Thank you, %s for your continuing generous donations of $%.2f.\n"
                          "We appreciate your support.\n\nSincerely, Grateful Team" % (name, all))
        print("\n" * 5)

def list_donors():
    """prints the donors which are the keys in the donors dictionary"""

    print('People who have donated:\n')
    for person, amount in donors.items():
        print(person)
    print('\n\n')

def exit_sub():
    """something might go here"""

menu1 = {
        '1': thanks,
        '2': report,
        '3': thank_files,
        '4': exit_menu
    }

def main():
    """Prints the menu dispay to the screen and gets user input"""

    while True:
        response = input(prompt)    # continuously collect user selection
        menu1.get(response)()       # use menu dictionary to select correct function

        print("you typed: ", response)

## Submenu calls main so it has to be here, but I usually like declarations at the top
menu2 = {
        '1': name_donors,
        '2': list_donors,
        '3': main
    }

# If not imported as a module, call the main function
if __name__ == "__main__":
    main()