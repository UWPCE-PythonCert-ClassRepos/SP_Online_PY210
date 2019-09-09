#!/usr/bin/env python3
import shelve
from collections import OrderedDict

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
        return True


class DonorCollection(object):
    def __init__(self, dbfile='donors'):
        self.db = shelve.open(dbfile, writeback=True)


    def donor(self, donor_name):
        return self.db[donor_name]


    def generate_report(self):
        tmp_report = {}
        for donor in self.db:
            donor_info = {'total': self.db[donor].donations, 'count': self.db[donor].count,
                          'average': self.db[donor].donations / self.db[donor].count}
            tmp_report[donor] = donor_info
        return OrderedDict(sorted(tmp_report.items(), key=lambda x: x[1]['total'], reverse=True))


    def add_donor(self, donor_name):
        if donor_name not in self.db.keys():
            self.db[donor_name] = Donor(donor_name)
            return True
        else:
            raise ValueError("Donor already exists")


    def del_donor(self, donor_name):
        try:
            self.db.pop(donor_name)
        except KeyError:
            raise
        else:
            return True


    def db_close(self):
        self.db.close()
