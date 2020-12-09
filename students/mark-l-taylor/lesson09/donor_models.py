#!/usr/bin/env python3

import datetime, copy


class Donor:
    def __init__(self, name, amount):
        self.name = name
        self.donations = [self.__check_value(amount)]

    def __str__(self):
        return '{}: {}'.format(self.name, self.donations)

    def __repr__(self):
        return 'Donor({})'.format(self.name)

    def __check_value(self, amount):
        """
        Check that the amount is a valid input

        :param amount: value to be checked/converted to float
        :returns : the amount as a float
        """
        try:
            amount = float(amount)
            if amount > 0.:
                # convert the amount to a float
                return float(amount)
            else:
                raise ValueError
        except:
            raise ValueError('Amount must be a number!')

    def add_donation(self, amount):
        """
        Add a single donation to the donor instance

        :param amount: value of the donation
        """
        amount = self.__check_value(amount)
        self.donations.append(amount)

    @property
    def generate_email(self):
        """
        Generate email thanking the last donation.
        """
        email = '\n'.join(['', 'Dear {},'.format(self.name), '',
                           'Thank you for your generous donation of ${:.2f}.'.format(float(self.donations[-1])),
                           'Your donation will continue to allow us to put a smile on our patients faces.', '',
                           'Sincerely,',
                           'The Last Laugh Program'])
        return email

    @property
    def summary(self):
        """
        Generate a summary of donations

        :returns: list: [name, total donations, number of donations, average donation]
        """
        return [self.name, sum(self.donations), len(self.donations), sum(self.donations) / len(self.donations)]

    @classmethod
    def multi_donation(cls, name, donation_list):
        """
        Generate a donor instance with a list of donations

        :param name: name of the donor
        :param donation_list: list of donoations, values must be a number
        :returns: Donor instance
        """
        donor = cls(name, donation_list[0])
        for amount in donation_list[1:]:
            donor.add_donation(amount)
        return donor


class DonorCollection():
    def __init__(self, donor_obj=None):
        self.donors = {}
        if donor_obj:
            self.add_donor(donor_obj)

    def __str__(self):
        return 'DonorCollection: {}'.format(self.donor_names())

    def __repr__(self):
        return 'DonorCollection'

    def add_donor(self, donorObj):
        """
        Add a donor instance to the collection

        :param donorObj: Donor instance
        """
        if isinstance(donorObj, Donor):
            if donorObj.name in self.donors:
                for d in donorObj.donations:
                    self.donors[donorObj.name].add_donation(d)
            else:
                self.donors[donorObj.name] = donorObj
        else:
            raise TypeError('Invalid input, requires an input of {}'.format(Donor.__repr__()))

    @classmethod
    def donorList(cls, donorList):
        """
        Create a DonorCollection with a list of Donors

        :param donorList: List of donor instances
        :returns: donorCollection instance
        """
        if donorList and isinstance(donorList, list):
            collection = cls(donorList[0])
            for d in donorList[1:]:
                collection.add_donor(d)
            return collection
        else:
            raise ValueError('donorList must be a list of donor objects')

    @classmethod
    def donorDict(cls, donorDict):
        """
        Create a DonorCollection with a dictionary of donor data

        :param donorDict: Dictionary of donor data; key=name, value=list of donations
        :returns: donorCollection instance
        """
        return cls.donorList([Donor.multi_donation(n, d) for n, d in donorDict.items()])

    @property
    def donor_names(self):
        """
        List of donors in donorCollection instance.

        :returns : list of donor names
        """
        return self.donors.keys()

    def letters_all(self):
        """
        Generate letters to each donor

        Creates a file that contains the donation thank you letter for last donation made.
        :returns : a list tuples(name, filename) of the filenames created.
        """
        fnames = []
        date = datetime.date.today().isoformat()
        for d in self.donors.values():
            filename = d.name.replace(' ', '_') + f'_{date}' + '.txt'
            with open(filename, 'w') as outf:
                outf.writelines(d.generate_email)
            fnames.append((d.name, filename))
        return fnames

    def generate_report_data(self):
        """
        Create the report data lines

        :returns : list of donation data, sorted by the total donations
        """
        # Convert the donor data into report form, using list comprehension
        data = [d.summary for d in self.donors.values()]
        # Sort the data by the total amount given
        data.sort(key=self.__donation_sort, reverse=True)
        return data

    def __donation_sort(self, data):
        """
        Sort the report data by the total given.
        """
        # Report data is a list: [name, total given, num donations, avg donation]
        # Sorting on the total given
        return data[1]

    def create_report(self):
        """
        Create a formatted report of the donor data.

        :returns : list of lines for report, includes header and data sorted by total donation.
        """
        r = ['Donations Summary:']
        # formatted header lines
        frmt_header = '{:<26}|{:^13}|{:^11}|{:>13}'
        frmt_line = '{:<26} ${:>11.2f} {:>11}  ${:>12.2f}'
        r.append(frmt_header.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
        r.append('-' * 66)

        # add sorted/formatted data in the report
        for f in self.generate_report_data():
            r.append(frmt_line.format(*f))

        return r
