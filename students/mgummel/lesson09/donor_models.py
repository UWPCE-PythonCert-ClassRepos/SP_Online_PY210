#! /usr/bin/env python3

class Donor(object):
    
    def __init__(self, donor_name, donation):
        self._full_name = donor_name
        self._total_donation = donation
        self._donations = [donation]
        

    @property
    def total_donation(self):
        return self._total_donation


    @property
    def num_of_donations(self):
        return len(self._donations)


    @property
    def avg_donation(self):
        return self._total_donation / self.num_of_donations

    @property
    def last_donation(self):
        return self._donations[-1]


    def add_donation(self, donation_amt):
        """
        adds the donation amount to the database.

        :param donation_amt: amount to add to new donation
        :type sponsor: float
        """

        self._donations.append(donation_amt)
        self._total_donation += donation_amt

    def report_data(self):
        return (self._full_name, self.total_donation, self.num_of_donations, self.avg_donation)

    def __str__(self):
        email_template = '\n'.join((f'\n\nDear {self._full_name},\n',
                            f'Thank you for your very kind donation of ${self.last_donation:.2f}.\n',
                            'It will be put to very good use.\n',
                            '           Sincerely,',
                            '             -The Team\n'))
        return email_template



class DonorCollection(object):
    donor_list = list()
    
    
    def __init__(self, *args: Donor):     
        for donor in args:
            self.donor_list.append(donor)


    def generate_list(self):
        names = [donor._full_name for donor in self.donor_list]
        name_selection = "\n".join(["{}"] * len(self.donor_list)).format(*names)
        return name_selection


    def add_donor(self, new_donor: Donor):
        self.donor_list.append(new_donor)


    def find_donor(self, existing_donor):
        donor_object = None
        for donor in self.donor_list:
            if existing_donor == donor._full_name:
                donor_object = donor
                break
        return donor_object


def main():
    d1 = Donor("Matt Gummel", 123.12)
    print(d1._full_name)
    print(d1.avg_donation)
    print(d1.total_donation)
    d1.add_donation(32.86)
    print(d1.avg_donation)
    print(d1.total_donation)
    print(d1)
    d2 = Donor("Elizabeth Gummel", 432.00)
    dc1 = DonorCollection("test")
    print(dc1.__repr__())

if __name__ == '__main__':
    main()