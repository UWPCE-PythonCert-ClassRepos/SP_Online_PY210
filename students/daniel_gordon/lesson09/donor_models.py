class Donor():
    """Contains a donors name and a list of donations"""
    def __init__(self, name, donations=[]):
        """
        Initialzes a Donor oject
        
        :param name: a multi word string, only the first and last words will be
                     stored as the donors name
        
        :param donations: either a number or a list of numbers to be stored in a list
        """
        #process name
        names = name.split(' ')
        self.first_name = names[0]
        if(len(names) == 1):
            self.last_name = ""
            self.middle_names = ""
        else:
            self.last_name = names[-1]
            self.middle_names = " ".join(names[1:-1])
        
        #process donations
        self.donations = []
        try:
            self.donations.extend(donations)
        except TypeError:
            self.donations.append(donations)
    
    @property
    def name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name

    @property
    def full_name(self):
        if self.middle_names:
            return f"{self.first_name} {self.middle_names} {self.last_name}"
        return self.name

    def add_donation(self, money):
        """Record a new donation from a donor"""
        try:
            self.donations.append(float(money))
        except ValueError as err:
            print("Donation must be a number value;", err)
            raise
    
    def thank_you(self):
        """Thank donor for most recent donation"""
        try:
            return f"Thank you {self.name} for your generous donation of {self.donations[-1]:.2f}"
        except IndexError as err:
            print("Donor has not yet donated:", err)
            raise
        
    def report_entry(self):
        total = sum(self.donations)
        num = len(self.donations)
        try:
            avg = total/num
        except ZeroDivisionError:
            avg = 0
        return f"{self.name:<25} | ${total:>10.2f} | {num:>9} | ${avg:>11.2f}"
    
    def letter(self):
        letter = [f"Dear {self.name}",""]
        try:
            letter.extend([f"\tThank you for your donation of {self.donations[-1]:0.2f}",""])
        except IndexError as err:
            print("Donor has not yet donated:", err)
            raise
        letter.extend([f"\tSincerly,","\t\tThe Team"])
        return "\n".join(letter)
    
    def __eq__(self, other):
        """Defined to support __getitem__ in DonorCollection"""
        return (self.last_name, self.first_name, self.middle_names) == (other.last_name, other.first_name, self.middle_names)
    
    @staticmethod
    def sort_by_name(self):
        return (self.last_name, self.first_name, self.middle_names)
    
    @staticmethod
    def sort_by_total(self):
        return sum(self.donations)

class DonorCollection():
    """Contains a list of donors and report functionality"""
    def __init__(self, donor=None):
        self.donors = []
        if donor:
            self.add_donor(donor)
    
    @classmethod        
    def from_list(cls, donors):
        """Creates a Donor Collection from a list of donors"""
        #I'm not 100% sure I'm using self and cls correctly here
        self = cls()
        for donor in donors:
            self.add_donor(donor)
        return self
            
    def add_donor(self, donor):
        """Add donor to the list, performs"""
        if type(donor) == Donor:
            self.donors.append(donor)
        else:
            raise TypeError("Must be a Donor type")
    
    def report(self):
        """Generate and return a multiline string summurizing contributions"""
        title_str = f"{'Donor Name':<25} | Total Given | Num Gifts | Average Gift"
        hr = '-'*len(title_str)
        report = [title_str, hr]
        for donor in sorted(self.donors, key=Donor.sort_by_total, reverse=True):
            report.append(donor.report_entry())
        return '\n'.join(report)
    
    def make_list(self):
        """Lists the full name of each donor"""
        result = []
        for donor in sorted(self.donors, key=Donor.sort_by_name):
            result.append(donor.full_name)
        return '\n'.join(result)
    
    def __getitem__(self, key):
        """Returns a donor based on the donors name"""
        donor = Donor(key)
        try:
            index=self.donors.index(donor)
        except ValueError:
            self.add_donor(donor)
            return self.donors[-1]
        else:
            return self.donors[index]
    
    def __contains__(self, item):
        """Returns true if the donor is in the collection"""
        return Donor(item) in self.donors
        
    def __iter__(self):
        """Allows user to loop through all donors"""
        self.n = 0
        return self
    
    def __next__(self):
        """Allows user to loop through all donors"""
        if self.n < len(self.donors):
            result = self.donors[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration