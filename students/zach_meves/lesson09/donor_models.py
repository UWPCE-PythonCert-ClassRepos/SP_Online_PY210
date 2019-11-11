"""
Data structures to hold and define donor and donation data.
"""

from typing import Union
import os

DONOR_THANK_TEMPLATE = "Dear {name},\n" + \
                       "    Thank you very much for your recent donation of $ {last_donation:.2f}. We truly \n" + \
                       "appreciate your contribution.\n\n    Your total tax-deductible donation amount is now " + \
                       "$ {total_donation:.2f}.\n\n" + \
                       "Sincerely,\n" + \
                       "    Zach"
DONOR_BLANK_TEMPLATE = "Thank you, {name}, for nothing.\nSincerely,\n    Zach"

REPORT_HEADER = "Donor Name                | Total Given | Num Gifts | Average Gift\n" + \
                "------------------------------------------------------------------\n"
REPORT_ENTRY = "{name:<25}   $ {sm:>9.2f}   {l:>9d}   $ {avg:>10.2f}\n"


class Donor:
    """Class defining a single donor. A donor has a name and record of
    all donations made."""

    def __init__(self, name: str, donations: Union[list, tuple, float] = None):
        """Construct a donor with a name and optionally a list of donations to
        start with.

        Parameters
        ----------
        name : str
            Name of donor
        donations : sequence or float
            Donation(s) to initialize donor with. If a sequence is provided,
            the values will be COPIED, not referred to.
        """

        self._name = ''
        self._donations = []

        self.name = name
        if hasattr(donations, '__iter__'):
            for donation in donations:
                self.add_donation(donation)
        elif donations is not None:
            self.add_donation(donations)

    @property
    def name(self):
        """str : Name of donor"""
        return self._name

    @name.setter
    def name(self, new_name: str):
        # Set the donor name
        if isinstance(new_name, str):
            new_name = new_name.strip()
            if not len(new_name):
                raise ValueError("Donor name must be a non-empty string")
            self._name = new_name
        else:
            raise TypeError("Donor name must be a string")

    @property
    def donations(self):
        """list : List of past donations (read-only)"""
        return self._donations[:]

    def add_donation(self, donation: float):
        """Add a donation for this donor.

        Parameters
        ----------
        donation : float
            Donation value to add
        """

        try:
            donation = float(donation)
        except ValueError:
            raise TypeError("Donations must be positive numbers.")
        else:
            if donation > 0:
                self._donations.append(float(donation))
            else:
                raise ValueError("Donations must be positive numbers")

    def last_donation(self) -> Union[float, None]:
        """Return the last donation this donor made.

        Returns
        -------
        float or None
            Last donation value, or ``None`` if no donations made
        """
        try:
            return self._donations[-1]
        except IndexError:
            return None

    def total_donations(self) -> float:
        """Return the total donation amount for this donor.

        Returns
        -------
        float
            Total donation amount for this donor"""

        return sum(self.donations)

    def number_of_donations(self) -> int:
        """Return the number of donations made by this donor.

        Returns
        -------
        int
            Number of donations"""

        return len(self._donations)

    def average_donation(self) -> float:
        """Return the average donation amount made by this donor.

        Returns
        -------
        float
            Average donation amount"""

        try:
            return self.total_donations() / self.number_of_donations()
        except ZeroDivisionError:
            return 0

    def get_thankyou(self) -> str:
        """Get a thank you letter for this donor.

        Returns
        -------
        str
            Thank you letter for this donor"""

        if self.total_donations() > 0:
            return DONOR_THANK_TEMPLATE.format(name=self.name, last_donation=self.last_donation(),
                                               total_donation=self.total_donations())
        else:
            return DONOR_BLANK_TEMPLATE.format(name=self.name)

    def __lt__(self, other):
        return self.total_donations() < other.total_donations()


class DonorCollection:
    """Class defining a collection of :py:class:`Donor` objects."""

    def __init__(self, *donors):
        """Initialize a DonorCollection with some optional Donors.

        Parameters
        ----------
        *donors
            Variable number of :py:class:`Donor` objects to start with
        """

        self._donors = []
        for donor in donors:
            if isinstance(donor, Donor):
                self._donors.append(donor)
            else:
                raise TypeError("Only objects of type 'Donor' are allowed.")

    @property
    def donors(self) -> tuple:
        """Return currently held :py:class:`Donor` objects."""
        return tuple(self._donors)

    def get_donor_names(self) -> tuple:
        """Return current Donor names."""
        return tuple([d.name for d in self.donors])

    def _get_donor_names_lower(self) -> tuple:
        """Return lowercase Donor names"""
        return tuple([d.name.lower() for d in self.donors])

    def add_donor(self, name: str, donations: Union[list, tuple, float] = None):
        """Create and add a Donor to this collection.

        Parameters
        ----------
        name : str
            Name of Donor
        donations : sequence or float
            Donation(s) to initialize Donor with
        """

        name = name.strip()
        if name.lower() in self._get_donor_names_lower():
            raise ValueError("Donor with name {} already exists".format(name))

        self._donors.append(Donor(name, donations=donations))

    def add_donation(self, name: str, donation: float):
        """Add a donation to a Donor, or create a new donor with the inital donation
        if not present in collection.

        Parameters
        ----------
        name : str
            Name of donor
        donation : float
            Donation amount"""

        try:
            self[name].add_donation(donation)
        except ValueError:
            self.add_donor(name, donation)

    def __getitem__(self, name) -> Donor:
        """Return a Donor with the given name, accessed with [] operator.

        Name matching is case-insensitive"""

        name = name.strip()
        try:
            return self._donors[self._get_donor_names_lower().index(name.lower())]
        except ValueError:
            raise ValueError(f"No Donor with name {name} exists.")

    def get_report(self) -> str:
        """Generate a report of all donors and donations, sorted by total donation amount.

        Returns
        -------
        str
            Report of donors and donations"""

        strs = [REPORT_HEADER]
        donors = sorted(self.donors)
        for donor in donors:
            strs.append(REPORT_ENTRY.format(name=donor.name, sm=donor.total_donations(),
                                            l=donor.number_of_donations(),
                                            avg=donor.average_donation()))
        return ''.join(strs)

    def write_thank_yous(self, directory='.'):
        """Generate thank you notes for all Donors and write as .txt files to a
        directory on the filesystem.

        Parameters
        ----------
        directory : str
            Directory to place output files in"""

        for donor in self.donors:
            note = donor.get_thankyou()
            with open(os.path.join(directory, f"{donor.name}_thanks.txt"), 'w') as f:
                f.write(note)
