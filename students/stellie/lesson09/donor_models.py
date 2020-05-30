#!/usr/bin/env python3

# Stella Kim
# Assignment 8: Object Oriented Mailroom

"""Donor Models"""


class Donor(object):
    def __init__(self, donor_name, donations=None):
        self.name = donor_name
        if donations is None:
            self.donations = []
        else:
            self.donations = donations

    # Add donation amount to donor in database
    def add_donation(self, donation_amount):
        self.donations.append(donation_amount)

    # Send donor a thank you email
    def thank_you_email(self):
        return(f'\nThank you {self.name} for your generous donation amount '
               f'of ${self.donations:.2f}!')

    # Track number of donations made by a donor
    def donation_count(self):
        return len(self.donations)

    # Sum all donations made by a donor
    def total_donations(self):
        return sum(self.donations)

    # Find the average of all donations made by a donor
    def avg_donations(self):
        return sum(self.donations) / len(self.donations)


class DonorCollection(object):
    def __init__(self, **donor_db):
        self.data = donor_db
        self.items = donor_db.items()

    # Search database to see if user already exists
    def search_db(self, donor_name):
        return self.data.get(donor_name)

    # Add new donor and donation amount to database
    def add_new_donor(self, donor_name, donation_amount):
        self.data[donor_name] = Donor(donor_name, [donation_amount]).donations
        return self.data

    # Create report for user to see list of all donors and donations made
    def create_report(self):
        def sum_total(donor_record):
            return(sum(donor_record[1]))  # return donor donations sum in DB
        donor_stat = []
        # Sort database by sum amounts in descending order
        sorted_db = sorted(self.items, key=sum_total, reverse=True)
        for item in sorted_db:
            total = Donor(item[0], item[1]).total_donations()
            count = Donor(item[0], item[1]).donation_count()
            average = Donor(item[0], item[1]).avg_donations()
            donor_stat.append(f'{item[0]:<20} | {total:<12.2f} | '
                              f'{count:<10} | {average:<15.2f}')
        return donor_stat
