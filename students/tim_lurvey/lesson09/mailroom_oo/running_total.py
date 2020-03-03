#!/usr/bin/env python
__author__ = 'Tim Lurvey, ig408c'


class RunningTotal(object):
    """A class for storing an accumulating total value.
    Provides the following access:
    :key (str):         value for object identity (settable)
    :total (float):     cumulative total
    :count (int):       cumulative counter or total additions
    :add_to_total():    add an amount to the total
    :average()          return the total / count"""

    _key = ""
    _total = 0.
    _count = 0

    def __init__(self, new_key: str, total: float = 0., count: int = 0):
        # all inputs must pass through assertive type checking
        self._set_key(new_key=new_key)
        self._set_total(new_total=total)
        self._set_count(new_count=count)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._set_key(new_key=new_key)

    def _set_key(self, new_key):
        """assertive type checking with error trapping"""
        try:
            assert isinstance(new_key, str)
            self._key = new_key
        except AssertionError:
            raise TypeError("Error:key must be a string")

    @property
    def total(self):
        return self._total

    def _set_total(self, new_total):
        """assertive type checking with error trapping"""
        try:
            self._total = float(new_total)
        except AssertionError:
            raise TypeError("Error:total must be numeric")

    @property
    def count(self):
        return self._count

    def _set_count(self, new_count):
        """assertive type checking with error trapping"""
        try:
            assert isinstance(new_count, int)
            self._count = new_count
        except AssertionError:
            raise TypeError("Error:key must be a integer")

    def add_to_total(self, amount):
        self._total = self.total + amount
        self._count += 1

    @property
    def average(self):
        return (self._total / self._count)
