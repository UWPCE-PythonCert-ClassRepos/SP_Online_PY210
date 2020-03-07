#!/usr/bin/env python

#import variable donors.py

from datetime import date
import os, sys

class Donor(object):


    def __init__(self, name, donation=None):
        self.date = date.today()
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

    def thanks_template(self):
        template =  """Hello {name},\n
Thank you for your gifts totaling ${amount:.2f}! 
We will use your gift to help with costs for our upcoming play!
Thank you for giving!\n
Best Regards,
The Blanchford Community Center!""".format(name=self.name, amount=self.sum_donations)
        return template

    def create_email(self, directory):
        z = "{name}".format(name=self.name)
        if " " in z:
            z = z.replace(" ", "_")
        else:
            z = z
        today = "{date}".format(date=self.date).replace("-", "_")
        dir = directory
        template = "{template}".format(template=self.thanks_template())
        try:
            with open('{dir}/{name}_{date}.txt'.format(dir=dir, name=z, date=today), 'w') as f:
                f.write(template)
            return "Email file '{z}_{date}.txt' has been created for {name}".format(z=z, date=today, name=self.name)
        except TypeError:
            raise TypeError



class DonorCollection():

    def __init__(self, donors_list):
        self.date = date.today()
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
        header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}'\
            .format(
            name='Donor Name',
            total='Total Given',
            count='Num Gifts',
            avg='Average Gift',
            width=10)
        line = "=" * 70
        return ('\n' + header + '\n' + line)


    def create_report(self):
        report = []
        for key, value in self.sorted_dict:
            action = Donor(key, value).report_template()
            report.append(action)
        return report

    def create_directory(self, dir):
        directory_name = "{dir}".format(dir=dir)
        try:
            os.mkdir(directory_name)
        except TypeError:
            raise TypeError


    def send_email_all(self):
        x = "{date}".format(date=self.date).replace("-", "_")
        dir = 'outgoing_emails_{date}'.format(date=x)
        dir_list = list(os.listdir())
        if dir not in dir_list:
            self.create_directory(dir)
        for key, value in self.sorted_dict:
            Donor(key, value).create_email(dir)



