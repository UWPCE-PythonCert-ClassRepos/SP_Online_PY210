#!/usr/bin/env python3

from collections import OrderedDict


class Donor:
    """
    Class representing an individual donor

    Args:
        name (str):
            Donor's name
        donations(list):
            Donation(s)

    Attributes:
        name (str):
            Donor's name
        donations (list):
            List of donations, order is old to new
        
    Methods:
        add_donation(amount):
            Add donation to donation attribute list

    Properties:
        donor():
            Return a dict of donor and donations
        sum_donations():
            Return total donations made by donor
        num_donations():
            Return the number of donations made by donor
        avg_donation():
            Return the average donation made by donor
        thank_you_letter():
            Generate text for email thanking donor for their last donation

    """
    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations


    @property
    def donor(self):
        '''Return a dict of donor and donations'''
        return {self.name: self.donations}


    def add_donation(self, donation=[]):
        """
        Add donation to donor's history

        Args:
            donation (list):
                Donation amount (must be a list)
        """
        self.donations.extend(donation)  


    @property    
    def sum_donations(self):
        '''Return total donations made by donor'''
        self._sum_donations = sum(self.donations)
        return self._sum_donations

    @property
    def num_donations(self):
        '''Return the number of donations made by donor'''
        self._num_donations = len(self.donations)
        return self._num_donations

    @property
    def avg_donations(self):
        '''Return the average of donations made by donor'''
        self._avg_donations = self.sum_donations/self.num_donations
        return self._avg_donations

    @property
    def thank_you_letter(self):
        '''Generate text for email thanking donor for their last donation'''
        email_dict = dict(name=self.name, donation=int(self.donations[-1]))
        result = """
        Dear {name},
        Thank you very much for the generous donation of ${donation:,.2f}
        It is very much appreciated.
        Respectfully,

        Eric G.
        """.format(**email_dict)

        return result
    
    
class DonorCollection:
    """
    Class representing a collection of Donor instances

    Args:
        donors (list):
            List of donor objects (object)

    Properties:
        donor_names():
            List of donor names. 

        donor_dict():
            A dictionary of donor name as key and donations as value

        report_data():
            A dictionary of all donors and donations, used to populate report

    Methods:
        add_donor(name, amount):
            Either updates existing donor with amount, or Creates a new donor 
            with amount if not in collection

        donor_data(name):
            Returns dictionary of donor instance 

        donor_obj(name):
            Returns the donor instance as an object

        generate_report(report_data):
            Generates report string from the data in the report_data property

    """
    def __init__(self):
        self.donor_list = []

    def add_donor(self, name, amount):
        '''Either updates existing donor with amount, or Creates a new donor 
            with amount if not in collection
        '''
        for donors in self.donor_list:
            if donors.name == name:
                donors.add_donation(amount)
                return
        
        new_donor = Donor(name, amount)
        self.donor_list.append(new_donor)

    @property
    def donor_names(self):
        '''Returns a list of donor names'''
        donor_name = []
        for donor in self.donor_list:
            donor_name.append(donor.name)
        return donor_name

    @property
    def donor_dict(self):
        '''Returns a dictionary of donor name as key and donations as value'''
        donor_dict = {}
        for donor in self.donor_list:
            donor_dict.update(donor.donor)
        return donor_dict

    
    def donor_data(self, name):
        '''Returns dictionary of donor instance '''
        for donors in self.donor_list:
            if donors.name == name:
                return donors.donor


    def donor_obj(self, name):
        '''Returns the donor instance as an object'''
        for donors in self.donor_list:
            if donors.name == name:
                return donors


    @property
    def report_data(self):
        '''Returns a dictionary of all donors and donations, used to populate report'''
        report_data_dict = {}
        for donor in self.donor_list:
            temp_dict = {donor.name: [donor.sum_donations, donor.num_donations, donor.avg_donations]}
            report_data_dict.update(temp_dict)
        sorted_report_data_dict = OrderedDict(sorted(report_data_dict.items(), key=lambda t: t[1], reverse=True))
        return sorted_report_data_dict


    def generate_report(self, sorted_report_data_dict):
        '''Returns a report string from the data in the report_data property'''
        header_row = ("{:<25s}|{:>15s} |{:>10s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        dash_line = "-" * 68
        data_lines = ''
        
        for k,v in sorted_report_data_dict.items():
            data_lines += ("{:<25s}|${:>14,.2f} |{:>10.0f} |${:>12,.2f}".format(k, v[0], v[1], v[2])) + '\n'
        text_to_print = '\n' + header_row + '\n' + dash_line + '\n' + data_lines + '\n'
        return text_to_print


    


