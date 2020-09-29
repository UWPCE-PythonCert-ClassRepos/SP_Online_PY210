#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:53:34 2019

@author: humberto gonzalez
"""

import sys  
import tempfile
import os
import operator


donor_db = {"Tyrod Taylor": [1000.00, 45.50],
            "Jarvis Landry": [150.25],
            "Philip Rivers": [650.23, 40.87, 111.32],
            "Melvin Gordon": [1677.25, 4300.23, 10532.00],
            "Mike Williams": [230.56, 12.45, 11.00],
            "Antonio Brown": [100.00, 88.88]
            }

donors = list(donor_db.keys())


main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a report",
              "3 - Send letters to all donors",
              "4 - Exit Program",
              ">>> "))

 
def create_report_db(db):
    '''Takes in the donor database and creates the required database to be used for printing out the report'''
    report_df = {}
    for donor in db:
           donations = db[donor]
           total = round(sum(donations),2)
           num = len(donations)
           average = round(total/num,2)
           report_df[donor] = [total,num,average]
    report_df = sorted(report_df.items(), key=operator.itemgetter(1),reverse=True)
    return report_df

def send_thank_you():
    '''Prompts user for a donor and donation amount, and then prints out a thank you email'''
    donor_name = input('What is the full name of the donor you would like to thank? ')
    if donor_name.lower() == "quit":
        main()
    if donor_name not in donors:
        donor_db[donor_name] = []
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
    report_db = create_report_db(donor_db)
    for donor_info in report_db:
        donor = donor_info[0]
        donation_info = donor_info[1]
        total = donation_info[0]
        num = donation_info[1]
        average = donation_info[2]
        print(formatter.format(donor,total,num,average))


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


















