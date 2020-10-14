#!/usr/bin/env python3

class Donor(Object)
    def __init__(self, first, last, donation=0):
        self._name = ' '.join(first, last)
        self._donations = donation

    @property
    def name(self):
        return self._name

    
