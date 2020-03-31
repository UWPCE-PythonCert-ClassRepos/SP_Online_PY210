#!/usr/bin/env python3


import mailroom4 as mailroom

####################################

mailroom.init()


def test_create_report():
    expected_report = mailroom.read_file(mailroom.canned_sorted_report)
    report = mailroom.create_report_sorted()
    assert report == expected_report


####################################


def test_suite():

    # run test suite tests
    print(f"Mailroom Test Suite Started")
    test_create_report()
    print(f"Mailroom Test Suite Completed")

####################################

# main tests

# tests for mailroom business logic

test_suite()



