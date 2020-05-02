#!/usr/bin/env python3

"""
Donor Class
Class responsible for donor data encapsulation

This class will hold all the information about a single donor, 
and have attributes, properties, and methods to provide access 
to the donor-specific information that is needed. Any code that 
only accesses information about a single donor should be part 
of this class.

DonorCollection Class
Class responsible for donor collection data encapsulation

This class will hold all of the donor objects, as well as methods 
to add a new donor, search for a given donor, etc. If you want a 
way to save and re-load your data, this class would hold that 
method, too.

Your class for the collection of donors will also hold the code 
that generates reports about multiple donors.

In short: if the functionality involves more than one donor – 
it belongs in this class.

Note that the DonorCollection class should be holding, and 
working with, Donor objects – it should NOT work directly with 
a list of donations, etc.
"""

class Donor(object):
    # Class responsible for donor data encapsulation
    def __init__(self, name):
        self.name = name
        self.donation = []
    
    def add_amount(self, amount):
        # add donation amount based on name
        self.donation.append(amount) 
    
class DonorCollection(object):
    # Class responsible for donor collection data encapsulation
    def __init__(self):
        self.donors = {}
    
    def update_donor(self, name, amount):
        # update donor
        ud = self.get_donor(name)
        ud.add_amount(amount)
        self.donors[name] = ud

    def get_donor(self, name):
        # get donor name based on input
        return self.donors.get(name, Donor(name))

    @property
    def donor_names(self):
        # return list of the donor names
        return list(self.donors)
