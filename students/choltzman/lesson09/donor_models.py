class Donor:
    def __init__(self, name):
        self.name = name
        self.donations = []

    def __eq__(self, other):
        if self.name == other.name and self.donations == other.donations:
            return True

    def add_donation(self, value):
        self.donations.append(value)

    @property
    def donations_total(self):
        return sum(self.donations)

    @property
    def donations_count(self):
        return len(self.donations)

    @property
    def donations_avg(self):
        return sum(self.donations) / len(self.donations)


class DonorCollection:
    def __init__(self):
        self.donors = {}

    def add_donor(self, name):
        """Add a new donor object with the given name."""
        if name not in self.donors:
            self.donors[name] = Donor(name)

    def get_donor(self, name):
        """Return a donor object by name. Return None if not found."""
        if name in self.donors:
            return self.donors[name]

    @property
    def names(self):
        """Return a list of donor names."""
        return [name for name in self.donors]

    @property
    def names_sorted(self):
        """Return a list of donor names sorted by total donations."""
        donors_sorted = sorted(self.donors.items(),
                               key=lambda i: i[1].donations_total,
                               reverse=True)
        names = [name for name, _ in donors_sorted]
        return names
