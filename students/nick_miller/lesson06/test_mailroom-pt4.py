#!/usr/bin/env python3

"""PY210_SP - mailroom part 4 unit tests
author: Nick Miller"""

import sys
import mailroom_pt4 as mail

donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}

test_db = {
    "Donor One": [10, 10],
    "Donor Two": [0],
    "Donor Three": [10, 25.50]
}


def test_letter_prep():
    expected = ['jeff', 40.0]
    assert mail.letter_prep("jeff staple", donor_db) == expected
    expected = ['donor', 35.5]
    assert mail.letter_prep("donor three", test_db) == expected


def test_letter_format():
    assert mail.letter_format("bob", 10) == ('\n'.join(['', 'Dearest bob,', '',
                             'Thank you for your generous support!',
                             'We appreciate your donation(s), which total $10.00 to date!', '',
                             'Sincerest regards,',
                             '',
                             'The Foundation']))


# def test_thanks_all():
#     assert mail.thanks_all(test_db)


def test_report_sort_key():
    expected = 1
    assert mail.report_sort_key([0, 1]) == expected


def test_quit_prog():
    expected = "exit menu"
    assert mail.quit_prog() == expected


print("Function check:")
if test_letter_prep() is None:
    print("letter_prep() is good")
if test_letter_format() is None:
    print("letter_format() is good")
# if test_thanks_all() is None:
#     print("thanks_all() is good")
if test_report_sort_key() is None:
    print("report_sort_key() is good")
if test_quit_prog() is None:
    print("quit_prog() is good")
