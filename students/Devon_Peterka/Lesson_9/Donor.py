#!/usr/bin/env python3

class Donor(object):
    '''
    Creates an object for a donor containing their first name, last
    name, and a list of their donations in order.
    
    Initialize as: D = Donor(first, last, donation)
    
    Donation field is optional.  Multiple initial donations can be input
    as a list.
    '''
    def __init__(self, first, last, donation=None):
        '''
        Initializes donor name atribute.  Initializes an empty list
        (donation history) if no initial donation is given.  If
        multiple initial donations are given, passes the list to
        donations attribute.  If a single initial donation is given,
        initializes a list starting with that donation value.
        '''
        self._name = (first.title(), last.title())
        if donation is None:
            donation = []
        self._donations = donation if type(donation) is list else [donation]

    def __repr__(self):
        '''
        Object is represented as a string "Donor(first, last)"
        No donation information is shown in the repr.
        '''
        return f'Donor({self._name[0]}, {self._name[1]})'

    def __lt__(self, other):
        '''
        Establishes how multiple Donor objects are to be compared.
        '''
        return (self.total_donation, self._name[1], self._name[0]) < (other.total_donation, other._name[1], other._name[0])


    @property
    def name(self):
        '''
        Returns the donor's name as a tuple.
        '''
        return self._name
    
    @property
    def full_name(self):
        '''
        Returns Donor object's full name, first then last.
        '''
        return f'{self._name[0]} {self._name[1]}'

    @property
    def donations(self):
        '''
        Returns a list of all donations of the Donor object.
        '''
        return list(self._donations)
    
    def add_donation(self, *donations):
        '''
        Adds a new donation to a Donor object's donation list.
        '''
        self._donations = self._donations + list(donations)
    
    @property
    def last_donation(self):
        '''
        Returns the most recent donation from a Donor object.  Or raises
        an AttributeError if none exists.
        '''
        if self._donations == []:
            raise AttributeError (f'No donations from {self.full_name} on record.')
        return self._donations[-1]
    
    @property
    def total_donation(self):
        '''
        Returns total sum of a Donor objects donations.  Or zero if no
        donations are present.
        '''
        if self._donations == []:
            return 0
        else:
            return sum(self._donations)

    @staticmethod
    def sort_by_name(self):
        '''
        Sort key function that allows for sorting of multiple Donor
        objects alphabetically by last name.
        '''
        return (self._name[1], self._name[0], self.total_donation)
    
    @staticmethod
    def sort_by_donations(self):
        '''
        Sort key function that allows for sorting by the total donation
        of each Donor object
        '''
        return (self.total_donation, self._name[1], self._name[0])

    @staticmethod
    def send_thanks(first, last, amount):
        if type(amount) not in (int, float):
            raise TypeError ('Donation amount must be a number.')
        return f"Dear {first.title()} {last.title()},\n\nThank you for your generous donation of ${amount:,.2f} toward our cause.  Your gift is most appreciated.\n\nThank you,\nOur Charity"
