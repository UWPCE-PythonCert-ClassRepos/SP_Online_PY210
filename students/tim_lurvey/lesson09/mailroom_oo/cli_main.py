#!/usr/bin/env python
__author__ = 'Tim Lurvey, ig408c'

import sys
import os
from donor_classes import DonorRepository


my_data_repo = DonorRepository()
my_data_repo.add_new_donor(('Tom Hanks', 24536.20, 3))
my_data_repo.add_new_donor(('Barry Larkin', 4521., 3))
my_data_repo.add_new_donor(('Mo Sizlack', 88.88, 2))
my_data_repo.add_new_donor(('Anonymous', 100., 1))
my_data_repo.add_new_donor(('Donnald Trump', 1., 3))


def print_formatted_name_list():
    print(my_data_repo.formatted_name_list)
    return True


def add_new_donor():
    """Add a new donor, from user input"""
    # get params
    name = input("Name:\n>>>")
    while True:
        try:
            total = input("Total (optional, default is $0):\n>>>$")
            float(total)
            break
        except:
            print("'{}' is not numeric.  Please input only numbers")
    count = 0
    # if total, must have count
    if total:
        while True:
            try:
                count = input("Number of donations:\n>>>")
                int(count)
                break
            except:
                print("'{}' is not numeric.  Please input only numbers")
    # add them
    my_data_repo.add_new_donor((name, total, count))
    donor = my_data_repo.get_donor(name=name)
    print("Added: {0}, Total: ${1}, Count: {2}".format(donor.name, donor.total, donor.count))
    return True


def get_name_from_user():
    """get name from input"""
    name = input("Please enter a full name (Case Sensitive)\n>>>")
    if name not in my_data_repo.name_list:
        print("name='{}' not in data set.  Please add the user at the main menu.".format(name))
        name = ""
    return name


def get_additional_donation_from_user(name: str):
    """get new donation, if any"""
    while True:
        additional = input(f"If {name} is making new donation, enter the amount. (0 for no new donation)\n>>>")
        try:
            float(additional)
            break
        except ValueError:
            print("Invalid numeric amount, please try again.")
    return float(additional)


def print_thank_you_donor():
    """print the string 'Thank you' message for a user selected donor"""
    name = get_name_from_user()
    if not name:
        return True
    additional = get_additional_donation_from_user(name=name)
    #
    print(my_data_repo.get_thank_you_email(donor=name, new_donation=float(additional)))
    return True


def all_donors_report():
    print(my_data_repo.report())
    return True


def get_path_from_user():
    """get the path from the user, or return to the previous menu"""
    while True:
        write_path = input("Enter a path to write letters to.  'q' to return to previous menu\n>>> ").strip()
        if write_path == 'q':
            # if quitting, unset the variable to return a False boolean test on return
            write_path = ""
            break
        elif os.path.exists(write_path):
            # write_path is good, boss!  return it
            break
        else:
            print("Cannot access '{}'".format(write_path))
    #
    return write_path


def write_letter_to_path(name: str, message: str, pathx: str):
    with open(os.path.join(pathx, "thank_you_{}.txt".format(name).replace(" ", "_")), "w") as W:
        W.write(message)


def write_thank_you_letters_to_path():
    wpath = get_path_from_user()
    for name in my_data_repo.name_list:
        write_letter_to_path(name=name,
                             message=my_data_repo.get_thank_you_email(donor=name),
                             pathx=wpath)
    return True


def quit_program():
    """Exit the application by unseating the switch"""
    exit("\nGoodbye! Exiting program...")


def error(inp: str = ""):
    """Report an error"""
    print("\nError on input.  Invalid selection \"{}\"".format(inp))
    return True


def main():
    """This is the controlling logic for the program.  The main loop will
    repeat forever until the user specifies to quit.
     -- LOGIC FLOW --
     1 print_name_list
     2 add_new_donor
     3 send_thank_you
        additional_donation ?
        print thank you message
     4 print_donor_report
     5 write_letters
        get_path
        write_files
     q quit
    """

    while True:
        # Define main input
        msg = "1 : See a list of donor names\n" \
              "2 : Add new donor\n" \
              "3 : Print a Thank You to individual donor\n" \
              "4 : Create Report of all donors\n" \
              "5 : Write Thank you letters to all donors\n" \
              "q : quit\n>>> "
        # Query
        request = input("Select:\n{}".format(msg)).strip()
        # Error check
        if len(request) > 1:
            print("\nplease input only '1' or '2' or 'q'\n")
            # keep looping until valid result
            continue
        # Define the logic
        logic_dict = {'1': print_formatted_name_list,
                      '2': add_new_donor,
                      '3': print_thank_you_donor,
                      '4': all_donors_report,
                      '5': write_thank_you_letters_to_path,
                      'q': quit_program}
        # Get the corresponding function and execute it
        logic_dict.get(request, error)()


if __name__ == '__main__':
    main()
