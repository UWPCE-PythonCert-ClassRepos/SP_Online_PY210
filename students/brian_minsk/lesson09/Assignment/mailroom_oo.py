# Author: Brian Minsk

from decimal import Decimal, ROUND_HALF_UP
from collections.abc import Iterable


class DonorCollection():
    """ DonorCollection contains Donor objects
    and, while a simple set (or dict) might be sufficient for this project,
    this class could conceivably be extended for more functionality.
    """
    def __init__(self, *args, **kwargs):
        self._donors = set()

    @property
    def donors(self):
        return self._donors

    @donors.setter
    def donors(self, some_donors):
        raise AttributeError("Donors cannot be set directly.")

    def is_existing_donor(self, name):
        """ Iterate through the Donors to see if the name matches a donor.
        If so, return True. If not, return False.

        Keyword arguments:
        name - string to match against the donor names in Donors or Donor
        object to match against the Objects.
        Assume name is in the form "Firstname Lastname"
        """
        if not isinstance(name, (str, Donor)):
            raise TypeError("Argument is not a string or Donor object.")
            return False

        if isinstance(name, Donor):
            if name in self._donors:
                return name
            else:
                return False

        # if function gets to here the name argument is a str
        for donor in self._donors:
            if (donor.full_name.lower() == name.lower()):
                return donor

        return False

    def add_donor(self, donor, donations=None):
        """ Add a single donor object to the collection.

        Keyword arguments:
        donor - A donor object or string representing a donor name.
        donations - A number representing a single donation, a iterable of
            numbers with multiple donations, or an iterable of Donations.
        """
        # first check if the donor is already in the collection
        if self.is_existing_donor(donor):
            raise ValueError("Donor already exists.")
            return None

        if not isinstance(donor, Donor):
            try:
                donor = Donor(donor)
            except TypeError:
                raise TypeError
                return None
            except ValueError:
                raise ValueError
                return None

        # The following exceptions are not actually created by add_donations
        # yet but they should be written ... some day ... ;)
        try:
            donor.donations.add_donations(donations)
        except TypeError:
            raise TypeError
            return False
        except ValueError:
            raise ValueError
            return False

        self._donors.add(donor)

        return donor

    def report(self):
        """ Print a list of donors, sorted by total historical donation amount.
        Include Donor Name, total donated, number of donations, and average
        donation amount as values in each row. The end result should be tabular
        (values in each column should align with those above and below) and
        look something like this:

        Donor Name                | Total Given | Num Gifts | Average Gift
        ------------------------------------------------------------------
        William Gates, III         $  653784.49           2  $   326892.24
        Mark Zuckerberg            $   16396.10           3  $     5465.37
        Jeff Bezos                 $     877.33           1  $      877.33
        Paul Allen                 $     708.42           3  $      236.14
        """
        sorted_donors = sorted(self._donors, key=Donor.sort_key, reverse=True)
        try:
            report_rows = [donor.create_report_row() for donor in sorted_donors]
        except AssertionError:
            raise AssertionError("Report creation failed.")
            return

        # create header
        first_row = "{:<26}| {:<11}| {:<10}| {:<12}\n".format("Donor Name",
                                                              "Total Given",
                                                              "Num Gifts",
                                                              "Average Gift")
        # create header line
        header_line = ("-" * 65) + "\n"

        report_rows_string = "\n".join(report_rows)

        return first_row + header_line + report_rows_string

    def get_donor_names(self):
        """ Return a list of all the donor names.
        """
        return [donor.full_name for donor in self._donors]


class Donor():
    def __init__(self, full_name="", donations=None):
        if full_name != "":
            try:
                self.test_name(full_name)
            except ValueError:
                raise ValueError("Name should be of the form 'Firstname Lastname'. Donor not created.")
            else:
                self._full_name = full_name
                self._donations = DonationCollection(donations)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, name):
        """ For purposes of this code the name argument should be of the form
        "Firstname Lastname", i.e. no middle name. Just a string with one space
        in the middle.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not self.test_name(name):
            raise ValueError('Name should be of the form "Firstname Lastname"')

        self._full_name = name

    @property
    def first_name(self):
        return self._full_name.split()[0]

    @first_name.setter
    def first_name(self, name):
        """ Prevent first name from being set since there needs to be both a
        first name and last name.
        """
        raise AttributeError("First name cannot be set by itself.")

    @property
    def last_name(self):
        return self._full_name.split()[1]

    @last_name.setter
    def last_name(self, name):
        """ Prevent last name from being set since there needs to be both a
        first name and last name.
        """
        raise AttributeError("Last name cannot be set by itself.")

    @property
    def donations(self):
        return self._donations

    @donations.setter
    def donations(self, donations=None):
        """ Donations argument can be any iterator with number values.
        """
        self._donations.add_donations(donations)

    def create_report_row(self):
        """ Create the rows in the body of the report with the actual donor
        data.
        """
        try:
            total_donation = self._donations.sum()
        except ValueError:
            raise ValueError("Non numeric values in donations.")

        num_donations = len(self._donations.donations)

        try:
            average_donation = self._donations.average()
        except ValueError:
            raise ValueError("Non numeric values in donations.")

        return "{:<26} ${:>11.2f} {:>10d}  ${:>12.2f}".format(self._full_name,
                                                              total_donation,
                                                              num_donations,
                                                              average_donation)

    def thank_you_message(self):
        """ Create a thank you letter and return as a string. Assume the last
        donation is the amount to use.
        """
        try:
            donation_amount = self._donations.donations[-1].get_formatted_donation_amount(with_sign=True)
        except IndexError:
            raise IndexError("No donations.")
            return None
        except NotImplementedError:
            raise NotImplementedError
            return None

        message_line1 = "\nDear {},\n".format(self._full_name)
        message_rest = "     Thank you very much for your generous donation of {}.\n     WINNING!\n".format(donation_amount)
        return message_line1 + message_rest

    def sort_key(self):
        try:
            return self._donations.sum()
        except TypeError:
            raise TypeError("Non numeric values in donations.")
            return 0

    @classmethod
    def test_name(cls, name):
        """ Test if the name is of the form "Firstname Lastname" i.e. a string
        with one space in the middle. If not, raise a ValueError exception.

        Keyword arguments:
        name - a string
        """
        if name.count(" ") != 1:
            raise ValueError
            return False

        if (name.find(" ") == 0
                or name.find(" ") == len(name) - 1):
            raise ValueError
            return False

        return True


class DonationCollection():
    """ DonationCollection is a simple list subclass and, while a simple list
    might be sufficient for this project, this class could conceivably be
    extended for more functionality.
    """
    # Note: "donations" is a bad name since it is also a property name for the
    # DonationCollection of a Donor. I just wasn't being inventive enough
    # with the name and I don't want to change in multiple places right now.
    def __init__(self, donations=[]):
        self.donations = []
        self.add_donation(donations)

    def add_donation(self, donation):
        """ Adds donation amounts if the are an int or a float regardless if a
        single donation or a group of donations in an iterable collection.
        """
        if isinstance(donation, (int, float)):
            self.donations.append(Donation(donation))
            return donation
        if isinstance(donation, Iterable):
            for item in donation:
                if isinstance(item, (int, float)):
                    self.donations.append(Donation(item))
                if isinstance(item, Donation):
                    self.donations.append(item)

    def add_donations(self, donations):
        """ Just another function name to call add_donations.
        """
        self.add_donation(donations)

    def average(self):
        """ Return the average of the donations.
        """
        if len(self.donations) == 0:
            return 0

        return self.sum() / len(self.donations)

    def sum(self):
        """ Return the sum of the donations.
        """
        sum = 0
        for donation in self.donations:
            # only add the amounts that are actually numbers
            if isinstance(donation.monetary_amount, (int, float, Decimal)):
                sum += donation.monetary_amount
        return sum


class Donation():
    """ For the current project donations are limited to monetary donations in
    USD but, presumably, this class could be extended to other types of
    donations, including money in other currencies, property, stock, etc.
    """
    def __init__(self, monetary_amount=0, currency="USD"):
        if not isinstance(monetary_amount, (int, float)):
            raise TypeError("Donation must be a monetary amount.")
            return None
        if monetary_amount < 0:
            raise ValueError("Donation must not be less than zero.")
            return None
        self._monetary_amount = Decimal(monetary_amount)
        self._currency = currency

    @property
    def monetary_amount(self):
        return self._monetary_amount

    @monetary_amount.setter
    def monetary_amount(self, amount):
        self._monetary_amount = Decimal(amount)

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    def get_formatted_donation_amount(self, with_sign=False):
        """ Return a donation amount formatted as US currency, with or without
        the dollar sign.

        Keyword arguments:
        with_sign - boolean to indicate whether or not a currency sign should
            be included in the output.
        """
        if self._currency == "USD":
            cents = Decimal('.01')
            amount = self._monetary_amount.quantize(cents, ROUND_HALF_UP)
            if with_sign:
                return "${}".format(amount)
            else:
                return "{}".format(amount)
        else:
            raise NotImplementedError("Not yet impletemented for non-monetary, non-USD donations.")
