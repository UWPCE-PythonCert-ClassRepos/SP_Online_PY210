#!/usr/bin/env python3

""" Donor classes to be run by cli_main.py
"""

# Starting data structure of donors:

import pathlib

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


class Donor:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def add_donation(self, amount):
        '''Appends the donation amount to an existing donor'''
        self.value.append(amount)

    @property
    def d_times(self):
        return len(self.value)

    @property
    def total(self):
        return sum(self.value)

    @property
    def avg(self):
        return self.total/self.d_times

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


class DonorCollections(object):
    '''DonorCollections class used to store and manipultate the main dict'''

    def __init__(self, *args):
        self.donors = {d.name: d for d in args}

    def add_donor(self, tyname, amt):
        '''Adds a new donor or updates an existing donor, returns thank you letter'''
        tyname = tyname.title()
        if self.donors.get(tyname) is None:
            self.donors[tyname] = Donor(tyname, [amt])
        else:
            self.donors[tyname].add_donation(amt)
        ty_output = ty_message.format(tyname, amt)
        return ty_output

    def make_report(self):
        '''Creates and returns the report on the data'''
        lines = []
        aggregate = ['\n', report_head, break_line]
        for donor_ob in self.donors.values():
            lines.append([donor_ob.format_donor(), donor_ob.total])
        [aggregate.append(item[0]) for item in sorted(lines, key=lambda i: i[1], reverse=True)]
        return aggregate

    def send_letter(self):
        '''Executes the loop to the Donor class to send letters to each donor'''
        for name in self.donors.values():
            letter = name.create_letter()
