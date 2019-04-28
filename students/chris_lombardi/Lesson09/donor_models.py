class Donor:
    """
    A class for a donor object
    Stores the name of the donor and donation history data.
    """

    def __init__(self, full_name):
        """
        Creates a donor.

        Keyword argument:
        full_name -- First and last name of a donor.
        """

        self.name = full_name.title()
        self.donation_hist = []

    def name(self):
        """Return full name of donor."""
        return self.name

    def donation_hist(self):
        """Return a list of all donations."""
        return self.donation_hist

    @property
    def total_donation(self):
        """A sum of all donations made by the donor."""
        return sum(self.donation_hist)

    @property
    def num_donation(self):
        """Return a count of individual donations made."""
        return len(self.donation_hist)

    @property
    def ave_donation(self):
        """Return the average donation for the donor."""
        #Checks that there is at least one donation for an average.
        if self.num_donation == 0:
            return 0
        else:
            return (self.total_donation/self.num_donation)

    def add_donation(self, *args):
        """Add a variable number of donations to the donation history."""
        self.donation_hist.extend(args)

    def __lt__(self, other):
        return self.total_donation < other.total_donation

    def __repr__(self):
        return self.name

    def send_thank_you(self, don_amnt):
        """Sends a thank you note when a donation is made."""
        ty_str = []
        ty_str.append(f'\nDear {self.name.title()},\n')
        ty_str.append(f'Thank you for your generous donation ' +
          'of ${don_amnt:,.2f}!\nWe appreciate your contribution to our ' +
          'charity.\n\nSincerley,\nThe Mailroom\n')
        return ''.join(ty_str)


class DonorCollection:

    """
    A class containing information of a list of Donor objects
    """

    def __init__(self):
        """Create a collection of donor objects."""
        self.list_donors = []

    def list_donors(self):
        """Return a list of all donors in the collection."""
        return list_donors

    def add_donor(self, *args):
        """Add a donor to the collection."""
        self.list_donors.extend(args)

    def __repr__(self):
        donor_names = [donor.name for donor in self.list_donors]
        return ', '.join(donor_names)

    def create_report(self):
        """Generate a tabular report of donors in the collection"""
        report_lines =[]
        header ='\n{:<18}|{:^13}|{:^13}|{:>13}\n'.format("Donor Name",
                "Total Given","Num Gifts", "Average Gift")
        report_lines.append(header)
        report_lines.append('-'*len(header))
        report_lines.append('\n')
        donor_sort = sorted(self.list_donors, reverse = True)
        for entry in donor_sort:
            name, num = entry.name, entry.num_donation
            total, ave = entry.total_donation, entry.ave_donation
            report_str = '{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}\n'.format(name,
                          total,num,ave)
            report_lines.append(report_str)
        report_lines.append('')
        return "".join(report_lines)
