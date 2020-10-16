#!/usr/bin/env python3

"""
Becky Larson
Created 10/5/2020
Updated 10/11/2020
"""

"""
Donor Class: responsible for donor data encapsulation

This class holds information about a single donor.
Donor has attributes, properties ^ methods to provide access to donor.
Only code accesses info about a single donor should be part of this class.
"""


class Donor:
    def __init__(self, donor_name="", donations=None):
        """ Initialize the Donor"""
        """
        :donor_name:   Name of donor
        :donations:    Donations the donor has made
        """

        self._donor_name = donor_name
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

    def add_donation(self, donation):
        """
        adds donation amount to Donor donations
        :donation:    The amount they donated
        """

        if donation <= 0:
            raise ValueError("invalid donation amount")
        else:
            try:
                self.donations.append(float(donation))
            except TypeError as type_err:
                raise type_err("invalid donation type")

    @property
    def donations(self):
        """
        getter for donations
        :return: list of donations
        """
        return self._donations

    @property
    def donor_name(self):
        """
        getter for donor_name
        :return: name of donor
        """
        return self._donor_name

    @property
    def first_name(self):
        """ getter for donor first name """
        return self.donor_name.split()[0]

    @property
    def last_name(self):
        """ getter for donor last name """
        try:
            last_name = self.donor_name.split()[1]
        except:
            last_name = ""

        return last_name

    @classmethod
    def from_donor_name(cls, donor_name):
        """
        alternate constructor when no donations
        :param cls: class object
        :param donor_name: donor name
        :return:
        """
        return cls(donor_name)

    @property
    def num_donations(self):
        """
        getter for number of donations
        :return: number of donations
        """
        return len(self.donations) if self.donations else 0

    @property
    def total_donations(self):
        """
        getter for sum of donations
        :return: donations sum for donor
        """
        return sum(self.donations) if self.donations else 0

    @property
    def avg_donation(self):
        """
        getter for average donation
        :return: average donation of donor
        """
        if self.num_donations == 0:
            return 0
        else:
            return(self.total_donations/self.num_donations)

    def __len__(self):
        """
        Return the count of the donations.
        """
        return len(self.donations)

    def format_ty(self):
        """
        create formatted letter string for donor
        :return: formatted thank you
        """
        formatted = f"Dear {self.donor_name},"\
        f"\n\n\tThank you for your very kind donation of ${self.donations[-1]:,.2f}."\
         "\n\n\tIt will be put to very good use.\n\n\t\t\tSincerely,"\
         "\n\t\t\t   -The Team"

        return formatted

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
        Return the donor in a string.
        Return an output format of the Donor's name and donations.
        """
        donations = ",".join([f"{d:.02f}" for d in self._donations])
        return f"{self._donor_name},{donations}"

    def __lt__(self, other):
        """
        Return if this donor is less than another donor based on donations.
        """
        tuple_self = (self.total_donations, self.avg_donation)
        tuple_other = (other.total_donations, other.avg_donation)
        return tuple_self < tuple_other

    @classmethod
    def from_string(cls, input):
        """
        Instantiate a donor from a string.
        :input:  The string to parse into a donor.
        """
        input = input.split(',')
        name = input[0]
        donations = [float(donation) for donation in input[1:]]
        self = cls(name, donations)
        return self

    def __repr__(self):
        """
        :return: string of self instantiation
        """
        return f"Donor({self._donor_name!r}, {self._donations!r})"

    def sort_key(self):
        return self.last_name, self.first_name, self.donations

    def sort_by_donations(self):
        return self.total_donations


class DonorCollection:
    """DonorCollection: holds all of the donor objects
    Methods to add a new donor, search for a given donor, etc.
    """
    def __init__(self, donors=()):
        """
        DonorCollection
        :param donors: dict of Donor object(s)
        """

        self._donors = dict()

        if hasattr(donors, '__iter__') and not isinstance(donors, str):
            for donor in donors:
                if isinstance(donor, Donor):
                    self._donors[donor.donor_name] = donor
                else:
                    raise TypeError("object is not of type Donor")
        self.append(donors)

    def __len__(self):
        """
        Return the length of the donor list.
        """
        return len(self._donors)

    @property
    def donors(self):
        """
        getter for tuple of Donor objects
        :return: donors
        """
        return tuple(self._donors)

    def __getitem__(self, donor_name: str):
        """
        return Donor object using [] operator
        :param donor_name: key as name of donor
        :return: Donor object donations
        """
        return self._donors[donor_name]

    def list_donors(self):
        returned_list = []
        for donor in self._donors:
            returned_list.append(donor)
        return returned_list

    def is_donor_new(self, donor_name):
        is_donor_new = True
        for donor in self._donors:
            if donor == donor_name:
                is_donor_new = False
                break

        return is_donor_new

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
        Print formatted report of donors and donations
        Sort report by total donations
        :return: formatted report of Donor objects in DonorCollection
        """
        header = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift']
        report_header = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*header)
        divider = "-" * 80
        if not self._donors:
            raise ValueError("donors is empty")
        return "\n" + report_header + "\n" \
               + divider + "\n" \
               + "\n".join([self._donors[donor].report_row() for donor in sorted(self._donors,
                            key=lambda donor: self._donors[donor].sort_by_donations(),
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
