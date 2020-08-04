#!/usr/bin/env python3
import sys
#Paths and File Processing
import pathlib

pth = pathlib.Path("./")
pth.is_dir()

#get path
pth.absolute()

#Christine Kim
#Python210 Lesson 3 Mailroom Part 1

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
        #direct user to proper function
        dispatch_dict[response]()

#method for sending thank you to donor
def thank_you():
    #receive user input donor full name
    giver = input("\nPlease enter the full name of the donor in 'first last' format,\n"
                    "or type 'list' to display names on the record: ")
    while giver.lower() == "list":
        for last, first in givetree:
            print("{} {}".format(first, last))
        giver = input("\nPlease enter the full name of the donor in 'first last' format: ")

    #prompt for donation amount
    received = int(float(input("\nPlease enter the amount of donation: ")))

    #split first/last name
    first_last = giver.split(" ")
    first_name = first_last[0].capitalize()
    last_name = first_last[1].capitalize()

    #Update Existing donor
    if (last_name, first_name) in givetree:
        new_entry = {(last_name, first_name): (givetree.get((last_name, first_name))) + (received,)}
        givetree.update(new_entry)
    #Add New donor
    else:
        givetree.setdefault((last_name, first_name), (received,))
    
    #Compose gratitude email
    print(email(first_name, last_name, received))

#Create donation histroy report for user
def report():
    #print report header
    print("\nBlight Orphans Charity Donation Report")
    header = "\n{:<30}|{:^15}|{:^10}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print("-" * len(header))

    #sort by donation total
    sorted_Giver = sorted(givetree.items(), key=total_v, reverse=True)

    #summarize value and print report content
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

#return the key for sorting = total amount of donation
def total_v(info):
    return sum(info[1:][0])

def letters():
    for l_name, f_name in givetree:
        total = total_v(("empty", givetree.get((l_name, f_name))))
        with open(f"{f_name}_{l_name}.txt", "w") as dest:
            dest.write(email(f_name, l_name, total))

def email(first_name, last_name, amt):
    #Compose gratitude email
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