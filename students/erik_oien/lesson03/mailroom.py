#!/usr/bin/env python3

import sys 

# creatign the doner database
donor_db = [
    ("Nathan Explosion", [39595, 35081, 93295]),
    ("Skwisgaar Skwigelf", [37198]),
    ("Toki Wartooth", [20037, 32892, 99788]),
    ("William Murderface", [87470, 86870, 4397]),
    ("Pickles", [87838, 60282, 26653])
]

# main menu for program 

def menu():
    while True:
        welcome_input = input(opening_promt)
        if welcome_input == "1":
            thank_you()
        elif welcome_input == "2":
            create_report()
        elif welcome_input == "3" or welcome_input.lower() == "quit":
            quit_program()
        else:
            print("Invalid option, please choose a number from the list below:")

# thank you menu
def thank_you():
    donor_list = donor_db
    while True:
        donor_name = input("Please choose a donor or type list to see previous donors.\nIf you would like to return to the menu type menu.\nIf you'd like to quit please type quit >>> ")
        past_donor = False
        if donor_name.lower() == "menu":
            menu()
        if donor_name.lower() == "quit":
            quit_program()
        if donor_name.lower() == 'list':
            past_donor = False
            for donor in donor_db:
                print(donor[0])
        else:
            for donor in donor_db:
                if donor_name.lower() == donor[0].lower():
                    past_donor = True
                    donation_amount = input("How much was the most recent donation from {}? >>> ".format(donor_name, donor[1]))
                    donor[1].append(int(donation_amount))
            if past_donor == False:
                print("Looks like this is a new donor, lets add them!")
                donation_amount = input("How much did {} donate? >>> ".format(donor_name))
                new_donor = (donor_name, [int(donation_amount)])
                donor_db.append(new_donor)
            email = thank_you_email(donor_name, donation_amount)
            print(email)
            return False

# create report menu

def create_report():
    donor_info = sorted(donor_db, key=sort_key, reverse=True)
    table_header()
    for donor in donor_info:
        row = [donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])]
        row_formatter(row)
    return_input = input("If you would like to return to the menu type menu.\nIf you'd like to quit please type quit >>> ")
    if return_input.lower() == "menu":
            menu()
    if return_input.lower() == "quit":
            quit_program()

# helper functions

# function to create email
def thank_you_email(donor, amount):
    email_text = "Dear {},\n\nThank you for your generous donation of ${}! As you certianly know, kittens\nand metal are awesome and your donation will insure that others will be able\nto enjoy kittens and metal.\n\nSincerely,\n\nKitten and Metal Charity \m/\n\n"
    return email_text.format(donor, amount)

# function for table header
def table_header():
    print("{:25}|{:12}|{:10}|{:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 62)

# function to format rows
def row_formatter(row):
    print("{:25}|${:11.2f}|{:10}|${:11.2f}".format(*row))

# function to quit program
def quit_program():
    print("Bye!")
    sys.exit()  

# sort key
def sort_key(donor_db):
        return sum(donor_db[1])

# prompts used in program

opening_promt = "\n".join(("Welcome to the mailroom!",
                "Please choose from the below options",
                "1 - Send a Thank You",
                "2 - Create a Report",
                "3 - Quit",
                ">>> "))

if __name__ == "__main__": 
    menu()