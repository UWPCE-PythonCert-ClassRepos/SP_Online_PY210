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
        self.key = new_key
        self.total = total
        self.count = count

    def __repr__(self):
        return f"RunningTotal('{self.key}', {self.total}, {self.count})"

    def __eq__(self, other):
        return (self.key, self.total, self.count) == \
               (other.key, other.total, other.count)

    @staticmethod
    def sort_key(self):
        return (self.name, self.total, self.count)

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        """assertive type checking with error trapping"""
        try:
            assert isinstance(new_key, str)
            self._key = new_key
        except AssertionError:
            raise TypeError("Error:key must be a string")

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, new_total):
        """assertive type checking with error trapping"""
        try:
            self._total = float(new_total)
        except AssertionError:
            raise TypeError("Error:total must be numeric")

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count):
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
