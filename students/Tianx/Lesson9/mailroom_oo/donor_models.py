# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: donor_models.py
# Desc: The module donor_models.py contains the Donor and DonorCollection classes.
# Tian Xie, 2020-05-21, Created File
# ------------------------------------------------------------------------#


class Donor(object):
    def __init__(self, donor_name, donation=None):
        """ Initialize the Donor class """
        self.name = donor_name

        if donation is None:
            self.donations = []
        else:
            self.donations = list(donation)

    def add_donation(self, donation):
        """
        adds donation to the donations list
        :param donation: Donation amount that will be added to donor list
        :return: donations with the new amount added
        """
        return self.donations.append(float(donation))

    @property
    def previous_donations(self):
        """
        returns the most recent donation in the donor list
        """
        return self.donations[-1]

    @property
    def num_donations(self):
        """
        returns the total number of donations made by the donor
        """
        return len(self.donations)

    @property
    def total_donations(self):
        """
        returns the total donations made by a single donor
        """
        return sum(self.donations)

    @property
    def avg_donation(self):
        """
        returns the average donation amount made by the donor
        """
        return self.total_donations / len(self.donations)

    @property
    def create_email(self):
        """
        returns an email template for each donor
        """
        email = f'Dear {self.name},\n\nThank you for your generosity, your donation of ${float(self.donations[-1]):.2f} will be put to good use.\n\n''Warm regards,\nMailroom Staff'
        return email

    # special method for sorting
    def __lt__(self, other):
        return self.total_donations < other.total_donations

    def __iter__(self):
        return self.name.__iter__()

    def __repr__(self):
        return (f'{self.name}, {self.donations}')


class DonorCollection:
    def __init__(self):
        self.donor_list = [Donor('Jeff Bezos', [1.00, 50.00]),
                           Donor('Warren Buffet', [100.00, 1000.00]),
                           Donor('Bill Gates', [100.00, 500.00]),
                           Donor('Tim Cook', [300.00]),
                           Donor('Jack Ma', [2000.00])]

    def add_donor(self, donor_name, donation):
        """
        Returns new donor object.
        """
        new_donor = Donor(donor_name, [float(donation)])
        self.donor_list.append(new_donor)
        return new_donor

    def get_donor(self, donor_name):
        """
        Return the donor if present.
        """
        for donor in self.donor_list:
            if donor_name == donor.name:
                return donor

    def donor_exists(self, donor_name):
        """
        Check if donor exists.
        """
        for donor in self.donor_list:
            if donor_name == donor.name:
                return True
        return False

    def add_new_donation(self, donor_name, donation):
        """
        Handles new donation, add donation to exiting the donor if present.
        Creates new donor and add donation if name is not found.
        """
        for donor in self.donor_list:
            if donor_name == donor.name:
                donor.add_donation(donation)
                return
        self.add_donor(donor_name, donation)

    @property
    def show_donor_list(self):
        """
        Return the all donor names.
        """
        donor_name = ""
        for donor in self.donor_list:
            donor_name += donor.name + '\n'
        return donor_name

    def create_report(self):
        """Formatting a report.

        Args:
           None

        Returns:
           report object

        """
        report = ['Donor Name                | Total Given | Num Gifts | Average Gift','------------------------------------------------------------------']
        self.donor_list.sort(reverse=True)
        for i in self.donor_list:
            report.append(f'{i.name:26} ${float(i.total_donations):>11.2f} {i.num_donations:>11.0f}  ${i.avg_donation:>12.2f}')
        return report

    def send_all(self):
        """Writing a letter for each donor and save them into a directory with the donor's name.

        Args:
           None

        Returns:
           None.
       """
        for donor in self.donor_list:
            file_name = f'{donor.name.replace(" ", "_"):}.txt'
            with open(file_name, 'w') as objfile:
                objfile.write(
                    f'Dear {donor.name},\n\nThank you for your generosity, your total donation amount is ${float(donor.total_donations):.2f}.\n\nWarm regards,\nMailroom Staff')
