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
    def sum_donations(self):
        """
        This property returns a sum of all donations for a given donor.
        """
        return sum(self.donations)


class DonorCollection:
    """
    The DonorCollection() class represents a DonorCollection
    and all related functionality.
    """
    pass
