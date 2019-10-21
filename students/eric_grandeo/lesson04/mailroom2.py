#!/usr/bin/env python3

import sys

#switch between users selections
#change exit menu
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        dispatch_dict[response]()

#this is for the thank you menu
def sub_menu_selection(prompt, dispatch_dict):
    while True:
        response = input(sub_prompt).title()
        if response in dispatch_dict:
            dispatch_dict[response]() == "exit menu"
            break
        else:
            donation = input("Please enter in a donation, or 'q' to quit: ")
            add_donation(response, donation)

def add_donation(name, donation):
    if name in donors:
        donors[name].append(int(donation))
    else:
        donors[name] = [int(donation)]
    print(donors)


#modify this to take a name as input, hopefully this works, or create a submenu function
def thank_you():
    sub_menu_selection(sub_prompt, sub_dispatch)

def create_report():
    pass

def quit_submenu():
    return "exit menu"


def quit_program():
    sys.exit()

def display_donors():
    print(donors.keys())


#donors as a dict
donors = {"Bill Gates": [653772.32, 12.17],
          "Jeff Bezos": [877.33],
          "Paul Allen": [663.23, 43.87, 1.32],
          "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
          "Tim Cook": [1563.32, 8976.54]}

main_prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          ">>> "))

#change quit program to just break the loop
main_dispatch = {"1" : thank_you,
                "2" : create_report,
                "3" : quit_program,}

sub_prompt = "\n".join(("Please enter one of the following",
            "A full name",
            "Type list to see all name",
            "Enter 'q' to quit",
            ">>> "))

sub_dispatch = {"List" : display_donors,
                "Q" : quit_submenu}



#may need to change this to menu selection
if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
