#!/usr/bin/env python3

"""
Class responsible for donor data encapsulation.
"""
class Donor(object):
    def __init__(self, name, donations=[0]):
        # Name must be a string
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be a string!")
        # All donations must be non-negative number (integer or float)
        for donation in donations:
            try:
                if donation < 0:
                    raise ValueError("donation can't be negative")
            except TypeError:
                print("donation must be a non-negative number")
        # Convert all donations to floats
        self._donations = [float(donation) for donation in donations]
           
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Name must be a string
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("name must be a string!")

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, value):
        # All donations must be non-negative number (integer or float)
        for donation in value:
            try:
                if donation < 0:
                    raise ValueError("donation can't be negative")
            except TypeError:
                print("donation must be a non-negative number")
        # Convert all donations to floats
        self._donations = [float(donation) for donation in value]

    def __str__(self):
        return '{}, {}'.format(self.name, self.donations)

    def send_thankyou(self):
        """Compose an email thanking the donor for their generous donation."""
        content = "\n\n".join([
            f"\nDear {self.name},",
            "Thank you for your generous donation in the amount of ${:.2f}! Have a great day!\n".format(self.donations[len(self.donations) - 1]),
        ])

        return content

    def add_donation(self, amount):
        """Add new amount to the donation list"""
        self.donations += [amount]

    @property
    def sum_donations(self):
        return sum(self.donations)
        
    @staticmethod
    def sort_key(self):
        return self.sum_donations

"""
Class responsible for donor collection data encapsulation.
"""
class DonorCollection(Donor):
    def __init__(self, donors=[]):
        for donor in donors:
            if isinstance(donor, Donor):
                super(Donor, donor).__init__()
                # Donor.__init__(donor, donor.name, donor.donations)
            else:
                raise TypeError("each donor must be a Donor class")
        self._donors = donors

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, value):
        for donor in value:
            if isinstance(donor, Donor):
                super(Donor, donor).__init__()
            else:
                raise TypeError("each donor must be a Donor class")
        self._donors = value
        
    def __str__(self):
        return '; '.join([donor.__str__() for donor in self.donors])

    def search_donor(self, name):
        """Return the donor's index in the list"""
        for index, donor in enumerate(self.donors):
            if donor.name == name:
                return index
        return -1

    def add_donor(self, name, amount=0.0):
        """Add new donor or update existing donor with given name and amount"""
        # Search donor
        index = self.search_donor(name)
        if index == -1:
            # Add new donor to the list
            self.donors += [Donor(name, [amount])]
        else:
            # Add donate amount to existing donor
            self.donors[index].add_donation(amount)

    def sort_by_donations(self, reverse=False):
        """Sort donors by total amount of donations"""
        if reverse:
            sorted_donors = sorted(self.donors, key=Donor.sort_key, reverse=True)
        else:
            sorted_donors = sorted(self.donors, key=Donor.sort_key)
        self.donors = sorted_donors
    
    def create_report(self):
        """Return a list of donors, sorted by total historical donation amount"""
        # Sort donors in descending order by total amount of their donations
        self.sort_by_donations(reverse=True)
        # Initialize report content
        content = []
        # Loop thru each donor
        for donor in self.donors:
            # Get total donated amount, number of gifts, and average gift amount
            total_given = donor.sum_donations
            num_gifts = len(donor.donations)
            ave_gift = total_given / num_gifts
            # Add to report content
            content.append([donor.name, total_given, num_gifts, ave_gift])

        return content
