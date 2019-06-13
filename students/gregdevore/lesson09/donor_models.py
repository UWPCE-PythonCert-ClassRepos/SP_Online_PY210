#!/usr/bin/env python3

"""
Module with classes for all donor data
Donor class: Encapsulate all data for a single donor
DonorCollection class: Encapsulate all data for handling multiple donors
"""

class Donor():
    """
    Class representing an individual donor

    Args:
        name (str):
            Donor's name

    Attributes:
        donations (list):
            List of donations (floats), arranged oldest to newest

    Methods:
        add_donation(amount):
            Add donation to donation attribute
        generate_email(donor_name, donation_amount, total_amount):
            Generate text for email thanking donor for their donation

    """

    def __init__(self, name):
        """
        Create a new donor instance

        Args:
            name (str):
                Donor's name
        """
        self.name = name
        self.donations = []

    def add_donation(self, amount):
        """
        Add donation to donor's history

        Args:
            amount (float):
                Donation amount (must be positive)
        """
        self.donations.append(amount)

    def last_donation(self):
        """
        Return last donation for donor.
        Returns $0 if donor has no donation history
        """
        return self.donations[-1] if self.donations else 0

    def total_donations(self):
        """
        Return total donations for donor
        """
        return sum(self.donations)

    def generate_email(self):
        """
        Generate email to donor
        """
        email_dict = {'donor_name':self.name,
                      'donation_amount':self.last_donation(),
                      'total_amount':self.total_donations()}

        # Create formatted email that can be copied & pasted
        email = ('\n'.join(['Dear {donor_name},','',
        'Thank you for your generous donation of ${donation_amount:.2f}.',
        'To date, you have donated a total of ${total_amount:.2f} to our charity.',
        'Your contributions help new arrivals receive the highest quality care possible.',
        'Please know that your donations make a world of difference!',
        '','Sincerely,','The Good Place Team'])).format(**email_dict)

        return(email)

class DonorCollection():
    """
    Class representing a collection of Donor instances

    Args:
        donors (dict):
            Dictionary of donor objects (key = donor name, value = donor object)

    Methods:
        addDonor(name):
            Creates a new Donor instance with the given name and adds it to the
            collection

        getDonor(name):
            Returns Donor instance (returns None if not found)

    """
    def __init__(self):
        """
        Create new DonorCollection instance with empty donor list
        """
        self.donors = {}

    def addDonor(self, name):
        """
        Create a new Donor instance and add it to the donors dictionary

        Args:
            name (str):
                Donor's name
        """
        d = Donor(name)
        self.donors[name] = d

    def getDonor(self, name):
        """
        Return Donor instance using name to lookup

        Args:
            name (str):
                Donor name to look up.

        Returns:
            donor (Donor):
                Donor instance. Will return None if donor name not found
        """
        return self.donors.get(name, None)
