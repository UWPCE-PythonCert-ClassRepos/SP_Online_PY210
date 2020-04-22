#!/usr/bin/env python3

from donor_models import Donor
from donor_models import Donor_Collection


###################################


charity_name = "ABC Charity"

db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}


all_donors = Donor_Collection()

###################################

def diag_show():
    for key, value in all_donors.dict_donors.items():
        donor_name = key
        donations_ary = value
        msg = ""
        msg += f"donor {donor_name} donations are {donations_ary}"
        print(msg)


def init_donors_from_db():

    for key, value in db_donors2.items():
        donor_name = key
        donations_ary = value
        dx = Donor(donor_name, donations_ary)
        all_donors.add_donor(dx)

    diag_show()

    #for donor in db_donors2:
    #    dx = Donor(donor)
    #d1 = Donor('Jeff Bezos')
    # d2 = dm.Donor('William Gates, III')
    # d3 = dm.Donor('Paul Allen')
    # d4 = dm.Donor('Mark Zuckerberg')
    # d1.add_donation(1000,400)
    # d2.add_donation(100,90)
    # d3.add_donation(556,4.9)
    # d4.add_donation(1010,400.9, 99900)
    # my_donors.add_donors(d1,d2,d3,d4)

def test_mailroom():

    init_donors_from_db()

    pass

###################################

if __name__ == "__main__":
    i = 0
    test_mailroom()


