#!/usr/bin/env python3

import os

class Donor():

    def __init__(self, name, donation_amount=None):
        self.name = name
        if donation_amount is None:
            self.donation_amount = []
        else:
            self.donation_amount = donation_amount

    def add_donation(self, amount):
        self.donation_amount.append(amount)

    def thank_you_letter(self):
        thank_you = "\n".join(("Dear {},\n".format(self.name),
        "Thank you for your generous donation of ${}! As you certianly know, kittens".format(self.donation_amount[-1]),
        "and metal are awesome and your donation will insure that others will be able",
        "to enjoy kittens and metal.\n",
        "Thank you,\n",
        "Kittens and Metal Charity\n"))
        return thank_you

class DonorCollection():
    
    def __init__(self):
        self.donors = {}
    
    def initialize_donor_dict(donor_data):
        donors = DonorCollection()
        for name, amounts in donor_data.items():
            donor = Donor(name, amounts)
            donors.add_donor(donor)
        return donors
    
    def add_donor(self, donor):
        self.donors[donor.name] = donor
    
    def check_donors(self, name):
        return any(donor for donor in self.donors.values()if donor.name.lower() == name.lower())

    def list_donors(self):
        donor_list = []
        for name in self.donors:
            donor_list.append(name)
        return "\n".join(donor_list)
    
    def report_of_donors(self):
        for donor in self.donors.values():
            name = donor.name
            total_donation_amount = sum(donor.donation_amount)
            total_donations = len(donor.donation_amount)
            avg_donation = total_donation_amount / total_donations
            print(self.row_formatter([name, total_donation_amount, total_donations, avg_donation]))

    def table_header(self):
        return "\n".join(("{:25}|{:12}|{:10}|{:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"), "-" * 62))
    
    def row_formatter(self, row):
        return "{:25}|${:11.2f}|{:10}|${:11.2f}".format(*row)

    def thank_all_donors(self, dir_name):
        wd = os.getcwd()
        for donor in self.donors.values():
            file_path = wd + "/" + dir_name + "/" + donor.name + ".txt"
            letter = donor.thank_you_letter()
            with open(file_path, "w") as f:
                f.write(letter)
