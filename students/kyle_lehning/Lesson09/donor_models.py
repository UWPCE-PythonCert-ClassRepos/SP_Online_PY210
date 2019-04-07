#!/usr/bin/env python3
"""
A class-based system for donors
"""


class Donor(object):
    def __init__(self, don_name):
        self.name = don_name
        self.total_donation = 0
        self.donation_num = 0
        self.most_recent_donation = 0

    @property
    def avg_donation(self):
        # Read only attribute
        return round(self.total_donation / self.donation_num, 2)

    def new_donation(self, value):
        self.total_donation += round(value, 2)
        self.donation_num += 1
        self.most_recent_donation = round(value, 2)

    @classmethod
    def from_existing(cls, don_name, don_total, don_number):
        self = cls(don_name)
        self.total_donation = don_total
        self.donation_num = don_number
        return self

    def generate_recent_thanks(self):
        string_to_format = ("Dear {},"
                            "\n\nThank you for your kind donation of ${:.2f}."
                            "\nIt will be put to very good use."
                            "\n\nSincerely,"
                            "\n-The Team")
        return string_to_format.format(self.name, self.most_recent_donation)

    def generate_total_thanks(self):
        string_to_format = ("Dear {},"
                            "\n\nThank you for your kind donations totalling ${:.2f}."
                            "\nIt will be put to very good use."
                            "\n\nSincerely,"
                            "\n-The Team")
        return string_to_format.format(self.name, self.total_donation)


class DonorCollection(object):
    def __init__(self, ):
        self.donor_list = []

    def add_new_donor(self, donor_name):
        self.donor_list.append(Donor(donor_name))

    def list_donor_names(self):
        return [x.name for x in self.donor_list]
