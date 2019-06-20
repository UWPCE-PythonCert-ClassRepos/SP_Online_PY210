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

def new_ordered_db(db):
    temp = [(name, sum(donations)) for name, donations in donor_db.items()]
    return sorted(temp, key=getKey,reverse=True)
    
    
main_prompt = "\n".join(("Welcome to the Mailroom!",
              "Please choose from below options:",
              "1 - Send a Thank You",
              "2 - Create a report",
              "3 - Send letters to all donors",
              "4 - Exit Program",
              ">>> "))


def obtain_donation_info():
    """Prompts user for a donor and donation amount"""
    donor_name = input('What is the full name of the donor you would like to thank? ')
    if donor_name.lower() == "quit":
        main()
    donation = input('What was the donation amount? ')
    try:
        float(donation)
    except ValueError as e:
        print('Donation amount needs to be a number, please enter a number')
        donation = input('What was the donation amount? ')
    if donation.lower()=="quit":
        main()
    return donor_name, donation


def append_donation_info(donor_name,donation):
    """Given a donor and donation amount, appends the info to the database"""
    if donor_name not in donors:
        donor_db[donor_name] = []
    donor_db[donor_name].append(float(donation))


def test_append_donation_info():
    expected = {"Tyrod Taylor": [1000.00, 45.50],
                "Jarvis Landry": [150.25],
                "Philip Rivers": [650.23, 40.87, 111.32],
                "Melvin Gordon": [1677.25, 4300.23, 10532.00],
                "Mike Williams": [230.56, 12.45, 11.00],
                "Antonio Brown": [100.00, 88.88],
                "Tom Brady": [50.0]
                }
    append_donation_info('Tom Brady',50.0)
    assert donor_db == expected
    print('Test Passed')


def create_thank_you_txt(donor_name,donation):  
    """Creates thank you text for a given donor and donation amount"""
    txt = f'Dear {donor_name},\n    Thank you for your generous donation of ${donation}'
    return txt

def test_create_thank_you_txt():
    expected = 'Dear Tom Brady,\n    Thank you for your generous donation of $50.0'
    assert create_thank_you_txt('Tom Brady',50.0) == expected
    print('Test Passed')
    
def print_thank_you_txt(txt):
    """Given text, will print out the thank you note"""
    print()
    print()
    print()
    print(txt)

    
def send_thank_you():
    """Prompts user for a donor and donation amount, and then prints out a thank you email"""
    donor_name, donation = obtain_donation_info()
    append_donation_info(donor_name,donation)
    txt = create_thank_you_txt(donor_name,donation)
    print_thank_you_txt(txt)

def create_report(db):
    """Creates the rows needed to print out the report"""
    report_rows = []
    ordered_db = new_ordered_db(db)
    for donor_item in ordered_db:
        donor_info = donor_item[0]
        donations = donor_db[donor_info]
        total = round(sum(donations),2)
        num = len(donations)
        average = round(total/num,2)
        report_rows.append([donor_info,total,num,average])
    return report_rows
    

def test_create_report():
    expected = [['Melvin Gordon', 16509.48, 3, 5503.16],
                ['Tyrod Taylor', 1045.5, 2, 522.75],
                ['Philip Rivers', 802.42, 3, 267.47],
                ['Mike Williams', 254.01, 3, 84.67],
                ['Antonio Brown', 188.88, 2, 94.44],
                ['Jarvis Landry', 150.25, 1, 150.25]]
    assert create_report(donor_db) == expected
    print('Test Passed')
    
    
def display_report():
    """Creates a report of the current donor database"""
    print('{:20} | {:^10} | {:^10} | {:^10} |'.format("Donor Name",
          "Total Given","Num Gifts","Average Gift"))
    print('-'*64)
    formatter = "{:20}   ${:>10}   {:>10}   ${:>10}"
    for row in create_report(donor_db):
        donor_info = row[0]
        total = row[1]    
        num = row[2]
        average = row[3]
        print(formatter.format(donor_info,total,num,average))


def create_letter_txt(donor,donation):
    """ Given a donor and donation, drafts up a letter to send """
    formatter = '''Dear {},\n    Thank you for your generous donation of ${}. \n    Your donation will be put to great use. \n         Sincerely, \n          -The Organization'''
    txt = formatter.format(donor,donation)
    return txt


def test_create_letter_txt():
    expected = '''Dear Tom Brady,\n    Thank you for your generous donation of $50.0. \n    Your donation will be put to great use. \n         Sincerely, \n          -The Organization'''
    assert create_letter_txt('Tom Brady',50.0) == expected
    print('Test Passed.')


def send_letters():
    """Writes and saves letters to all donors in the database
       in the form of txt files"""
    path = tempfile.gettempdir()
    path = path + "/" + "Letters to Donors"
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    for donor in donor_db:
        donation = donor_db[donor][0]
        temp = path + "/" + donor.replace(' ','_') + '.txt'
        with open(temp,'w') as tfile:
            txt = create_letter_txt(donor,donation)
            tfile.write(txt)
    print('Letters have been created and saved to \n a new folder in your temp directory')
   

def test_send_letters():
    send_letters()   
    for donor in donor_db:
        path = tempfile.gettempdir()
        path = path + "/" + "Letters to Donors"
        temp = path + "/" + donor.replace(' ','_') + '.txt'
        assert os.path.exists(temp)
    print('Test Passed.')
    
        
def exit_program():
    print("Bye!")
    sys.exit()

def main():
    while True:
        response = input(main_prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        menu_options = {"1":send_thank_you,
                        "2":display_report,
                        "3":send_letters,
                        "4":exit_program}
        try:
            menu_options.get(response)()
        except Exception as e:
            print()
            print("Please select one of the available options")
            print("You will be returned to the main menu")
            continue
        


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()


















