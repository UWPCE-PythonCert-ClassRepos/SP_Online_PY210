#!/usr/bin/env python3

class Donor(Object):
    ledger = []

    def __init__(self, donor_name):
        self.name = donor_name


    def count(self):
        return len(ledger)


    def donations(self):
        return sum(ledger)
