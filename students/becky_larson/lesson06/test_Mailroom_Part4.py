#!/usr/bin/env python

"""
Testing Mailroom
"""

import mailroom_part4


def test_donor_exists():
    mailroom_part4.donor_exists('Cher') is True


def test_list_donors():
    mailroom_part4.list_donors() == ['Cher','Drew Barrymore','Charlie Brown','Jack Black','Sam Smith',]


def test_add_donor():
    mailroom_part4.add_donor('Mike', 245.00) is True
    expected = [245.00]
    assert mailroom_part4.donor_db['Mike'] == expected


def test_update_donor():
    mailroom_part4.update_donor('Cher', 44) is True
    expected = [1000.00, 245.00, 44]
    assert mailroom_part4.donor_db['Cher'] == expected


def test_get_report():
    results = mailroom_part4.get_report(mailroom_part4.assert_donor_db)
    row1 = results[0]
    row2 = results[1]
    row3 = results[2]
    row4 = results[3]
    row5 = results[4]
    assert row1 == "Drew Barrymore             $    25,000.00             1  $   25,000.00"
    assert row2 == "Jack Black                 $    11,109.50             3  $    3,703.17"
    assert row3 == "Sam Smith                  $     5,524.00             2  $    2,762.00"
    assert row4 == "Cher                       $     1,245.00             2  $      622.50"
    assert row5 == "Charlie Brown              $       175.01             3  $       58.34"


def test_get_letter_text_1():
    donation_dict = {}
    donation_dict['name'] = 'Frank'
    donation_dict['donation'] = float(100)
    expected = "Dear Frank,"
    actual = mailroom_part4.get_letter_text(donation_dict)
    assert actual[0:11] == expected


def test_get_letter_text_2():
    donation_dict = {}
    donation_dict['name'] = 'Frank'
    donation_dict['donation'] = float(100)
    actual = mailroom_part4.get_letter_text(donation_dict)
    assert(donation_dict['name']) in actual
    money = "{0:.2f}".format(donation_dict['donation'])
    print(money)
    assert(money) in actual
