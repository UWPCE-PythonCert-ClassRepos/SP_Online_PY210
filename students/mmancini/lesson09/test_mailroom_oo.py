#!/usr/bin/env python3

from donor_models import Donor
from donor_models import DonorCollection

from cli_main import *
from mailroom_control import MailroomControl


###################################

init()

###################################

# test cases

def test_mailroom_list_donors():
    pass
    init_donors_collection()
    expected_all_donors_listed = read_file(canned_all_donors_listed)
    all_donors_listed = op_display_list_of_donors()
    assert expected_all_donors_listed == all_donors_listed


def test_existing_donor_donation():
    pass
    init_donors_collection()
    mailroom_control = get_mailroom_control()
    thankyou_email = mailroom_control.process_donor_donation(all_donors, "Ming Chan", 100)
    checkpoint_donor = thankyou_email.__contains__("Ming Chan")
    checkpoint_amount = thankyou_email.__contains__("100")
    assert checkpoint_donor == True
    assert checkpoint_amount == True


def test_new_donor_donation():
    pass
    init_donors_collection()
    expected_thankyou_email = read_file(canned_thankyou_email)
    test_name = "Sam Adams"
    test_amount = 5000
    mailroom_control = get_mailroom_control()
    thankyou_email = mailroom_control.process_donor_donation(all_donors, test_name, test_amount)
    assert expected_thankyou_email == thankyou_email


def test_mailroom_create_report():
    pass
    init_donors_collection()
    expected_report = read_file(canned_sorted_report)
    report = mailroom_control.create_report(all_donors.dict_donors)
    assert report == expected_report


def test_mailroom_write_letters():
    pass
    init_donors_collection()
    expected_all_thankyou_letters = read_file(canned_all_thankyou_letters)
    all_thankyou_letters = mailroom_control.write_letters_to_all_donors(all_donors.dict_donors)
    assert all_thankyou_letters == expected_all_thankyou_letters


###################################

if __name__ == "__main__":
    pass

    # test suite

    test_mailroom_list_donors()
    test_existing_donor_donation()
    test_new_donor_donation()
    test_mailroom_create_report()
    test_mailroom_write_letters()

