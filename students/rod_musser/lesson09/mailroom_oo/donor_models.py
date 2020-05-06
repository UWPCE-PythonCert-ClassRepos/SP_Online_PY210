class Donor:
    """
    Represents a single donor.  Provides information about an individual donor including their
     donation history.
    """
    def __init__(self, full_name):
        """
        Create a new donor

        :param full_name: The first and last name of the donor.
        """
        self._name = full_name
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, full_name):
        self._name = full_name

    @property
    def num_of_donations(self):
        """
        Returns the number of donations this donor has made.
        """
        return len(self._donations)

    @property
    def sum_of_donations(self):
        """
        Returns the total number of donations this donor has made"""
        return round(sum(self._donations[:]), 2)

    @property
    def average_donation(self):
        """
        Returns the average number of donations this donor has made
        """
        return round(self.sum_of_donations / self.num_of_donations, 2)

    def add_donation(self, amount):
        """
        Add a donation to this donor's donation history

        :param amount: The amount of the donation
        """
        amount = float(amount)
        self._donations.append(round(amount, 2))


class DonorCollection:
    """
    Represents all the donors to the charity.  Provides methods to add a donor, search for a
    donor, etc.
    """
