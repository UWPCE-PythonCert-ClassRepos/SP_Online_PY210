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
    
    def __init__(self, name, *args):
        self.name = name
        self.donor_info = {}
        self.donor_info[self.name] = list(args)
    
    def __str__(self):
        if self.donor_info[self.name] == []:
            return f"Donor name: {self.name}\nDonations: This donor has not made any donations."
        else:
            return f"Donor name: {self.name}\nDonations: {self._donations()}\n"
    
    def __repr__(self):
        return f"Donor({self.name}: {self._donations()})"
    
    @property
    def donation(self):
        #return the last donation a donor made
        if self.donor_info[self.name] == []:
            return f"{self.name} has no logged donations."
        else:
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
        if self.total_donations == 0:
            return 0
        else:
            return round((self.total_amount / self.total_donations), 2)
    
    @property
    def thank_you(self):
        return f"Thank you, {self.name}, for your generous donation of ${self.donor_info[self.name][-1]:,.2f}."

    
class Donor_Collection():
    """ This class holds and works with a collection of donors & donor objects.
    
    Its attributes, properties, and/or methods deal with functionality involving more than one donor.
    
    Examples of what should be in this class:
        add a donor to a list of donors
        list all donors
        search for a given donor
        save & update donor data
        generate reports about multiple donors
        etc.
    """
    
    #key = donor.name, value = donor_object
    donor_objects = {}

    def __init__(self, *args):
        self.donor_objects.clear()
        for obj in args:
            self.donor_objects[obj.name] = obj
        #self.reload_donor_objects(args)
        
    #add a Donor object to a list of donor_objects
    def add_donor_object(self, donor_obj):
        self.donor_objects[donor_obj.name] = donor_obj
        return self.donor_objects 
    
    #list all donors
    def list_all_donors(self):
        _donor_names = []
        for key, value in self.donor_objects.items():
            _donor_names.append(key)
        
        return "\n".join(_donor_names)
        
    #search for a given donor
    def find_donor(self, donor_name):
        if donor_name not in self.list_all_donors():
            return f"{donor_name} is not a current donor."
        else:
            return self.donor_objects[donor_name]
    
    #save & update data
    def donor_letters(self):
    
        for key, obj in self.donor_objects.items():
            text = "Dear {name},\n\nYour total donations to date equal ${total:,.2f}.\n\nWe are grateful for your continued patronage and we can't wait to show you what your generosity will help us achieve.\n\nThank you!\nThe Team\n"
            a_dict = obj.donor_info
            for key in a_dict:
                letter_dict = {'name': key, 'total': sum(a_dict[key])}
                with open(f"./{key}.txt", 'w') as f:
                    f.write(text.format(**letter_dict))
        
    #generate a report for multiple donors
    def report_header(self):
        top_row = f"{'Donor Name':30} |{'Total Given':>20} |{'Num Gifts':>15} |{'Avg Gifts':>20}"
        top_row_border = '-' * len(top_row)
        
        header = [top_row, top_row_border]
        return "\n".join(header)
    
    def report_data(self):
        report_info = []

        for key, obj in self.donor_objects.items():
            report_info.extend([f"{obj.name:30}  ${obj.total_amount:>19,.2f}  {obj.total_donations:>15}  ${obj.avg_amount:>19,.2f}"])
        
        return "\n".join(report_info)