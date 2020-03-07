#!/usr/bin/env python

#import variable donors.py

class Donor(object):

    def __init__(self, name, donation=None):
        self.name = name.title()
        if donation == None:
            self.donations = list()
        else:
            self.donations = list(donation)


    def add_donation(self, amount):
        return self.donations.append(amount)

    @property
    def sum_donations(self):
        self._donations = sum(self.donations)
        return self._donations

    @property
    def num_donations(self):
        self._donations = len(self.donations)
        return self._donations

    @property
    def avg_donation(self):
        self._donations = self.sum_donations / self.num_donations
        return self._donations

    def report_template(self):
        template = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}' \
            .format(
            name=self.name,
            total=self.sum_donations,
            count=self.num_donations,
            avg=self.avg_donation,
            width=10)
        return template





class DonorCollection():

    def __init__(self, donors_list):
        self.donors_dict = { donor[0]:donor[1] for donor in donors_list}
        self.sorted_dict = sorted(self.donors_dict.items(), key=lambda x: (sum(x[1]), x[0]), reverse=True)

    def add_donor(self, name, donation):
        if name not in self.donors_dict:
            self.donors_dict[name]=donation
        else:
            self.donors_dict[name]+= [donation]

    def list_donors(self):
        self.donors = self.donors_dict.keys()
        return self.donors

    def report_header(self):
        # Print a header for the report
        header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}'.format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)

        # print('{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
        #       .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10))
        line = "=" * 70
        return ('\n' + header + '\n' + line)


    def create_report(self):
        report = []
        for key, value in self.sorted_dict:
            action = Donor(key, value).report_template()
            report.append(action)
        return report


