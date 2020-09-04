"""Contains the DonationData and Donor classes"""

import os
import re


class Donor:
    """Holds specific donor data"""

    def __init__(self, name=""):  # TODO remove KWARG
        """
        Creates a new donor

        Parameters
        ----------
        name : str, optional
            Donor Name, by default "", default raises error

        Raises
        ------
        ValueError
            If no "name" is specified
        """
        if not name:
            raise ValueError("Must enter a donor name.")
        self.name = name
        self.donations = []

    @property
    def total_given(self):
        """
        Return the sum of all the donor's donations.

        Returns
        -------
        total_given: int or float
            The sum of donations
        """
        return sum(self.donations)

    @property
    def total_gifts(self):
        """
        Return the number of donations the donor has made.

        Returns
        -------
        total_gifts: int
            The number of donations
        """
        return len(self.donations)

    def add_donation(self, new_amount):
        """
        Add a new donation to the donor's record.

        Parameters
        ----------
        new_amount : int or float
            The new donation amount for the donor

        Raises
        ------
        ValueError
            If donation amount is non-specified or is negative
        """
        if not new_amount or new_amount <= 0:
            raise ValueError("Donation new_amount must be a positive number")
        self.donations.append(new_amount)

    def thank_you_latest(self):
        """
        Return a personalized thank-you message to the donor for their latest donation.

        Returns
        -------
        text: str
            Thank you message

        Raises
        ------
        IndexError, subclass of LookupError
            If donor has not made any donations
        """
        last_donation = self.donations[-1]  # Raises LookupError(IndexError) if empty
        time_s = "times" if self.total_gifts > 1 else "time"
        text = (
            f"Thank you {self.name}"
            f" for your donation of ${last_donation:.2f}!"
            f" You have donated {self.total_gifts:d} {time_s}"
            f" for a total of ${self.total_given:.2f}."
        )
        return text

    def thank_you_overall(self):
        """
        Return a personalized thank-you message to the donor for their overall donations.

        Returns
        -------
        text: str
            Thank you message

        Raises
        ------
        LookupError
            If donor has not made any donations
        """
        if not self.donations:
            raise LookupError("Donor has not made any donations.")
        time_s = (
            f"{self.total_gifts:d} donations" if self.total_gifts > 1 else "donation"
        )  # Grammer correction of "donation" vs "# donations"
        text = (
            f"Thank you {self.name},\n\n"
            f"Your {time_s}"
            f" totaling ${self.total_given:.2f} will help us.\n\n"
            f"{'':>40}Best Regards,\n{'':>40}Jacob Erickson"
        )
        return text


class Record:
    """Holds all donation data for the charity"""

    def __init__(self):
        self.donors = {}

    def add_donor(self, new_donor_name):
        """
        Adds a donor to the charity's record.

        Stores donors in dict{name: Donor Object}

        Parameters
        ----------
        new_donor_name : str
            Name of new donor
        """
        self.donors[new_donor_name] = Donor(name=new_donor_name)

    @property
    def donor_list(self):
        """
        Return the list of donor names in record, sorted by decending total_given.

        Returns
        -------
        list
            All Donor names sorted decending by donor's total_given
        """
        return sorted(
            self.donors, key=lambda name: self.donors[name].total_given, reverse=True
        )

    def compose_report(self):
        """
        Return pretty-formatted report of all the donors.

        Produces a 'pretty' ASCII formatted table
        If no donors, return is empty formatted table.
        Donors are sorted in the report in decending order according to total-given amount.
        Uses double braces "{{}}" in format strings to dynamically update name field to
        accommodate long donor names without breaking report format.

        Returns
        -------
        report_list : list of str
            List of strings for each row of the report.
        """
        header_columns = ["Name", "Total Given", "# Gifts", "Average Gift"]
        report_list = []

        # Create Name Field Dynamically
        longest_name = max(self.donor_list + ["Name"], key=len)
        name_field_dynamic = "{{:^{:d}}}".format(len(longest_name) + 2)

        # Format report lines
        report_header = "|{}|  {{:^12}}|{{:^13}}|  {{:^13}}|"
        report_header = report_header.format(name_field_dynamic).format(*header_columns)

        report_length = len(report_header)
        report_break = re.sub("[^|]", "-", report_header).replace("|", "+")
        report_end = "-" * report_length
        report_title = "|{{:^{:d}}}|".format(report_length - 2).format("Donor Report")

        # Append Report Title and Header
        report_list.extend([report_end, report_title, report_break, report_header])

        # Append Sorted Donor Records
        for name in self.donor_list:
            total_given = self.donors[name].total_given
            if not total_given:  # Exclude donors with 0 given
                continue
            num_gifts = self.donors[name].total_gifts
            donor_average = float(total_given / num_gifts)
            donor_string = "|{}| ${{:>12.2f}}|{{:^13d}}| ${{:>13.2f}}|".format(
                name_field_dynamic
            ).format(name, total_given, num_gifts, donor_average)

            report_list.extend([report_break, donor_string])

        report_list.append(report_end)
        return report_list

    def save_all_donor_emails(self):
        """Write to disk thank-you emails for each donor."""
        path = os.path.dirname(os.path.realpath(__file__))
        file_id = 0
        for donor_name, donor_data in self.donors.items():
            try:
                thank_you_message = donor_data.thank_you_overall()
            except LookupError:  # Skips donors with $0 donated
                continue

            file_name = f"Donor{file_id:03d}_{donor_name}_gitnore.txt"
            file_id += 1
            with open(path + "\\" + file_name, "w") as file:
                file.write(thank_you_message)
