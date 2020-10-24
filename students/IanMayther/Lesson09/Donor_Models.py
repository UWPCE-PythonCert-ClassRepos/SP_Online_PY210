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

    # donors = []

    def __init__(self):
        MS = Donor("Morgan Stanely")
        '''
        CV = Donor("Cornelius Vanderbilt")
        JDR = Donor("John D. Rockefeller")
        SG = Donor("Stephen Girard")
        AC = Donor("Andrew Carnegie")
        '''
        self.donors = [MS]

    def __str__(self):
        return "Collection of Donors: {}".format(str(self.donors))

    def __repr__(self):
        return "{}".format(repr(self.donors))