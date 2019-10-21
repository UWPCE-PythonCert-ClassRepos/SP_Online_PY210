EMAIL_TEMPLATE = (
    "Dear {},\n\n"
    "Thank you for your last donation of ${:.2f}.\n"
    "You have contributed a total of ${:.2f} over {} donation(s).\n"
    "Your generosity is appreciated.\n"
    "\nSincerely,\n"
    "-The Team\n\n"
)

THANK_YOU_TEMPLATE = (
    """\nDear {},\n"""
    """Thank you for your recent donation of ${:.2f}. """
    """Your donation will help us purchase a taxidermied seagull.\n"""
    """Please consider donating again at your earliest convenience.\n\n"""
    """Sincerely,\n"""
    """The Human Fund\n"""
)

class Donor(object):
    """
    Donor class

    The Donor class contains all information about a single donor.

    Args:
        name: Donor name
        donations: donation amount(s)

    """
    def __init__(self, name, donations=[]):
        self._name = name.title()
        self._donations = []
        self.add_donation(donations)

    @property
    def name(self):
        return self._name

    def add_donation(self, donation):
        """ 
        Adds donations to donor by value or by list of numeric values

        Args:
            donation: Value or list of numeric values to add to donor donation
        Raises:
            ValueError
        """
        if (type(donation) != list):
            donation = [donation]
        if all(isinstance(x,(float, int)) for x in donation):
            self._donations.extend(donation)
        else:
            raise ValueError("Donation amount must be numeric")

    def thank_you_email(self):
        """
        Generates the thank you email for the donor's last donation,
        number of donations and total donation amount.
        """
        return EMAIL_TEMPLATE.format(self.name, 
                                        self.last_donation,
                                        self.donation_total, 
                                        self.num_donations)

    def thank_you_letter(self):
        """
        Generates a thank you letter for the last donation amount
        """
        return THANK_YOU_TEMPLATE.format(self.name, self.last_donation)

    @property
    def donations(self):
        if self._donations:
            return self._donations
        else:
            return 0.00
    @property
    def donation_total(self):
        return sum(self._donations)

    @property
    def num_donations(self):
        return len(self._donations)

    @property
    def last_donation(self):
        return self._donations[-1]

    @property
    def average_donation(self):
        if self.num_donations:
            return self.donation_total / self.num_donations
        else:
            return 0.00

    def __lt__(self, other):
        return self.donation_total < other.donation_total

    def __gt__(self, other):
        return self.donation_total > other.donation_total

    def __str__(self):
        return f"Donor total donations: {self.donation_total}"

    def __repr__(self):
        return self.name

class DonorCollection(object):
    """
    DonorCollection class

    The DonorCollection class holds the donor subclass consisting
    within the study.

    """
    def __init__(self):
        self._donors = []

    def add_donor(self, donor):
        """
        Adds new donor or appends to existing donor donation values.

        Args:
            donor: Donor class instance with name and donation amount

        Raises:
            ValueError: If empty donor already exists
            TypeError: If other than Donor class is passed in

        """
        if isinstance(donor, Donor):
            if donor.name not in [repr(x) for x in self.donor_list]:
                self._donors.append(donor)
            else:
                if donor.donations:
                    for d in self._donors:
                        if d.name == donor.name:
                            d.add_donation(donor.donation_total)
                else:
                    raise ValueError("Donor '" + repr(donor) + "' Already Exists")
        else:
            raise TypeError("donor needs to be of class Donor")
            
        self._donors.sort(reverse=True)

    @property
    def donor_list(self):
        return self._donors

    @property
    def max_name_length(self):
        return max([len(x.name) for x in self.donor_list])

    def generate_report(self):
        """
        Creates a report of all donors and donation totals, number of donations, 
        and average donation amount.
        """
        report = []
        name_length = self.max_name_length
        f_str = " {" + f":<{name_length}" + "} | {} | {} | {}" 
        title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        report.append(title_str)
        report.append("-" * len(title_str))

        for donor in self._donors:
            spaces = " " * (name_length - len(donor.name))
            f_str = f"{donor.name}{spaces}   ${donor.donation_total:12.2f} {donor.num_donations:11} ${donor.average_donation:12.2f}"
            report.append(f_str)

        return "\n".join(report)

