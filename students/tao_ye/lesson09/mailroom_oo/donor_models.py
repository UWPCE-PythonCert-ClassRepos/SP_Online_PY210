class Donor():
    """
    This class holds all the information about a single donor,
    and has attributes, properties, and methods to provide access
    to the donor-specific information that is needed.
    """
    def __init__(self, name, donation=None):
        self._name = name
        if donation is not None:
            if type(donation) is list:
                self._donation = donation
            else:
                self._donation = [donation]
        else:
            self._donation = []

    def __str__(self):
        return f"Donor: {self._name}"

    def __repr__(self):
        return f'Donor("{self._name}")'

    @property
    def name(self):
        return self._name

    @property
    def donation(self):
        return self._donation

    @property
    def total_donation(self):
        return sum(self._donation)

    @property
    def num_donations(self):
        return len(self._donation)

    @property
    def avg_donation(self):
        return self.total_donation / self.num_donations

    def add_donation(self, amount):
        """ add a donation amount to the Donor object donation list """
        self._donation.append(amount)

    def email_text(self):
        return ('-'*60 +
                '\nDear ' + self._name.title() + ',' +
                '\n\nThank you for your generous donation of' +
                f" ${self._donation[-1]:.2f}." +
                '\n\nSincerely,' +
                '\nThe Team\n' +
                '-'*60)

    def sort_key(self):
        return self.total_donation


class DonorCollection():
    """
    This class holds all of the donor objects, as well as methods
    to add a new donor, search for a given donor, create a list of donors,
    create a report, etc.
    """
    def __init__(self, donor_list=None):
        if donor_list is not None:
            self._donor_list = donor_list
        else:
            self._donor_list = []

    def __str__(self):
        name_list = [donor.name for donor in self._donor_list]
        return "donor list: " + str(name_list)

    def __repr__(self):
        return f"DonorCollection({self._donor_list})"

    @property
    def donor_list(self):
        return self._donor_list

    def list_donors(self):
        """ return a list of donor names """
        return [donor.name for donor in self._donor_list]

    def add_donor(self, donor):
        """ add a new donor """
        self._donor_list.append(donor)

    def search_donor(self, name):
        for donor in self._donor_list:
            if donor.name.lower() == name.lower():
                return donor

        return None

    def get_report(self):
        """
        Generate a list of strings for donor collection report. Each list element
        represents a line in the print out
        """
        self._donor_list.sort(key=Donor.sort_key, reverse=True)

        report = ['{:20}| {:>12} |{:>10} |{:>15}'.
                  format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'),
                  '-' * 63]

        for donor in self._donor_list:
            report.append(f'{donor.name:20} ${donor.total_donation:12.2f}  ' +
                          f'{donor.num_donations:>10d}  ${donor.avg_donation:14.2f}')

        return report
