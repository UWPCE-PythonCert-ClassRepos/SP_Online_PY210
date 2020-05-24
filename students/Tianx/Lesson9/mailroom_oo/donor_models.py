# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: donor_models.py
# Desc: The module donor_models.py contains the Donor and DonorCollection classes.
# Tian Xie, 2020-05-21, Created File
# ------------------------------------------------------------------------#
import operator

class Donor(object):
    def __init__(self, donor_name, donation=None):
        """ Initialize the Donor class """

        self.name = donor_name
        if donation == None:
            self.donations = []
        else:
            self.donations = list(donation)

    def add_donation(self, donation):
        """
        adds donation to the donations list
        :param donation: Donation amount that will be added to donor list
        :return: donations with the new amount added
        """
        return self.donations.append(donation)

    @property
    def previous_donations(self):
        """
        returns the most recent donation in the  donor list
        """
        return self.donations[-1]

    @property
    def num_donations(self):
        """
        returns the total number of donations made by the donor
        """
        return len(self.donations)

    @property
    def total_donations(self):
        """
		returns the total donations made by a single donor
		"""
        return sum(self.donations)

    @property
    def avg_donation(self):
        """
        returns the average donation amount made by thr donor
        """
        return self.total_donations / len(self.donations)

    def create_email(self):
        email = f'Dear {self.name},\n\nThank you for your generosity, your donation of ${float(self.donations[-1]):.2f} will be put to good use.\n\n''Warm regards,\nMailroom Staff'
        return email


    def __lt__(self, other):
        return self.total_donations < other.total_donations


class DonorCollection:
    def __init__(self):
        self.donor_list = [Donor('Jeff Bezos', [1.00, 50.00]),
                           Donor('Warren Buffet', [100.00, 1000.00]),
                           Donor('Bill Gates', [100.00, 500.00]),
                           Donor('Tim Cook', [300.00]),
                           Donor('Jack Ma', [2000.00])]

    def __iter__(self):
        # Iterates over donor_list
        return self.donor_list.__iter__()

    def __len__(self):
        # Iterates over donor_list
        return self.donor_list.__len__()


    def add_donor(self, donor_name, donation):
        """ """
        new_donor = Donor(donor_name, [donation])
        self.donor_list.append(new_donor)
        return new_donor

    def get_donor(self, donor_name):
        '''Return the donor if present, otherwise return False.'''
        for donor in self.donor_list:
            if donor_name == donor.name:
                return donor


    def add_new_donation(self, donor_name, donation):
        for donor in self.donor_list:
            if donor_name == donor.name:
                print('adding to old name')
                donor.add_donation(donation)
                return

        print('creating new donor')
        self.add_donor(donor_name, donation)

    def show_donor_list(self):
        donor_name = ""
        for donor in self.donor_list:
            donor_name += donor.name + '\n'
        return donor_name

    def dict_of_donors(self):
        '''Returns a dictionary of donor name as key and donations as value'''
        dict_of_donors = {}
        for donor in self.donor_list:
            dict_of_donors.update({donor.name: [(donor.donations)]})
        return dict_of_donors

    def create_report_format(self):
        """Formatting a report.

        Args:
           None

        Returns:
           report object

        """
        report = ['Donor Name                | Total Given | Num Gifts | Average Gift','------------------------------------------------------------------']
        self.donor_list.sort(reverse=True)
        for i in self.donor_list:
            report.append(f'{i.name:26} ${float(i.total_donations):>11.2f} {i.num_donations:>11.0f}  ${i.avg_donation:>12.2f}')
        return report

