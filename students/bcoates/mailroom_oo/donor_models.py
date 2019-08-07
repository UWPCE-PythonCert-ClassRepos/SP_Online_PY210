#!/usr/bin/env python3

class Donor():
    
    def __init__(self, full_name):
        """ Initialize a Donor for a given full name """
        
        self.full_name = full_name
        self.donations = []
    
    def add_donation(self, donation):
        """ Add a given donation to the list of donations """
        
        self.donations.append(donation)
    
    def format_thank_you(self):
        """ Format a thank you letter for a donor/donation """
        
        letter = ("Dear {},\n\n"
                  "Thank you for your generous donation of ${:.2f}!\n\n"
                  "Sincerely,\n\n"
                  "The Owners").format(self.full_name, self.donations[-1])
        return(letter)

    @property
    def donation_total(self):
        """ Return the sum of donations for a donor """
        
        return sum(self.donations)
    
    @property
    def donation_count(self):
        """ Return a count of donations for a donor """
        
        return len(self.donations)

    @property
    def donation_avg(self):
        """ Return the average donation for a donor """
        
        return self.donation_total / self.donation_count

class DonorCollection():
    
    def __init__(self):
        """ Initialize an empty donor collection """
        
        self.donors = []

    def add_donor(self, donor):
        """ Add a donor to the collection """
        
        for current_donor in self.donors:
            if current_donor.full_name == donor.full_name:
                current_donor.add_donation(donor.donations[0])
                break
        else:
            self.donors.append(donor)

    def list_donors(self):
        """ Return the donor names in the collection """
        
        donor_names = ""
        for donor in self.donors:
            donor_names += donor.full_name + "\n"
        return donor_names

    def create_report(self):
        """ Return a report of donors and donations """
        
        self.donors.sort(key=lambda x: x.donation_total, reverse=True)
        report = []
        for donor in self.donors:
            report.append([donor.full_name, donor.donation_total, donor.donation_count, donor.donation_avg])
        return report