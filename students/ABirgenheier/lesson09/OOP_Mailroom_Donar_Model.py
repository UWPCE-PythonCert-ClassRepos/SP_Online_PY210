
from operator import itemgetter


class Donar(object):

    def __init__(self, name, donation_amt=None):
        """ Donar init obj """
        self.name = name
        self.donation_amt = donation_amt if donation_amt is not None else []

    def add_donation(self, amount):
        """ Add donar donation amount """
        self.donation_amt.append(amount)

    def print_thank_you_message(self):
        """ Print Thank You message """
        message = (f'\nDear {self.name},'
                   f'\n\nThank you for your generous donation of ${self.donation_amt[-1]:.2f}.'
                   '\nWe value your contribution and support.'
                   '\n\nSincerely,\n\nNew Horizon Charity Director\n')
        return message

    def sort_key(self):
        return sum(self.donation_amt)


class DonarCollection():
    """ Donar dictionary init """

    def __init__(self):
        self.donars = {}

    @staticmethod
    def initialize_donars_dict(donar_data):
        # create a new collection object
        donars = DonarCollection()
        for name, amounts in donar_data.items():
            donar = Donar(name, amounts)
            # add the new donar to the collection
            donars.add(donar)
        return donars

    def add(self, donar):
        """ Add donar to the collection """
        self.donars[donar.name] = donar

    def list_of_donars(self):
        """ Generate donars list """
        list_of_donars = []
        for name in self.donars:
            list_of_donars.append(name)
        return '\n'.join(list_of_donars)

    def send_to_all(self):
        """ Save donar letters to files """
        for donar in self.donars.values():
            filename = donar.name + '.txt'
            with open(filename, 'w') as f:
                f.write(Donar.print_thank_you_message(donar))

    def create(self):
        """ Generate a donation history report """
        header = '\n{:<20}|{:^15}|{:^15}|{:>15}'.format("Donar Name", "Total Given",
                                                        "Num Gifts", "Average Gift")
        print("Donation Report")
        print(header)
        print('-'*len(header))
        for entry in self.donars.values():
            total = sum(entry.donation_amt)
            num = len(entry.donation_amt)
            avg = total/num
            print('{:<20} ${:>14,.2f}{:>14}  ${:>16,.2f}'.format(
                entry.name, total, num, avg))
        print('')

    def donor_exists(self, name):
        # Search for donar name in donar collection.
        return any(d for d in self.donars.values() if d.name.upper() == name.upper())
