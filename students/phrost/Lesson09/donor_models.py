#!/usr/bin/env python3

import operator
import os
import sys


class Donor (object):

    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations if donations is not None else []

    
    def add_donation (self, amount):
        self.donations.append(amount)
    
    
    def compose_thank_you (self):
        msg = f"\n{self.name},\n\nThank you for your donation of ${self.donations[-1]:.2f}.\n"
        return msg
    
    
    def get_donor_summary(self):
        num_donations = len(self.donations)
        sum_donations = sum(self.donations)
        average_donation = sum_donations/num_donations if num_donations else 0

        return (self.name, sum_donations, num_donations, average_donation)
    
    
class DonorCollection():

    def __init__(self):
        self.donors={}

 
    def add (self, donor):
        self.donors[donor.name] = donor
    
    
    def list_donors (self):
        return_list = ''
        for donor in self.donors:
            return_list += f'{donor}\n'
        return return_list


    def donor_exists(self, name):
        return any(d for d in self.donors.values() if d.name.upper() == name.upper())
   

    def print_report (self):
        cur_dir = os.getcwd()
    
        for donor in self.donors.values():
    
            letter = "Thank you {0:s} for your donations totaling ${1:.2f}.".format (donor.name, sum(donor.donations))
    
            file_name = donor.name.replace(" ","_") + ".txt"
            full_path = os.path.join (cur_dir,file_name)
    
            with open (full_path, "w") as file:
                file.write (letter)
 
 
    def create_report (self):
        sorted_values = sorted(
            [x.get_donor_summary() for x in self.donors.values()], key=operator.itemgetter(1), reverse=True)
        result = "\n"
        result += 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
        result += '-'*66 + '\n'
        for name, total_given, number_gifts, avg_gift in sorted_values:
            result += f'{name:<27}${total_given:>11.2f}{number_gifts:>12}  ${avg_gift:>11.2f}\n'
        return result
