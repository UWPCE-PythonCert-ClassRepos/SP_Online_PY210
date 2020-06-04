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

    # Search database to see if user already exists
    def search_db(self, donor_name):
        return self.data.get(donor_name)

    # Add new donor and donation amount to database
    def add_new_donor(self, donor_name, donation_amount):
        self.data[donor_name] = Donor(donor_name, [donation_amount]).donations
        return self.data

    # Create report for user to see list of all donors and donations made
    def create_report(self):
        # Sort database by sum amounts in descending order
        sorted_db = sorted(self.data.items(), key=lambda donor_record:
                           sum(donor_record[1]), reverse=True)
        for item in sorted_db:
            donor_record = Donor(item[0], item[1])
            yield (f'{donor_record.name:<20} | '
                   f'{donor_record.total_donations():<12.2f} | '
                   f'{donor_record.donation_count():<10} | '
                   f'{donor_record.avg_donations():<15.2f}')
