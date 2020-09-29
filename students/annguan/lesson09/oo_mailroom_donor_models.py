#!/usr/bin/env python

# Lesson 9 Object Oriented Mailroom

import operator

donor_db = {"Abraham Lincoln": [145674.32, 23465],
            "Barack Obama": [3456324.11, 3495, 323], 
            "Charlie Brown":[453.67],
            "Doctor Who": [5600, 42],
            "Eve WallE":[2.22]
                }
"""Use Object Oriended Approach for Donor Models"""
"""Per assignment suggestion, creating Donor class and Donor Collection Class"""
class Donor():
    def __init__(self,donor_name,donation):
        self.donor_name = donor_name
        self.donation_amount = donation[0]
        self.donation_number = donation[1]

    @staticmethod
    def thanks_one(donor_name,donation_amount):
        return f'Generating a Thank You Note:\n' \
                f'Dear {donor_name}, thank you for your donation of ${donation_amount:^10.2f}!'

class DonorCollection():
    donor_dict = {}

    @staticmethod
    def add_donor(donor_name,donation):
        DonorCollection.donor_dict[donor_name] = donation

    @staticmethod
    def add_donation(donor_name,donation):
        DonorCollection.donor_dict[donor_name][0] += donation_amount
        DonorCollection.donor_dict[donor_name][1] += 1
        return f"{donor_name}'s ${donation_amount} donation has been recorded."

    @staticmethod
    def list_donors():
        return str(DonorCollection.donor_dict.keys())

    @staticmethod
    def create_report_header():
        header = ('Donor Name', 'Total Donation', 'Number of Donations', 'Average Donation')
        line = "-" * 66
        return "{:<24} | {:^13} | {:^11} | {:^11}\n" \
        "{}".format(*header, line)
    def create_report_rows(key,val):
        return "{:<25} ${:>13.2f} {:>13}  ${:>20.2f}\n".format(key, val[0], val[1], val[0] / val[1])
    def create_report():
        sorted_donor_dict = sort (DonorCollection.donor_dict.items(), key=operator.itemgetter(1), reverse=True)
        report_string = ' '
        for key, val in sorted_donor_dict:
            report_string += DonorCollection.create_report_rows(key,val)
            return report_string

