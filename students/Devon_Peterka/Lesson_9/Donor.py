#!/usr/bin/env python3

class Donor(object):
    '''
    Creates an object for a donor containing their first name, last
    name, and a list of their donations in order.
    
    Initialize as: D = Donor(first, last, donation)
    
    Donation field is optional.  Multiple initial donations can be input
    as a list.
    '''
    def __init__(self, first, last, donation=[]):
        self._name = (first.title(), last.title())
        donation = donation if type(donation) is list else [donation]
        self._donations = donation

    def __repr__(self):
        '''
        Object is represented as a string "Donor(first, last)"
        No donation information is shown in the repr.
        '''
        return f'Donor({self._name[0]}, {self._name[1]})'

    @property
    def name(self):
        '''
        Returns the donor's name as a tuple.
        '''
        return self._name
    
    @property
    def full_name(self):
        '''
        Returns
        '''
        return f'{self._name[0]} {self._name[1]}'

    @property
    def donations(self):
        return list(self._donations)
    
    def add_donation(self, *donations):
        self._donations = self._donations + list(donations)
    
    @property
    def last_donation(self):
        if self._donations == []:
            raise AttributeError (f'No donations from {self.full_name} on record.')
        return self._donations[-1]
    
    @property
    def total_donation(self):
        if self._donations == []:
            raise AttributeError (f'No donations from {self.full_name} on record.')
        else:
            return sum(self._donations)
