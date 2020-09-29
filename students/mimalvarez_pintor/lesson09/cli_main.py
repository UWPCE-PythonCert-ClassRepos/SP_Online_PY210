# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:00:40 2020

@author: miriam
"""

import sys
from donor_models import Donor
from donor_models import DonorCollection

donors = DonorCollection.initialize_dict(
    {'Miriam Pintor': [100, 300],
     'Waleed Alvarez': [500, 200, 800],
     'Ricardo Gallegos': [50, 75, 100],
     'Dina Sayury': [125, 120],
     'Urias Gramajo': [1000]})


# Main Menu
def options_menu():
    print("\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send Letters to all donors",
          "4 - Quit"
          ">>> ")))
    option = input('')
    return option

def quit_action():
    print("Bye")
    sys.exit()


def send_thankyou():
    donor_name = input ("Enter the donor's Full Name or 'list' for current"
                        "donors")

    while donor_name.lower() == "list":
        print(donors.donors_list())
        donor_name = input ("Please enter a  FULL Name ")
       
    try:       
        donation_amt = float(input ("Enter the Amount for donation "))             
    except ValueError:
        print("\n Invalid Amount. Please Enter a valid number \n")
    else:   
        if donors.donor_exists(donor_name) is False:
            donor = Donor(donor_name)
            donors.add(donor)
        else:
            donor = donors.donors[donor_name]        
        donor.add_donation(donation_amt)
        print(donor.print_thanksnote())    
   

def create_report():
    """Display a report showing donations."""
    donors.create_report()

def send_letters_all():
    """Generate a letter for each donor in the collection."""
    donors.send_letters_all()
    print('sending Letters to ALL.\n')

def main_menu():
     switch_dict = {1: send_thankyou, 2: create_report, 3: send_letters_all, 4: quit_action }
     while True:
         try:
            option = int(options_menu())
            switch_dict.get(option)()
         except TypeError:
            print("\n Invalid Option \n"
                  "Enter a Valid Option from the above list\n")


if __name__ == "__main__":
     main_menu()