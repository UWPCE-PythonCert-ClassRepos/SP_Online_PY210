class Donor:

    '''
    A donor class that holds information about an individual donor
    '''

    def __init__(self, donor):

        '''
        Initialize a new instance of the Donor class
        :param donor: The donor name to add
        '''

        self.donor_name = donor
        self.donations = []


    def add_donation(self, *args):

        '''
        Add the donation amount to the donation list
        :param args: The donation amount(s)
        :return: void
        '''

        self.donations.extend(args)


    @property
    def total_donations(self):

        '''
        Return the total sum of donations for the donor
        :return: The total sum of donations
        '''

        return sum(self.donations)


    @property
    def all_donations(self):

        '''
        Return the donation list
        :return: The list of donations for the donor
        '''

        return self.donations


    def format_thank_you_note(self, donation_amount):

        '''
        Format the thank you note before writing to file
        :param donation_amount: The donation amount
        :return: a formatted thank you note
        '''

        note_format = ["Dear {},\n\n".format(self.donor_name.title()),
                       "\tThank you for your very kind donation of  ${:10.2f}!\n".format(donation_amount),
                       "\tIt will be put to very good use.\n\n", "\t\t\tSincerely,\n", "\t\t\t\t\t - The Team"]

        return "".join(note_format)


    @property
    def donation_count(self):

        '''
        Get the number of donations made
        :return: The number of donations for the donor
        '''

        return len(self.donations)


    def __lt__(self, other):

        '''
        Override the less than operator for the sorted call during report generation
        :param other: the Donor object to compare
        :return: True if current object's total donations is less than other's
        '''

        return self.total_donations < other.total_donations


class DonorCollection:

    '''
    A Donor Collection that holds collection information about a group of Donors
    '''

    def __init__(self, donor_list = []):

        '''
        Initialize a new instance of the DonorCollection class
        :param donor_list: optional donor list
        '''

        self.donors = donor_list


    def add_donor(self, *args):

        '''
        Add a donor to the collection
        :param args: Arguments of type Donor
        :return: void
        '''

        self.donors.extend(args)


    def get_donors(self):

        '''
        Get the current donors
        :return: the current donors
        '''

        return self.donors


    @staticmethod
    def get_donation_report_for_donor(donor, donation_amounts):

        '''
        Get the formatted text for the report generation
        :param donor: The donor name
        :param donation_amounts: The donation amounts
        :return: Formatted text for the donation report
        '''

        total = sum(donation_amounts)
        num = len(donation_amounts)
        average = total / num
        return '{:^18} ${:>12,.2f}{:^13}  ${:>12,.2f}\n'.format(donor, total, num, average)


    def create_report(self):

        '''
        Create a report of all donors, and amounts in sorted order with most donations first
        :return: A reported formatted in the expected format
        '''

        report = []
        header = '\n{:^18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
        report.append(header)
        report.append("\n")
        report.append('-' * len(header))
        report.append("\n")
        sorted_list = sorted(self.donors, reverse=True)
        for d in sorted_list:
            report.append(self.get_donation_report_for_donor(d.donor_name, d.all_donations))

        return "".join(report)


    def donor_present(self, donor_name):

        '''
        Check if the donor name is a part of the collection
        :param donor_name: The name of the donor
        :return: True if part of the collection, false if not
        '''

        donor_present = False
        for d in self.donors:
            if (d.donor_name == donor_name):
                donor_present = True
                break

        return donor_present