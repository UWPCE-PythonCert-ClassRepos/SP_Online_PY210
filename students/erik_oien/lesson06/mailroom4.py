#!/usr/bin/env python3

import sys 
import os

donor_dict = {
    "Nathan Explosion": [39595, 35081, 93295], 
    "Skwisgaar Skwigelf": [37198], 
    "Toki Wartooth": [20037, 32892, 99788],
    "William Murderface": [87470, 86870, 4397],
    "Pickles": [87838, 60282, 26653],
}

# main menu for program 

def menu():
    while True:
        welcome_input = input(opening_promt)
        try:
            main_menu_switch[welcome_input]()
        except KeyError:
            print("Invalid option, please choose a number from the list below:")

# thank you menu
def thank_you():
    while True:
        donor_name = input(f"Please choose a donor or type list to see previous donors.\n{sub_menu_prompt}")
        past_donor = False
        if donor_name.lower() in ["menu", "quit"]:
            sub_menu_switch[donor_name.lower()]()
        elif donor_name.lower() == 'list':
            past_donor = False
            for donor in donor_dict.keys():
                print(donor)
        else:
            for donor in donor_dict:
                if donor_name.lower() == donor.lower():
                    past_donor = True
                    donation_amount = input("How much was the most recent donation from {}? >>> ".format(donor_name))
                    donor_dict_update(donor, donation_amount)
            if past_donor == False:
                print("Looks like this is a new donor, lets add them!")
                donation_amount = input("How much did {} donate? >>> ".format(donor_name))
                donor_dict_update(donor_name, donation_amount, new_donor=True)
        donor_info = [donor_name, donation_amount]
        letter = thank_you_letter(donor_info)
        print(letter)
        return False
   
# create report menu

def create_report():
    donor_dict_sorted = sorted(donor_dict.items(), key=lambda x: sum(x[1]), reverse=True)
    print(table_header())
    for donor in donor_dict_sorted:
        print(row_formatter(donor_info(donor)))
    return_input = input(f"{sub_menu_prompt}")
    if return_input in ["menu", "quit"]:
            sub_menu_switch[return_input.lower()]()
        
# send letters to all donors

def thank_all_donors():
    while True:
        dir_name = input(f"What would you like to call the directory?\n{sub_menu_prompt}")
        if dir_name.lower() in ["menu", "quit"]:
            sub_menu_switch[dir_name.lower()]()
            return False
        else:
            try:
                wd = os.getcwd()
                os.mkdir(wd + "/" + dir_name)
                for donor in donor_dict.items():
                    donor_facts = donor_info(donor, letters=True)
                    donor_letter = thank_you_letter(donor_facts, all_donors=True)
                    write_to_file(donor_letter, dir_name, donor_facts[0])
                return False
            except FileExistsError:
                print("Please try a different file name")

# function to create email
def thank_you_letter(donor_info, all_donors=False):
    if all_donors:
        letter_text = "Dear {},\n\n\tYou have made {} donations to the kittens and metal charity totaling ${}.\n\nThank you,\n\n\tKitten and Metal Charity"
    else:
        letter_text = "Dear {},\n\nThank you for your generous donation of ${}! As you certianly know, kittens\nand metal are awesome and your donation will insure that others will be able\nto enjoy kittens and metal.\n\nThank you,\n\nKitten and Metal Charity\n\n"
    return letter_text.format(*donor_info)

# function for table header
def table_header():
    return "\n".join(("{:25}|{:12}|{:10}|{:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"), "-" * 62))

# function to format rows
def row_formatter(row):
    return "{:25}|${:11.2f}|{:10}|${:11.2f}".format(*row)

# function to quit program
def quit_program():
    print("Bye!")
    sys.exit()  

# donor dict update

def donor_dict_update(donor, donation_amount, new_donor=False, donor_dict=donor_dict):
    if new_donor:
        donor_dict[donor] = [int(donation_amount)]
    else:
        donor_dict[donor].append(int(donation_amount))

# donor info

def donor_info(donor, letters=False):
    donor_name = donor[0]
    donation_sum = sum(donor[1])
    n_donotions = len(donor[1])
    if letters:
        return [donor_name, n_donotions, donation_sum]
    else:
        return [donor_name, donation_sum, n_donotions, donation_sum/n_donotions]

# create directory

def make_dir(dir_name):
    wd = os.getcwd()
    os.mkdir(wd + "/" + dir_name)

# write files to directory

def write_to_file(donor_letter, dir_name, file_name):
    wd = os.getcwd()
    file_path = wd + "/" + dir_name + "/" + file_name + ".txt"
    with open(file_path, "w") as f:
        f.write(donor_letter)

# using dictionary for switch

main_menu_switch = {
    "1": thank_you,
    "2": create_report,
    "3": thank_all_donors,
    "4": quit_program,
    "quit": quit_program,
}

sub_menu_switch = {
    "menu": menu,
    "quit": quit_program,
}

# prompts used in program

opening_promt = "\n".join(("Welcome to the mailroom!",
                "Please choose from the below options",
                "1 - Send a Thank You",
                "2 - Create a Report",
                "3 - Send letters to all donors",
                "4 - Quit",
                ">>> "))

sub_menu_prompt = "\n".join(("If you would like to return to the menu type menu.",
                    "If you would like to quit please type quit.",
                    ">>> "))

if __name__ == "__main__": 
    menu()
    