# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: donor_models.py
# Desc: The module donor_models.py contains the Donor and DonorCollection classes.
# Tian Xie, 2020-05-21, Created File
# ------------------------------------------------------------------------#


class Donor(object):
    def __init__(self, name, donation=None):
        """ Initialize the Donor class """

        self._name = name
        if donation == None:
            self.donations = []
        else:
            self.donations = list(donation)

    def add_donation(self, donation):
        """
        adds donation to the donations list
        :param donation: Donation amount that will be added to donor list
        :return: donations with the new amount added
        """
        return self.donations.append(donation)

    @property
    def previous_donations(self):
        """
        returns the most recent donation in the  donor list
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
        return self.donations[-1]

    @property
    def avg_donation(self):
        """
        returns the average donation amount made by thr donor
        """
        return sum(self.donations) / len(self.donations)


class DonorCollection():
    # Default donor dictionary
    dict_of_donors = {'Jeff Bezos': [1.00, 50.00],
                      'Warren Buffet': [100.00, 1000.00],
                      'Bill Gates': [100.00, 500.00],
                      'Tim Cook': [300.00],
                      'Jack Ma': [2000.00]}

    def __init__(self):

        self.donor_list = []

    def __iter__(self):
        # Iterates over donor_list
        return self.donor_list.__iter__()

    def adding_donor_info(name, donation, donor_dict):
        """Adding donor info to the dict.

        Args:
            name: donor name
            donation: donation amount
            donor_dict: dictionary of donors.

        Returns:
            None.

        """
        if name not in donor_dict:
            added_donor = {name: [float(donation)]}
            donor_dict.update(added_donor)
        else:
            donor_dict[name].append(
                float(donation))  # If donor name exists, append the donation amount rather than updating the dictionary



    def show_donor_dict(self):
        """Displays current donor list.

        Args:
            donor_dict: dictionary of donors.

        Returns:
            None.

        """
        donor_lst = []
        for name in donor_dict:
            donor_lst.append(name)
        return donor_lst

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
