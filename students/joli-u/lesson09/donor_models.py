from operator import itemgetter
import pathlib

"""
donor_models.py: module containing donor classes
lesson 9
joli umetsu
python210
"""

class Donor(object):
    """ class responsible for single donor information """
    
    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations

    def add_donation(self, amount):
        self.donations.append(amount)
        
    @property
    def donation_total(self):
        return sum(self.donations)
        
    @property
    def donation_number(self):
        return len(self.donations)
        
    @property
    def donation_average(self):
        return round(sum(self.donations)/len(self.donations), 2)
                
    def letter(self):
        text = "\n".join(("Dear {},\n".format(self.name), 
            "\tThank you for your generous donations totaling ${:.2f}.\n".format(self.donation_total), 
            "\tIt will be put to very good use.\n",
            "\t\tSincerely,",
            "\t\t  -The Team"))
        return text


class DonorCollection():
    """ class responsible for donor collection data encapsulation """
    
    def __init__(self):
        # initial list of donors and donations
        self.donors = [
        Donor('Peregrin Took', [3002.50, 100.25]),
        Donor('Gandalf the Grey', [5000.00, 580.00]),
        Donor('Smeagol', [45.01]),
        Donor('Samwise Gamgee', [500.53, 10000.89, 100.51]),
        Donor('Frodo Baggins', [850.95, 9000.30])
        ]
        
    def list_donors(self):
        """ returns string of current donor names """
        names = "\n"
        for donor in self.donors:
            names += donor.name + "\n"
        return names
    
    
    def search_donor(self, name):
        """ looks through list of current donors
            returns list of names matching input name """
        return [ donor.name for donor in self.donors if donor.name.lower() == name.lower() ]
        
        
    def add_donor(self, name, amount):
        """ adds new donor record
            returns donor object that was added """
        new_donor = Donor(name, [amount])
        self.donors.append(new_donor)
        return new_donor
    

    def update_donor(self, name, amount):
        """ updates existing donor record
            returns donor object that was updated """
        for donor in self.donors:
            if donor.name.lower() == name.lower():
                donor.donations.append(float(amount))
                return donor


    def report(self):
        """ generates report of donor history
            returns sorted list of donors and donation metrics """
        info = [ [donor.name, donor.donation_total, donor.donation_number, donor.donation_average] for donor in self.donors ]
        report = sorted(info, key=itemgetter(2))
        report.reverse()
        return report

        
    def letters(self):
        """ generates thank you letters for all donors and saves in a file in cwd
            returns nothing """
        cur_dir = pathlib.Path('./').absolute()
        try:
            new_fdr = 'ThankYouLetters'    
            (cur_dir / new_fdr).mkdir()
        except FileExistsError:
            print("\n\tERROR: Files already exist!")
            return None 
        else:  
            for donor in self.donors:
                text = donor.letter()
                file_name = ('_'.join(donor.name.split(' ')))+".txt"
                with open((cur_dir / new_fdr / file_name), 'w') as f:
                    f.write(text)   
