import sys
from operator import itemgetter
import os
from donor_models import *


#Show list of names
def send_thank_you():
    """Finds name of who should be thanked, calls donation and email functions"""
    name = input("Who would you like to thank?>")
    if name.lower() == 'quit':
        return
    
    #show the list of names using show_list function
    while name.title() == 'List':
        print(donor_dict.list_donors())
        name = input("Who whould you like to thank?>")
        if name.lower() == 'quit':
            return
    while True:
        try:
            donation = float(input("Please enter an amount to donate >"))
        except ValueError:
            if donation.lower() == 'quit':
                return
            donation = float(input(f"\nInvalid response.\n\nEnter a number.\n\nPlease enter an amount to donate >"))
        else:
            break

    donor_dict.sort_donation(name, donation)  
    donor_dict.compose_email(name)


# make the program quit
def quit_prog():
    """quits program"""
    print("Thank you. Goodbye!")
    sys.exit()


def thank_you_all():
    """writes a thank you email for all donors"""
    donor_dict.email_all()


def write_report():
    # create a variable as the length of each column other than  names. For ease of updating
    l = 15
    # same but for name column
    ln = 25
    #Create header names
    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    #Print header line
    print(f"\n{headers[0]:<{ln}}|{headers[1]:^{l}}|{headers[2]:^{l}}|{headers[3]:^{l}}")
    print("- "*int((l*3+3+ln)/2))
    report = donor_dict.build_report()
    sort_by_tot = sorted(report, key = itemgetter(1), reverse=True)
    for name,total,donations,average in sort_by_tot:
        print(f"{name:<{ln}} ${total:>{l-1}.2f}{donations:>{l+1}} ${average:>{l-3}.2f}")


if __name__ ==  '__main__':
    #Create a database
    jen = Donor('Jenny Jones', [272.00, 8700.11, 4.22])
    ste = Donor('Steve Martin', [85000.00, 12345.67, 54321.99])
    che = Donor('Cher', [0.01, 0.01])
    aba = Donor('Aba Ababa', [101.01, 10101.01, 1100.10])
    juan = Donor('Juan Doe Nation', [1.00])
    database = [jen, ste, che, aba, juan]
    donor_dict = DonorCollection()
    for donor in database:
        donor_dict.new_donor(donor)
    
        
    #Create a dictionary to switch between input options
    switch_dict = {
        '1': send_thank_you,
        '2': write_report,
        '3': thank_you_all,
        '4': quit_prog,
        'quit': quit_prog
        }
    
    while True:
        try:
            prompt = input("Choose:\n"
                           "1) Send a Thank you\n"
                           "2) Create a Report\n"
                           "3) Send letters to all donors\n"
                           "4) Quit \n"
                           "Respond with 1, 2, 3 or 'quit'>")                       
            switch_dict.get(prompt,"nothing")()
        except TypeError:
            print(f"\nInvalid response.\n\n")