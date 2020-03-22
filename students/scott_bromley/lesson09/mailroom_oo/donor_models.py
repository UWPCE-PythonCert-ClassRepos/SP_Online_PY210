#!/usr/bin/env python3

from datetime import datetime
from statistics import mean
from re import match


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
        self._donor_name = donor_name
        self.donor_name = donor_name if donor_name is not None else ""
        self._donations = []
        if not donations:
            self._donations = []
        elif hasattr(donations, "__iter__"):
            try:
                [self.add_donation(donation) for donation in donations]
            except TypeError as iter_err:
                raise iter_err(f"{donations} is not iterable")
        else:
            self.add_donation(donations)

    def __call__(self, donor_name, donations):
        return self._donor_name, self._donations

    @classmethod
    def from_donor_name(cls, donor_name):
        """
        alternate constructor w/ no donations
        :param cls: class object
        :param donor_name: donor name
        :return:
        """
        return cls(donor_name)

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
        :param name: name of donor
        :return: None
        """
        if not isinstance(name, str):
            raise TypeError("donor name must be a string")
        if not name.strip():
            raise ValueError("invalid donor name")
        name_regexp = r"^[a-zA-Z ]+$"
        self._donor_name = match(name_regexp, name).group()

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
        if self.num_donations == 0:
            raise ValueError(f"{self.donor_name} has no donations")
        return round(mean(self.donations), 2)

    def add_donation(self, donation):
        """
        adds donation to Donor donations
        :param self:
        :param donation: donation amount
        :return: None
        """
        if donation <= 0:
            raise ValueError("invalid donation amount")
        else:
            try:
                self.donations.append(float(donation))
            except TypeError as type_err:
                raise type_err("invalid donation type")

    def thank_you(self):
        """
        create formatted letter string for donor
        :return: formatted letter
        """
        if not self._donations:
            raise ValueError("donor has no donations")
        else:
            return f"\n\n{datetime.today().strftime('%Y-%d-%m')},\n\n\n" \
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
        if not self._donations:
            raise ValueError("donor has no donations")
        else:
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
        return f"Donor: {self._donor_name}, Donations: {self._donations}"

    def __repr__(self):
        """
        :return: string of self instantiation
        """
        return f"Donor({self._donor_name!r}, {self._donations!r})"

    @classmethod
    def sort_key(cls):
        return cls.last_name, cls.first_name, cls.donations

    @classmethod
    def sort_by_donations(cls):
        return cls.donations


class DonorCollection:
    """
    DonorCollection class is a collection of Donor objects
    """
    def __init__(self, donors=None):
        """
        DonorCollection
        :param donors: dict of Donor object(s)
        """
        self._donors = donors if donors else dict()
        if hasattr(donors, '__iter__') and not isinstance(donors, str):
            for donor in donors:
                if isinstance(donor, Donor):
                    self._donors[donor.donor_name] = donor
                else:
                    raise TypeError("object is not of type Donor")

    @property
    def donors(self):
        """
        getter for tuple of Donor objects
        :return: donors
        """
        return tuple(self._donors)

    def __getitem__(self, donor_name):
        """
        return Donor object using [] operator
        :param donor_name: key as name of donor
        :return: Donor object
        """
        try:
            return self._donors[donor_name]
        except KeyError as key_err:
            raise key_err

    def append(self, donor: Donor):
        """
        add Donor object to collection
        :param donor: Donor object or sequence of Donor objects
        :return: None
        """
        if hasattr(donor, '__iter__'):
            for _ in donor:
                if isinstance(_, Donor):
                    self._donors[_.donor_name] = _
                else:
                    raise TypeError("object is not of type Donor")
        else:
            self._donors[donor.donor_name] = donor

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
               + "\n".join([donor.report_row for donor in sorted(self._donors, key=lambda donor: donor.donations,
                                                                 reverse=True)]) \
               + "\n"

    def __str__(self):
        """
        prints Donor Collection object
        :return: String representation of Donor Collection object
        """
        return f"DonorCollection: {self._donors}"

    def __repr__(self):
        """
        :return: string of self instantiation
        """
        return f"DonorCollection({self._donors})"

