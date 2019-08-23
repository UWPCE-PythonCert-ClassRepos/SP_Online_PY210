import sys
import os

class Donor(object):

    """
    Class responsible for donor data encapsulation

    This class will hold all the information about a single donor,
    and have attributes, properties, and methods to provide access
    to the donor-specific information that is needed. Any code that
    only accesses information about a single donor should be part of
    this class.
    """

    def __init__(self, name="Anonymous", initial_donation=0):
        """New donor instance may be created with a name and/or a donation amount.
        The donation may be a single value, or a list of donations (as you would
        if you were backfilling an entry
        """
        self.name = name
        if type(initial_donation) is list:
            self.donations = [i for i in initial_donation]
            # grab the last item in the list for the "most recent donation"
            self.most_recent_donation = initial_donation.pop(-1)
        else:
            self.donations = [initial_donation]
            self.most_recent_donation = initial_donation

    def __repr__(self):
        return f"Donor('{self.name}', {self.donations})"

    def __eq__(self, other):
        return ((self.name.lower(), self.sum_donations) ==
                (other.name.lower(), other.sum_donations))

    def __lt__(self, other):
        return ((self.name.lower(), self.sum_donations) <
                (other.name.lower(), other.sum_donations))

    @property
    def sum_donations(self):
        return sum(self.donations)

    @property
    def number_donations(self):
        return len(self.donations)

    @property
    def average_donation(self):
        return round(self.sum_donations / self.number_donations, 2)

    def add_donation(self, donation=0):
        '''Logic for handling user input donation'''
        try:
            if float(donation):
                self.donations.append(donation)
                self.most_recent_donation = donation
        except (TypeError, ValueError) as e:
            pass

    def thank(self):
        '''Prints a summary thank you letter to a donor'''
        return(f"Dearest {self.name},\n"
          "We are writing to formally thank you for your generous"
          f" donation of ${self.most_recent_donation}.\n"
          f"To date, you have donated ${self.sum_donations} "
          "to our honorable mission.\n"
          "You are truly a valuable patron, and we thank you "
          "for your service (and money)")


class Donor_Collection(object):

    """
    This class will hold all of the donor objects, as well as methods
    to add a new donor, search for a given donor, etc. If you want a
    way to save and re-load your data, this class would hold that method,
    too.
    """
    def __init__(self):
        self.donors = []
        self.donors.append(Donor("William Gates, III", [653772.32, 12.17]))
        self.donors.append(Donor("Jeff Bezos", [877.33, 3, 555, 132, 77, 1]))
        self.donors.append(Donor("Paul Allen", [663.23, 43.87, 1.32]))
        self.donors.append(Donor("Mark Zuckerberg", [163.23, 4300.87, 1432.0]))
        self.donors.append(Donor("Brax Dingle", [231, 3232.87, 566.20, 23.23,
                                                 76, 323, 3.87]))

    def __repr__(self):
        return "Donor_Collection()"

    def add_donor(self, donor, donation=0):
        # expects a Donor object to be passed, but if not, will create one
        if isinstance(donor, Donor):
            self.donors.append(donor)
        else:
            self.donors.append(Donor(donor, donation))

    def sort_donors_by_last_name(self):
        return sorted(self.donors,
                      key=lambda donor: donor.name.split()[1], reverse=True)

    def sort_donors_by_first_name(self):
        return sorted(self.donors,
                      key=lambda donor: donor.name.split()[0], reverse=True)

    def sort_donors_by_donation_count(self):
        return sorted(self.donors,
                      key=lambda donor: donor.number_donations, reverse=True)

    def sort_donors_by_total_donations(self):
        return sorted(self.donors,
                      key=lambda donor: donor.sum_donations, reverse=True)

    def thank_everyone(self):

        for i in self.donors:
            with open(f'{i.name}.txt', 'w') as f:
                f.write(f"Dearest {i.name},\n"
                        "We are writing to formally thank you for your most recent"
                        f" donation of ${i.most_recent_donation}.\n"
                        f"To date, you have donated ${i.sum_donations} "
                        "to our honorable mission.\n"
                        "You are truly a valuable patron, and we thank you "
                        "for your service (and money).\n"
                        "Kindest regards\n"
                        "Baron Von Munchausen")

    @property
    def number_of_donors(self):
        return len(self.donors)

    @property
    def top_donor(self):
        return self.sort_donors_by_total_donations()[0].name

    @property
    def most_active(self):
        return self.sort_donors_by_donation_count()[0].name