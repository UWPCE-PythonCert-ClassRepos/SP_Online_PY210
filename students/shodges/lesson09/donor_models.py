#!/usr/bin/env python3
import shelve
from collections import OrderedDict
from pathlib import Path
from datetime import datetime

class Donor(object):
    """
    Base individual donor class.

    donor_name is the only required argument; all additional arguments will be converted to
    floats and added as initial donations.

    Each instance has two variables:
      * name -- the donor's name
      * ledger -- a list with all donations as floats
    """
    def __init__(self, donor_name, *args):
        self.name = donor_name
        self.ledger = []
        for i in args:
            self.ledger.append(float(i))

    @property
    def count(self):
        """
        Returns the number of donations in the donor's ledger.
        """
        return len(self.ledger)

    @property
    def donations(self):
        """
        Returns the total of all donations in the donor's ledger.
        """
        return sum(self.ledger)

    def process(self, donation):
        """
        Appends donation to the donor's ledger.  Returns True if successful.  No exceptions
        raised are caught and are required to be caught by the implementing code.
        """
        self.ledger.append(float(donation))

    def format_letter(self, extra_whitespace = False):
        """
        Returns a formatted thank you letter with the donor's name, most recent donation, and
        donation total filled in.  If optional argument extra_whitespace is True, extra
        newlines are appended on top and bottom to allow for visual differentiation.
        """
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

        if extra_whitespace == True:
            return (letter_whitespace.format(letter_template)).format(**letter_values)
        else:
            return letter_template.format(**letter_values)

    def save_letter(self, dirpath):
        """
        Saves a letter in dirpath (as a pathlib.posixpath).  Letter name will be donor.txt
        (with spaces replaced by underscores).

        Returns the pathlib.posixpath of the saved letter if successful; else returns False.

        All exceptions are caught here.
        """
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
    """
    Class allowing for grouping of multiple Donor classes for a given charity.  All Donors
    are stored in a shelve database which is opened at init; DonorCollection.db_close() must
    be called to properly close the database -- changes are made to the database stored in
    memory, and closing the database sycns back the changes to the file.
    """
    def __init__(self, dbfile='donors'):
        self.db = shelve.open(dbfile, writeback=True)

    def donor(self, donor_name):
        """
        Returns the Donor object of donor_name (or passes through the raised KeyError if not
        found).
        """
        return self.db[donor_name]

    @property
    def donors(self):
        """
        Returns a list of all donors in the database.
        """
        return [k for k in self.db.keys()]

    def generate_report(self):
        """
        Returns an OrderedDict sorted by total donations in descending order.

        Format:
        [DonorName: {'total': TotalDonations, 'count': NumberOfDonations,
                     'average': AverageDonation}]

        Implementing code is not expected to handle any exceptions.
        """
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
        """
        Saves all letters in the DonorCollection in a directory created in the specified
        dirpath of format YYYYMMDD-HHMM.  Calls each Donor's save_letter method.

        Implementing code is not expected to handle exceptions.

        Returns a list with 3 elements:
        * 0
          - Success: pathlib.posixpath of created directory
          - Failure: False
        * 1
          - Success: list of pathlib.posixpath of all saved letters (return values from
                     Donor's save_letter() method)
          - Failure: None
        * 2
          - Success: list of donor names whose Donor save_letter() method returned False
          - Failure: None
        """
        success = []
        failure = []
        letter_dir = Path(dirpath) / ('{:%Y%m%d-%H%M}'.format(datetime.now()))
        try:
            letter_dir.mkdir(exist_ok=True)
        except (NotADirectoryError, FileNotFoundError, PermissionError):
            return (False, None, None)
        else:
            for donor in self.db.keys():
                try:
                    result = self.donor(donor).save_letter(letter_dir)
                except IndexError:
                    failure.append(donor)
                else:
                    success.append(result)
        return [letter_dir, success, failure]

    def add_donor(self, donor_name):
        """
        Instantiates a new Donor class for donor_name.  Returns True if successfully added;
        raises a ValueError if the donor exists.
        """
        if donor_name not in self.db.keys():
            self.db[donor_name] = Donor(donor_name)
            return True
        else:
            raise ValueError("Donor already exists")

    def del_donor(self, donor_name):
        """
        Deletes donor_name from the database.  Returns True if successfully deleted; re-
        raises the KeyError if the donor was not found.
        """
        try:
            self.db.pop(donor_name)
        except KeyError:
            raise
        else:
            return True

    def db_close(self):
        """
        Closes the shelf.  This also syncs back all changes.
        """
        self.db.close()
