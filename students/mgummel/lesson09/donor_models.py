#! /usr/bin/env python3

class Donor(object):
    full_name = ""
    donations = list()
    
    def __init__(self, donor_name, donation):
        self.full_name = donor_name
        self.donations = [donation]
        self._total_donation = donation

    @property
    def total_donation(self):
        return self._total_donation


    @property
    def num_of_donations(self):
        return len(self.donations)


    @property
    def avg_donation(self):
        return self._total_donation / self.num_of_donations

    @property
    def last_donation(self):
        return self.donations[-1]


    def add_donation(self, donation_amt):
        """
        adds the donation amount to the database.

        :param donation_amt: amount to add to new donation
        :type sponsor: float
        """

        self.donations.append(donation_amt)
        self._total_donation += donation_amt


    def __str__(self):
        email_template = '\n'.join((f'\n\nDear {self.full_name},\n',
                            f'Thank you for your very kind donation of ${self.last_donation:.2f}.\n',
                            'It will be put to very good use.\n',
                            '           Sincerely,',
                            '             -The Team\n'))
        return email_template



class DonorCollection(object):
    donor_map = list()

    def __init__(self, *args: Donor):
        for donor in args:
            self.donor_map.append(donor)

    def generate_list(self):
        names = [key for key in self.donor_map.keys()]
        name_selection = "\n".join(["{}"] * len(self.donor_map)).format(*names)
        return name_selection

    def __repr__(self):
        names = list()
        for donor_object in self.donor_map:
            names.append(donor_object.full_name)
        return names
def main():
    d1 = Donor("Matt Gummel", 123.12)
    print(d1.full_name)
    print(d1.avg_donation)
    print(d1.total_donation)
    d1.add_donation(32.86)
    print(d1.avg_donation)
    print(d1.total_donation)
    print(d1)
    d2 = Donor("Elizabeth Gummel", 432.00)
    dc1 = DonorCollection(d1, d2)
    print(dc1.__repr__())

    


if __name__ == '__main__':
    main()