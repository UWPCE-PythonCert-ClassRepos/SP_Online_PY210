#!/usr/bin/env python3


###################################


class Donor():
    def __init__(self, full_name):
        self.name = full_name
        self.lst_donations = []

    def __init__(self, full_name, in_donations):
        self.name = full_name
        self.lst_donations = in_donations


class Donor_Collection():
    # def __init__(self, donors=[]):
    #     self.lst_donors = donors
    #
    # def add_donor(self, in_donor):
    #     self.lst_donors.append(in_donor)

    def __init__(self, donors={}):
        self.dict_donors = donors

    def add_donor(self, in_donor):
        self.dict_donors[in_donor.name] = in_donor.lst_donations

    # def diag_show(self):
    #     for key, value in self.dict_donors.items():
    #         donor_name = key
    #         donations_ary = value
    #         msg = ""
    #         msg += f"donor {donor_name} donations are {donations_ary}"
    #         print(msg)

