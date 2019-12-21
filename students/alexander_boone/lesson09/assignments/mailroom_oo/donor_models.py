#!/usr/bin/env python


class Donor:
    """A class to track a donor's information."""
    def __init__(self, fullname, don_sum=0, don_count=0):
        """Initialize Donor object."""
        self.fullname = fullname
        self.firstname = fullname.split()[0]
        try:
            self.lastname = fullname.split()[1]
        except IndexError:
            self.lastname = ""
        self.donation_sum = don_sum
        self.donation_count = don_count
        self.donation_avg = (self.donation_sum /
                             self.donation_count)

    def __repr__(self):
        """Return repr of Donor object."""
        return f"[{self.fullname}, ${self.donation_sum:03.2f}, " \
               f"{self.donation_count}, ${self.donation_avg:03.2f}]"

    def __str__(self):
        """Return str of Donor object."""
        return "Donor profile for " + self.fullname

    def new_donation(self, amount):
        """Add new donation to Donor object."""
        self.donation_sum += amount
        self.donation_count += 1
        self.donation_avg = (self.donation_sum /
                             self.donation_count)

    def thank_you(self):
        """Return thank_you letter for Donor."""
        return f"\nDear {self.fullname},\n\n" \
               "Thank you for your generosity.\n\n" \
               f"You have donated: ${self.donation_sum:03.2f}" \
               "\n\nWe are very grateful." \
               "\n\nBest,\n\n" \
               "Local Charity\n"

    def report_row(self):
        """Return formatted report_row for Donor object."""
        return ('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'
                ).format(self.fullname, ' ',
                         self.donation_sum, ' ',
                         self.donation_count, ' ',
                         self.donation_avg
                         )


class DonorCollection:
    """A class to store a collection of Donor objects."""
    def __init__(self, *donors):
        """Initialize DonorCollection object."""
        self.names = []
        self.data = []
        self.donors = list(donors)
        for donor in donors:
            self.names.append(donor.fullname)
            self.data.append(repr(donor))

    def __repr__(self):
        """Return repr of DonorCollection object."""
        return "\n".join(self.data)

    def __str__(self):
        """Return str of DonorCollection object."""
        return ("A collection of data for "
                + "the following donors:\n\n"
                + "\n".join(self.names)
                )

    def append(self, donor):
        """Append new Donor object to DonorCollection."""
        self.names.append(donor.fullname)
        self.data.append(repr(donor))
        self.donors.append(donor)

    def report(self):
        """Return formatted report of Donor objects in DonorCollection."""
        h = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts',
             '|', 'Average Gift']
        # create table heading
        report_headers = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*h)
        table_divider = '-' * 80
        return "\n" + report_headers + "\n" \
               + table_divider + "\n" \
               + "\n".join([donor.report_row() for donor in self.donors]) \
               + "\n"
