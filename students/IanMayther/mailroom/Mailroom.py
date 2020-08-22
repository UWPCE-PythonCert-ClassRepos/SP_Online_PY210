#!/usr/bin/env python3

#Donors
donors = [("Morgan Stanely", [0.01, 20.00]),
            ("Cornelius Vanderbilt", [800, 15, 10]),
            ("John D. Rockefeller", [7000, 150, 25]),
            ("Stephen Girard", [60000]),
            ("Andrew Carnegie", [0.04, 999.99])]


#Send Thank You
def receiver(giver):
    name = giver
    #Determine Previous Donor
    if giver == "list":
        for i in range(len(donors)):
            print(f"[{i+1}] " + donors[i][0])
        existing = False
        while existing:
            num = input("Please select the corresponding number for existing donor? ")
            if (int(num)-1) in range(len(donors)):
                print(f"You selected: {donors[int(num)-1]}")
                existing = True
    else:
        new = input("Is this a new donor; [Y] or [N]?")
        if new.upper() == "Y":
            name = new
        else:
            print("My mistake")
    return name

#Create Report

#Main Exicutable
if __name__ == '__main__':
    #Initial Menu
    real_response = False
    while real_response == False:
        directive = input("What would you like to do; [1]Send Thank you, [2]Create Report, [3]Quit: ")
        if directive == "1" or directive == "2" or directive == "3":
            if directive == "1":
                #Launch Send Thank you
                print("Send Thank You")
                grat = input("Who would you like to send a Thank You to? Enter 'list' for a list of previous donors.  ")
                receiver(grat.lower())
                print(grat)
                real_response = True
            elif directive == "2":
                #Launch Create Report
                print("Create Report")
                real_response = True
            elif directive == "3":
                #Quit
                print("Quiter")
                real_response = True
        else:
            print("Please select one of the options above")