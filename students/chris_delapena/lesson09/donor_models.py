# Chris Dela Pena
# donor_models.py

class Donor():

    def __init__(self, donor, donations=[]):
        self.donor = donor
        self.donations = donations

    def add_donation(self, *args):
        for amount in args:
            self.donations.append(amount)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def sum_donations(self):
        return sum(self.donations)

    def print_thank_you(self, amount):
        print(f"Dear {self.name}, thank you for your generous donation of ${amount}. Regards, the Club Owners")

class DonorCollection():

    def __init_(self):
        self.donor_db = []

    def add_donor(self, donor, donation):
        self.donor_db[donor] = Donor(donor,[donation])
        return self.donor_db

    @property
    def donor_list(self):
        return list(self.donor_db)
