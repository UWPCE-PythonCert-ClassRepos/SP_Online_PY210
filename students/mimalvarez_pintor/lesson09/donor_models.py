# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:01:08 2020

@author: miriam
"""

from operator import itemgetter


class Donor(object):
   
    def __init__(self, name, donation_amt=None):
        """ Initializes the donor object """
        self.name = name
        self.donation_amt = donation_amt if donation_amt is not None else []

    def add_donation(self, amount):
        self.donation_amt.append(amount)


    def print_thanksnote(self):
        note = (f'\nDear {self.name},'
                    f'\nThank you for your very kind donation of ${self.donation_amt[-1]:.2f}.'
                    '\nIt will be put to very good use,'
                    '\n\nSincerely,\n-TheTeam\n')
        return note

    def sort_key(self):
        return sum(self.donation_amt)

class DonorCollection():
    """ Initialize donors dictionary """
    def __init__(self):
        self.donors = {}

    @staticmethod
    def initialize_dict(donor_data):
        # create a new collection object
        donors = DonorCollection()                     
        for name, amounts in donor_data.items():     
            donor = Donor(name, amounts)            
            # add the new donor to the collection
            donors.add(donor)
        return donors  

    def add(self, donor):
        """ Add donor to the collection """
        self.donors[donor.name] = donor

    def donors_list(self):
        """ Generate a list of donors """
        ls=[]
        for names in self.donors:
            ls.append(names)
        return '\n'.join(ls)
      
    def send_letters_all(self):
        """ Save donor letters to files """
        for donor in self.donors.values():
            filename = donor.name + '.txt'
            with open(filename, 'w') as f:
                f.write(Donor.print_thanksnote(donor))
                 
    
    def create_report(self):
        """ Generate a tabular report of donation history """

        header ='\n{:<20}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
        print(header)
        print('-'*len(header))

        for entry in self.donors.values():
            total = sum(entry.donation_amt)
            num = len(entry.donation_amt)
            average = total/num
            print('{:<20} ${:>13,.2f}{:>13}  ${:>12,.2f}'.format(entry.name,total,num,average))
        print('')
  
    def donor_exists(self, name):
        #Search for donor name in donor collection.    
        return any(d for d in self.donors.values() if d.name.upper() == name.upper())