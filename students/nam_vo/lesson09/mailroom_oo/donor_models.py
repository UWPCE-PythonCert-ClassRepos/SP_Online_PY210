#!/usr/bin/env python3

"""
Class responsible for donor data encapsulation.
"""
class Donor(object):
    def __init__(self, name, donations=[0]):
        self.name = name
        self.donations = donations

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
            # Python throws TypeError if donation is not a number (can' compare against zero)
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
class DonorCollection(object):

    def __init__(self, donors=[]):
        self.donors = donors

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, value):
        self._donors = []
        for id in value:
            self._donors.append(id)

    def __str__(self):
        return '{}: {}'.format('DonorCollection', self.donors)

    def search_donor(self, name, donor_dict):
        """Return the donor's index in the list"""
        for index, donor in enumerate(self.donors):
            try:
                if donor_dict[donor].name == name:
                    return index
            except KeyError:
                return -1
        return -1

    def add_donor(self, name, donor_dict, amount=0.0):
        """Return new donor object or index of existing donor with given name and amount"""
        # Search donor
        index = self.search_donor(name, donor_dict)
        if index == -1:
            # Create a new donor object
            obj = Donor(name, [amount])
            # Add new donor id to the list
            self.donors.append(id(obj))
            # Return new donor obj
            return obj
        else:
            # Add donate amount to existing donor
            donor_dict[self.donors[index]].add_donation(amount)
            # Return index
            return index

    def sort_by_donations(self, donor_dict, reverse=False):
        """Sort donors by total amount of donations"""
        if reverse:
            sorted_donors = sorted(donor_dict.values(), key=Donor.sort_key, reverse=True)
        else:
            sorted_donors = sorted(donor_dict.values(), key=Donor.sort_key)
        self.donors = [id(donor) for donor in sorted_donors]

    def create_report(self, donor_dict):
        """Return a list of donors, sorted by total historical donation amount"""
        # Sort donors in descending order by total amount of their donations
        self.sort_by_donations(donor_dict, reverse=True)
        # Initialize report content
        content = []
        # Loop thru each donor
        for donor in self.donors:
            # Get total donated amount, number of gifts, and average gift amount
            total_given = donor_dict[donor].sum_donations
            num_gifts = len(donor_dict[donor].donations)
            ave_gift = total_given / num_gifts
            # Add to report content
            content.append([donor_dict[donor].name, total_given, num_gifts, ave_gift])

        return content
