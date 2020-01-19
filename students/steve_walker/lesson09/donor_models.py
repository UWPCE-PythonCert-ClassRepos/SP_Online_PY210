"""
Creates a Donor class to store and return data for individual donors and
a DonorCollection class that contains a list of Donor objects to store
and return data for all donors at once.
"""


class Donor():
    """Store and return donation records for individual donors."""

    def __init__(self, name, donations=None):
        """Initialize the donor."""
        self.name = name
        self.donations = donations if donations is not None else []

    @property
    def sum_donations(self):
        return sum(self.donations, 0)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def avg_donation(self):
        return sum(self.donations, 0)/len(self.donations)

    def add_donation(self, donation_amount):
        """Store new donation record."""

        self.donations.append(donation_amount)

    def write_letter(self):
        """Write a thank you note for the most recent donation."""

        return f"To the esteemed {self.name}:\n\n" \
               "Thank you for your generous donation of " \
               f"${self.donations[-1]:.2f}. You're a champion!"


class DonorCollection():
    """Store and return donation records for all donors, stored as a dict."""

    def __init__(self):
        """Initialize the list to hold donor objects."""
        self.donors = []

    def add(self, donor):
        """Add donor to the DonorCollection."""

        self.donors.append(donor)

    def list(self):
        """Create list of donor names."""

        donor_list = [self.donors[i].name for i in range(len(self.donors))]
        return donor_list

    def sorted(self):
        """Return list of records sorted by greatest total donations."""

        return sorted(self.donors, key=lambda x: x.sum_donations, reverse=True)

    @staticmethod
    def from_dict(donor_info):
        """Create a DonorCollection instance from a pre-populated dict."""

        donors = DonorCollection()
        for k, v in donor_info.items():
            donor = Donor(k, v)
            donors.add(donor)

        return donors
