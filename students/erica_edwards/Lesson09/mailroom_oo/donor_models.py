from operator import itemgetter


class Donor(object):
   
    def __init__(self, name, donations=None):
        """Initializes the donor object."""
        self.name = name
        self.donations = donations if donations is not None else []

    def donation_add(self, amount):
        """Add a new donation to the donor's list of donations.
        
        Args:
            amount (number): The amount of the donation.
        """
        self.donations.append(amount)

    def single_donation_letter(self):
        """Generate a single donation letter.
        
        Returns:
            string: A string containing a letter for a single donation.
        """
        result = (f'Thank you {self.name} for your donation of ${self.donations[-1]:.2f}.'
                  ' We appreciate your generous support of our club.\n')
        return result

    def multi_donation_letter(self):
        """Generate a letter for the sum of all donations
        
        Returns:
            string: The letter.
        """
        return (f'Thank you {self.name}. You have donated a total of ${sum(self.donations):.2f}.'
                'We appreciate your generous support for our club.\n')

    def report_values(self):
        """Calculate the sum, length, and average.
        
        Returns:
            tuple: (name, total, quanity, average)
        """
        return (self.name,
                sum(self.donations),
                len(self.donations),
                sum(self.donations) / len(self.donations))


class DonorCollection():
    """Initialize donors dictionary."""
    def __init__(self):
        self.donors = {}

    def add(self, donor):
        """Add donor to the collection.
        
        Args:
            donor (Donor):  A donor
        """
        self.donors[donor.name] = donor

    def list_donors(self):
        """Generate a list of donors.
        
        Returns:
            string: list of donors
        """
        result = ''
        for item in self.donors:
            result += f'{item}\n'
        return result

    def generate_letters(self):
        """Save donor letters to files."""

        for donor in self.donors.values():
            with open(f'{donor.name}.txt', 'w') as f:
                f.write(donor.multi_donation_letter())

    def create_report(self):
        """Create nicely formated report with four columns.

        Returns:
            string:  List of donors and donation information
        """

        sorted_values = sorted(
            [x.report_values() for x in self.donors.values()], key=itemgetter(2), reverse=True)
        result = "\n"
        result += 'Donor Name                | Total Given | Num Gifts | Average Gift\n'
        result += '-'*66 + '\n'
        for name, total_given, number_gifts, avg_gift in sorted_values:
            result += f'{name:<27}${total_given:>11.2f}{number_gifts:>12}  ${avg_gift:>11.2f}\n'
        return result

    def donor_exists(self, name):
        """Search for donor name in donor collection.
        
        Args:
            name (Donor): the donor name
        
        Returns:
            boolean: True if name exists
        """
        return any(d for d in self.donors.values() if d.name.upper() == name.upper())

    @staticmethod
    def from_dict(donor_data):
        """Create a populated DonorCollection from a given dict. 

        Args:
            donor_data (dict): string : list of numbers

        Returns:
            Donor: DonorCollection object
        """
        donors = DonorCollection()                      # Make a new collection object
        for k, v in donor_data.items():     # iterate through donor_data dict
            donor = Donor(k, v)             # create a new donor from k,v
            # add the new donor to the collection
            donors.add(donor)
        return donors                       # return the new collection
