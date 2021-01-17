#!/usr/bin/env python3

"""
A class-based system for creating Donor objects and DonorCollections objects.
"""

import os
import functools


@functools.total_ordering
class Donor:
    """Render Donor objects"""

    def __init__(self, name, amount=0, number=0):
        """Initialize new object with name, amount and number of donations"""

        self.name = name

        if amount >= 0:
            self.donation = amount
        else:
            self.donation = 0

        if isinstance(number, int) and number >= 0:
            self.number = number
        else:
            self.number = 0

    def __str__(self):
        """Return string with Donor name"""
        return "Donor: {}".format(self.name)

    def __eq__(self, other):
        """Define equals operator"""
        return self.donation == other.donation

    def __lt__(self, other):
        """Define less than operator"""
        return self.donation < other.donation

    def add_donation(self, amount):
        """Add donation amount for existing donor (and update number of donations)"""
        if amount >= 0:
            self.donation += amount
            self.add_number(1)

    def add_number(self, number):
        """Add to number of existing donations"""
        if isinstance(number, int) and number >= 0:
            self.number += number

    @property
    def average(self):
        """Return read only attribute for average donation"""
        return float("{:.2f}".format(self.donation / self.number))

    @property
    def write_letter(self):
        """Return string of thank you letter text to donor"""
        letter = """
        Dear {},
        Thank you for your collective contributions of ${:.2f} over the years.
        Your generous donations have been put to good use!
        Sincerely,
        Kyle at Kelby Doggo, Inc\n""".format(self.name, self.donation)
        return letter

    def send_letter(self):
        """Write thank you letter to text file in local directory"""
        text = self.write_letter
        name_list = (self.name.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(text)


class DonorCollections:
    """Render custom class object for set of Donor objects"""

    def __init__(self, donors=None):
        """Initialize DonorCollections as sorted list of Donors"""
        try:
            self.list = [x for x in donors]
            self.list.sort(reverse=True)
        except TypeError:
            self.list = []

    def __str__(self):
        """Return string with Donor names in DonorCollections"""
        text = [x.name for x in self.list]
        return "Donor Collection: {}".format(str(text))

    @property
    def get_names(self):
        """Return read only list of Donor Names in DonorCollections"""
        names = []
        for x in self.list:
            names.append(x.name)
        return names

    def add_donor(self, donor):
        """Add new donor to Donor List"""
        self.list.append(donor)
        self.list.sort(reverse=True)

    def format(self):
        """Return list of formatted rows for donors"""
        self.list.sort(reverse=True)
        heading = "| {dn:<20s}\t| {tg:<15s}\t| {ng:<10s}| {ag:<15s}  |".format
        report_list = [heading(dn="Donor Name", tg="Total Given",
                               ng="Num Gifts", ag="Average Gift"), 76 * "*"]
        row = "| {dn:<20s} \t| {ds:<1s} {tg:>14.2f} \t|" \
              "{ng:>10d}\t| {ds2:<1} {ag:>14.2f} |".format
        for i in self.list:
            report_list.append(row(dn=i.name, ds="$", tg=i.donation,
                                   ng=i.number, ds2="$", ag=i.average))
        return report_list

    def send_letters(self):
        """Write thank you letters to text files for all donors in DonorCollections"""
        for d in self.list:
            d.send_letter()
