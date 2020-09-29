#!/usr/bin/env python3

class Donor():
#donor class for one single donor methods
    def __init__(self, name):

        self.name = name
        self.donations = []

    def __lt__(self, other):

        if self.total_donations() < other.total_donations():
            return True
        elif self.total_donations() == other.total_donations(): # Otherwise, sort by last name
            return self.name.split()[-1] < other.name.split()[-1]
        else:
            return False

    def add_donation(self, amount):

        self.donations.append(amount)

    def last_donation(self):
        if self.donations:
            return self.donations[-1]
        else:
            return 0

    def total_donations(self):
        return sum(self.donations)

    def num_donations(self):
        return len(self.donations)

    def average_donation(self):
        return self.total_donations()/self.num_donations() if self.donations else 0

    def generate_email(self):
        """
        Generate email to donor
        """
        email_dict = {'donor_name':self.name,
                      'donation_amount':self.last_donation()}

        # Create formatted email that can be copied & pasted
        email = ('\n'.join(['Dear {donor_name},','',
        'Thank you for your generous donation of ${donation_amount:.2f}.',
        'Please know that your donations make a world of difference!',
        '','Sincerely,','The Mailroom Team'])).format(**email_dict)

        return(email)

class DonorCollection():
#class for the donors list methods
    def __init__(self):
        self.donors = {}

    def update_donor(self, name, amount):
        d = self.get_donor(name)
        # Update donor object and replace in collection
        d.add_donation(amount)
        self.donors[name] = d

    def get_donor(self, name):
        return self.donors.get(name, Donor(name))

    @property
    def donor_names(self):
        return list(self.donors)

    def generate_report_data(self):
        #generate the data needed for option 2 report
        donors = list(self.donors.values())
        donors.sort(reverse=True)
        report = [(donor.name, donor.total_donations(), donor.num_donations(),
            donor.average_donation()) for donor in donors]
        return report
