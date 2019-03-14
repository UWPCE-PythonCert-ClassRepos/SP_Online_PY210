#!/usr/bin/env python3
import mailroom_part4 as mail
import os.path
import tempfile


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


def test_thank_you_text():
    donor = {"name": "Steve Jobs", "total_don": 1002.40, "donations": 2, "avg": 501.20}
    test_text1 = ("Dear Steve Jobs,"
                  "\n\nThank you for your kind donation of $1002.40."
                  "\nIt will be put to very good use."
                  "\n\nSincerely,"
                  "\n-The Team")
    test_text2 = ("Dear Steve Jobs,"
                  "\n\nThank you for your kind donation of $80.00."
                  "\nIt will be put to very good use."
                  "\n\nSincerely,"
                  "\n-The Team")
    assert mail.thank_you_text(donor) == test_text1
    assert mail.thank_you_text(donor, "80.00") == test_text2


def test_find_widths():
    test_seq = [["this", "is", "a", "test"], ["another", "test", "line", "here"], ["one", "more", "test", "written"]]
    assert mail.find_widths(test_seq) == [7, 4, 4, 7]


def test_print_line():
    header = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    header_string = "{0:<{w1}} | ${1:>{w2}} | {2:>{w3}} | ${3:>{w4}}"
    widths = [12, 14, 16, 18]
    expected = "Donor Name   | $   Total Given |        Num Gifts | $      Average Gift"
    assert mail.print_line(header_string, header, widths) == expected


def test_add_donor():
    assert mail.add_donor("Kyle Lehning") == \
           {"name": "Kyle Lehning", "total_don": 0, "donations": 0, "avg": 0}
    assert mail.donors["KYLE LEHNING"] == {"name": "Kyle Lehning", "total_don": 0, "donations": 0, "avg": 0}


def test_add_donation():
    test_donor = {"name": "Paul Allen", "total_don": 708.42, "donations": 3, "avg": 236.14}
    mail.add_donation(test_donor, 150.006)
    assert test_donor == {"name": "Paul Allen", "total_don": 858.43, "donations": 4, "avg": 214.61}


def test_file_creation():
    file_location = tempfile.gettempdir()
    file_path_name = "{}{}{}".format(file_location, "\\", "test_creation")
    test_file = mail.file_creation(file_path_name)
    test_file.close()
    assert os.path.isfile(test_file.name) is True
