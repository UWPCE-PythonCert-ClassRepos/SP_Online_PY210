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

    def __lt__(self, other):
        """
        Sort donor instances by total amount or last name, if amounts are equal

        Args:
            self, other (Donor):
                Two donor objects to compare
        """
        # If total amount is strictly less than, sort by it
        if self.total_donations() < other.total_donations():
            return self.total_donations() < other.total_donations()
        else:
        # Otherwise, sort by last name
            return self.name.split()[-1] < other.name.split()[-1]

    def add_donation(self, amount):
        """
        Add donation to donor's history

        Args:
            amount (float):
                Donation amount (must be strictly positive)
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
        updateDonor(name, amount):
            Creates a new donor with amount if not in collection, Otherwise
            adds donation to existing donor

        getDonor(name):
            Returns Donor instance (returns None if not found)

    """
    def __init__(self):
        """
        Create new DonorCollection instance with empty donor list
        """
        self.donors = {}

    def updateDonor(self, name, amount):
        """
        Updates collection with new donation for donor

        Args:
            name (str):
                Donor's name
            amount (float):
                Donation amount
        """
        # Create donor object if it doesn't exist, otherwise retrieve from collection
        d = self.getDonor(name)
        # Update donor object and replace in collection
        d.add_donation(amount)
        self.donors[name] = d

    def getDonor(self, name):
        """
        Return Donor instance using name to lookup

        Args:
            name (str):
                Donor name to look up.

        Returns:
            donor (Donor):
                Donor instance. Will return new donor instance if donor not found
        """
        return self.donors.get(name, Donor(name))

    def generate_report_data(self):
        """
        Generate report containing data for all donors
        """
        # Initialize list for report data
        report = []
        # Get list of donors and sort using custom sort
        donors = list(self.donors.values())
        donors.sort(reverse=True)
        for donor in donors:
            total = donor.total_donations()
            num_donation = len(donor.donations)
            report.append((donor.name, total, num_donation, total/num_donation))
        return report
