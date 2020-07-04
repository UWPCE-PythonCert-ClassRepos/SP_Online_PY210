# donor_models.py
# opcode6502: SP_Online_PY210


class Donor:
    """
    The Donor() class represents a Donor
    and all related functionality.
    """

    def __init__(self, name, donations=[]):
        """
        This will initialize a Donor object.
        This will set the 'name' and 'donations' for the new object.
        """
        self.name = name
        self.donations = donations

    def add_donation(self, donation=[]):
        """
        This method adds a given donation for a given donor.
        """
        self.donations.extend(donation)

    @property
    def average_donation(self):
        """
        This method returns the average donations for a given donor.
        """
        #
        # We need to check for no donations to avoid a ZeroDivisionError.
        if self.num_donations == 0:
            return 0
        else:
            return self.sum_donations / self.num_donations

    @property
    def num_donations(self):
        """
        This property returns the total number of donations for a given donor.
        """
        return len(self.donations)

    @property
    def sum_donations(self):
        """
        This property returns a sum of all donations for a given donor.
        """
        return sum(self.donations)

    def thank_you_message(self):
        """
        This property returns a thank you message.
        """
        return ('Thank you: Donor: {}: Amount: ${}').format(self.name, self.donations[-1])


class DonorCollection:
    """
    The DonorCollection() class represents a DonorCollection
    and all related functionality.
    """

    def __init__(self):
        """
        This will initialize a DonorCollection object.
        This will create a new list 'donors_db'.
        """
        self.donors_db = []
