#!/usr/bin/env python3
"""
A class-based system for donors
"""


class Donor(object):
    def __init__(self, don_name):
        self.name = don_name
        self.total_donation = 0
        self.donation_num = 0
        self.most_recent_donation = 0

    @property
    def avg_donation(self):
        # Read only attribute
        try:
            return round(self.total_donation / self.donation_num, 2)
        except ZeroDivisionError:
            return 0

    def new_donation(self, value):
        self.total_donation += round(value, 2)
        self.donation_num += 1
        self.most_recent_donation = round(value, 2)

    @classmethod
    def from_existing(cls, don_name, don_total, don_number):
        self = cls(don_name)
        self.total_donation = don_total
        self.donation_num = don_number
        return self

    def generate_recent_thanks(self):
        string_to_format = ("Dear {},"
                            "\n\nThank you for your kind donation of ${:.2f}."
                            "\nIt will be put to very good use."
                            "\n\nSincerely,"
                            "\n-The Team")
        return string_to_format.format(self.name, self.most_recent_donation)

    def generate_total_thanks(self):
        string_to_format = ("Dear {},"
                            "\n\nThank you for your kind donations totalling ${:.2f}."
                            "\nIt will be put to very good use."
                            "\n\nSincerely,"
                            "\n-The Team")
        return string_to_format.format(self.name, self.total_donation)


class DonorCollection(object):
    def __init__(self, ):
        self.donor_list = []

    def add_new_donor(self, donor_name):
        self.donor_list.append(Donor(donor_name))

    def add_existing_donor(self, don_name, don_total, don_number):
        self.donor_list.append(Donor.from_existing(don_name, don_total, don_number))

    def list_donor_names(self):
        return [x.name for x in self.donor_list]

    def generate_report(self):
        header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
        header_string = "{0:<{w1}} | {1:>{w2}} | {2:>{w3}} | {3:>{w4}}"
        data_string = "{0:<{w1}}  ${1:>{w2}}   {2:>{w3}}  ${3:>{w4}}"
        w = self.__find_widths()
        header_to_print = (header_string.format(*header, w1=w[0], w2=w[1], w3=w[2], w4=w[3]))
        report = '\n' + header_to_print + '\n' + ('-' * len(header_to_print)) + '\n'
        sorted_list = sorted(self.donor_list, key=lambda x: x.total_donation, reverse=True)
        for donor in sorted_list:
            report += (self.__print_line(data_string, donor, w) + '\n')
        return report

    def __find_widths(self):
        donor_length = max([len(x.name) for x in self.donor_list])
        if 10 > donor_length:
            donor_length = 10
        total_length = max([len(str(x.total_donation)) for x in self.donor_list])
        if 11 > total_length:
            total_length = 11
        num_length = max([len(str(x.donation_num)) for x in self.donor_list])
        if 9 > num_length:
            num_length = 9
        avg_length = max([len(str(x.avg_donation)) for x in self.donor_list])
        if 12 > avg_length:
            avg_length = 12
        return [donor_length, total_length, num_length, avg_length]

    @staticmethod
    def __print_line(line_format, donor, width):
        row_string = (line_format.format(donor.name, donor.total_donation, donor.donation_num, donor.avg_donation,
                                         w1=width[0], w2=width[1], w3=width[2], w4=width[3]))
        return row_string
