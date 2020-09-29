#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mailroom import initialize_donors
from mailroom import calculate_stats
from mailroom import thank_you_email
from mailroom import update_donation_dict
from mailroom import generate_report
from mailroom import sort_donors_by_total
from mailroom import create_report_header
from mailroom import create_report_body
from mailroom import THANK_YOU_TEMPLATE
from mailroom import EMAIL_TEMPLATE
from mailroom import donors
from mailroom import create_directory
from mailroom import save_letters

import os
import pathlib
import shutil


def test_initialize_donors_creates_donor_list():
    initialize_donors()
    assert donors["Neil Armstrong"] == [15000.00, 15000.00]
    assert donors["Chris Hadfield"] == [17325.42, 13823.83, 0.99]


def test_update_donation_dict():
    initialize_donors()
    update_donation_dict("R2 D2", 777.66)
    update_donation_dict("Matt C", 9876.54)
    update_donation_dict("R2 D2", 44.23)

    assert donors["Matt C"] == [9876.54]
    assert donors["R2 D2"] == [777.66, 44.23]


def test_calculate_stats_generates_valid_answers():
    values = [1000, 2000, 3000]
    result = {"sum": 6000, "len": 3, "average": 2000}
    assert result == calculate_stats(values)


def test_thank_you_email():
    donor = {"name": "Matt C", "amount": 1234.56}

    test_email = (
        """\nDear Matt C,\n"""
        """Thank you for your recent donation of $1234.56. """
        """Your donation will help us purchase a taxidermied seagull.\n"""
        """Please consider donating again at your earliest convenience.\n\n"""
        """Sincerely,\n"""
        """The Human Fund\n"""
    )
    assert test_email == thank_you_email(donor)


def test_update_donation_histor():
    initialize_donors()
    update_donation_dict("Alan Bean", 111.11)

    assert donors["Alan Bean"] == [28477.13, 727.10, 111.11]


def test_create_report_header():
    name_length = 15

    expected_str = []
    expected_str.append(" Donor Name      | Total Given | Num Gifts | Average Gift")
    expected_str.append("---------------------------------------------------------")
    expected_str = "\n".join(expected_str)
    assert expected_str == create_report_header(name_length)


def test_create_report_body():
    donor_test = {"Matt C": [100.00, 200.00], "R2 D2": [50.00, 100.00, 150.00]}

    length = len("Matt C") + 5
    expected_str = []
    expected_str.append(" Matt C       $     300.00           2  $      150.00")
    expected_str.append(" R2 D2        $     300.00           3  $      100.00")
    expected_str = "\n".join(expected_str)

    result = create_report_body(length, donor_test)
    assert expected_str == result


def test_sort_donors_by_total():
    temp = {"Matt C": [200.0], "R2 D2": [150]}
    names = sorted(temp, key=sort_donors_by_total, reverse=True)
    names = "\n".join(names)
    expected_names = "Matt C\nR2 D2"

    assert expected_names == names


def test_generate_report():
    test_donors = {"Matt C": [5000.00], "R2 D2": [100.00, 100.00]}

    expected_str = []
    expected_str.append(" Donor Name  | Total Given | Num Gifts | Average Gift")
    expected_str.append("-----------------------------------------------------")
    expected_str.append(" Matt C       $    5000.00           1  $     5000.00")
    expected_str.append(" R2 D2        $     200.00           2  $      100.00")
    expected_str = "\n".join(expected_str)

    report = generate_report(test_donors)

    assert expected_str == report


def test_create_directory():
    directory = "temp"

    path = pathlib.Path("./")
    path = path / directory

    create_directory(directory)

    assert path.exists()
    shutil.rmtree(path)


def test_save_letters():
    directory = "temp"
    path = pathlib.Path("./")
    path = path / directory
    create_directory(directory)

    dlist = {"Matt C": [100.00], "R2 D2": [40.00, 140.00]}

    save_letters(dlist, path)

    m_path = path / "Matt_C.txt"
    r_path = path / "R2_D2.txt"

    assert r_path.exists()
    assert m_path.exists()
    shutil.rmtree(path)
