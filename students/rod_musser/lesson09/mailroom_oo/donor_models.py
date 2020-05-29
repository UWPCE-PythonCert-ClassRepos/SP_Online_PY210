from functools import total_ordering

class Letter:
    """
    Represents a letter sent to the donor after a donation is made
    """
    letter_template = "Dear {name},\n\n\
Thank you for your generous support of Rod's Early \
Retirement Fund.\n\nYour donation totaling ${amt:.2f} makes Rod's early retirement \
dreams a reality.  Your generous support will enable Rod to perform critical early retirement \
tasks like \n\n\t- Mai Tais on the beach \n\t- First class airline travel \n\t- Alpine skiing. \
\n\nAgain, thank you for your generous support. \
\n\nSincerely, \n\nRod Musser \nChairperson\nRod's Early Retirement Fund"

    def __init__(self, donor):
        """
        Gets donor name and amount of donor's most recent donation.
        """
        self._letter_data = {}
        self._letter_data['name'] = donor.name
        self._letter_data['amt'] = donor.last_donation.amount

    def generate_letter(self):
        """
        Returns a formatted string of the thank you letter
        """
        return Letter.letter_template.format(**self._letter_data)


class Donation:
    """
    Represents a single donation.  Currently only has one attribute - amount.
    However, in the future, additional informtion that could be tracked is date
    of the donation, payment type, currency, or other donation info.
    """

    def __init__(self, amt):
        """
        Create a new donation

        :param amt: The amount of the donation
        """
        self.amount = amt

    def __radd__(self, other):
        return round((other + self.amount), 2)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amt):
        try:
            amt = float(amt)
        except ValueError:
            raise ValueError('Please enter a number for the donation amount.')
        if (amt <= 0):
            raise ValueError('Donation amount must be more than 0')
        self._amount = round(amt, 2)


@total_ordering
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
        self.name = full_name
        self._donations = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        return self.sum_of_donations < other.sum_of_donations

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
        Returns the total amount of donations this donor has made
        """
        return sum(self._donations[:])

    @property
    def average_donation(self):
        """
        Returns the average number of donations this donor has made
        """
        return round(self.sum_of_donations / self.num_of_donations, 2)

    @property
    def last_donation(self):
        """
        Reutrns the most recent donation made by the donor
        """
        return self._donations[-1]

    def add_donation(self, amount):
        """
        Add a donation to this donor's donation history

        :param amount: The amount of the donation
        """
        self._donations.append(Donation(amount))

    def create_thank_you_letter(self):
        """
        Returns a thank you letter for the donor's most recent donation.
        """
        return Letter(self).generate_letter()


class DonorCollection:
    """
    Represents all the donors to the charity.  Provides methods to add a donor, search for a
    donor, etc.
    """
    def __init__(self):
        self._donors = {}

    def add_donation(self, full_name, amount):
        """
        Adds a donation for the donor.  If the donor does not exist, it will create
        a new Donor object.

        :param full_name: The first and last name of the donor

        :param amount: The amount of the donation.  It must be a positive number
        """
        self._donors.setdefault(full_name, Donor(full_name)).add_donation(amount)

    def get_donor(self, full_name):
        """
        Returns donor for name

        :param full_name: The first and last name of the donor
        """
        try:
            return self._donors[full_name]
        except KeyError:
            return None

    def has_donor(self, full_name):
        """
        Does case insensitve serach for donor name.
        If found, returns correctly cased name.  Otherwise, returns None

        :param full_name: The first and last name of the donor
        """
        for name in self._donors.keys():
            if name.lower() == full_name.lower():
                return name
        return None

    def list_donors(self):
        """
        Return a list of donor names with each name on a new line.
        """
        newLine = '\n'
        return f"{newLine.join(self._donors)}"

    def print_report(self):
        """
        Formats and returns the report
        """
        report_contents = []
        report_contents.append("Donor Name" + (' ' * 16) +
                               ("| Total Given | Num Gifts | Avergage Gift"))
        report_contents.append("-" * 68)
        row = "{name:<26s} ${total:=12.2f}  {num:10d} ${avg:14.2f}".format
        if len(self._donors) > 0:
            donors = list(self._donors.values())
            donors.sort(reverse=True)
            for donor in donors:
                report_contents.append(row(name=donor.name, total=donor.sum_of_donations,
                                           num=donor.num_of_donations,
                                           avg=donor.average_donation))
        return ('\n').join(report_contents)
