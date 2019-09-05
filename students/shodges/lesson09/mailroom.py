#!/usr/bin/env python3

class Donor(object):
    def __init__(self, donor_name, *args):
        self.name = donor_name
        self.ledger = []
        for i in args:
            self.ledger.append(float(i))


    @property
    def count(self):
        return len(self.ledger)


    @property
    def donations(self):
        return sum(self.ledger)
