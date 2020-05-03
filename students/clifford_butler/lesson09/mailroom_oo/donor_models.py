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

class Donor():
    # Class responsible for donor data encapsulation
    def __init__(self, name):
        self.name = name
        self.donations = []
        
    def __lt__(self, other):
        if self.total_donations() < other.total_donations():
            return True
        elif self.total_donations() == other.total_donations(): # Otherwise, sort by last name
            return self.name.split()[-1] < other.name.split()[-1]
        else:
            return False
        
    def add_amount(self, amount):
        # add donation amount based on name
        self.donations.append(amount) 
    
    def last_donation(self):
        if self.donations:
            return self.donations[-1]
        else:
            return 0

    def total_donations(self):
        return sum(self.donations)

    def num_donations(self):
        return len(self.donations)

    def average_donation(self):
        return self.total_donations()/self.num_donations() if self.donations else 0
        
        
    
class DonorCollection():
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

dc = DonorCollection()
donors = ["William Gates, III", "Jeff Bezos", "Paul Allen", "Mark Zuckerberg", "Alexandra Butler"]
amounts = [[653772.32, 12.17], [877.33], [663.23, 43.87, 1.32], [1663.23, 4300.87, 10432.0], [777.77, 44.44]]
'''
for donor, amount in zip(donors,amounts):
    if donor == donor:
        break
    else:
        for donation in amount:
            dc.update_donor(donor, donation)
'''        

for donor, amount in zip(donors,amounts):
    for donation in amount:
        dc.update_donor(donor, donation)
            
        
            

for key in dc.donors:
   print(key) 

d = Donor([]).donations   
print(d)
#print(Donor([]).donations)              
#print(dc.donors.keys())        
