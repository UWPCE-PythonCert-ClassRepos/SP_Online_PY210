#!/usr/bin/env python3

""" Donor classes to be run by cli_main.py
"""

# Starting data structure of donors:

import copy
import pathlib

donor_db = {"Scrooge McDuck": [8000.00, 70000.00],
            "Montgomery Burns": [49.53],
            "Richie Rich": [1000000.00, 500000.00],
            "Chet Worthington": [200.00, 44387.63, 10200.00],
            "Silas Skinflint": [0.25, 1.00, 0.43]}

report_head = '{:20}| {:>15}|{:>15}| {:>15}'.format(
    'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')

letter = "\n".join(("", "Dear {},", "",
                        "    Thank you for your very kind donations totaling ${:.2f}.", "",
                        "    It will be put to very good use.", "",
                        "               Sincerely,",
                        "                  - The team"))

break_line = '-'*72

ty_message = "\n".join(("", "Dear {}",
                            "Thank you for your generous donation of {:.2f}", ""))

repform = '{:20} ${:>15.2f}  {:>15}  ${:15.2f}'


class DonorCollections(object):
    '''DonorCollections class used to store and manipultate the main dict'''

    donors = copy.deepcopy(donor_db)

    def __init__(self, donors=donors):
        self.donors = donors

    def add_donor(self, tyname, amt):
        '''Adds a new donor or updates an existing donor, returns thank you letter'''
        tyname = tyname.title()
        if self.donors.get(tyname) is None:
            self.donors[tyname] = [amt]
        else:
            self.donors.get(tyname).append(amt)
        ty_output = ty_message.format(tyname, amt)
        return ty_output

    def make_report(self):
        '''Creates and returns the report on the data'''
        aggregate = ['\n', report_head, break_line]
        for key, value in sorted(self.donors.items(), key=lambda i: sum(i[1]), reverse=True):
            don = Donor(key, value)
            line = don.format_donor()
            aggregate.append(line)
        return aggregate

    def send_letter(self):
        '''Executes the loop to the Donor class to send letters to each donor'''
        for key, value in sorted(self.donors.items(), key=lambda i: sum(i[1]), reverse=True):
            don = Donor(key, value)
            letter = don.create_letter()


class Donor(object):
    '''Donor class used to access data for a single donor'''

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.d_times = len(value)
        self.total = sum(self.value)
        self.avg = self.total/self.d_times

    def format_donor(self):
        '''Formats the donor information for the report in DonorCollections'''
        self.line = repform.format(self.name, self.total, self.d_times, self.avg)
        return self.line

    def create_letter(self):
        '''Creates the thank you file for a specific person'''
        form_letter = self.write_letter()
        file_name = self.name.replace(" ", "_") + ".txt"
        pth = pathlib.Path('./')
        dest = pth.absolute() / file_name
        with open(dest, 'w') as outfile:
            outfile.write(form_letter)

    def write_letter(self):
        '''Writes an individual letter'''
        form_letter = letter.format(self.name, self.total)
        return form_letter
