#!/usr/bin/env python3

import sys
from collections import OrderedDict

#switch between users selections
#change exit menu
def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        dispatch_dict[response]()

#this is for the thank you menu - change exit menu to break?
def sub_menu_selection(prompt, dispatch_dict):
    while True:
        response = input(sub_prompt).title()
        if response in dispatch_dict:
            dispatch_dict[response]() == "exit menu"
            break
        else:
            donation = input("Please enter in a donation, or 'q' to quit: ")
            if donation == "q":
                break
            else:
                add_donation(response, donation)
                thankyou_email(response, donation)
                break

def add_donation(name, donation):
    if name in donors:
        donors[name].append(int(donation))
    else:
        donors[name] = [int(donation)]
    #print(donors)

def thankyou_email(name, donation):
    """Prints the letter with the user inputted name and donation """
    email_dict = {}
    email_dict["name"] = name
    email_dict["donation"] = int(donation)

    print("""
    Dear {name},
    Thank you very much for the generous donation of ${donation:,.2f}
    It is very much appreciated.
    Respectfully,

    Eric G.
    """.format(**email_dict))

def thank_you():
    sub_menu_selection(sub_prompt, sub_dispatch)

def sort_key(items):
    """Sort key for the sorted list in create report"""
    return items[1]

#make this a formatted dict
def create_report():
    new_dict = {}
    print("{:<25s}|{:>15s} |{:>10s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(68 * '-')
    for k,v in donors.items():
        sum_don = sum(donors.get(k))
        len_don = len(donors.get(k))
        avg_don = sum_don/len_don
        new_dict[k] = [sum_don, len_don, avg_don]

    sorted_donors2 = OrderedDict(sorted(new_dict.items(), key=lambda t: t[1], reverse=True))

    for k,v in sorted_donors2.items():
        print("{:<25s}|${:>14.2f} |{:>10.0f} |${:>12.2f}".format(k, v[0], v[1], v[2]))
    print()

def send_letters():
    for donor,donation in donors.items():
        #print(donor,donation)
        with open(donor.replace(" ", "_") + '.txt', 'w+') as f:
           f.write("This is a test for {}".format(donor))
       

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
