class Donor(object):
    def __init__(self, name=None, amount=None):
        self.name = name.title()
        self.amount = []
        if amount is not None:
            self.amount = amount

    def __repr__(self):
        return '{} donated ${}'.format(self.name, self.amount)

    def __str__(self):
        return 'Donor({}, {})'.format(self.name, self.amount)

    def send_letter(self):
        content = ('''Dear {}, 
            Thank you for your generous donation of ${:,.2f} to us.
            It will be put to very good use.

                                Sincerely,
                                    -The Team
                                              '''.format(self.name, self.amount))
        return content


class DonorCollection:

    def __init__(self, donor_list=None):
        self.donors = {}
        if donor_list is not None:
            self.donors = donor_list

    def add_new_donor(self, name, amount):
        self.donors[name] = [amount]
        return self.donors

    def add_amount_same_donor(self, name, amount):
        self.donors[name] += [amount]
        return self.donors

    def times(self, name):
        return len(self.donors[name])

    def total(self, name):
        return sum(self.donors[name])

    def donor_name_list(self):
        name_list = {name for name in self.donors.keys()}
        return name_list

    def sort_donor(self, item):
        return sum(self.donors.get(item))

    def sorted(self):
        sort = sorted(self.donors, key=self.sort_donor, reverse=True)
        return sort

    def send_letters_to_all(self):
        for name in self.donors.keys():
            first, last = name.split()
            filename = first + '_' + last
            filename = '{}.txt'.format(filename)
            with open(filename, 'w') as file:
                file.write(f'''Dear {name},
            Thank you for your generous donation of ${self.sort_donor(name):,.2f} to us.
            It will be put to very good use.
                                Sincerely,
                                    -The Team
                                          ''')
