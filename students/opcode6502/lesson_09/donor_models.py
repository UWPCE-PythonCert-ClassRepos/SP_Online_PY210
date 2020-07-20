# donor_models.py
# opcode6502: SP_Online_PY210


class Donor():
    """
    The Donor class represents a Donor
    and all related functionality.
    """

    def __init__(self, name, donations=None):
        """
        This will initialize a Donor object.
        This will set the 'name' and 'donations' for the new object.
        """
        self.name = name
        #
        # We need to check 'donations' here or we could generate an exception.
        if donations is None:
            self.donations = []
        else:
            self.donations = donations

    def add_donation(self, donation_amount):
        """
        This method adds a given donation for a given donor.
        """
        self.donations.append(donation_amount)

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
        return '[ THANK ]: Thank you: Donor: {}: Amount: ${}'.format(self.name, self.donations[-1])


class DonorCollection():
    """
    The DonorCollection class represents a DonorCollection
    and all related functionality.
    """

    def __init__(self):
        """
        This will initialize a DonorCollection object.
        This will create a new list 'donors_db'.
        """
        self.donors_db = []

    def add(self, donor):
        """
        Add a donor to the 'donors_db'.
        """
        self.donors_db.append(donor)

    def data_import(data):
        """
        This will initialize a DonorCollection object and populate it.
        """
        #
        # Create the DonorCollection object.
        dc = DonorCollection()
        #
        # For each item in 'data', add to the DonorCollection.
        for key, value in data.items():
            d = Donor(key, value)
            dc.add(d)
        #
        # Return statement.
        return dc

    def list(self):
        """
        Create and return a list of donor names.
        """
        #
        # This could be refactored and simplified.
        # This is not very 'pythonic'.
        # I am sure there is a slick one-liner that would to this in Python.
        # Leaving as is for now to meet submission deadline with existing
        # functionality. A code review would catch this and flag it.
        #
        # Create the list.
        temp_list = []
        index = 0
        for d in self.donors_db:
            temp_list.append(self.donors_db[index].name)
            index += 1
        #
        # Return statement.
        return temp_list

    def sorted(self):
        """
        Create and return a list of donor names sorted by
        the highest sum_donation.
        """
        #
        # Return statement.
        return sorted(self.donors_db, key=lambda x: x.sum_donations, reverse=True)
