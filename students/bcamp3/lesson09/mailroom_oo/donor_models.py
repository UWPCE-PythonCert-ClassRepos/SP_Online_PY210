
"""Module with Donor and DonorCollection classes."""
"""Also contains string formating for 'thank you' message and donor report."""

thank_you_tmp = ("\n Subject: Thank You !!!\n"
                 "\n Dear {0:},\n"
                 "\n Thank you for your latest donation of ${1:,.2f}.\n"
                 " We are so glad you have made {2:} donation(s)"
                 " totaling ${3:,.2f}.\n"
                 " Your continued support will help our"
                 " foundation achive our goals.\n\n"
                 " Regards,\n       Foundation Leadership Team\n"
                 )

report_tmp = " {0:<25} ${1:>11.2f}  {2:>10d}  ${3:>12.2f}"

class Donor():
    """
    Class representing an individual donor

    Args:
        name (str):
            Donor's name

        donation (str):
            Initial donation
            Default = None

    Attributes:
        donations (list):
            List of donations (floats), arranged oldest to newest

    Methods:
        __lt__(self, other):
            Magic method to enable custom sorting of Donor objects
        add_donation(amount):
            Add donation to donation attribute
        total_donations():
            Return total donations made by donor
        average_donation():
            Return the average donation made by donor
        send_thank_you():
            Generate text for message thanking donor for their donation

    """

    def __init__(self, name, donation=None):
        """
        Create a new donor instance

        Args:
            name (str):
                Donor's name

            donation (str):
                Initial donation
                Default = None
        """
        if isinstance(name, str):
            self.name = name.upper()
        else:
            raise TypeError("Donor class initialization requires a 'str' "
                            "object as first input argument")
        if donation:
            self.donations = self._check_input(donation)
        else:
            self.donations = ()

    def __lt__(self, other):
        """
        Sort donor instances by total amount

        Args:
            self, other (Donor):
                Two donor objects to compare
        """
        return self.total_donation < other.total_donation

    def add_donation(self, donation):
        """
        Add donation to donor's history

        Args:
            amount (float):
                Donation amount
        """
        self.donations = self.donations + self._check_input(donation)

    def _check_input(self, donation):
        """
        Check donation input

        Args:
            amount (float):
                Donation amount (must be a number equal to or greater than zero)
        """
        amt = float(donation)
        if amt <= 0:
            raise ValueError("Donation amount must be greater than zero")
        return (amt,)

    @property
    def total_donation(self):
        """
        Return sum of donor's total donations
        """
        return sum(self.donations)

    @property
    def avg_donation(self):
        """
        Return donor's average donation amount
        """
        return self.total_donation/len(self.donations)

    @property
    def send_thank_you(self, tmp=thank_you_tmp):
        """
        Return Thank You message text
        """
        return tmp.format(self.name,
                          self.donations[-1],
                          len(self.donations),
                          self.total_donation)

    def __str__(self):
        return (" This is a Donor object:\n"
                f"  donor name: {self.name}\n"
                f"  donor total donations = ${self.total_donation:.2f}")

    def __repr__(self):
        return f"Donor({self.name})"


class DonorCollection():
    """DonorCollection class."""
    def __init__(self):
        """Initialize DonorCollection object with empty dict 'donors'"""
        self.donors = {}

    def update_donor(self, name, donation):
        """Create new donor object if not already in collection."""
        """Update existing donor object in collection."""
        # Ensure name is all upper-case
        _name = name.upper()
        # Create donor object if it doesn't exist
        if _name not in self.donors:
            self.donors[_name] = Donor(_name)
        self.donors[_name].add_donation(donation)

    @property
    def report(self):
        """
        Generate report summary of donations by donor
        """
        donors = list(self.donors.values())
        donors.sort(reverse=True)
        report_out = []
        for donor in donors:
            report_out.append(report_tmp.format(donor.name,
                                                donor.total_donation,
                                                len(donor.donations),
                                                donor.avg_donation))
        return report_out

    @property
    def donor_list(self):
        """
        Create a sorted list of donor names by last name
        """
        sorted_list = []
        for name in self.donors:
            name_list = name.split(' ')
            sorted_list.append([name_list[-1], name])
        sorted_list.sort()
        return [name[1] for name in sorted_list]

    def __str__(self):
        return (" This is a DonorCollection object,\n"
                f" containing {len(self.donors.keys())} Donor object(s)")

    def __repr__(self):
        return "DonorCollection(Donor())"
