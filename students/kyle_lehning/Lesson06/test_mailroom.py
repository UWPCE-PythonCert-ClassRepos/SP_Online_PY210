#!/usr/bin/env python3
import mailroom_part4 as mail


def test_add_donor():
    assert mail.add_donor("Kyle Lehning") == \
           {"name": "Kyle Lehning", "total_don": 0, "donations": 0, "avg": 0}
    assert mail.donors["KYLE LEHNING"] == {"name": "Kyle Lehning", "total_don": 0, "donations": 0, "avg": 0}


def test_add_donation():
    test_donor = {"name": "Paul Allen", "total_don": 708.42, "donations": 3, "avg": 236.14}
    mail.add_donation(test_donor, 150.006)
    assert test_donor == {"name": "Paul Allen", "total_don": 858.43, "donations": 4, "avg": 214.61}


def test_generate_report():
    compare_string = """
Donor Name      | Total Given | Num Gifts | Average Gift
--------------------------------------------------------
Bill Gates       $  653784.49           2  $   326892.24
Mark Zuckerberg  $    16396.1           3  $     5465.37
Steve Jobs       $     1002.4           2  $       501.2
Jeff Bezos       $     877.33           1  $      877.33
Paul Allen       $     708.42           3  $      236.14
"""
    test_string = mail.generate_report()
    assert test_string == compare_string



