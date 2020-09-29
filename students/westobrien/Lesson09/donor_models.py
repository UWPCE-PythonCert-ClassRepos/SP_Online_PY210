
class Donor(object):

    def __init__(self, name, donation_list=None):
        if donation_list is None:
            donation_list = []
        self.name = name
        self.donation_list = donation_list

    # def donation_list_getter(self):
    #     return self.donation_list

    # def donation_list_setter(self, donation_amount):
    #     self.donation_list.append(donation_amount)

    # donation_list = property(donation_list_getter, donation_list_setter)

    def __lt__(self, other):
        return self.sum_donations < other.sum_donations

    def __eq__(self, other):
        return self.sum_donations == other.sum_donations

    @property
    def average_donation(self):
        return float(sum(self.donation_list) / len(self.donation_list))

    @property
    def sum_donations(self):
        return sum(self.donation_list)

    @property
    def num_donations(self):
        return len(self.donation_list)

    def letter_write(self):
        return "\n".join(("Dear {},".format(self.name),
                          "Thank you for your very kind donation of ${:.2f}".format(
                              self.sum_donations),
                          "\nIt will be put to very good use",
                          "Sincerely, \n\t The Team",
                          ))


class DonorCollection(object):

    def __init__(self, list_donors=None):
        if list_donors is None:
            list_donors = []
        self.list_donors = list_donors

    def add_donor(self, donor):
        self.list_donors.append(donor)

    def is_in_list(self, donor_name):
        in_list = False
        for donor in self.list_donors:
            if donor.name == donor_name:
                in_list = True
        return in_list

    def donor_names(self):
        donor_names_list = None
        donor_names_list = []
        for donor in self.list_donors:
            donor_names_list.append(donor.name)
        return donor_names_list

    def generate_report(self):
        #sorting list of donors based upon total donations
        self.list_donors.sort(reverse=True)
        report_string = "Donor Name" + " " * 16 + \
            "|  Total Given  |  Num Gifts  |  Average Gift\n" + "-" * 71
        for donor in self.list_donors:
            report_string += "\n {:25s} $ {:13.2f} {:13}  $ {:12.2f}".format(
                donor.name, donor.sum_donations, donor.num_donations, donor.average_donation)
        return report_string

    def get_donor(self, name):
        for donor in self.list_donors:
            if name == donor.name:
                return donor

    def write_letters(self):
        pass