#!/usr/bin/env python3

import datetime


class Donor:
##TODO: Improve docstring to include input requirements
    def __init__(self, name, amount):
        self.name = name
        self.donations = [self.__check_value(amount)]

    def __check_value(self, amount):
        """Check that the amount is a valid input"""
        try:
            # convert the amount to a float
            return float(amount)
        except:
            raise ValueError('Amount must be a number!')

    def add_donation(self, amount):
        """Add donation information to donor data"""
        amount = self.__check_value(amount)
        self.donations.append(amount)
        self.generate_email(amount)


    def generate_email(self, amount):
        """Generate email thanking the donation."""
        email = '\n'.join(['', 'Dear {},'.format(self.name), '',
                           'Thank you for your generous donation of ${:.2f}.'.format(float(amount)),
                           'Your donation will continue to allow us to put a smile on our patients faces.', '',
                           'Sincerely,',
                           'The Last Laugh Program'])
        return email

    @property
    def summary(self):
        """Generate a summary of donations
            returns a list: [name, total donations, number of donations, average donation]
        """
        return [self.name, sum(self.donations), len(self.donations), sum(self.donations) / len(self.donations)]

    @classmethod
    def multi_donation(cls, name, donation_list):
        """Generate a donor object with a list of donations"""
        donor = cls(name, donation_list.pop(0))
        for amount in donation_list:
            donor.add_donation(amount)
        return donor


class DonorCollection:

    def __init__(self, donorObj):
        self.donors = []
        self.add_donors(donorObj)

    def add_donor(self, donorObj):
        """Add a donor object to the collection"""
        if isinstance(Donor, donorObj):
            self.donors.append(donorObj)
        else:
            raise TypeError('Invalid input, requires an input of {}'.format(Donor.__repr__()))

    def get_donor_names(self):
        """Generate a list of donors."""
        return [d.name for d in self.donors]

    def letters_all(self):
        """Generate letters to each donor"""
        print('\nGenerating donations letters:')
        date = datetime.date.today().isoformat()
        for d in self.donors:
            filename = d.name.replace(' ', '_') + f'_{date}' + '.txt'
            print(f'{d.name:20} --> {filename}')
            with open(filename, 'w') as outf:
                outf.writelines(d.generate_email(d.name, d.donations[-1]))

    def generate_report_data(self):
        """ Create the report data lines"""
        # Convert the donor data into report form, using list comprehension
        fmt_data = [d.generate_summary() for d in self.donors]

        # Sort the data by the total amount given
        fmt_data.sort(key=self.donation_sort, reverse=True)
        return fmt_data

    def donation_sort(self, data):
        """ Sort the report data by the total given."""
        # Report data is a list: [name, total given, num donations, avg donation]
        # Sorting on the total given
        return data[1]

    def create_report(self):
        """ Create a formatted report of the donor data."""
        r = []
        # Print the formatted header lines
        frmt_header = '{:<26}|{:^13}|{:^11}|{:>13}'
        frmt_line = '{:<26} ${:>11.2f} {:>11}  ${:>12.2f}'
        r.extend('Donations Summary:')
        r.extend(frmt_header.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
        r.extend('-' * 66)

        # Print the sorted data in the report format
        for f in self.generate_report_data():
            r.extend(frmt_line.format(*f))
