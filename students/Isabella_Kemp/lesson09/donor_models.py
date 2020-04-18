# class responsible for donor data encapsulation 
class Donor():

    def __init__(self, name, donations=[]):
        """Initialize Donor object."""
        self.name = name
        if type(donations) is list:
            self.donations = donations
        else:
            raise TypeError('Enter donations as a List.')

    def add_donation(self, *args):
        for x in args:
            self.donations.append(x)
        
    @property
    def num_donations(self):
        return len(self.donations)

    @property
    def total_donation(self):
        # sum of donation history
        return sum(self.donations)

    @property
    def avg_donation(self):
        if self.num_donations == 0:
            return 0
        else:
            return(self.total_donation/self.num_donations)

    def thank_you_mail(self, amount):
        return ("Thank you {}, for your generous donation of ${:.2f} !".format(self.name, amount))
    

# Class responsible for donor collection data encapsulation
class DonorCollection():

    def __init__(self, **data):
        self._data = dict(data)
        
    #Add donor info
    def add_donor(self, donor, donation):
        self._data[donor] = Donor(donor, [donation])
        return self._data
            
    def create_report(self):
        def sort_key(donor):
            return int(sum(donor.donation))
        rows = []
        header = ("\n{:<19}| {:<13} | {:<13} | {:>13}".format('Donor Name', 'Total Donated',
                                                                  'Number of Donations',
                                                                  'Avg. Donation Amount'))
        rows.append(header)
        rows.append("-" * 80)
        rows.append('\n')
        sorted_data = sorted(self._data.values(), key=sort_key, reverse=True)
        for donor in sorted_data:
            name, num = (donor.name, donor.num_donations)
            total, avg = (donor.total_donation, donor.avg_donation)
            row_string = ('{:<20} ${:>11,.2f}{:>13}            ${:>11,.2f}'.format(
                    name, total, num, avg))
            rows.append(row_string)
        return "".join(rows)

