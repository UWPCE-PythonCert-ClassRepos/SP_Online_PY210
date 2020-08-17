#!/usr/bin/env python3
"""
Purpose: OO Mailroom Part 1 python certificate from UW
Author: Pirouz Naghavi
Date: 08/14/2020
"""


class Donor:
    """Donor has object has name and a list of donations along with methods for data handling.

        Attributes:
            name: Is the name of the donor.
            donations: List of all the donations made by the donor.
    """
    def __init__(self, name, donations):
        """Initialises the donor object.

        Arguments:
            name: Is the name of the donor.
            donations: List of all the donations made by the donor.
        """
        self.check_name(name)
        self._name = name
        self.check_donation_list(donations)
        self._donations = donations[:]

    def add_donation(self, donation):
        """Adds a new donation to the donations.

        Arguments:
            donation: the amount of money being donated

        Raises:
            TypeError: If donation is not a float.
            ValueError: If Donation is negative zero or inf.
        """
        self.check_donation(donation)
        self._donations.append(donation)

    @property
    def name(self):
        """Donor name property."""
        return self._name

    @property
    def donations(self):
        """Donations name property."""
        return self._donations

    @property
    def donations_sum(self):
        """Sum of all donations made by the donor and rounds it to eight decimal places."""
        return round(sum(self._donations), 8)

    @property
    def donations_average(self):
        """Average of all donations made by the donor. Value is accurate up to eight decimal places. """
        return round(self.donations_sum / len(self._donations), 8)

    def generate_letter(self):
        """Generates a thank you letter for the donor."""
        letter = ''
        letter += 'Dear {},\n\n'.format(self._name)
        letter += 'Thank you for your latest donation of ${:0.2f}.'.format(self._donations[-1])
        letter += ' With this donation your overall donation has reached'
        letter += ' ${:0.2f}. We are very grateful for all your {} donations,'\
            .format(self.donations_sum, len(self._donations))
        letter += ' and we appreciate all your support. Please do not forget us in future we need because there is' \
                  ' still more work that needs to be done and we need your help to accomplish them.\n\n'
        letter += 'Best Regards\n'
        letter += 'Pirouz Naghavi'
        return letter

    def generate_report(self):
        """Generates donor's report."""
        return '{:<30.30s}\t ${:>15.15s}\t{:>12.12s}\t ${:>15.15s}'\
            .format(self._name, str(self.donations_sum), str(len(self._donations)), str(self.donations_average))

    @staticmethod
    def check_name(name):
        """Checks the name is an string and it is not an empty string.

        Arguments:
            name: Is the name of the donor.

        Raises:
            TypeError: If name is not of type str.
            ValueError: If name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError('Donor Name must be a string.')
        if name == "":
            raise ValueError('Name is required for every donor.')

    @staticmethod
    def check_donation(donation):
        """Checks the donation is a float.

        Arguments:
            donation: Is the list of donations of a given donor.

        Raises:
            TypeError: If donation is not a float.
            ValueError: If Donation is negative zero or inf.
        """
        if not isinstance(donation, float):
            raise TypeError('Donation must be of type float.')
        if donation <= 0:
            raise ValueError('Donation must be larger than zero.')
        if donation == float('inf'):
            raise ValueError('Donation cannot be infinity.')

    @staticmethod
    def check_donation_list(donations_list):
        """Checks the donor list contains only floats and it is not of type list and it is not None.

        Arguments:
            donations_list: Is the list of donations of a given donor.

        Raises:
            TypeError: If donations_list is not a list. If a value in the list is not a float.
                If donations_list is None.
        """
        if donations_list is None:
            raise TypeError('Donations list cannot be None.')
        if not isinstance(donations_list, list):
            raise TypeError('Donations list must be a list.')
        for donation in donations_list:
            Donor.check_donation(donation)

    def __eq__(self, other):
        """Checks if donor is equal to another donor."""
        if not isinstance(other, Donor):
            raise TypeError("Other must be a Donor.")
        return self.name == other.name and self.donations == other.donations


class DonorCollection:
    """Donor collection has all the donor object and can create collection reports and letters.

        Attributes:
            donors: Is the the collection of donors.
    """
    def __init__(self, donors_table):
        """Initialises the donorCollection object.

        Arguments:
            donors_table: Is the donor table used to creat the collection.
        """
        self.donors = self.read_donor_table_to_list(donors_table)
        self.sort_donors()

    def sort_donors(self):
        """Sorts donors according to top donor."""
        self.donors.sort(key=lambda i: i.donations_sum, reverse=True)

    @staticmethod
    def read_donor_table_to_list(donors_table):
        """Creates a list of donors from donor table.

        Arguments:
            donors_table: Is the donor table used to create the collection.

        Returns:
            List of donors.
        """
        donors = []
        for item in donors_table:
            donors.append(Donor(item[0], item[1]))
        return donors

    def list_of_donor_names(self):
        """"This function will return list of donors."""
        donor_names = '{:<30.30s}\t\n'.format('Donor Name')
        donor_names += '---------------------------------\n'
        for donor in self.donors:
            donor_names += '{:<30.30s}\t\n'.format(donor.name)
        return donor_names

    def add_donor_or_donation(self, name, donation):
        """Adds a donor to the donors list and resorts it with top donor at the top.

        Arguments:
            name: Name of the donor.
            donation: List of donations made by donor.

        Returns:
            A bool showing if the donor is existing or new. A thank you letter to the donor.

        """
        Donor.check_donation(donation)
        for donor in self.donors:
            if name == donor.name:
                donor.add_donation(donation)
                self.sort_donors()
                return False, donor.generate_letter()
        new_donor = Donor(name, [])
        new_donor.add_donation(donation)
        self.donors.append(new_donor)
        self.sort_donors()
        return True, new_donor.generate_letter()

    def create_donor_table(self):
        """Creates a list of donors in the format of the donor table."""
        return [(donor.name, donor.donations) for donor in self.donors]

    def thank_all_donors(self):
        """Creates thank you letters for all donors"""
        all_letters = ''
        for donor in self.donors:
            all_letters += donor.generate_letter() + '\n'
        return all_letters

    def report_all_donors(self):
        """Creates a report of all donors"""
        report = '{:<30.30s}\t|{:^16.16s}\t|{:^12.12s}\t|{:^16.16s}\n'\
            .format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
        report += '------------------------------------------------------------------------------------------------\n'
        for donor in self.donors:
            report += donor.generate_report() + '\n'
        return report

    def donor_name_exists(self, name):
        """Checks if donor name is in amongst the donors."""
        if isinstance(name, str):
            for donor in self.donors:
                if donor.name == name:
                    return True
            return False
        else:
            raise TypeError("Name is not a text.")

    def donor_exists(self, item):
        """Checks if donor is amongst the donors."""
        if isinstance(item, Donor):
            for donor in self.donors:
                if donor.name == item.name and donor.donations == item.donations:
                    return True
            return False
        else:
            raise TypeError("Item must be a donor object is not a text.")

    def __contains__(self, item):
        """Checks if donor or donor name is in amongst the donors"""
        if isinstance(item, str):
            return self.donor_name_exists(item)
        elif isinstance(item, Donor):
            return self.donor_exists(item)
        else:
            raise TypeError("Item must be of be ether the name of the donor or a Donor object.")