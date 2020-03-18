#!/usr/bin/env python
"""
Jack Anderson
03/10/2020
UW PY210
Lesson 09

donor_models.py contains classes and functions to run the mailroom program.
The Donor class handles functionality for individual donors and the DonorCollection class handles functionality for all
donors.  All donor information is stored in the 'donors.pckl' file. If file is not present at launch a file with a
default list of donors is created and stored in the same directory as the mailroom program.
"""

from datetime import date
import os, sys, pickle

class Donor():
    """
    The Donor() class handles all functionality required for a single donor
    """


    def __init__(self, name, donation=None):
        # Set name variable and ensure donation is list type
        self.name = name.title()
        if donation == None:
            self.donations = list()
        else:
            self.donations = list(donation)


    def add_donation(self, amount):
        """
        Appends donation to donation list for donor
        :param amount: Donation amount to add to donors donations list
        :return: donations with the new amount added
        """
        return self.donations.append(amount)

    @property
    def sum_donations(self):
        """
        Property to sum donations
        :return: sum of all donations in donations list for donor
        """
        self._donations = sum(self.donations)
        return self._donations

    @property
    def num_donations(self):
        """
        Property to count the number of donations made for a donor
        :return: number of donations in donations list for donor
        """
        self._donations = len(self.donations)
        return self._donations

    @property
    def avg_donation(self):
        """
        Property to return the avg donation made
        :return: sum of donations / number of donations made
        """
        self._donations = self.sum_donations / self.num_donations
        return self._donations


    def report_template(self):
        """
        Returns text string of donor in a formatted layout containing name, total donations, num of donations made,
        and the avg amount donated.
        """
        d = dict(name=self.name, total=self.sum_donations,count=self.num_donations, avg=self.avg_donation, width=10)
        template = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}'.format(**d)
        return template



    def thanks_template(self):
        """
        Returns a 'thank you' style text string with donor name and total donations made for donor
        """
        d = dict(name=self.name, amount=self.sum_donations)
        template =  "Hello {name},\nThank you for your gifts totaling ${amount:.2f}! \n" \
                    "We will use your gift to help with costs for our upcoming play!\n" \
                    "Thank you for giving!\nBest Regards,The Blanchford Community Center!".format(**d)
        return template


    def create_email(self, directory):
        """Action to save a txt file of email to directory containing todays date
        :param directory: name of directory to store emails
        :return: text file of email to send to donor
        """
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
        # Load donors info from donors.pckl file, if no file exists, create default file.
        # Set self sorted dict variable
        try:
            with open('donors.pckl', 'rb') as f:
                self.donors_dict = pickle.load(f)
                f.close()
        except (FileNotFoundError, AttributeError):
            self.create_sample_list()
            self.__init__()
        self.sorted_dict = sorted(self.donors_dict.items(), key=lambda x: (sum(x[1]), x[0]), reverse=True)




    def add_donor(self, name, amount):
        """
        Action to add a new donor and donation to the donor file or if donor already in file, add new donation
        :param name: Name of donor
        :param amount: Amount of dontation made
        """
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
        # Return a list of donor names
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
        """
        Action to get all donors in a sorted dict and iterate through the Donor.report_template function
        :return: Donors in a report format sorted by most donated
        """
        report = []
        for key, value in self.sorted_dict:
            action = Donor(key, value).report_template()
            report.append(action)
        return report


    def create_directory(self, dir):
        """
        Action to create a directory
        :param dir: name of dir to create
        """
        directory_name = "{dir}".format(dir=dir)
        try:
            os.mkdir(directory_name)
        except TypeError:
            raise TypeError


    def send_email_all(self):
        """
        Action to check if email directory is created. Creates if not exists. Then calls Donor create_email function
        """
        self.sorted_dict = sorted(self.donors_dict.items(), key=lambda x: (sum(x[1]), x[0]), reverse=True)
        dir = 'outgoing_emails_{date}'.format(date=date.today()).replace("-", "_")
        dir_list = list(os.listdir())
        if dir not in dir_list:
            self.create_directory(dir)
        for key, value in self.sorted_dict:
            Donor(key, value).create_email(dir)



    def remove_donor(self, name):
        """
        Action to remove donor from donors dict and then updates donors file. Uses are for testing typically
        :param name:  Name of donor to remove from the donors dict
        """
        if name in self.donors_dict:
            del self.donors_dict[name]
        x = self.donors_dict
        with open('donors.pckl', 'wb') as f:
            pickle.dump(x, f)
            f.close()



    def create_sample_list(self):
        # Creates a sample donors list if donor file not already created. Will create this file on first run of
        # mailroom program.
        donors_list = [['Bubbles Trailer', [1500.24, 2523.33, 3012.12]],
               ['Julien Park', [2520.99, 1623, 123.23]],
               ['Ricky Boys', [1345.50, 1123.00]],
               ['Jack', [1044, 2232, 123.49]],
               ['Lacey Coffin Greene', [1500, 1625, 1305, 3400.87]]]

        sample = {donor[0]: donor[1] for donor in donors_list}
        with open('donors.pckl', 'wb') as f:
            pickle.dump(sample, f)
            f.close()
