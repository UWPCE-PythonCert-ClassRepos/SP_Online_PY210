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
            raise AttributeError()
