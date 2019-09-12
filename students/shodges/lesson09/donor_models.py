#!/usr/bin/env python3
import shelve
from collections import OrderedDict
from pathlib import Path
from datetime import datetime

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


    def format_letter(self, extra_whitespace = False):
        letter_template = """Dear {name},
On behalf of all of us at Save the Marmots, thank you for your recent gift of ${amount:.2f}.  When it comes to ensuring marmots have loving homes, every dollar goes a long way.

Your very generous gifts of ${total:.2f} will help us provide food and shelter for all of the rescued marmots, and ensure our staff have the resources to train them for placement.

Warmest regards,

Sean Hodges
"""

        letter_whitespace = """



{}


"""
        letter_values = {'name': self.name, 'amount': self.ledger[-1], 'total': self.donations}

        if extra_whitespace == True: # I still like the extra whitespace in the user interactive mode :)
            return (letter_whitespace.format(letter_template)).format(**letter_values)
        else:
            return letter_template.format(**letter_values)


    def save_letter(self, dirpath):
        letter = dirpath / (self.name.replace(' ', '_') + '.txt')
        try:
            with letter.open("w") as fileio:
                fileio.write(self.format_letter())
        except (FileNotFoundError, PermissionError):
            return False
        except TypeError:
            try:
                letter.unlink()
            except (PermissionError, OSError, FileNotFoundError):
                pass
            finally:
                return False
        else:
            return letter


class DonorCollection(object):
    def __init__(self, dbfile='donors'):
        self.db = shelve.open(dbfile, writeback=True)


    def donor(self, donor_name):
        return self.db[donor_name]


    @property
    def donors(self):
        donorlist = []
        for k in self.db.keys():
            donorlist.append(k)
        return donorlist

    def generate_report(self):
        tmp_report = {}
        for donor in self.db:
            donor_info = {'total': self.db[donor].donations, 'count': self.db[donor].count}
            try:
                donor_info['average'] = self.db[donor].donations / self.db[donor].count
            except ZeroDivisionError:
                donor_info['average'] = 0
                pass
            tmp_report[donor] = donor_info
        return OrderedDict(sorted(tmp_report.items(), key=lambda x: x[1]['total'], reverse=True))


    def save_letters(self, dirpath):
        results = []
        letter_dir = Path(dirpath) / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
        try:
            letter_dir.mkdir(exist_ok=True)
        except (NotADirectoryError, FileNotFoundError, PermissionError):
            return (False, None)
        else:
            for donor in self.db.keys():
                results.append(self.donor(donor).save_letter(letter_dir))
        return (letter_dir, results)


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
