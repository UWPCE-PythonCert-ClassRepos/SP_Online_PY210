#!/usr/bin/env python3

"""
Lesson 9: Mail Room Part Object Oriented (Donor models)
Course: UW PY210
Author: Jason Jenkins
"""

# Define a multiple inheritance scheme:
from operator import itemgetter

class Donor(object):

    def __init__(self, full_name, donation_amount):
        self.full_name = full_name
        self._total_given = 0
        self.num_gifts = 0

        self.give(donation_amount)

    @property
    def average(self):
        if self.num_gifts < 1:
            return 0
        else:
            return round(self.total_given / self.num_gifts, 2)

    @property
    def total_given(self):
        return round(self._total_given, 2)

    def give(self, val):
        if(val > 0):
            self._total_given += val
            self.num_gifts += 1

    def thanks(self):
        return f"Thank you {self.full_name} for your donation."

    def __str__(self):
        return self.full_name

    def __eq__(self, other):
        if self.full_name.lower() == other.lower():
            return True
        else:
            return False


# Define a multiple inheritance scheme:
class DonorCollection(list):
    def get_list(self):
        output = list()
        for item in self:
            output.append(item.full_name)

        return "\n".join(filter(None, output))

    def get_report(self):
        output = list()

        for item in self:
            output.append([item.full_name, item.total_given, item.num_gifts, item.average])

        return sorted(output, key=itemgetter(1), reverse=True)

    def donate(self, person, amount):
        try:
            self.lookup(person).give(amount)
        except AttributeError:
            new_doner = Donor(person, amount)
            self.append(new_doner)
        finally:
            return self.lookup(person).thanks()

    def lookup(self, person):
        for item in self:
            if item == person:
                return item
