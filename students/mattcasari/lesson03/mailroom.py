#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 1

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
data = [ ["William Gates, III", [300000.00, 353784.49],[],[],[]],
["Mark Zuckerberg", [12000.10, 4395.00, 1],[],[],[]],
["Jeff Bezos", [877.33],[],[],[]],
["Paul Allen", [7.00, 1.42, 700],[],[],[]],
["The RZA", [225000.10, 171000.23],[],[],[]],
["ODB", [0.0, 0.0, 0.0],[],[],[]]]

def prompt_user():
    """ Prompts the user for menu option """
    PROMPT_TEXT = ("Select an option:\n"
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
    txt = f"""\nDear {name},\n
Thank you for your recent donation of ${amount:.2f}. The money donated will go toward many useful purchases,
such as: blankets, pool floaties, chick peas and a taxidermied seagull.
Please consider donating again at your earliest convenience.

Regretfully yours,
The Human Fund\n"""

    print(txt)

def send_thank_you(values):
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
            
         
    while True:
        amount = input("Enter donation amount ($): ")
        if amount.isnumeric():
            amount = float(amount)
            break
    
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
            send_thank_you(data)
        elif option == 2:
            generate_report(data)
        elif option == 3:
            print("\nExiting Program")
            break
        else:
            pass
    

if __name__ == "__main__":
    main()