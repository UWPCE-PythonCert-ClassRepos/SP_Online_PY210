#!/usr/bin/env python3

import operator
import os
import sys

"""
Steve Morehouse
Lesson 09
"""

class Donor (object):

    def __init__(self, name, donations=None):
        self.name = name
        self.donations = donations if donations is not None else []

    
    def add_donation (self, amount):
        self.donations.append(amount)
    
    
    def compose_thank_you (self):
        msg = f"\n{self.name},\n\nThank you for your donation of ${self.donations[-1]:.2f}.\n"
        return msg

    
    def get_max_lengths(seq, header):
        name_len = len(header[0])
        total_len = len(header[1])
        count_len = len(header[2])
        avg_len = len(header[3])
    
        for item in seq:
            total = f"${item[1]:.02f}"
            count = str(item[2])
            avg = f"${item[3]:.02f}"
    
            name_len = len(item[0]) if len(item[0]) > name_len else name_len
            total_len = len(total) if len(total) > total_len else total_len
            count_len = len(count) if len(count) > count_len else count_len
            avg_len = len(avg) if len(avg) > avg_len else avg_len
    
        return [name_len, total_len, count_len, avg_len]
    
    
    def get_donor_summary(self):
        len_donations = len(self.donations)
        sum_donations = sum(self.donations)
        average_donation = sum_donations/len_donations if len_donations else 0

        return (self.name, sum_donations, len_donations, average_donation)
    
    
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
    
            name = donor[0]
            total_donations = sum(donor[1])
            count_donations = len(donor[1])
    
            letter = "Thank you {0:s} for your donations totaling ${1:.2f}.".format (name, total_donations)
    
            file_name = name.replace(" ","_") + ".txt"
            full_path = os.path.join (cur_dir,file_name)
    
            with open (full_path, "w") as file:
                file.write (letter)
 
 
    """
    Return a formatted string that will fit in the donor summary table.
    """
    def format_line(item, lengths):
        total = f"{item[1]:.02f}"
        avg = f"{item[3]:.02f}"
        return f"{item[0]:<{lengths[0]}}  ${total:>{lengths[1]}}   {item[2]:>{lengths[2]}}  ${avg:>{lengths[3]}}"
   

    def sort_key (item):
        return (item[1])


    def create_report (self):
        sorted_values = sorted(
            [x.get_donor_summary() for x in self.donors.values()], key=operator.itemgetter(1), reverse=True)
        result = "\n"
        result += 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
        result += '-'*66 + '\n'
        for name, total_given, number_gifts, avg_gift in sorted_values:
            result += f'{name:<27}${total_given:>11.2f}{number_gifts:>12}  ${avg_gift:>11.2f}\n'
        return result
    
#!/usr/bin/env python3
