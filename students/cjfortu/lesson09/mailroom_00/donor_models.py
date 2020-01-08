#!/usr/bin/env python

"""
The Mailroom assignment, donor models.

Donor object creation is under the Donor class, while assembling the donor objects is in the DonorCollection class.
The donor object collection structure is:
{'name": object'}
In words, it is a dict with each donor name in string form as the keys, and the donor object as the value.

The remaining features follow the assignment instructions.
"""


class Donor:
    """Class that holds and accesses information about a single donor."""
    new_donations = []
    
    def __init__(self, donor_name=None, *donations):
        """Initiate a donor by name and donations."""
        self.name = donor_name
        self.donations = [*donations]
        self.new_donations = [*donations]

    @property
    def number_donations(self):
        return len(self.donations)
    
    @property
    def lifetime_donations_sum(self):
        return sum(self.donations)
    
    @property
    def average_donations(self):
        return self.lifetime_donations_sum / self.number_donations
        
    def add_donations(self, new_donations):
        """Append new donations to the existing donations attribute."""
        [self.donations.append(donation) for donation in new_donations]
        self.new_donations = new_donations
        
    @property
    def compose_letter(self):
        """Generate text for a single letter."""
        text = "\n\nHi {},\n\nThank you for your total donation of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".\
            format(self.name, sum(self.new_donations))
        return text
        
    @property
    def mass_letter(self):
        """Generate text for letters for all donors."""
        text = "\nHi {},\n\nThank you for your lifetime donations of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".\
            format(self.name, self.lifetime_donations_sum)
        return text
        
    
class DonorCollection:
    """Class that holds all donor objects, as well as methods for multiple donors."""
    data = {}
    
    def __init__(self, **start_data):
        """Build a collection of existing donor objects without creating new donor objects."""
        self.data = {key: Donor(key, *value) for key, value in start_data.items()}
        
    def add_donor(self, donor_name = None, *donations):
        """Add a donor using the Donor.__init__ method."""
        self.data[donor_name] = Donor(donor_name, *donations)
        
    @property
    def names(self):
        """Build a list of donor names."""
        return [self.data[donor_name].name for donor_name in self.data]
        
    @property
    def new_structure(self):
        """Build a new data structure for use by send_all and create_a_report."""
        key1 = 'Donor Name'
        key2 = '# Gifts'
        key3 = 'Total Given($)'
        key4 = 'Average Gift'
        # leveraged comprehensions and exceptions here!
        try:
            report_data = [{key1: self.data[donor_name].name, key2: self.data[donor_name].number_donations,\
                key3: self.data[donor_name].lifetime_donations_sum, key4: self.data[donor_name].average_donations}
                for donor_name in self.data]
        except ZeroDivisionError:
            report_data = [{key1: self.data[donor_name].name, key2: self.data[donor_name].number_donations,\
                key3: self.data[donor_name].lifetime_donations_sum, key4: self.data[donor_name].lifetime_donations_sum}
                for donor_name in self.data]
        def sort_total(val):
            return val[key3]
        report_data.sort(key=sort_total, reverse=True)
        return report_data, key1, key2, key3, key4
