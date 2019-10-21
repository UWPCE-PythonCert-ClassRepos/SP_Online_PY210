#!/usr/bin/env python3

# ------------------------------ #
# Assignment 4 (Mailroom Part 2) for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/11/2019, Created and tested script (Mailroom Part 1)
#   BPA, 8/18/2019, Updated to add dictionaries and dispatch menu
#                   Adding function to print emails to text files
#   BPA, 8/20/2019, Updated dictionary for main donor list to be solely a dictionary
#   BPA, 8/31/2019, Added error/exception handling
#   BPA, 9/3/2019, Added option to view list before adding new donor
# ------------------------------ #

import sys

# ----- DATA ----- #
# ---------------- #
donors = {}
dict_menu = {} # holds menu options (dispatch)
str_menu = ("""\n--------------------
Choose an action:
1 - Send a Thank You to a single donor
2 - Create a Report
3 - Send letters to all donors
4 - Quit
--------------------\n\n""") # holds menu options


# ----- PROCESSING ----- #
# ---------------------- #
def load_data():
    update_list("Bill Gates", 326892.24)
    update_list("Bill Gates", 326892.24)
    update_list("Mark Zuckerberg", 5465.39)
    update_list("Mark Zuckerberg", 5465.39)
    update_list("Mark Zuckerberg", 5465.39)
    update_list("Jeff Bezo", 877.33)
    update_list("Paul Allen", 236.14)
    update_list("Paul Allen", 236.14)
    update_list("Paul Allen", 236.14)
    update_list("M Bezo", 110463.25)


def main():
    """ main function """
    while True: # display a menu of choices to the user
        try:
            response = int(input(str_menu)) # refers to preset menu declared under Data
            dict_menu.get(response)()
        except TypeError:
            print("\nPlease choose an action from the above list.")
            print("Type the menu number associated with the action you would like to perform.")
        except ValueError:
            print("\nPlease choose an action from the above list.")
            print("Type the menu number associated with the action you would like to perform.")


def send_thank_you():
    """ option to add a new entry/donation amount to the list and print a thank you email"""
    while True:
        name = get_name()
        if name.upper() == "EXIT":
            return # return to main menu
        elif name.upper() == "LIST":
            current = current_donors() # Display current donors
            print(current)
            send_thank_you() # recursion - go to the beginning
            break
        else:
            donation = get_donation(name) # get the donation amount
            update_list(name, donation) # update the list with the name and/or donation amount
            print(print_thank_you(name, donation)) # print the thank you email
            break


def get_name():
    print("\nType 'exit' to return the main menu or 'list' to see a current list of donors.")
    name = input("Who would you like to send a Thank You to?: ").title().strip()
    return name


def current_donors():
    new_list = [key for key in donors.keys()] # create a list from the keys
    return "\nCurrent donors are: " + ", ".join(new_list).title()


def get_donation(name):
    while True:
        try:
            donation = input(f"Type 'exit' to return the main menu. What was the donation amount for {name:s}?: ").strip() # gather donation
            print()
            if donation.upper() == "EXIT":
                return # return to main menu
            else:
                donation = float(donation)
                return donation
        except ValueError:
            print("Please enter a valid donation amount. \n")


def update_list(name, donation):
    """ udpdates list with name and/or donation amount """
    donors.setdefault(name.lower(), (name, [])) # create a key from the name if not found alreay in existance
    donors[name.lower()][1].append(donation) # append the donation to the list within the second item in the tuple value
    return donors


def print_thank_you(name, donation):
    """ prints a thank you email to be sent to the donor """
    frequency = ordinal_freq(len(donors[name.lower()][1])) # find the ordinal frequency
    total = total_given(donors[name.lower()][1]) # find the sum for the total amount given
    return (f"""
Dear {name},

    We are reaching out to thank you for your {frequency} donation. We appreciate your 
    continued support. You have donated a total of {total:.02f} USD. Your recent docation 
    of {donation:.02f} USD will go towards clean food and water for your local citizens 
    in need.
    
    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team
        """) # print the email to the donor


def ordinal_freq(fq):
    """ converts the number of times donated to an ordinal number """
    if fq == 1 or (fq % 10 == 1 and fq != 11):
        fq = (f"{fq}st") # format with 'st'
    elif fq == 2 or (fq % 10 == 2 and fq != 12):
        fq = (f"{fq}nd") # format with 'nd'
    elif fq == 3 or (fq % 10 == 3 and fq != 13):
        fq = (f"{fq}rd") # format with 'rd'
    else:
        fq = (f"{fq}th") # format with 'th'
    return fq


def total_given(sub_list):
    """ calculates the total amount donated by a donor """
    total_sum = sum(sub_list) # sum all entries in the donation list
    return total_sum


def send_all_letters():
    """ option to print/write thank you emails to all donors"""
    location = get_location()
    for key, value in donors.items(): # for each dictionary entry in the donor list
        name = value[0] # take the donor name
        recent_donation = value[1][-1] # and the last donation amount made
        if location == "": # if there is no specified location, don't pass it though
            write_send_all(name, recent_donation) # print the thank you email
        else: # if there is a specified location, pass it though
            try:
                write_send_all(name, recent_donation, location)
            except FileNotFoundError:
                print("Please try again and enter a valid location.")
                return # return to main menu
    print("Letters have been saved!")


def get_location():
    while True:
        response = input("Do you want to set a specific directory? (Y/N): ")
        if response.upper() == "Y":
            location = input("Where you you like the letters saved?: ") + "\\"
            return location
        elif response.upper() == "N":
            return ""
        else:
            print("Please enter either 'Y' for Yes or 'N' for No. \n")


def write_send_all(name, donation, location = "./"):
    """ prints/writes thank you emails to be sent all donors """
    total = total_given(donors[name.lower()][1]) # find the sum for the total amount given
    obj_file_name = location + name.replace(" ", "_") + ".txt" # create file name for current folder
    with open(obj_file_name, "w") as outfile: # open file in write mode
        outfile.write(f"""Dear {name},

    We are reaching out to thank you for your continued support.

    You have donated a total of {total:.02f} USD. Your recent docation 
    of {donation:.02f} USD will go towards clean food and water for your local citizens 
    in need.

    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team""") # write the letter to the donor in a txt file and save the file


def reporting_main():
    report_items = create_report()
    display_report(report_items)


def create_report():
    """ prints current data in list in a reporting format """
    donor_items = [] # define/empty list
    for key, value in donors.items(): # for each donor...
        name = value[0] # get the name
        total = round(total_given(donors[name.lower()][1]), 2) # get the total donation amount
        count = len(value[1]) # find the number of donations
        avg = round(total/count,2) # take the average
        donor_items.append((name, total, count, avg)) # create a new list with summation information
    return donor_items


def display_report(report_items):
    header = "\nDonor Name                    |Total Given    |Num Gifts |Average Gift   "
    header2 = "-------------------------------------------------------------------------"
    print(header + "\n" + header2)
    from operator import itemgetter
    for row in sorted(report_items, key=itemgetter(1), reverse=True): # sort and print in a fixed length format
        print("{:<30}|{:>15}|{:>10}|{:>15}".format(row[0], row[1], row[2], row[3]))


def quit_program():
    sys.exit()


# ----- PRESENTATION ----- #
# ------------------------ #
if __name__ == '__main__':
    dict_menu = {1: send_thank_you, 2: reporting_main, 3: send_all_letters, 4: quit_program} # holds menu options (dispatch)
    load_data()
    main() # run main
