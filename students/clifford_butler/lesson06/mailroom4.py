# -*- coding: utf-8 -*-
"""
Created on Mon April 27 2020

@author: cliff
"""

#!/usr/bin/env python3
'''
Use dicts where appropriate.
Part 1 of this assignment used these basic data types: numbers, strings, 
ists and tuples.

However, using dictionaries, covered in Lesson 4, will let you re-write 
your program a bit more simply and efficiently.

Update your mailroom program to:

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
See if you can use a dict to switch between the users selections. 
see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the letter 
as one big template, rather than building up a big string that 
produces the letter in parts.
'''

import sys
import operator

prompt_name = "\n".join(("Type the donors full name or,",
              "type 'list' to display a list of the donors names.",
              ">>> "))

prompt_amount = "\n".join(("Whats the donation amount?",
                ">>> "))

exit_report = "\n".join(("Press 1 to exit to the initial prompt.",
                         "\n"))

def donors():
    # dictionary of donors and donation amounts
    return {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos":  [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Alexandra Butler": [777.77, 44.44]}

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
            donor_dict[donor_name] = []
            print (donor_dict)
            break

def display_dict():
    # use of comprehension to display a list of the donors
    show_list = [print(i) for i in donor_dict.keys()]   
            
def send_thank_you():
    # Request the user to input donor name, and donation information.
    response = str(input(prompt_name))
    while response.lower() == 'list':
        display_dict()
        response = str(input(prompt_name))
       
    else:
        try:
            response_amount = float(input(prompt_amount))
        except ValueError:
            print('Input must be a number. Donor information not entered. Try again!')
        else:
            if response in donor_dict.keys():
                donor_dict[response].append(response_amount)
            
            else:
                donor_dict[response] = [response_amount]
               
            print(f"Hi {response},\n\nThank you for the generous donation of {response_amount}.\n\nSincerely,\nClifford Butler")

def create_report():
    # Generate and display a report of the donors in donor_dict
    while True:
        print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
        print ('-'*90)

        for donor, value in sorted(donor_dict.items(), key=operator.itemgetter(1)):
            print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(donor, '$', round(sum(value),2), len(value), '$',round(sum(value)/len(value),1))))

        
        response_quit = input(exit_report)
        # Return back to the initial prompt
        if response_quit == "1":
            break
        
        else:
            print("Not a valid option!")      
        
def letter_to_all():
    for donor_name in donor_dict:
        with open(f"{donor_name}.txt","w+") as donor_letter:
            donor_letter.write(f"Hi {donor_name},\n\nThank you for the generous donation of ${sum(donor_dict[donor_name]):.2f}.\n\nSincerely,\nClifford Butler")
    return("Thank you letters sent!")
            
def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit()  

def main():
    # continuously collect user selection
    switch_dict = {
            1: send_thank_you, 
            2: create_report, 
            3: letter_to_all, 
            4: exit_program
            } 
    
    # get user response for nagivating the program
    while True:
        try:
            response = int(input(prompt))
        except ValueError:
            print('Not a valid option! Enter 1, 2, 3, or 4\n')
        else: 
            if response not in switch_dict:
                print('Not a valid option! Enter 1, 2, 3, or 4\n')
            else:
                switch_dict.get(response)()
    switch_dict.get(response)()

if __name__ == "__main__" :
    # run main function
    donor_dict = donors()
    main()
   