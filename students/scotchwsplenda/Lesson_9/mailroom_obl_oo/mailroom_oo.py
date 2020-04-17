

class Donor():

    def __init__(self, name, initial_donation=0):
        """New donor instance may be created with a name and/or a donation amount.
        The donation may be a single value, or a list of donations
        """
        self.name = name
        if type(initial_donation) is list:
            self.donations = [i for i in initial_donation]
            # grab the last item in the list for the "most recent donation"
            self.most_recent_donation = initial_donation.pop(-1)
        else:
            self.donations = [initial_donation]
            self.most_recent_donation = initial_donation

    def add_donation(self, donation=0):
        self.donations.append(donation)


class Donor_Collection(object):

    def __init__(self):
        self.donors = []
        # load em up
        self.donors.append(Donor("Gordian", [30.0, 45.0]))
        self.donors.append(Donor("Maximus", [65.0, 12.0]))
        self.donors.append(Donor("Tacitus", [33.0, 22.0, 25.00]))
        self.donors.append(Donor("Commodus", [43.0, 11.0]))

    def __repr__(self):
        return "Donor_Collection()"

    @property
    def donor_names(self):
        return [i.name for i in self.donors]

    @property
    def don_count(self):
        return len(self.donors)

    def data_mets(self):
        for x in self.donors:
            print(x.name, x.donations)

    def add_donor(self, donor, donation=0):
        # expects a Donor object to be passed, but if not, will create one
        if isinstance(donor, Donor):
            self.donors.append(donor)
        else:
            self.donors.append(Donor(donor, donation))

    def add_donation(self, donation=0):
        self.donors.donations.append(donation)
