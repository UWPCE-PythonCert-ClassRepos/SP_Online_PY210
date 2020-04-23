#!/usr/bin/env python3

from donor_models import Donor
from donor_models import DonorCollection

from cli_main import *

###################################

# test db
db_donors2 = {
            "Jane Smith": [25, 50],
            "Tom Adams": [100],
            "Helen Smalls": [10, 20, 30],
            "Ming Chan": [50],
            "Mary Jones": [5, 10, 15]}

###################################

init()


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
    # diag_show()


###################################

# test cases

def test_mailroom_list_donors():
    pass
    init_donors_collection()
    expected_all_donors_listed = read_file(canned_all_donors_listed)
    all_donors_listed = display_donors(all_donors.dict_donors)
    assert expected_all_donors_listed == all_donors_listed


def test_existing_donor_donation():
    pass
    init_donors_collection()
    thankyou_email = process_donor_donation("Ming Chan", 100)
    checkpoint_donor = thankyou_email.__contains__("Ming Chan")
    checkpoint_amount = thankyou_email.__contains__("100")
    assert checkpoint_donor == True
    assert checkpoint_amount == True
    # diag_show()


def test_new_donor_donation():
    pass
    init_donors_collection()
    expected_thankyou_email = read_file(canned_thankyou_email)
    test_name = "Sam Adams"
    test_amount = 5000
    thankyou_email = process_donor_donation(test_name, test_amount)
    assert expected_thankyou_email == thankyou_email


def test_mailroom_create_report():
    pass
    init_donors_collection()
    expected_report = read_file(canned_sorted_report)
    report = op_create_report(all_donors.dict_donors)
    assert report == expected_report


def test_mailroom_write_letters():
    pass
    init_donors_collection()
    op_write_letters_to_all(all_donors.dict_donors)




###################################

if __name__ == "__main__":
    pass

    # test suite

    test_mailroom_list_donors()
    test_existing_donor_donation()
    test_new_donor_donation()
    test_mailroom_create_report()
    test_mailroom_write_letters()

