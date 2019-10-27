#!/usr/bin/env python3


"""
Class to hold a information for one donor first name lastname and donation amount
"""
class Donor():
    def __init__(self, firstname, lastname,donation):
        self.fname = firstname.title().strip()
        self.lname = lastname.title().strip()
        if donation <= 0:
            donationError = ValueError('Donation cannot be negative')
            raise donationError
        else:
            self.donations = [donation]
        self.dc = DonorCollection()

    @property
    def fullname(self):
       """ Returns the first and lastname as one string """
       return self.fname + " " + self.lname

    @property
    def totaldonation(self):
        """ Returns the sum of all donations for a donor """
        return sum(self.donations)

    def add_donation(self,donation):
        """ Returns the sum of all donations for a donor """
        if donation < 0:
            donationError = ValueError('Donation cannot be negative')
            raise donationError
        else:
            self.donations.append(donation)

class DonorCollection():
    """ Class to hold a collection of donor objects """
    def __init__(self, donor=None):
        if donor is None:
            self.donors = []
        else:
            self.donors = donor


    def add_donor(self, donor):
        self.donors.append(donor)


    def list_donors(self):
        return self.donors


    def add_donation(self, donor_name, amount):
        #add to the donation list of lists when donor exists
        for i, donor in enumerate(self.donors):
            if donor.fullname.lower() == donor_name.lower():
                self.donors[i].donations.append(amount)


    def search_fullname(self, donor_name):
        #search to see if donor already exits
        for donor in self.donors:
            if donor.fullname.lower().strip() == donor_name.lower().strip():
                return True
        return False


    def create_summary(self):
        """ Returns a list of donation summaries for each donor """
        summary_values =[]
        for donor in self.donors:
            #aggregate dontations and get averages
            donor_name = donor.fullname
            total = sum(donor.donations)
            donate_count = len(donor.donations)
            donate_avg = total / donate_count
            summary_values.append([donor_name, total, donate_count, donate_avg])
        return summary_values
