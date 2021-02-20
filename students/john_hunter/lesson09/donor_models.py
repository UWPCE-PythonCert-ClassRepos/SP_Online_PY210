#!/usr/bin/env python3
"""
Created on Fri Jan  8 17:39:10 2021

@author: johnh
"""

import sys
import pathlib
import datetime
from operator import itemgetter

now = datetime.datetime.now()

class Donor():
    """
    Base class to structure the default information needed to define an entry by donor
    """    
    
    def __init__(self, name, total = 0, status = False):
        self.donations = []
        self.total = self.get_total()
        self.activity_date = object()
        self.address = str()
        self.phone_number = str()
        self.status = status
        self.name = name
        
    #@property
    #def amounts(self, *args):# gets the individual amounts for each donation from each donor 
    #    self.donations = args
    def first(self):
        first = self.name.split()[0]
        return first
    
    def last(self):
        try:
            last = self.name.split()[1]
        except:
            return 'Unknown'
        return last
    
    #@property
    def get_total(self):
        self.total = sum(self.donations[:])
        return self.total
    #@property
    def number_of_donations(self):
        return len(self.donations)
    
    #@property
    def average(self):
        total = self.get_total()
        number = self.number_of_donations()
        if number == 0:
            return 0
        return total/number
    
    #view donor profile and information
    def view_donor_info(self, name):
        view = 0
        print("Donor Name is {}".format(name))
        print("first: {} and last: {} names".format(self.first, self.last))
        print("donations{} and total{}".format(self.donations, self.total))
        print("Address: {}".format(self.address))
        print("Phone Number: {}".format(phone_number))
        print("Date{} and Status{}".format(self.activity_date, self.status))
        return view
    def construct_email(self):
        name = self.name.title()
        email = (f"Dear {name},\n\n"
        f"Thank you for your generous donation(s) of ${self.get_total():,d}\n"
        "\n"
        "Sincerly,\n"
        "John Hunter\n")
        return email
    def get_status(self):
        #print(now.year, now.month, now.day)
        #self.day = self.activity_date.date()
        #self.month = self.activity_date.month()
        #self.year = self.activity_date.year()
        a = datetime.datetime(now.year,now.month,now.day)
        b = datetime.datetime(self.activity_date.year, self.activity_date.month, self.activity_date.day)
        #print(b, a)
        #print((a-b).total_seconds())
        self.status = ((a-b).total_seconds() < 31536000)
        return self.status
    
    def update_date(self):
        self.activity_date.day = now.day
        self.activity_date.month = now.month
        self.activity_date.year = now.year
        self.get_status()
    def sort_key(self, value):
        return self.value
#sort by other types than total, like alphbetical, allows extension to other data fields 
class DonorCollection():
    """
    """
    #donors = []
    def __init__(self):
        self.donors = []
        self.donors_names = []
        self.averages = []
        
    def add_donor(self, donor):
        self.donors.append(donor)

    def get_donors(self):
        return self.donors
    
    def donors_listed(self, donor):
        self.donors_names.append(donor.name)
    
    def averages_listed(self, donor):
        self.averages.append(donor.average)
        
    """
    def add_donor(donor_list, new_donor):
        print(type(donor_list))
        new_donor = Donor(new_donor)
        new_list = donor_list.append(new_donor)
        return new_list
    """
    #organizes but does not print the header for the current set of parameters for the donor set
    #@staticmethod
    
        
    #Since not all donors will have all donor attributes there should be some 
    #way of checking, "yes, this donor has an address", toggle on off to include in reports
    def extend(self, selection):
        
        return report_attributes[selection]
    # Allow the user to remove any of the four data field extensions
    def remove_data_field():
        pass
    
    # If any other information needs to be included, or after the structure is extened 
    # we could include the mailing address, and a return address, gift receipt
    def construct_email():
        pass
    # allow the user to sort by the total donation
    def sort_key(self):
        return self.val
    
    def list_of_donors(self):
        for name in donors:
            print("do we need this?")
    #organizes but does not print the data
    def report_data():
        pass
    
    #allow vertical sort by other types(name, first or last alphabetical, most recent donations, group by city)
    #def sort_key():
     #   pass


    
    