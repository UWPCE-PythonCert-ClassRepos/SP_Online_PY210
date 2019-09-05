#!/usr/bin/env python3

class Donor(object):
    def __init__(self, donor_name, ledger=[]):
        self.name = donor_name
        self.ledger = ledger


    @property
    def count(self):
        return len(self.ledger)


    @property
    def donations(self):
        return sum(self.ledger)
