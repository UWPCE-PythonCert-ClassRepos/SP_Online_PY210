#!/usr/bin/env python3

class Donor():

    def __init__(self, name, donations: list):
        """ Initialize new instance of Donor class """
        self._name = name
        self._donations = donations

    @property
    def name(self):
        return self._name
    
    @property
    def donations(self):
        return self._donations

    def add_donation(self, amount):
        """ Add a new donation amount to a Donor """
        if isinstance(amount, (int, float)):
            if amount > 0:
                self._donations.append(amount)    
            else:
                raise ValueError("Donation must be greater than 0")        
        else:
            raise TypeError("Donation must be a number")
        
    def sum_donations(self):
        """ Return a sum of all donations """
        return sum(self._donations)

    def donation_count(self):
        """ Returns the number of donations made """
        return len(self._donations)

    def average_donation(self):
        """ Returns the average donation amount for a Donor """
        average = self.sum_donations() / self.donation_count()
        return round(average, 2)    
        

class DonorCollection():

    def __init__(self):
        """ Initialize new instance of DonorCollection class """
        self.donors = []

    def add_donor(self, donor):
        """ Adds a new donor to the list """ 
        for seed_donor in self.donors:
            if seed_donor.name.lower() == donor.name.lower():
                seed_donor.add_donation(donor.donations[0])
                break
        else:
            self.donors.append(donor)

    def list_donors(self):
        """ Return the list of donors in the collection """
        donor_names = []
        for donor in self.donors:
            donor_names.append(donor.name)
        return donor_names

    def get_donors(self):
        return self.donors

    def generate_report(self):
        """ Generate report of donors and their donations """
        # Sort the donor list
        self.donors.sort(key=lambda donor: donor.sum_donations(), reverse=True)
        
        # Return the formatted report
        report = []
        for donor in self.donors:
            report.append([donor.name, donor.sum_donations(), donor.donation_count(), donor.average_donation()])
        return report