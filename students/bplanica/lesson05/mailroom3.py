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

# ----- DATA ----- #
# ---------------- #
donors = {"bill gates": ("Bill Gates", [326892.24, 326892.24]),
"mark zuckerberg": ("Mark Zuckerberg", [5465.39, 5465.39, 5465.39]),
"jeff bezo": ("Jeff Bezo", [877.33]),
"paul allen": ("Paul Allen", [236.14, 236.14, 236.14]),
"m bezo": ("M Bezo", [110463.25])} # holds original data set to start with

dict_menu = {} # holds menu options (dispatch)
str_menu = ("""--------------------
Choose an action:
1 - Send a Thank You to a single donor
2 - Create a Report
3 - Send letters to all donors
4 - Quit
--------------------

""") # holds menu options


# ----- PROCESSING ----- #
# ---------------------- #
def main():
    """ main function """
    while True: # display a menu of choices to the user
        try:
            response = int(input(str_menu)) # refers to preset menu declared under Data
            if response == 4: raise SystemExit
            dict_menu.get(response)()
        except TypeError:
            print("\nPlease choose an action from the above list.")
            print("Type the menu number associated with the action you would like to perform.")
        except ValueError:
            print("\nPlease choose an action from the above list.")
            print("Type the menu number associated with the action you would like to perform.")


def one_ty_name(name = ""):
    """ option to add a new entry/donation amount to the list and print a thank you email"""
    if name == "":
        print("\nType 'exit' to return the main menu or 'list' to see a current list of donors.")
        name = input("Who would you like to send a Thank You to?: ").title().strip() # gather name
    if name.upper() == "EXIT":
        return # return to main menu
    elif name.upper() == "LIST":
        new_list = [key for key in donors.keys()] # create a list from the keys
        print("\nCurrent donors are:", ", ".join(new_list).title()) # print list to user
        one_ty_name() # recursion - go to the beginning
    else:
        one_ty_donation(name) # get the donation amount


def one_ty_donation(name):
    """option to add a new entry/donation amount to the list and print a thank you email"""
    try:
        donation = input(f"Type 'exit' to return the main menu. What was the donation amount for {name:s}?: ").strip() # gather donation
        print()
        if donation.upper() == "EXIT":
            return # return to main menu
        else:
            donation = float(donation)
    except ValueError:
        print("Please enter a valid donation amount. \n")
        one_ty_donation(name) # recursion - go to the beginning
    else:
        update_list(name, donation) # update the list with the name and/or donation amount
        print_email(name, donation) # print the thank you email


def all_thank_you():
    """ option to print/write thank you emails to all donors"""
    location = ""
    response = input("Do you want to set a specific directory? (Y/N): ")
    print()
    if response.upper() == "Y":
        location = input("Where you you like the letters saved?: ") + "\\"
        print()
    elif response.upper() == "N":
        pass
    else:
        print("Please try again and enter either 'Y' for Yes or 'N' for No. \n")
        return # return to main menu
    for kay, value in donors.items(): # for each dictionary entry in the donor list
        name = value[0] # take the donor name
        donation = value[1][-1] # and the last donation amoutn made
        if location == "": # if there is no specified location, don't pass it though
            all_print_email(name, donation) # print the thank you email
        else: # if there is a specified location, pass it though
            try:
                all_print_email(name, donation, location)
            except FileNotFoundError:
                print("Please try again and enter a valid location. \n")
                return # return to main menu
    print("Letters have been saved! \n")


def update_list(name, donation):
    """ udpdates list with name and/or donation amount """
    donors.setdefault(name.lower(), (name, [])) # create a key from the name if not found alreay in existance
    donors[name.lower()][1].append(donation) # append the donation to the list within the second item in the tuple value


def ordinal_freq(name):
    """ converts the number of times donated to an ordinal number """
    fq = len(donors[name.lower()][1]) # get the count of the list for donations
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
    total_sum = 0
    total_sum = sum(donors[name.lower()][1]) # sum all entries in the donation list
    return total_sum


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
    
    We look forward to seeing you at our upcoming fundraiser event. 

Sincerely, 

The Fundraiser Team
        """) # print the email to the donor


def all_print_email(name, donation, location = "./"):
    """ prints/writes thank you emails to be sent all donors """
    total = total_given(name) # find the sum for the total amount given
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


def create_report():
    """ prints current data in list in a reporting format """
    header = "Donor Name                    |Total Given    |Num Gifts |Average Gift   "
    header2 = "-------------------------------------------------------------------------"
    print(header)
    print(header2)

    sub_list = [] # define/empty list
    for key, value in donors.items(): # for each donor...
        name = value[0] # get the name
        total = round(total_given(name), 2) # get the total donation amount
        count = len(value[1]) # find the number of donations
        avg = round(total/count,2) # take the average
        sub_list.append((name, total, count, avg)) # create a new list with summation information

    from operator import itemgetter
    for row in sorted(sub_list, key=itemgetter(1), reverse=True): # sort and print in a fixed length format
        print("{:<30}|{:>15}|{:>10}|{:>15}".format(row[0], row[1], row[2], row[3]))
    print()


# ----- PRESENTATION ----- #
# ------------------------ #
if __name__ == '__main__':
    dict_menu = {1: one_ty_name, 2: create_report,
        3: all_thank_you} # holds menu options (dispatch)
    main() # run main
