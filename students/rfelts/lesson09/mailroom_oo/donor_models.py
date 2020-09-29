#!/usr/bin/env python3

# Russell Felts
# Assignment 9 - Donor Classes


import operator
import datetime


class Donor(object):
    """ Handles all the information about a single donor: attributes, properties, and methods to provide access to the
    donor-specific information that is needed.  """

    def __init__(self, name, donations=None):
        """ Initialize the Donor class """

        self.name = name
        assert type(donations) is list, "\nThe donation value must be entered as a list.\n"
        self.donations = donations

    def add_donation(self, donation_amount):
        """ Append the donation to the donations list """
        float(donation_amount)
        self.donations.append(donation_amount)

    @property
    def donations_total(self):
        """ Sums the values in the donation list """
        return sum(self.donations)

    @property
    def compose_message(self):
        """ Compose a thank you message listing the current/previous donation and the donor's donation total
        :return: a String containing the thank you message for the donor """

        return (f'\nTo: {self.name}\nSubject: Thank you.\n\n{self.name} thank you for your previous generous donation'
                f' of {self.donations[-1]:<,.2f}.\nYour total donations to date are now: {self.donations_total:<,.2f}.')

    def write_letter(self):
        """ Write a file to disk with the donation message """

        now = datetime.datetime.now()

        with open(self.name + '_' + str(now.month) + '_' + str(now.year) + '.txt', 'w') as f:
            f.write(self.compose_message)


class DonorCollection:

    def __init__(self):
        """ Create an initial list of donor objects - potentially convert to be read from a file """

        self.donor_list = [Donor("Lionel Messi", [100]), Donor("Cristiano Ronaldo", [5000, 25, 9450]),
                           Donor("Gianluigi Buffon", [1000000, 2500.50]), Donor("Neymar", [25.25, 30, 99.99, 250]),
                           Donor("Paolo Maldini", [9500, 6789.95, 250, 7500])]

    @property
    def list_donors(self):
        """ Return a string containing the current donor names
        :return: A string of the current donor names """

        names = "\n"
        for item in self.donor_list:
            names += f'{item.name}\n'

        return names

    @property
    def get_name_padding(self):
        """ Create dynamic padding for the name
        :return int: Integer containing the padding value """

        padding = 0
        for item in self.donor_list:
            temp_padding = len(item.name) + 4
            if padding < temp_padding:
                padding = temp_padding

        return padding

    @staticmethod
    def get_donation_padding(report_data):
        """ Create dynamic padding for the donation amount data
        :return int: The value to use for the donation padding """

        donation_padding = len(str(report_data[1]))
        donation_padding += int((donation_padding / 3) + 2)

        return donation_padding

    def donor_exists(self, name):
        """ Check for the donor in the current donor list
        :param name: String representing the donor's name
        :return: a list containing a donor object """

        return [d for d in self.donor_list if d.name.upper() == name.upper()]

    def add_donor(self, name, amount):
        """ Add a new donor to the donor list
        :param name: String containing the donor's name
        :param amount: Float containing the donation amount """

        new_donor = Donor(name, [amount])
        self.donor_list.append(new_donor)
        return new_donor

    def create_report(self):
        """ Print a list including Donor Name, total donated, number of donations and average donation amount sorted by
        total historical donation amount. """

        report_data = [[donor.name, sum(donor.donations), len(donor.donations), sum(donor.donations) / len(donor.donations)]
                       for donor in self.donor_list]

        # Sort the list by donation total (index 1) of the list
        report_data.sort(key=operator.itemgetter(1), reverse=True)

        return report_data

    def send_to_everyone(self):
        """ Write a file for each donor containing the thank you message. """

        for donor in self.donor_list:
            donor.write_letter()
