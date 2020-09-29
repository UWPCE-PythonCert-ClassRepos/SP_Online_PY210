"""
Author: Philip Behrend
Project: Assignment L09
Date: 11/5/2019
"""

import numpy as np

class Donor:
    """ The Donor class holds information for a single donor"""

    def __init__(self,name="",donation=[]):
        self.name = name
        self.donation = donation

    def __lt__(self,other):
        return self.total_donated < other.total_donated

    @property
    def total_donated(self):
        if type(self.donation) == list:
            return sum(self.donation)
        elif type(self.donation) == int:
            return self.donation
        else:
            raise TypeError
    
    @property
    def avg_donation(self):
        if type(self.donation) == list:
            return np.mean(self.donation)
        elif type(self.donation) == int:
            return self.donation
        else:
            raise TypeError


    @property 
    def num_donations(self):
        if type(self.donation) == list:
            return len(self.donation)
        elif type(self.donation) == int:
            return 1
        else:
            raise TypeError


class DonorCollection:
    """ The DonorCollection class holds information for a collection of donors"""

    def __init__(self):
        self.donors = []

    
    def add_donor(self,new_donor,donations=[]):
        if type(donations) == int:
            self.donors.append(Donor(new_donor,[donations]))
        elif type(donations) == list:
            self.donors.append(Donor(new_donor,donations))
        else:
            raise TypeError
    
    def add_donation(self, donation_name, new_donation):
        cur_names = []
        [cur_names.append(i.name) for i in self.donors]

        if donation_name not in cur_names:
            self.donors.append(Donor(donation_name))
        if type(new_donation) == int:
            [i.donation.append(new_donation) for i in self.donors if i.name == donation_name]
        elif type(new_donation) == list:
            [i.donation.extend(new_donation) for i in self.donors if i.name == donation_name]
        else:
            raise TypeError
    



        

"""
d2 = DonorCollection()
d2.add_donor('henry',50)
d2.add_donor('george',[500,3000])
d2.add_donation('mary',40)
[print(i.donation) for i in d2.donors]

d2.create_metrics()
[print(i.metrics) for i in d2.donors]

d2.donors.sort(reverse=True)
[print(i.total_donated) for i in d2.donors]
"""
