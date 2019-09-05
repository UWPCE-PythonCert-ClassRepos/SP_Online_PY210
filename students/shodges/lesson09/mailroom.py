#!/usr/bin/env python3

class Donor(object):
    def __init__(self, donor_name, ledger=[]):
        self.name = donor_name
        self.ledger = ledger


    def count(self):
        return len(ledger)


    def donations(self):
        return sum(ledger)
