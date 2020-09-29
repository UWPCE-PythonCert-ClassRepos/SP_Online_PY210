#!/usr/bin/env python3

import mailroom4 as mailroom


####################################

mailroom.init()


def test_create_report():
    expected_report = mailroom.read_file(mailroom.canned_sorted_report)
    report = mailroom.create_report_sorted()
    assert report == expected_report


def test_send_thankyou_email():
    expected_thankyou_email = mailroom.read_file(mailroom.canned_thankyou_email)
    test_name = "Phil Sims"
    test_amount = 35
    thankyou_email = mailroom.process_send_thankyou_email(test_name, test_amount)
    assert expected_thankyou_email == thankyou_email


def test_all_donors_listed():
    expected_all_donors_listed = mailroom.read_file(mailroom.canned_all_donors_listed)
    all_donors_listed = mailroom.show_donors()
    assert expected_all_donors_listed == all_donors_listed


def test_write_letters():

    # first write all the letters
    mailroom.write_letters_to_all()

    # now test the letters were created correctly
    for key, value in mailroom.db_donors.items():

        # prepare the expected test data
        donor_name = key
        donations_ary = value
        donations_total = sum(donations_ary)

        # test the created letter
        dict_data_line = {"donor_name": donor_name, "donation_amount": float(donations_total)}
        expected_thank_you_letter = ""
        expected_thank_you_letter += f"Dear {donor_name} Thank You for your generous donations " \
                                     f"totaling ${donations_total}:\n".format(**dict_data_line)
        thank_you_letter = mailroom.create_letter(donor_name)
        assert thank_you_letter == expected_thank_you_letter

        # test the persisted letter data
        filename = donor_name + ".txt"
        with open(filename, "r") as f:
            thank_you_letter_data = f.read()
            assert thank_you_letter_data == expected_thank_you_letter

####################################


def test_suite():

    # run test suite tests
    print(f"Mailroom Test Suite Started")
    test_create_report()
    test_send_thankyou_email()
    test_all_donors_listed()
    test_write_letters()
    print(f"Mailroom Test Suite Completed")

####################################

# main tests

# tests for mailroom business logic


test_suite()




