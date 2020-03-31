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


def test_suite():

    # run test suite tests
    print(f"Mailroom Test Suite Started")
    test_create_report()
	test_send_thankyou_email()
    print(f"Mailroom Test Suite Completed")

####################################

# main tests

# tests for mailroom business logic

test_suite()



