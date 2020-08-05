#!/usr/bin/env python3
import sys
#Paths and File Processing
import pathlib

pth = pathlib.Path("./")
pth.is_dir()

#get path
pth.absolute()

#Christine Kim
#Python210 Lesson 5 Mailroom Part 3

#Donor dictionary created 
givetree = {("Rutherford", "Cullen"): (1500, 4200, 50000),
            ("Theirin", "Alistair"): (200, 80000, 1500000),
            ("Arainai", "Zevran"): (50,),
            ("Amell", "Solona"): (2, 500000, 2000000),
            ("Lavellan", "Soufehla"): (70, 600)}


#Prompt for user to be displayed
prompt = ("\nWelcome to the Blight Orphans Charity. Plase select from the following options.\n"
                "1: Send a Thank You\n"
                "2: Create a Report\n"
                "3: Send a Letter to All\n"
                "4: Quit\n")

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

#method for sending thank you to donor
def thank_you():
    #receive user input donor full name
    giver = input("\nPlease enter the full name of the donor in 'first last' format,\n"
                    "or type 'list' to display names on the record: ")
    while giver.lower() == "list":
        #display list of donor names
        print(list_names())
        giver = input("\nPlease enter the full name of the donor in 'first last' format: ")
    #in case of not full name
    while True:
        try:
            #split first/last name
            first_last = giver.split()
            first_name = first_last[0].capitalize()
            last_name = first_last[1].capitalize()
        #receive new info
        except IndexError:
            print("You've not entered a full name. Please enter the full name of the donor in 'first name' 'last name' format.")
            giver = input("\nPlease enter the full name of the donor in 'first last' format,\n"
                    "or type 'list' to display names on the record: ")
            while giver.lower() == "list":
                for last, first in givetree:
                    print("{} {}".format(first, last))
                giver = input("\nPlease enter the full name of the donor in 'first last' format: ")
        else:
            break
    #catch bad user input
    while True:
        try:    
            #prompt for donation amount
            received = int(float(input("\nPlease enter the amount of donation: ")))
        except ValueError:
            print("\nPlease enter a numeric donation amount")
        else:
            break
    #Update Existing donor
    if (last_name, first_name) in givetree:
        new_entry = {(last_name, first_name): (givetree.get((last_name, first_name))) + (received,)}
        givetree.update(new_entry)
    #Add New donor
    else:
        givetree.setdefault((last_name, first_name), (received,))
    
    #Compose gratitude email
    print(email(first_name, last_name, received))

#print list of donor names
def list_names(in_dict=givetree):
    names = ""
    for last, first in in_dict:
        names += "{} {}\n".format(first, last)
    return names

#create donation histroy report for user
def report():
    #print report header
    header()

    #sort by donation total
    sorted_Giver = sort()

    #summarize value and print report content
    #comprehension cleanup possible?
    for person in sorted_Giver:
        #get name tuple
        last_first = person[:1][0]
        #Summarize value
        total = total_v(person)
        donation_num = len(person[1:])
        average = total / donation_num
        #print content
        print("{:<14} {:<14}${:>15.2f}{:>10} ${:>15.2f}\n"
            .format(last_first[1], last_first[0], total, donation_num, average))

#write report header
def header():
    print("\nBlight Orphans Charity Donation Report")
    header = "\n{:<30}|{:^15}|{:^10}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

#sort by total donation
def sort(in_dict=givetree):
    return sorted(in_dict.items(), key=total_v, reverse=True)

#return the key for sorting = total amount of donation
def total_v(info):
    return sum(info[1:][0])

#create files of gratitude letters
#comprehension cleanup possible?
def letters():
    for l_name, f_name in givetree:
        with open(f"{f_name}_{l_name}.txt", "w") as dest:
            dest.write(email(f_name, l_name, total_v(("empty", givetree.get((l_name, f_name))))))

#Compose gratitude email
def email(first_name="first", last_name="last", amt=0):
    thanks = (f"\nDear Ser {first_name} {last_name},\n"
    f"Thank you for your generous donation of ${amt:,d}\n"
    "We will make certain your goodwill is directed to aid those affected by the Fifth Blight.\n"
    "With regards,\n"
    "The Blight Orphans Charity,\n")
    return thanks

#quit the script
def end():
    print("\nThank you for your patronage. Farewell!\n")
    sys.exit()

#main menu dictionary
menu_dict = {"1": thank_you,
            "2": report,
            "3": letters,
            "4": end}

if __name__ == '__main__':
    #initiate menu selection
    menu(prompt, menu_dict)