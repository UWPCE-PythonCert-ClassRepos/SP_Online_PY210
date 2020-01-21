#!/usr/bin/env python3

#class donor
#class report(sub of donor?)
#class thank_you(sub of donor?)

#hold all information about a single donor, including thank you letter, donation and donation history
class Donor():
    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations

    @property
    def donor(self):
        return {self.name: self.donations}
    
    def add_donation(self, donation):
        self.donations.append(int(donation))  

    @property    
    def sum_donations(self):
        self._sum_donations = sum(self.donations)
        return self._sum_donations

    @property
    def num_donations(self):
        self._num_donations = len(self.donations)
        return self._num_donations

    @property
    def avg_donations(self):
        self._avg_donations = self.sum_donations/self.num_donations
        return self._avg_donations

    @property
    def thank_you(self):
        email_dict = dict(name=self.name, donation=self.donations[-1])

        result = """
        Dear {name},
        Thank you very much for the generous donation of ${donation:,.2f}
        It is very much appreciated.
        Respectfully,

        Eric G.
        """.format(**email_dict)

        return result
    
    

#hold all of the donor objects, method to add a new donor, search for a donor, 
#save and reload data, generate reports
class DonorCollection:
    def __init__(self):
        self.donor_list = []

    def add_donor(self, name, amount=[]):
        
        if name not in self.donor_list:
            new_donor = Donor(name, [amount])
            self.donor_list.append(new_donor.name)
        else:
            name.add_donation(amount)


    #trying to get object to return values, may need string represenations of objects

    '''
    def get_donor(self, name):
        if name in self.donor_list:
            return self.donor_list(name)
    ''' 

    def generate_report():
        pass

    


