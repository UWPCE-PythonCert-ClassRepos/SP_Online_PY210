EMAIL_TEMPLATE = (
    "Dear {},\n\n"
    "Thank you for your last donation of ${:.2f}.\n"
    "You have contributed a total of ${:.2f} over {} donation(s).\n"
    "Your generosity is appreciated.\n"
    "\nSincerely,\n"
    "-The Team\n\n"
)

class Donor():
    def __init__(self, name):
        self._name = name.title()
        self._donations = []

    @property
    def name(self):
        return self._name

    def add_donation(self, amount):
       self._donations.append(amount)

    def create_thank_you(self):
        return EMAIL_TEMPLATE.format(self.name, 
                                        self.last_donation,
                                        self.donation_total, 
                                        self.num_donations)

    @property
    def donations(self):
        return self._donations

    @property
    def donation_total(self):
        return sum(self._donations)

    @property
    def num_donations(self):
        return len(self._donations)

    @property
    def last_donation(self):
        return self._donations[-1]

    @property
    def average_donation(self):
        if self.num_donations:
            return self.donation_total / self.num_donations
        else:
            return 0.00

    def __lt__(self, other):
        return self.donation_total < other.donation_total

    def __gt__(self, other):
        return self.donation_total > other.donation_total

    def __str__(self):
        return f"Donor total donations: {self.donation_total}"

    def __repr__(self):
        return self.name

class DonorCollection():
    def __init__(self, donors=[]):
        self._donors = donors

    def add_donor(self, donor):
        self._donors.append(donor)
    
    @property
    def donors(self):
        return self._donors