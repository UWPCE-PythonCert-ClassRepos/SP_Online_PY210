#!/usr/bin/env python3

from datetime import datetime
from statistics import mean


class Donor:
    """
    Donor class represents a single donor
    """
    def __init__(self, donor_name="", donations=None):
        """
        Donor object initialization
        :param donor_name: full name of donor
        :param donations: donations
        """
        self.donor_name = donor_name.title().strip()
        self._donations = []
        if hasattr(donations, "__iter__"):
            try:
                [self.add_donation(donation) for donation in donations]
            except TypeError:
                print(f"{donations} is not iterable")
        else:
            self.add_donation(donations)

    def __call__(self, donor_name, donations):
        return self._donor_name, self._donations

    @property
    def donor_name(self):
        """
        getter for donor_name
        :return: name of donor
        """
        return self._donor_name

    @donor_name.setter
    def donor_name(self, name):
        """
        setter for donor_name
        :param value: name of donor
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError("donor_name must be a string")
        self._donor_name = name

    @property
    def donations(self):
        """
        getter for donations
        :return: list of donations
        """
        return self._donations

    @property
    def first_name(self):
        """
        getter for donor first name
        :return: first name of donor
        """
        return self.donor_name.split()[0]

    @property
    def last_name(self):
        """
        getter for donor last name
        :return: last name of donor
        """
        return self.donor_name.split()[1]

    @property
    def num_donations(self):
        """
        getter for number of donations
        :return: number of donations
        """
        return len(self.donations)

    @property
    def total_donations(self):
        """
        getter for sum of donations
        :return: donations sum for donor
        """
        return sum(self.donations)

    @property
    def avg_donation(self):
        """
        getter for average donation
        :return: average donation of donor
        """
        return round(mean(self.donations), 2)

    def add_donation(self, donation: float):
        """
        adds donation to Donor object
        :param self:
        :param donation: donation amount
        :return: None
        """
        if not donation or donation < 0:
            raise ValueError("invalid donation amount")
        try:
            self.donations.append(float(donation))
        except TypeError as type_err:
            raise type_err("invalid donation type")

    def thank_you(self):
        """
        create formatted letter string for donor
        :return: formatted letter
        """
        return f"\n\n{datetime.now.date()},\n\n\n" \
               f"Dear {self.donor_name},\n\n\n" \
               f"On behalf of all of us we thank you for your generous\n" \
               f"donation of ${self.donations[-1]:03.2f}.\n" \
               f"To date, you have donated: ${self.total_donations:03.2f}.\n" \
               "We look forward to seeing you at our annual meeting.\n\n" \
               "Sincerely,\n\n" \
               "ADL\n"

    def report_row(self):
        """
        format report row for Donor object
        :return: formatted report row Donor
        """
        return ('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'
                ).format(self.donor_name, ' ',
                         self.total_donations, ' ',
                         self.num_donations, ' ',
                         self.avg_donation
                         )

    def __str__(self):
        """
        prints Donor object
        :return: String representation of Donor object
        """
        return f"Donor Name: {self.donor_name}, Donations: {self.donations}"

    def __repr__(self):
        """
        :return: string of self instantiation
        """
        return f"Donor({self._donor_name, self.donations})"

    @staticmethod
    def sort_key(self):
        return self.last_name, self.first_name, self.donations

    @staticmethod
    def sort_by_donations(self):
        return self.donations


class DonorCollection:
    """
    DonorCollection class is a collection of Donor objects
    """
    def __init__(self, **donors):
        """
        DonorCollection
        :param donors: iterable of Donor object(s)
        """
        self.donors = []
        for donor in donors:
            try:
                self.donors.append(donor)
            except TypeError as type_err:
                raise type_err(f"invalid object type: {type(donor)}")

    @property
    def donors(self):
        """
        getter for tuple of Donor objects
        :return: donors
        """
        return tuple(self.donors)

    def append(self, donor):
        """
        add Donor object to collection
        :param donor: Donor object
        :return:
        """
        pass

    def report(self):
        """
        create report of Donor objects
        :return: formatted report of Donor objects in DonorCollection
        """
        """Return formatted report of Donor objects in DonorCollection."""
        header = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift']
        report_header = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*header)
        divider = "-" * 72
        return "\n" + report_header + "\n" \
               + divider + "\n" \
               + "\n".join([donor.report_row() for donor in self.donors]) \
               + "\n"



