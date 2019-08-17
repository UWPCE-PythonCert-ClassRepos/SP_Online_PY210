#!/usr/bin/env python3

# ------------------------------ #
# Assignment 3 (Mailroom Part 1) for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/11/2019, Created and tested script
# ------------------------------ #

# ----- DATA ----- #
# ---------------- #
DonorLst = [["Bill Gates", 326892.24, 326892.24],
["Mark Zuckerberg", 5465.39, 5465.39, 5465.39], 
["Jeff Bezo", 877.33], 
["Paul Allen", 236.14, 236.14, 236.14], 
["M Bezo", 110463.25]] # holds original data set to start with

strMenu = (""" 
*************************************
     Menu of Options
     1) Send a Thank You
     2) Create a Report
     3) Exit
*************************************
     """) # holds menu options


# ----- PROCESSING ----- #
# ---------------------- #

def main():
    """ main function """
    while True: # display a menu of choices to the user
        print(strMenu) # refers to preset menu declared under Data
        strChoice = str(input("Which option would you like to perform? ")).strip() # gathers the user's choice
        print() # adding a new line

        if strChoice == "1": # gathers new informaiton and print email to send to donor
            thank_you()
            continue
        elif strChoice == "2": #  prints current data in list in a reporting format
            print_report()
            continue
        elif strChoice == "3": # exits the program
            break


def thank_you():
    """ option to add a new entry to the list and print a thank you email"""
    name = input("Type 'exit' to return the main menu. Who would you like to send a Thank You to?: ").strip() # gather name
    if name.upper() == "EXIT":
        return # return to main menu
    donation = input(f"Type 'exit' to return the main menu. What was the donation amount for {name:s}?: ").strip() # gather donation
    if donation.upper() == "EXIT":
        return # return to main menu
    else:
        donation = float(donation)
    update_list(name, donation) # update the list with the name and/or donation amount
    print_email(name, donation) # print the thank you email


def update_list(name, donation):
    """ udpdates list with name and/or donation amount """
    match = False # set flag
    for row in DonorLst:
        if name == row[0]: # if the name is found...
            row.append(donation) # add the donation amount
            match = True # mar flag as found
    if match == False: # if not found...
        sub_List = [name, donation] # create a new inner list for the donor
        DonorLst.append(sub_List) # add the name and donation amount to the list


def ordinal_freq(name):
    """ converts the number of times donated to an ordinal number """
    for row in DonorLst:
        if name == row[0]: # if the name is found...
            fq = (len(row) - 1) # take the count of list entries, minus the name to get the count of donations
            if fq == 1 or (fq % 10 == 1 and fq != 11):
                fq = (f"{fq}st") # format with 'st'
            elif fq == 2 or (fq % 10 == 2 and fq != 12):
                fq = (f"{fq}nd") # format with 'nd'
            elif fq == 3 or (fq % 10 == 3 and fq != 13):
                fq = (f"{fq}rd") # format with 'rd'
            else:
                fq = (f"{fq}th") # format with 'th'
            return fq


def total_given(name):
    """ calculates the total amount donated by a donor """
    for row in DonorLst:
        if name == row[0]: # if the name is found...
            i = 1
            sum = 0
            while i < len(row):
                sum = sum + row[i] # sum for the total amount given
                i += 1
    return sum


def print_email(name, donation):
    """ prints a thank you email to be sent to the donor """
    frequency = ordinal_freq(name) # find the ordinal frequency
    total = total_given(name) # find the sum for the total amount given
    print(f"""
Dear {name},

    We are reaching out to thank you for your {frequency} donation. We appreciate your 
    continued support. You have donated a total of {total:.02f} USD. Your recent docation 
    of {donation:.02f} USD will go towards clean food and water for your local citizens 
    in need.
    
    We look forward to seeing you at our upcoming funraiser event. 

Sincerely, 

The Fundraiser Team
        """) # print the email to the donor

def print_report():
    """ prints current data in list in a reporting format """
    header = "Donor Name                    |Total Given    |Num Gifts |Average Gift   "
    header2 = "-------------------------------------------------------------------------"
    print(header)
    print(header2)

    sub_List = [] # define/empty list
    for row in DonorLst: # for each donor...
        name = row[0]
        total = round(total_given(name), 2)
        count = len(row) - 1
        avg = round(total/count,2)
        sub_List.append((name, total, count, avg)) # create a new list with summation information
    from operator import itemgetter
    for row in sorted(sub_List, key=itemgetter(1), reverse=True): # sort and print in a fixed length format
        print("{:<30}|{:>15}|{:>10}|{:>15}".format(row[0], row[1], row[2], row[3]))


# ----- PRESENTATION ----- #
# ------------------------ #

if __name__ == '__main__':
    main() # run main
