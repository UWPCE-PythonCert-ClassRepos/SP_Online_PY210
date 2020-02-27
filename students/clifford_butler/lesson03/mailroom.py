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
        ["Alexandra Butler", 777.77, 44.44],
        ]

prompt = "\n".join(("Welcome to the mail room!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))

prompt_name = "\n".join(("Type the donors full name or,",
              "type 'list' to display a list of the donors names.",
              ">>> "))

prompt_amount = "\n".join(("Whats the donation amount?",
                ">>> "))

exit_report = "\n".join(("Press 1 to exit to the initial prompt.",
                         "\n"))

report_header = "\n".join(("Donor Name           | Total Given | Num Gifts | Average Gift",
                            "{:-^61}")).format('')

def dis_info():
    for item in donor_dict:
        spaces = ((20 - len(item[0]))*" ")
        
        sum_donations = sum(item[1:])
        sum_donations = round(sum_donations,2)
        num_gifts = len(item[1:])
        avg_gift = (str(round(sum_donations/num_gifts,2)))
        spaces_two = ((15 - len(str(sum_donations)))*' ')
        spaces_three = (42*" ")
        
        print(item[0], spaces, ('$'), sum_donations, spaces_two, num_gifts, spaces_three, ('$'), avg_gift)

def get_index(donor_name):
    # Return the index number based on user input
    for item in (donor_dict):
        if item[0] == donor_name:
            index = donor_dict.index(item)
            
            return index
        
    return None

def add_donor(donor_name):
    # Add donor name to the data structure.
    for item in donor_dict:
        if item[0] not in donor_dict:
            donor_dict.append([donor_name])
            break

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
            # Request the user for a donation amount.
            response_amount = input(prompt_amount)
            x = get_index(response) 
            donor_dict[x].append(float(response_amount))
            break
    
    else:
        # Add the name to the list
        add_donor(response)
        # Request the user for a donation amount.
        response_amount = input(prompt_amount)
        x = get_index(response)
        donor_dict[x].append(float(response_amount))
            
    print(
            f"Hi {response},\n\n"
            f"Thank you for the generous donation of {response_amount}.\n\n"
            f"Sincerely,\n"
            f"Clifford Butler"
            )
    
def create_report():
    # Generate and display a report of the donors in donor_dict
    while True:
        print(report_header)
        dis_info()
        
        response_quit = input(exit_report)
        # Return back to the initial prompt
        if response_quit == "1":
            print("fake exit")
            break
        else:
            print("Not a valid option!")
            break
            
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
    
    