#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:53:34 2019

@author: humberto gonzalez
"""

import sys  
import tempfile
import os


donor_db = {"Tyrod Taylor": [1000.00, 45.50],
            "Jarvis Landry": [150.25],
            "Philip Rivers": [650.23, 40.87, 111.32],
            "Melvin Gordon": [1677.25, 4300.23, 10532.00],
            "Mike Williams": [230.56, 12.45, 11.00],
            "Antonio Brown": [100.00, 88.88]
            }

donors = list(donor_db.keys())

def getKey(item):
    return item[1]

def ordered_db(db):
    keys = list(db.keys())
    temp = []
    for name in keys:
        donation_total = sum(db[name])
        temp.append((name,donation_total))
    return sorted(temp, key=getKey,reverse=True)
    
        
    
    
main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a report",
              "3 - Send letters to all donors",
              "4 - Exit Program",
              ">>> "))

    

def send_thank_you():
    '''Prompts user for a donor and donation amount, and then prints out a thank you email'''
    donor_name = input('What is the full name of the donor you would like to thank? ')
    if donor_name.lower() == "quit":
        main()
    if donor_name not in donors:
        donor_db[donor_name] = []
    try:
        donation = input('What was the donation amount? ')
        a = float(donation)
    except ValueError as e:
        print('Donation amount needs to be a number, please enter a number')
        donation = input('What was the donation amount? ')
    if donation.lower()=="quit":
        main()
    donor_db[donor_name].append(float(donation))
    print()
    print()
    print(f'Dear {donor_name},\n    Thank you for your generous donation of ${donation}')



def create_report():
    '''Creates a report of the current donor database'''
    print('{:20} | {:^10} | {:^10} | {:^10} |'.format("Donor Name",
          "Total Given","Num Gifts","Average Gift"))
    print('-'*64)
    formatter = "{:20}   ${:>10}   {:>10}   ${:>10}"
    ordered_donor_db = ordered_db(donor_db)
    for donor_item in ordered_donor_db:
        donor_info = donor_item[0]
        donations = donor_db[donor_info]
        total = round(sum(donations),2)
        num = len(donations)
        average = round(total/num,2)
        print(formatter.format(donor_info,total,num,average))



def send_letters():
    '''Writes and saves letters to all donors in the database
       in the form of txt files'''
    formatter = '''Dear {},\n    Thank you for your generous donation of ${}. \n    Your donation will be put to great use. \n         Sincerely, \n          -The Organization'''
    path = tempfile.gettempdir()
    path = path + "/" + "Letters to Donors"
    os.mkdir(path)
    for donor in donor_db:
        temp = path + "/" + donor.replace(' ','_') + '.txt'
        with open(temp,'w') as file:
            txt = formatter.format(donor,donor_db[donor][0])
            file.write(txt)
            file.close()
    print('Letters have been created and saved to \n a new folder in your temp directory')
            
        
def exit_program():
    print("Bye!")
    sys.exit()

def main():
    while True:
        response = input(main_prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        menu_options = {"1":send_thank_you,
                        "2":create_report,
                        "3":send_letters,
                        "4":exit_program}
        if response not in menu_options:
            print()
            print("Please select one of the available options")
            print("You will be returned to the main menu")
            main()
        menu_options.get(response)()


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()


















