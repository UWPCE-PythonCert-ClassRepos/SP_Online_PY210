class Donor:
    def __init__(self, donor_name, donations = []):
        self.name = donor_name
        self.donations = donations

    @property
    def tot_donations(self):
        return sum(self.donations)

    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def avg_donation(self):
        return round(sum(self.donations)/len(self.donations), 2)

    def new_donation(self, donation_amount):
        self.donations.append(donation_amount)

class DonorCollection:
    def __init__(self):
        self.donor_list = []

    def new_donor(self, new_donor: Donor):
        self.donor_list.append(new_donor)

    def new_donation(self, donor_name, donation_amount):
        for donors in self.donor_list:
            if donor_name == donors.name:
                donors.new_donation(donation_amount)
                return

        new_donor = Donor(donor_name, [donation_amount])
        self.donor_list.append(new_donor)

    def list_donors(self):
        donor_names = ''
        for donors in self.donor_list:
            donor_names += donors.name + '\n'
        return donor_names

    def ty_text(self, donor_name):
        for donors in self.donor_list:
            if donor_name == donors.name:
                return f'Dear {donors.name}, thanks for the ${donors.donations[-1]:.2f}'