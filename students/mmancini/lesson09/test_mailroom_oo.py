#!/usr/bin/env python3

from donor_models import Donor
from donor_models import Donor_Collection

from cli_main import *

###################################

db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

###################################

def diag_show():
    for key, value in all_donors.dict_donors.items():
        donor_name = key
        donations_ary = value
        msg = ""
        msg += f"donor {donor_name} donations are {donations_ary}"
        print(msg)


def init_donors_collection():

    for key, value in db_donors2.items():
        donor_name = key
        donations_ary = value
        dx = Donor(donor_name, donations_ary)
        all_donors.add_donor(dx)

    diag_show()


def test_mailroom_create_report():
    pass
    init_donors_collection()
    create_report(all_donors.dict_donors)


def test_mailroom_write_letters():
    pass
    init_donors_collection()
    write_letters_to_all(all_donors.dict_donors)


###################################

if __name__ == "__main__":
    pass
    test_mailroom_create_report()
    test_mailroom_write_letters()
