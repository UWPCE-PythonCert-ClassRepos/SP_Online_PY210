#!/bin/user/env python3

#Runs the user interface and uses Donor Collection

import pathlib

from donor_models import *


def menu_dispatch(prompt, menu):
    """prints prompt and uses response to call functions from a dictionary"""
    while True: 
        try:
            response = input(prompt).upper()
            if menu[response]() == "quit":
                break
        except KeyError:
            print(f"{response} is not an option")

def send_thank_you():
    """Records a new donation and thanks the donor"""
    #Find out who to thank
    name = 'List'
    while name == 'List':
        print(donors.make_list())
        #Ensure correct capitalization
        try:
            name = input("Enter Doners Full Name> ").strip().title()                
        except EOFError:
            #If this happens, the user may be trying to quit
            print("End of file detected, leaving program")
            return False
        #Allow user to leave mid task
        if name == 'Q':
            return False
        if name not in donors:
            new_name = input("Create new entry? (Y/N)> ").strip().upper()
            if new_name == "N":
                name = "List"
    #Enter ammount
    while True:
        try:
            money = float(input("Enter ammount donated> "))
            break
        except ValueError:
            print("Please enter a number")
    donors[name].add_donation(money)
    print(donors[name].thank_you())

def create_a_report():
    print(donors.report())

def send_letters():
    """Creates a letter for each donor thanking them for there latest donation"""
    path = pathlib.Path("./letters")
    if not path.exists(): 
        path.mkdir()
    for donor in donors:
        with open(f"./letters/{donor.full_name}.txt", "w") as file:
            file.write(donor.letter())
    
def exit_menu():
    return "quit"

#Holds main menu data
main_menu = {'S': send_thank_you,
             'C': create_a_report,
             'L': send_letters,
             'Q': exit_menu}

#Main menu prompt 
main_prompt = "(S)end a Thank you | (C)reate a Report | Send (L)etters to all donors | (Q)uit >"

if __name__ == "__main__":#Generate list of donors
    donors = DonorCollection.from_list([Donor("Nick Esen", [1800, 720]),
                              Donor("Sabina", 1500),
                              Donor("Marceline Theodosia", [30000, 500000, 100]),
                              Donor("Rafat Rein", 1500000),
                              Donor("Kevin Both", [150, 1200, 750])])
    menu_dispatch(main_prompt, main_menu)