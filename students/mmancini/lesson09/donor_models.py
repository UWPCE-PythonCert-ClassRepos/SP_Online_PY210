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

    def get_dict_donors(self):
        return self.dict_donors

    def add_donation(self, in_donor_name, in_donation_amount):
        donor_names_lst = self.dict_donors.keys()
        if in_donor_name in donor_names_lst:
            self.dict_donors[in_donor_name].append(in_donation_amount)
        else:
            amount_ary = []
            amount_ary.append(in_donation_amount)
            self.dict_donors.update({in_donor_name: amount_ary})


