#!/usr/bin/env python3

import sys
from collections import defaultdict
from operator import itemgetter

class Donor():
    """ This class holds all the information about any single donor.
    
    Its attributes, properties, and/or methods provide access to donor-specific information.
    
    Examples of donor-specific info:
        donor name (first and last)
        $ amount of last donation
        add a donation
        $ amount of total donations
        average $ amount of all donations
        number of total donations
        generate reports with the above info for a single donor
        etc.
    """

    name = ""
    donor_info = {}
    
    def __init__(self, name, value):
        self.name = name
        self.donor_info[self.name] = [value]
    
    @property
    def donation(self):
        #return the last donation a donor made
        return self.donor_info[self.name][-1]
    
    @donation.setter
    def new_donation(self, value):
        #add a donation to a list
        return self.donor_info[self.name].append(value)
    
    def _donations(self):
        donations = self.donor_info[self.name]
        return donations
    
    @property
    def total_donations(self):
        #return the total number of donations
        return len(self._donations())
    
    @property
    def total_amount(self):
        return sum(self._donations())
    
    @property
    def avg_amount(self):
        return round((self.total_amount / self.total_donations), 2)
    
    @property
    def thank_you(self):
        return f"Thank you, {self.name}, for your generous donation of ${self.donor_info[self.name][-1]:,.2f}."
    
    @property
    def report(self):
        #header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gifts']
        top_row = f"{'Donor Name':30} |{'Total Given':>20} |{'Num Gifts':>15} |{'Avg Gifts':>20}"
        
        report_data = [self.name, self.total_amount, self.total_donations, self.avg_amount]
        #report_info = [[x, sum(a_dict[x]), len(a_dict[x]), sum(a_dict[x])/len(a_dict[x])] for x in a_dict]
        
        report_content = [top_row, report_data]
        
        return report_content
    
class Donor_Collection():
    """ This class holds and works with a collection of donors & donor objects.
    
    Its attributes, properties, and/or methods deal with functionality involving more than one donor.
    
    Examples of what should be in this class:
        add a donor to a list of donors
        list all donors
        search for a given donor
        save & re-load data
        generate reports about multiple donors
        etc.
    """
    