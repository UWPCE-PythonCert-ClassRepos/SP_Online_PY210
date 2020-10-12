#!/usr/bin/env python3
import mailroom4
import os.path as path  # for testing file creation

'''
program used in tandem with pytest to complete unit tests on mailroom4.py
program.
'''


def test_get_donor_list_1():
    # works with default donor dict
    mailroom4.donors = {
              "William Gates, III": [653772.32, 12.17],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32]
    }
    expected_list = ["William Gates, III", "Mark Zuckerberg", "Jeff Bezos",
                     "Paul Allen"]
    assert mailroom4.get_donor_list() == expected_list


def test_get_donor_list_2():
    # works with single donor
    mailroom4.donors = {"William Gates, III": [653772.32, 12.17]}
    expected_list = ["William Gates, III"]
    assert mailroom4.get_donor_list() == expected_list


def test_get_donor_list_3():
    # works with empty donor dict
    mailroom4.donors = {}
    expected_list = []
    assert mailroom4.get_donor_list() == expected_list


def test_add_donation_1():
    # adds single donor and donation as expected
    mailroom4.donors = {
              "William Gates, III": [653772.32, 12.17],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32]
    }
    donor_name = "The Dude"
    donation_amount = 100.00
    expected_dict = {
              "William Gates, III": [653772.32, 12.17],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "The Dude": [100.0]
    }
    mailroom4.add_donation(donor_name, donation_amount)
    assert mailroom4.donors == expected_dict


def test_add_donation_2():
    # correctly adds donation if donor already in dict
    mailroom4.donors = {"William Gates, III": [653772.32, 12.17]}
    expected_dict = {"William Gates, III": [653772.32, 12.17, 100.0]}
    mailroom4.add_donation("William Gates, III", 100.00)
    assert mailroom4.donors == expected_dict


def test_get_report_text_1():
    # works with default donor dict
    mailroom4.donors = {
              "William Gates, III": [653772.32, 12.17],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32]
    }
    expected_list = [
        "William Gates, III        $    653,784.49          2  $"
        "      326,892.24",
        "Mark Zuckerberg           $     16,396.10          3  $"
        "        5,465.37",
        "Jeff Bezos                $        877.33          1  $"
        "          877.33",
        "Paul Allen                $        708.42          3  $"
        "          236.14"
    ]
    assert mailroom4.get_report_text() == expected_list


def test_get_report_text_2():
    # works with 1 donor in dict
    mailroom4.donors = {"William Gates, III": [653772.32, 12.17]}
    expected_list = [
        "William Gates, III        $    653,784.49          2  $"
        "      326,892.24"]
    assert mailroom4.get_report_text() == expected_list


def test_get_report_text_3():
    # works with empty donor dict
    mailroom4.donors = {}
    expected_list = []
    assert mailroom4.get_report_text() == expected_list


def test_get_report_text_4():
    # works with initial dict in backwards summation order
    mailroom4.donors = {
            "Paul Allen": [663.23, 43.87, 1.32],
            "Jeff Bezos": [877.33],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "William Gates, III": [653772.32, 12.17]
    }
    expected_list = [
        "William Gates, III        $    653,784.49          2  $"
        "      326,892.24",
        "Mark Zuckerberg           $     16,396.10          3  $"
        "        5,465.37",
        "Jeff Bezos                $        877.33          1  $"
        "          877.33",
        "Paul Allen                $        708.42          3  $"
        "          236.14"
    ]
    assert mailroom4.get_report_text() == expected_list


def test_write_letters():
    # files are created in directory
    mailroom4.donors = {
            "test1": [663.23, 43.87, 1.32],
            "test2": [877.33]
    }
    mailroom4.write_letters()
    for donor in mailroom4.donors:
        assert path.exists(f"{donor}.txt")


def test_create_email_text():
    text = ("Dear Donor,\n\n"
            "It is with incredible gratitude that we accept your wonderfully "
            "generous donation of $1,000.00.  Your "
            "contribution will truly make a difference in the path forward "
            "towards funding our common goal."
            "\n\nEver Greatefully Yours,\n\n"
            "X" + ("_" * 20) + "\n")
    assert mailroom4.create_email_text("Donor", 1000) == text
