#!/usr/bin/env python

import datetime
import os.path
import pathlib
import sys
from functools import reduce

class Donor:
    """
    A class used to represent a Donor
    """
    def __init__(self, name):
        """
        Parameters
        ----------
        name : str
            The name of the Donor
        donations : list
            List of donations from the given Donor
        """
        self.name = name
        self.donations = []
    
    def name(self):
        return self.name
        
    def add_donation(self, donation):
        """Add a donation to the list of donations"""
        self.donations.append(donation)
    
    def total_donation(self):
        """Return the total donation amount"""
        return sum(self.donations)
        
    def num_donation(self):
        """Return the quantity of donations"""
        return len(self.donations)
        
    def avg_donation(self):
        """Return the average donation amount"""
        return sum(self.donations) / len(self.donations)

    def donations(self):
        return self.donations
        
        
class DonorCollection:
    """
    A class used to represent a collection of Donors
    """
    
    def __init__(self):
        """
        Parameters
        ----------
        donor_list : list
            List of donors with their associated total donation, number of donations, and average donation
        """
        self.donor_list = []
        self.donation_log = []
            
    def add_donor(self, donor):
        """Add donor information to the donor list"""
        self.donor_list.append(donor)
        for donation in donor.donations:
            self.donation_log.append(donation)
        
    def donor_names(self):
        """Return a list of the active donor names"""
        self.names = []
        return [donor.name for donor in self.donor_list]
    
    def list_data(self):
        """Print formatted columns of donors and their associated donation information from the donor list"""
        self.report_list = []
        for donor in self.donor_list:
            self.report_list.append([donor.name, donor.total_donation(), donor.num_donation(), donor.avg_donation()])
        self.report_list.sort(key=lambda donor: int(donor[1]), reverse = True)
        max_len_str = [0]*4  # List providing the lengths of the longest items in each column
        for row in self.report_list:
            for item in range(len(row)):
                if len(str(row[item])) > max_len_str[item]:
                    max_len_str[item] = len(str(row[item]))

        format_string = f'{{:<{max_len_str[0]+10}}}${{:<{max_len_str[1]+9}}}{{:<{max_len_str[2]+15}}}${{:<{max_len_str[3]+10}}}' # Format string taking into account the longest item in each column.
        format_string_header = f'{{:<{max_len_str[0]+10}}}{{:<{max_len_str[1]+10}}}{{:<{max_len_str[2]+15}}}{{:<{max_len_str[3]+10}}}'
        
        print("\n")
        print(format_string_header.format(*("Donor Name", "Total Given", "Num Gifts", "Average Gift")))
        print("-"*(max_len_str[0]+max_len_str[1]+max_len_str[2]+max_len_str[3]+39))
        for row in self.report_list:
            print(format_string.format(*row))
            
    def write_letter(self):
        """Generate letters for each donor in the list with their total donation amount and stores the letters in a new directory"""
        current = datetime.datetime.now()
        abs_path = pathlib.Path('./').absolute()
        final_path = os.path.join(abs_path, "letter_storage/")
        if not os.path.exists(final_path):
            os.makedirs(final_path)
        for donor in self.donor_list:
            with open("{}{}_{:02}_{:02}_{:02}.txt".format(final_path, donor.name, current.month, current.day, current.year), 'w') as thank_you_file:
                thank_you_file.write("Dear {},\n\nThank you for your continuous support over the years\nand for your total donation amount of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(donor.name, donor.total_donation()))
    
    def challenge(self, factor, min_donation = 0, max_donation = 0):
        self.philanthropy_filter = list(filter(lambda x: x >= min_donation and x <= max_donation, self.donation_log))
        self.philanthropy_log = list(map(lambda x: x*(factor - 1), self.philanthropy_filter))
        try:
            return reduce(lambda x,y: x+y, self.philanthropy_log)
        except TypeError:
            pass
        
def name_prompt():
    """Returns full name of new or existing donor to add to the donor database"""
    ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    while ask_name.lower() == "list":
        print(donor_collection.donor_names())
        ask_name = input("\nPlease enter a full name or type 'list' for a list of the donor names: ")
    return ask_name


def thank_you():
    """Prompt user to input new donor information."""
    ask_name = name_prompt()
    
    for donor in donor_collection.donor_list:
        if ask_name == donor.name:  # Check if the entered name is already in the list
            while True:
                try:
                    ask_donor = float(input("Please enter a donation amount: "))
                    break
                except ValueError:
                    print("Input invalid! Donation amount needs to be a number.")
            donor.add_donation(ask_donor)
            print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(donor.name,ask_donor))
            break
    else:  # Check if the entered name is not in the list 
        while True:
            try:
                ask_donor = float(input("Please enter a donation amount: "))
                break
            except ValueError:
                print("Input invalid! Donation amount needs to be a number.")
        new_donor = Donor(ask_name)
        new_donor.add_donation(ask_donor)
        donor_collection.add_donor(new_donor)
        print("\nDear {},\n\nThank you for your generous donation of ${:,.2f}.\n\nSincerely,\nThe Best Charity Ever".format(ask_name,ask_donor))      


def philanthropy_projection():
    """Return projected total matching amount based on past donations and matching criteria"""
    print("This program will provide the projected amount of matching funds that a philanthropist\n"
          "would contribute based on past donations and the following selected matching criteria.\n")
    while True:
        try:
            match_min = float(input("Please enter a minimum donation amount: "))
            break
        except ValueError:
            print("Input invalid! Value needs to be a number.")
    while True:
        try:
            match_max = float(input("Please enter a maximum donation amount: "))
            break
        except ValueError:
            print("Input invalid! Value needs to be a number.")
    while True:
        try:
            match_factor = float(input("Please enter a matching factor: "))
            break
        except ValueError:
            print("Input invalid! Value needs to be a number.")
            
    if donor_collection.challenge(match_factor, match_min, match_max) is None:
        print("\nNo donations match the specified criteria. Please try again with a different set of criteria.")
    else:
        print("\nHere is the projected total matching contribution: ${:,.2f}".format(donor_collection.challenge(match_factor, match_min, match_max)))
    
def initial_setup():
    """Populate donor collection with initial donor information"""
    init_collection = DonorCollection()
    d1 = Donor("Warren Buffett")
    d1.add_donation(600)
    d1.add_donation(50)
    
    d2 = Donor("Jack Bogle")
    d2.add_donation(150.50)
    
    d3 = Donor("William Boeing")
    d3.add_donation(40)
    d3.add_donation(50)
    
    d4 = Donor("George Clooney")
    d4.add_donation(75)
    d4.add_donation(25)
    
    d5 = Donor("Orville Wright")
    d5.add_donation(95)
    
    initial_donor_list = [d1, d2, d3, d4, d5]
    for donor in initial_donor_list:
        init_collection.add_donor(donor)
    
    return init_collection


def quit_program():
    """Exit out of the program"""
    print("Exiting the program.")
    sys.exit()


if __name__ == "__main__":
    donor_collection = initial_setup()
    option_select = {'1': thank_you, '2': donor_collection.list_data, '3': donor_collection.write_letter, '4': philanthropy_projection}
    while True:  # loop until user inputs something other than the keys in option_select
        user_prompt = input("\nPlease choose from the following menu of actions:\n[1] Send a Thank You\n[2] Create a Report\n[3] Send letters to everyone\n[4] Philanthropy\n[Press any other key to quit.]\n\nInput: ")
        if user_prompt not in option_select:
            quit_program()
        option_select.get(user_prompt)()