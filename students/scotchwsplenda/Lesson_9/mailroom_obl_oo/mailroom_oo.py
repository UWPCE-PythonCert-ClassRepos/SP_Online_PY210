
class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)


class Donor():

    __metaclass__ = IterRegistry
    donlist = []

    def __init__(self, cname, donations=[]):
        """New donor instance may be created with a name and/or a donation amount.
        The donation may be a single value, or a list of donations
        """
        self.cname = cname
        self.donations = donations
        self.donlist.append(self)

    def add_donation(self, donation=0):
        self.donations.append(donation)


class Donor_Collection(object):

    def __init__(self):
        self.donors = []

    def __repr__(self):
        return "Donor_Collection()"

    @property
    def donor_names(self):
        return [i.cname for i in self.donors]

    @property
    def don_count(self):
        return len(self.donors)

# why doesn't this work?
    def data_mets(self):
        for x in self.donors:
            print(x.cname, x.donations)

    def add_donor(self, donor, donation=0):
        # expects a Donor object to be passed, but if not, will create one
        if isinstance(donor, Donor):
            self.donors.append(donor)
        else:
            self.donors.append(Donor(donor, donation))

    def add_donation(self, donation=0):
        self.donors.donations.append(donation)


# load em up
# Gordian = Donor_Collection.donors.append(Donor("Gordian", [30.0, 45.0]))
# Maximus = Donor_Collection.donors.append(Donor("Maximus", [65.0, 12.0]))
# Tacitus = Donor_Collection.donors.append(Donor("Tacitus", [33.0, 22.0, 25.00]))
# Commodus = Donor_Collection.donors.append(Donor("Commodus", [43.0, 11.0]))

Gordian = Donor("Gordian", [30.0, 45.0])
Maximus = Donor("Maximus", [65.0, 12.0])
Tacitus = Donor("Tacitus", [33.0, 22.0, 25.00])
Commodus = Donor("Commodus", [43.0, 11.0])

print(Donor.donlist.index(Commodus))
x = Commodus
x.add_donation(55)
print(x.donations, x.cname)
