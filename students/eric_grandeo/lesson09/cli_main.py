#!/usr/bin/env python3

from mailroom_oo import *
import sys
from collections import OrderedDict
import os

donors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54]}

d = DonorCollection()

for k,v in donors.items():
    d.add_donor(k, v)


#switch between users selections, using a dict
def menu_selection(prompt, dispatch_dict):
    while True:
        #handle KeyError
        try:
            response = input(prompt)
            dispatch_dict[response](donors)
        except KeyError:
            print("Please select 1 through 4. \n")

#this function is for the submenu
def sub_menu_selection(prompt, dispatch_dict):
    while True:
        try:
            response = input(sub_prompt).title()
            #removes spaces and checks if there is a number
            if not response.replace(" ", "").isalpha():
                raise ValueError
        except ValueError:
            print("Please enter a name, list, or q to quit \n")
        
        else:
            if response in dispatch_dict:
                dispatch_dict[response](donors) == "exit menu"
                break
            else:
                try:
                    donation = input("Please enter in a donation, or 'q' to quit: ")
                    if donation == "q":
                        break
                    elif donation.isalpha():
                        raise ValueError
                    else:
                        d.add_donor(response, donation)
                        d.donor_obj(response).thank_you
                        #add_donation(response, donation, donors)
                        #thankyou_email(response, donation)    
                        break 
                except ValueError:
                    print("Please enter a number \n")        

                

#calls the sub menu function when thank you is selected from main menu
def thank_you(donors):
    sub_menu_selection(sub_prompt, sub_dispatch)



def quit_submenu(donors):
    return "exit menu"

def quit_program(donors):
    print("Good Bye")
    sys.exit()



main_prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Send letters to all donors",
          "4 - Quit",
          ">>> "))

#change quit program to just break the loop
main_dispatch = {"1" : thank_you,
                "2" : create_report,
                "3" : send_letters,
                "4": quit_program}

sub_prompt = "\n".join(("Please enter one of the following",
            "A full name",
            "Type list to see all name",
            "Enter 'q' to quit",
            ">>> "))

sub_dispatch = {"List" : display_donors,
                "Q" : quit_submenu}


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)



