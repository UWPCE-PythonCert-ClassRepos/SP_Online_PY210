#!/usr/bin/env python

'''
Overall Program Goal:
You work in the mail room at a local charity. 
Part of your job is to write incredibly boring, 
repetitive emails thanking your donors for their 
generous gifts. You are tired of doing this over 
and over again, so you’ve decided to let Python 
help you out of a jam and do your work for you.

The Program: Part 1
Write a small command-line script called 
mailroom.py. This script should be executable. 
The script should accomplish the following goals:

It should have a data structure that holds a list 
of your donors and a history of the amounts they 
have donated. This structure should be populated 
at first with at least five donors, with between 
1 and 3 donations each. You can store that data 
structure in the global namespace.
The script should prompt the user (you) to choose 
from a menu of 3 actions: “Send a Thank You”, 
“Create a Report” or “quit”.
'''

import sys

donor_dict = [
        ["William Gates, III", 653772.32, 12.17],
        ["Jeff Bezos", 877.33],
        ["Paul Allen", 663.23, 43.87, 1.32],
        ["Mark Zuckerberg", 1663.23, 4300.87, 10432.0],
        ["Clifford Butler", 777.77, 44.44],
        ]

prompt = "\n".join(("Welcome to the mail room!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

prompt_name = "\n".join(("Type the donors name or,",
          "type 'list' to display a list of the donors names.",
          ">>> "))

prompt_amount = "\n".join(("Whats the donation amount?",
          ">>> "))

def get_index(donor_name):
    # Return the index number based on user input
    for item in (donor_dict):
        if item[0] == donor_name:
            index = donor_dict.index(item)
            return index
        
    return None

def view_list():
    # Display the donor list.
    print("\n".join(donor_dict))

def send_thank_you():
    # Request the user to input donor name, and donation information.
    response = str(input(prompt_name))
    while response == 'list':
        for names_in_list in donor_dict:
            print(names_in_list[0])
            
        response = str(input(prompt_name))
        
    for names_in_list in donor_dict:
        if names_in_list[0] == response:
            response_amount = input(prompt_amount)
            x = get_index(response) 
            donor_dict[x].append(float(response_amount))
            print (donor_dict)

def create_report():
    # place holder
    pass

def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit()  

def main():
    # continuously collect user selection
    while True:
        response = input(prompt)  
        # redirect to feature functions based on the user selection
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__" :
    # run main function
    main()
    
    