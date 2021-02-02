#-------------------------------------------#
#Tittle: donor_modles.py, PYTHON210 - Assignment 8
#Desc: Create a donor and handle multiple donors
#Change Log: (Who, When, What)
#Brent Kieszling, 2021-Jan-25, created file
#-------------------------------------------#

import numpy as np
import pickle

class Donor(object):
    """Stores Data about a donor:
    
    properties:
        person: (str) Name of donor
        donations: (lst) Holds each donation made by the donor
        gifts: (int) Total number of donations made
        average: (float) Average of donations made
        total: (flaot) Total donations made
    methods:
        new_donation(amount) -> None
        change_donation(number, amount) -> None
        thank_you() -> (str)
        create_file() -> None
    """
    def __init__(self, person, donation):
        if type(person) != str:
            raise TypeError("String expected")
        try:
            donation = float(donation)
        except:
            raise TypeError("Provide donations in numeric format (1 or 1.11)")
        self._person = person
        self._donations = [donation]

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = person

    @property
    def donations(self):
        return self._donations

    @property
    def gifts(self):
        return len(self._donations)

    @property
    def average(self):
        return round(np.mean(self._donations), 2)

    @property
    def total(self):
        return sum(self._donations)

    def __str__(self):
        f_title = "Donation Summary:"
        f_seperate = "-----------------------------------------------------------------"
        f_header = "{name:<20} | {total:<10} | {gifts:<9} | {average:<10}"\
                    .format(name = "Donor Name", total = "Total Given",\
                    gifts = "Num Gifts", average = "Average Gift")
        f_row = repr(self)
        f_gift = "Donation {number}: $ {amount:.2f}"
        display = [f_title, f_seperate, f_header, f_seperate, f_row, f_seperate]
        x = 1
        for item in self._donations:
            a = f_gift.format(number = x, amount = item)
            display.append(a)
            x += 1
        return "\n".join(display)

    def __repr__(self):
        f_row = "{:<20} $ {:<10.2f}   {:^9}  $ {:>10.2f}"
        f_row = f_row.format(self._person, self.total, self.gifts, self.average)
        return f_row

    def new_donation(self, amount):
        if amount < 0:
            amount = 0
        self._donations.append(amount)

    def change_donation(self, number, amount):
        if amount < 0:
            amount = 0
        self._donations[ number-1] = amount

    def thank_you(self):
        letter = """
    Dear {donor},
    
    Thank you for your most recent donation of ${last:.2f}. We are humbled by your 
    lifetime contribution of ${total:.2f}.
    
    Sincerly,
    Making Good Things Happen"""
        return letter.format(donor = self._person, total = self.total, last = self.donations[-1])

    def create_file(self):
        save_file = self._person.replace(" ", "_").lower() + ".txt"
        letter = self.thank_you()
        with open(save_file, 'w') as file:
            file.write(letter)


class Donors(object):
    """Processes donor objects:
    
    properties:
        profiles: (lst) Holds each donor
    methods:
        find_donor(person) -> donor
        new_donor(person, donation) -> None
        save(file_name) -> None
        load(file_name) -> None
        thank_yous(person) -> None
    """
    def __init__(self, donor_info = None):
        if donor_info == None:
            self._profiles = []
        else:
            self._profiles = [donor_info]

    def __str__(self):
        self._profiles.sort(reverse = True, key = lambda y: y.total)
        f_title = "Donor Rankings:"
        f_seperate = "-----------------------------------------------------------------"
        f_header = "{name:<20} | {total:<10} | {gifts:<9} | {average:<10}"\
                    .format(name = "Donor Name", total = "Total Given",\
                    gifts = "Num Gifts", average = "Average Gift")
        display = [f_title, f_seperate, f_header]
        rank = 1
        for item in self._profiles:
            display.append(str(rank) + " " + repr(item))
            rank += 1
        return "\n".join(display)

    @property
    def profiles(self):
        return self._profiles

    def find_donor(self, person):
        a = False
        for item in self._profiles:
            if item.person == person:
                a = True
                return item
        if a == False:
            raise IndexError

    def new_donor(self, person, donation):
        a = Donor(person, donation)
        self._profiles.append(a)

    def save(self, file_name):
        with open(file_name, 'wb') as fileObj:
            pickle.dump(self._profiles, fileObj)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as fileObj:
                self._profiles = pickle.load(fileObj)
        except FileNotFoundError:
            self._profiles = []

    def thank_yous(self, person = None):
        if person == None:
            for item in self.profiles:
                donor = self.find_donor(item.person)
                donor.create_file()
        else:
            donor = self.find_donor(person)
            donor.create_file()





























