#!/usr/bin/env python3
import shelve

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


    def process(self, donation):
        self.ledger.append(float(donation))


class DonorCollection(object):
    def __init__(self, dbfile='donors.db'):
        self.db = shelve.open(dbfile, writeback=True)


    def donor(self, donor_name):
        return self.db[donor_name]


    def add_donor(self, donor_name):
        self.db[donor_name] = Donor(donor_name)


    def del_donor(self, donor_name):
        try:
            self.db.pop(donor_name)
        except KeyError:
            raise
        else:
            return True


    def db_close(self):
        self.db.close()
