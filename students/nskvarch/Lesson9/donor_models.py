# Mailroom OO exercise, Class Module, created by Niels Skvarch

import os


class Donor(object):
    """creates a donor object with an associated list of donations"""
    def __init__(self, name):
        self.name = name
        self.donation = []

    @property
    # returns the times the donor has donated
    def times_donated(self):
        return len(self.donation)

    @property
    # returns a total of all donations associated with that donor object
    def total_donated(self):
        return sum(self.donation)

    @property
    # returns an average of all donations associated with a donor object
    def avg_donated(self):
        return sum(self.donation) / len(self.donation)

    @property
    # returns the last donation made
    def last_donation(self):
        return self.donation[-1]

    @property
    # returns a tuple for reporting on a specific donor
    def report_tuple(self):
        return str(self.name), str(self.total_donated), str(self.times_donated), str(self.avg_donated)

    def add_donation(self, amount):
        # adds a donation value to a donor object
        self.donation.append(float(amount))


class DonorCollections(object):
    """A collection of donor objects and reporting functions"""
    def __init__(self):
        self.donor_db = []

    def __contains__(self, item):
        return item in self.donor_db

    @property
    # returns a tuple with all donor names in the data base
    def donor_names(self):
        return tuple(d.name for d in self.donor_db)

    @property
    # returns all of the donor objects in the collection
    def donors(self):
        return tuple(d for d in self.donor_db)

    @property
    # returns a list of donors and their associated donations sorted by total donated in descending order
    def report_list(self):
        return [("Name", "Total Donated", "Times Donated", "Average Donation")] + \
               sorted([d.report_tuple for d in self.donor_db], key=lambda x: float(x[1]), reverse=True)

    def add_donor(self, donor):
        # adds a donor object to the collection
        self.donor_db.append(donor)

    def get_donor_by_name(self, donor_name):
        # takes a donor name and returns a donor object
        for donor in self.donor_db:
            if donor_name == donor.name:
                return donor
        return Donor(donor_name)

    def create_letters(self, path):
        # uses the collection of donor objects and generates a text file in the current working directory
        # with a thank you note for each donor in the collection
        nl = "\n"
        for donor in self.donor_db:
            filename = donor.name + ".txt"
            full_filename = os.path.join(path, filename.replace(" ", ""))
            with open(full_filename, 'w') as f:
                f.write(f"Dear {donor.name},{nl}" +
                        f"    Thank you for your donation of $ {donor.last_donation}. We {nl}" +
                        f"appreciate your contribution.{nl}{nl}    Your total donation amount is now " +
                        f"$ {donor.total_donated}.{nl}{nl}" +
                        f"Sincerely,{nl}" +
                        f"Your Charity of Choice"
                        )
