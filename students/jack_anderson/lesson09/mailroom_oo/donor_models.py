#!/usr/bin/env python

from datetime import date
import os, sys, pickle

class Donor():


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
        d = dict(name=self.name, total=self.sum_donations,count=self.num_donations, avg=self.avg_donation, width=10)
        template = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}'.format(**d)
        return template


    def thanks_template(self):
        d = dict(name=self.name, amount=self.sum_donations)
        template =  "Hello {name},\nThank you for your gifts totaling ${amount:.2f}! \n" \
                    "We will use your gift to help with costs for our upcoming play!\n" \
                    "Thank you for giving!\nBest Regards,The Blanchford Community Center!".format(**d)
        return template


    def create_email(self, directory):
        self.date = date.today()
        z = "{name}".format(name=self.name).replace(" ", "_")
        now = "{date}".format(date=date.today()).replace("-", "_")
        dir = directory
        template = "{template}".format(template=self.thanks_template())
        try:
            with open('{dir}/{name}_{date}.txt'.format(dir=dir, name=z, date=now), 'w') as f:
                f.write(template)
        except TypeError:
            raise TypeError



class DonorCollection():

    def __init__(self):
        try:
            with open('donors.pckl', 'rb') as f:
                self.donors_dict = pickle.load(f)
                f.close()
        except (FileNotFoundError, AttributeError):
            self.create_sample_list()
            self.__init__()
        self.sorted_dict = sorted(self.donors_dict.items(), key=lambda x: (sum(x[1]), x[0]), reverse=True)




    def add_donor(self, name, amount):
        new_donation = amount
        if name not in self.donors_dict.keys():
            self.donors_dict[name]= new_donation
        else:
            self.donors_dict[name]+= new_donation
        x = self.donors_dict
        with open('donors.pckl', 'wb') as f:
            pickle.dump(x, f)
            f.close()


    def list_donors(self):
        donor_names = ''
        for key in self.donors_dict.keys():
            donor_names += key + '\n'
        return donor_names


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
        self.sorted_dict = sorted(self.donors_dict.items(), key=lambda x: (sum(x[1]), x[0]), reverse=True)
        dir = 'outgoing_emails_{date}'.format(date=date.today()).replace("-", "_")
        dir_list = list(os.listdir())
        if dir not in dir_list:
            self.create_directory(dir)
        for key, value in self.sorted_dict:
            Donor(key, value).create_email(dir)



    def remove_donor(self, name):
        if name in self.donors_dict:
            del self.donors_dict[name]
        x = self.donors_dict
        with open('donors.pckl', 'wb') as f:
            pickle.dump(x, f)
            f.close()




    def create_sample_list(self):
        donors_list = [['Bubbles Trailer', [1500.24, 2523.33, 3012.12]],
               ['Julien Park', [2520.99, 1623, 123.23]],
               ['Ricky Boys', [1345.50, 1123.00]],
               ['Jack', [1044, 2232, 123.49]],
               ['Lacey Coffin Greene', [1500, 1625, 1305, 3400.87]]]

        sample = {donor[0]: donor[1] for donor in donors_list}
        with open('donors.pckl', 'wb') as f:
            pickle.dump(sample, f)
            f.close()
