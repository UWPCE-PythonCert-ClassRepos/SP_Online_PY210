#!/usr/bin/env python3

"""
Lesson 8: Test Mail Room Part 5
Course: UW PY210
Author: Jason Jenkins
"""
import mailroom_part4 as mailroom
import pathlib
from os import listdir
from os.path import isfile, join


def setup():
    mailroom.donor_dict.update({"william gates": [1345.462]})
    mailroom.donor_dict.update({"mark zuckerberg": [12546.124, 13445.124]})
    mailroom.donor_dict.update({"jeff bezos": [1234.123, 12341431.12]})
    mailroom.donor_dict.update({"paul allen": [734.12, 124.41, 10000]})
    mailroom.donor_dict.update({"jason jenkins": [10, 20, 30, 40, 50, 60]})


def test_get_report():
    expected = []
    expected.append(["jeff bezos", 12342665.24, 2, 6171332.62])
    expected.append(["mark zuckerberg", 25991.25, 2, 12995.62])
    expected.append(["paul allen", 10858.53, 3, 3619.51])
    expected.append(["william gates", 1345.46, 1, 1345.46])
    expected.append(["jason jenkins", 210.00, 6, 35.00])

    assert mailroom.get_report() == expected


def test_get_letter_text():
    mailroom.donor_dict.update({"jason jenkins": [10, 20, 30, 40, 50, 60]})

    expected = "Dear jason jenkins\n"
    expected += "\tThank you for your donation of $210.00.\n"
    expected += "\tIt will be put to very good use.\n"
    expected += "Sincerely,\n"
    expected += "-The Team\n"

    assert mailroom.get_letter_text("jason jenkins") == expected


def test_send_all_thanks():
    p = pathlib.Path("emails/")

    mailroom.send_all_thanks()

    files = [f for f in listdir(p) if isfile(join(p, f))]

    expected_files = []
    expected_files.append("william_gates.txt")
    expected_files.append("mark_zuckerberg.txt")
    expected_files.append("jeff_bezos.txt")
    expected_files.append("paul_allen.txt")
    expected_files.append("jason_jenkins.txt")

    assert expected_files[0] in files
    assert expected_files[1] in files
    assert expected_files[2] in files
    assert expected_files[3] in files
    assert expected_files[4] in files


def test_print_donor_dict():
    expected = "List of donors\n"
    expected += "--------------\n"
    expected += "william gates\n"
    expected += "mark zuckerberg\n"
    expected += "jeff bezos\n"
    expected += "paul allen\n"
    expected += "jason jenkins\n"

    assert mailroom.print_donor_dict() == expected


def test_thank_you_email():
    expected = f"Thank you jason jenkins for your donation."

    assert mailroom.thank_you_email("jason jenkins") == expected


def test_update_donor_list():
    mailroom.update_donor_list("test", 20)
    mailroom.update_donor_list("william gates", 1234)

    assert mailroom.donor_dict.get("test") == [20]
    assert mailroom.donor_dict.get("william gates") == [1345.462, 1234]
