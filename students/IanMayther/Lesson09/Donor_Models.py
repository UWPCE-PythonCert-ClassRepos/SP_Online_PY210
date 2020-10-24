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
        if isinstance(new_content, (float, int)):
            self.donations.append(float(new_content))
        elif isinstance(new_content, list):
            for i in range(len(new_content)):
                self.donations.append(new_content[i])
        return self.donations


class Donor_Collect(object):
    """
    Processes all the donors information doesn't work with donor functions
    """
    donors = {"Morgan Stanely": [0.01, 20.00],
            "Cornelius Vanderbilt": [800, 15, 10.00],
            "John D. Rockefeller": [7000, 150.00, 25],
            "Stephen Girard": [60000],
            "Andrew Carnegie": [0.04, 999.99],}        