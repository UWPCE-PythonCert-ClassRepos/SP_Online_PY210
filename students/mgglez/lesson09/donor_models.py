# ----------------------------------------------------------------------------------- #
# Title: Lesson09 - Mailroom - Object Oriented
# Description: Assignment from Lesson09 - Mailroom - Object Oriented
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-06-2021, Created Donor & DonorCollection Classes
# ----------------------------------------------------------------------------------- #

import functools


# Business Logic - Donor Class
@functools.total_ordering
class Donor(object):
    """
    Donor Class representing a donor and tracking its contribution history
    """

    def __init__(self, full_name, donation_history=None):
        self.full_name = full_name
        if donation_history is not None:
            self.donation_history = donation_history
        else:
            self.donation_history = []

    @property
    def full_name(self):
        return self.__full_name.title()

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name.strip().lower()

    @property
    def donation_history(self):
        self.__donation_history.sort(reverse=True)
        return self.__donation_history

    @donation_history.setter
    def donation_history(self, donation_history):
        if type(donation_history) == list and all(type(donation) in (int, float) for donation in donation_history):
            self.__donation_history = donation_history
        else:
            raise ValueError("The donation history must be a list of numeric values (integers or floating points) "
                             "representing the donation amounts made by a donor. An invalid data type was provided "
                             "instead: {}".format(donation_history))

    @property
    def total_donation_sum(self):
        return sum(self.__donation_history)

    @property
    def num_donation(self):
        return len(self.__donation_history)

    @property
    def average_donation(self):
        try:
            average = sum(self.__donation_history) / len(self.__donation_history)
        except ZeroDivisionError:
            average = 0
        return average

    def generate_thank_you_email_to_single_donor(self):
        email_to_donor = (
            "Dear {},\nWe would like to thank you for your donation. So far, you "
            "have donated $ {:.2f} to our organization and for that, we are grateful."
            "You are helping us continue our work supporting and growing our "
            "community.\nYou truly make a difference! We could not do this work "
            "without your support.\n\n".format(self.full_name, self.total_donation_sum)
        )
        return email_to_donor

    def add_donation(self, donation_amount):
        self.donation_history += [donation_amount]

    def __str__(self):
        return "{} total donation sum is : {}".format(self.full_name, self.total_donation_sum)

    def __repr__(self):
        return f"Donor('{self.full_name}', {self.donation_history})"

    def __eq__(self, other):
        return self.full_name == other.full_name and self.donation_history == other.donation_history

    def __lt__(self, other):
        return self.total_donation_sum < other.total_donation_sum


# Business Logic - DonorCollection Class
class DonorCollection(object):
    """
    DonorCollection Class representing a collection of donors
    """

    def __init__(self, donor_list=None):
        if donor_list is not None:
            self.donor_list = donor_list
        else:
            self.donor_list = []

    @property
    def donor_list(self):
        self.__donor_list.sort(key=lambda donor: donor.total_donation_sum, reverse=True)
        return self.__donor_list

    @donor_list.setter
    def donor_list(self, donor_list):
        if type(donor_list) == list and all(isinstance(donor, Donor) for donor in donor_list):
            self.__donor_list = donor_list
        else:
            raise ValueError("The donor list must be a list of donor objects (instances of class Donor) "
                             "representing a donor and their donation history. An invalid data type was provided "
                             "instead: {}".format(donor_list))

    def add_donor(self, donor):
        if isinstance(donor, Donor):
            self.donor_list.append(donor)
        else:
            raise ValueError("You tried to add an invalid Donor to our records ->  invalid type: {}. "
                             "Only Donor instances can be added.".format(type(donor)))

    def get_donor_records(self, donor_full_name):
        for donor in self.donor_list:
            if donor.full_name.lower() == donor_full_name.strip().lower():
                return donor
        return None

    def generate_donor_report(self):
        donor_report_text = ""
        if len(self.donor_list):
            donor_report_text += "******* The current donors are: *******\n"
            headers = ('Donor Full Name', 'Total Given', 'Num Gifts', 'Average Gift')
            header_str = "{:<20s} | {:>16s} | {:^15s} | {:>16s}\n".format(*headers)
            donor_report_text += header_str
            donor_report_text += "-" * len(header_str)
            for donor in self.donor_list:
                donor_report_text += "\n{:<20s}   ${:>15.2f}   {:>15d}   ${:>15.2f}".format(
                    donor.full_name,
                    donor.total_donation_sum,
                    donor.num_donation,
                    donor.average_donation
                )
        else:
            donor_report_text += "There are no donors in our current database records. Please add them"
        return donor_report_text

    @staticmethod
    def _build_donor_list_from_file(filename):
        donor_list = []
        try:
            with open(filename, 'r') as fh:
                for line in fh:
                    full_name, donation_history = line.strip().split(';')
                    donation_history = [float(amount) for amount in donation_history.strip().split(',')]
                    donor = Donor(full_name, donation_history)
                    donor_list.append(donor)
            return donor_list, "Donors records successfully loaded from {} !".format(filename)
        except FileNotFoundError:
            return donor_list, "File {} does not exist. The donors record history is currently empty!".format(filename)

    @classmethod
    def build_donor_collection_from_file(cls, filename):
        donor_list, msg = cls._build_donor_list_from_file(filename)
        return cls(donor_list), msg

    def load_donor_data_from_file(self, filename):
        self.donor_list.clear()
        self.donor_list, msg = self._build_donor_list_from_file(filename)
        return msg

    def save_donor_data_to_file(self, filename):
        with open(filename, "w+") as fh:
            for donor in self.donor_list:
                donation_history = [str(amount) for amount in donor.donation_history]
                donor_str = "{};{}\n".format(donor.full_name, ','.join(donation_history))
                fh.write(donor_str)

    def generate_letter_to_all_donors(self):
        if len(self.donor_list):
            for donor in self.donor_list:
                email = donor.generate_thank_you_email_to_single_donor()
                donor_filename = "{}.txt".format(donor.full_name.lower().replace(' ', '_'))
                with open(donor_filename, "w+") as fh:
                    fh.write(email)
            return "A letter has been successfully sent to every donor in our records!"
        else:
            return "There are no donors in our current database records. Please add them"
