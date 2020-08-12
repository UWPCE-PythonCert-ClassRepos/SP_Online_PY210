#!/usr/bin/env python3
"""
Christine Kim
Lesson 9
Client class
"""
import sys
from donor_models import Giver
from donor_models import GiverCollection

#Donor dictionary created 

givetree = GiverCollection({"Cullen Rutherford": Giver("Cullen Rutherford", [1500, 4200, 50000]),
                            "Alistair Theirin": Giver("Alistair Theirin", [200, 80000, 1500000]),
                            "Zevran Arainai": Giver("Zevran Arainai", [50]),
                            "Solona Amell": Giver("Solona Amell", [2, 500000, 2000000]),
                            "Soufehla Lavellan": Giver("Soufehla Lavellan", [70, 600])})

#Prompt for user to be displayed
prompt = ("\nWelcome to the Blight Orphans Charity. Plase select from the following options.\n"
                "1: Send a Thank You to a Single Donor\n"
                "2: Create a Report\n"
                "3: Send a Letter to All\n"
                "4: Quit\n")

# ---------------------------------------------------------------------------

#method for sending thank you to donor
def thank_you():
    #receive donor name from user input
    giver_name = input("\nPlease enter the full name in 'first name' 'last name' format,\n"
                    "or type 'list' to display names on the record: ")
    while giver_name.lower() == "list":
        #display list of donor names
        print(givetree.names())
        giver_name = input("\nPlease enter the full name of the donor: ")

    #in case of not full name
    while True:
        try:
            #split first/last name
            first_last = giver_name.split()
            first_name = first_last[0].capitalize()
            last_name = first_last[1].capitalize()
        #receive new info
        except IndexError:
            print("You've not entered a full name. Please enter the full name of the donor in 'first name' 'last name' format.")
            giver_name = input("\nPlease enter the full name of the donor in 'first last' format,\n"
                    "or type 'list' to display names on the record: ")
            while giver_name.lower() == "list":
                #display list of donor names
                print(givetree.names())
                giver_name = input("\nPlease enter the full name of the donor: ")
        else:
            break

    #update name with capitalized format
    giver_name = "{} {}".format(first_name, last_name)

    #catch bad user input
    while True:
        try:    
            #prompt user for donation amount
            received = int(float(input("\nPlease enter the amount of donation: ")))
        except ValueError:
            print("\nPlease enter a numeric donation amount")
        else:
            break

    giver = Giver(giver_name, received)

    #update donor information
    givetree.add_giver(giver, received)

    #print thank you email
    print(giver.gratitude(received))

# ---------------------------------------------------------------------------

#create donation histroy report for user
def report():
    #print report header
    header()
    #print report content
    givetree.report_givers()

#write report header
def header():
    print("\nBlight Orphans Charity Donation Report")
    header = "\n{:<30}|{:^15}|{:^10}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

# ---------------------------------------------------------------------------

#write letter to all donors
def letters():
    for person in givetree.dict_givers().values():
        with open(f"{person.name}.txt", "w") as outfile:
            outfile.write(person.gratitude(person.total_v()))

# ---------------------------------------------------------------------------

#quit the script
def end():
    print("\nThank you for your patronage. Farewell!\n")
    sys.exit()

# ---------------------------------------------------------------------------

#method for menu selection
def menu(prompt, dispatch_dict):
    while True:
        #receive user input
        response = input(prompt)
        #Catch bad user input
        try:
            #direct user to proper function
            dispatch_dict[response]()
        except KeyError:
            print("\nPlease choose from 1, 2, 3, or 4")

#main menu dictionary
menu_dict = {"1": thank_you,
            "2": report,
            "3": letters,
            "4": end}

if __name__ == '__main__':
    #initiate menu selection
    menu(prompt, menu_dict)