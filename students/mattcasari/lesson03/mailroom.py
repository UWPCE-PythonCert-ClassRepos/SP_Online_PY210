#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 4

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part1.html

Description:
    The Program: Part 1
    Write a small command-line script called mailroom.py. This script should be
    executable. The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a 
    history of the amounts they have donated. This structure should be 
    populated at first with at least five donors, with between 1 and 3 
    donations each. You can store that data structure in the global namespace.
    The script should prompt the user (you) to choose from a menu of 3 
    actions: “Send a Thank You”, “Create a Report” or “quit”.    

"""

# data list structure is [Name, [Amount1, Amount 2,...], Sum, Len, Average]
data = [ ["Neil Armstrong", [15000.00, 15000.00],[],[],[]],
["Buzz Aldrin", [23021.10, 25020.30, 28999.29],[],[],[]],
["Sally Ride", [42917.42, 38281.28],[],[],[]],
["Al Shepard", [2387.00,  2321.42, 3700.00],[],[],[]],
["Alan Bean", [28477.13, 727.1],[],[],[]],
["Chris Hadfield", [17325.42, 13823.83, 0.99],[],[],[]]]

def prompt_user():
    """ Prompts the user for menu option """
    PROMPT_TEXT = ("\nSelect an option:\n"
    "1. Send a Thank You\n"
    "2. Create a Report\n"
    "3. Quit\n"
    "> ")

    result = input(PROMPT_TEXT)
    if result.isnumeric():
        result = int(result)
        if 0 < result < 4:
            return result
    else:
        return False

def calculate_stats(donor):
    """ Calculates the sum, average and number of donations for a donor """
    donor_sum = sum(donor[1])
    donor_num = len(donor[1])
    donor_average = donor_sum/donor_num

    return (donor_sum, donor_num, donor_average)

def sort_donors_by_total(donors):
    """ Function used to sort donors by total contributions """
    return donors[2]

def generate_report(values):
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    print("\n")
    column_donor_length = 0

    for idx, value in enumerate(values[:]):
        column_donor_length = max(len(value[0]),column_donor_length)+5
        [values[idx][2], values[idx][3], values[idx][4]] = calculate_stats(value)

    f_str = " {" + f":<{column_donor_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(title_str)
    print("-"*len(title_str))
    
    values = sorted(values, key=sort_donors_by_total, reverse=True)

    for value in values:
        f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
        v_str = f_str.format(value[0], value[2], value[3], value[4])
        print(v_str)

def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value[0])

def thank_you_email(name, amount):
    """ Format the email and print to terminal """
    txt = f"""\nDear {name},\n""" \
          f"""Thank you for your recent donation of ${amount:.2f}. """ \
          f"""Your donation will help us purchase a taxidermied seagull.\n""" \
          f"""Please consider donating again at your earliest convenience.\n\n""" \
          f"""Sincerely,\n""" \
          f"""The Human Fund\n"""

    print(txt)

def add_donor(values):
    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        donor = input("Enter Full Name (or list): ")

        for idx, value in enumerate(values):
            if value[0] == donor:
                valid_donor = True
                break
        else:
            if donor == "list":
                print_donor_list(values)
                continue
            else:   
                values.append([donor,[]])
                
                idx += 1
                valid_donor = True
                break
            
    
    amount = input("Enter donation amount ($): ")
    amount = float(amount)
            # break
    
    # Add amount to data
    values[idx][1].append(amount)
    values[idx].append([])
    values[idx].append([])
    values[idx].append([])

    thank_you_email(values[idx][0], amount)

    return values

def main():
    """ Main Run Loop """
    while True:
        option = prompt_user()

        if option == 1:
            add_donor(data)
        elif option == 2:
            generate_report(data)
        elif option == 3:
            print("\nExiting Program")
            break
        else:
            print("\nPlease select a valid option")
    

if __name__ == "__main__":
    main()