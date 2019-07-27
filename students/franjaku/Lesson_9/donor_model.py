#!/usr/bin/env python
"""
Donor models contains the Donor and DonorColletion classes.
"""
from functools import total_ordering
from collections import OrderedDict

# Donor
@total_ordering
class Donor(object):
    """
    Create a new donor object (expand).

    Contains all the information for a single donor, including all methods
    necessary to work on that donor. Uses total_ordering to be able to sort.

    Donor Properties
    - donor.name: string with donor name
        - can't be change after init
    - donor.donations: list containing donations
        - can append to it
    - total dontation amount
    - total # of donations
    - average donation amount

    Donor Methods
    - add a donation to donors history
    - compute total donation amount by a donor
    - compute total number of donations by a donor
    - compute average donation amount
    - send thank you note to a donor
    """
    def __init__(self, name):
        """
        Initialize with only a name.
        Because of the error checking required for adding a donation I am
        choosing to not add a donation amount in __init__.
        """
        self._name = name
        self._donations = []

    def __str__(self):
        return "Donor: {}".format(self.name)

    def __repr__(self):
        return "Donor({})".format(self.name)

    def __lt__(self, other):
        return (self.total_donated < other.total_donated)

    def __eq__(self, other):
        return (self.total_donated == other.total_donated)

    def add_donation(self, donation):
        try:
            donation = float(donation)
            if donation > 0:
                self._donations.append(donation)
            else:
                print('Donation must be > 0')
                raise ValueError
        except ValueError:
            raise ValueError
            print('\nValue Error: Donation must by integer or float\n')

    def create_thank_you_note(self):
        if self.donations == []:
            print("Error: Donor has no donation history.\n")
            raise RuntimeError
        else:
            thank_you = "\nDear {},\n Thank you for your donation of ${:.2f}!\n".format(self.name, self.donations[-1])
            return thank_you

    @property
    def name(self):
        return self._name

    @property
    def donations(self):
        return self._donations

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donated(self):
        return sum(self.donations)

    @property
    def average_donation(self):
        return self.total_donated / self.num_donations


# Collection of donors
class DonorCollection(object):
    """
    Colletion object that has all the donor objects.

    Stores the donors in a dict with the name as the key.

    DonorCollection Properties
    - DonorCollection.donors: set-like items with names of donors
    - DonorCollection.items: returns DonorCollection.donors.items()

    DonorCollection Methods
    - Add a donor new donor
    - Interface with Donor objects to add a new donation to an existing donor
    - Generate a report
    """
    def __init__(self):
        self._donors = {}

    def __str__(self):
        print("\n Donor List\n-------------")
        for donor in self.donors:
            print(donor)
        print("\n")

        return "DonorCollection({})".format(self.donors)

    def add_donor(self, *args):
        if args == ():
            print('No donor added')
            raise UserWarning
        else:
            for Donor in args:
                self._donors.setdefault(Donor.name, Donor)

    def create_report(self):
        sorted_donors = OrderedDict(sorted(self.items, key=sort_key, reverse=True))

        lines = list()
        lines.append('-----Donation Report-----')
        lines.append('\n{:<15} | {:>14} | {:>11} | {:>16}'.format('Donor Name', 'Total Donation', '# donations', 'Average Donation'))
        lines.append('-'*66)
        line = "{:<15} | ${:>13.2f} | {:^11} | ${:>15.2f}"

        for key, d in sorted_donors.items():
            lines.append(line.format(d.name, d.total_donated, d.num_donations, d.average_donation))

        return lines

    def add_donation(self, key, amount):
        if key in self.donors:
            self._donors[key].add_donation(amount)
        else:
            d = Donor(key)
            d.add_donation(amount)
            self.add_donor(d)

    def get_donor(self, key):
        return self._donors.get(key)

    def send_letters(self):
        # if self.items:
        print(self.items)
        for donor, data in self.items:
            print(donor)
            print(data)
            print(data.total_donated)
            print("")
            with open(f"{donor}.txt", 'w') as outfile:
                print(f"Dear {donor}\n")
                outfile.write(f"Dear {donor}\n")
                print(f"Thank you for your total donation amount of ${data.total_donated}!\n")
                outfile.write(f"Thank you for your total donation amount of ${data.total_donated}!\n")
                print(f"Best wishes,\nThe Team")
                outfile.write(f"Best wishes,\nThe Team")
        # else:
        #     print('\nNo donor data available.\n')

    @property
    def donors(self):
        return self._donors.keys()

    @property
    def items(self):
        return self._donors.items()


def sort_key(Donor):
    return Donor[1].total_donated