#!/usr/bin/env python3

class Donor(object):
    def __init__(self, first, last, donation=None):
        self._name = [first, last]
        self._donations = [] if donation is None else [donation]

    def __repr__(self):
        return f'Donor({self._name[0]}, {self._name[1]})'

    @property
    def name(self):
        return self._name
    
    @property
    def full_name(self):
        return f'{self._name[0]} {self._name[1]}'

    @property
    def donations(self):
        return self._donations
    
    def add_donation(self, donations):
        self._donations.append(donations)
    
    def last_donation(self):
        if self._donations == []:
            raise AttributeError (f'No donations from {self.full_name} on record.')
        return self._donations[-1]
