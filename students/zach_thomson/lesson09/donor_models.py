#!/usr/bin/env python3

class Donor():

    def __init__(self, name, *args):
        self.name = name
        self.donations = list(args)

    def new_donation(self, donation):
        self.donations.append(donation)

    def number_of_donations(self):
        return len(self.donations)

    def avg_donation(self):
        return sum(self.donations)/len(self.donations)

    def sum_donations(self):
        return sum(self.donations)

#    def email(self):
#        return "\nDear {},\nThank you for your generous donation of ${:.2f}!\n".format(self.name, donation)


class DonorCollection():

    def __init__(self, *args):
        self.donors = {d.name: d for d in args}

    def new_donation(self, name, donation):
        if self.donors.get(name):
            self.donors[name].new_donation(donation)
        else:
            self.donors[name] = Donor(name, donation)
