#!/usr/bin/env python3

"""
Donor Class and Donation Class
"""

class Donor(object):
    """
    Control all data related to a specific donor
    """
    donations = []

    def __init__(self, name=None):
        if name is None:
            raise AttributeError("Must supply Donor Name")
        elif isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Input must be str")

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "{}({})".format(self.name, self.donations)

    def append(self,new_content):
        don = float(new_content)
        return self.donations.append(don)
        