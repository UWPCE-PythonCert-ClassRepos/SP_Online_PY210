#!/usr/bin/env python3

import pytest
import os
from pathlib import Path

"""
test code for Mailroom

Different scenarios to test:
Thank you:
    Donor Name
    Gift Value
    Letter

Create report:
    create report
    print report

Send Letters:
    Body of letters
    Letters are created

Quit:
    Quits
"""


# you can change this import to test different versions receiver, quit, donors, gift, new_donor, email
from Mailroom import *

@pytest.mark.parametrize(
    'a, expected', [
        ("Morgan Stanely", True),
        ("Cornelius Vanderbilt", True),
        ("John D. Rockefeller", True),
        ("Stephen Girard", True),
        ("Andrew Carnegie", True),
        ("William Gates", False),
        ("Jeffery Bezos", False)
    ]
)
def test_new_donor(a, expected):
    assert new_donor(a) is expected

def test_gift_float():
    assert gift(75.54) == 75.54

def test_gift_string():
    with pytest.raises(ValueError):
        gift("String")

def test_thank_you():
    output = "Thanks Andrew Carnegie for your $77.0 in donations."
    assert thank_you("Andrew Carnegie", 77.00) == output

@pytest.mark.parametrize(
    'a, ex1,', [
        (0, "Adam"),
        (1, "Bernie"),
        (2, "Carl"),
    ]
)
def test_calc_report(a, ex1):
    tester = {"Bernie": [1, 1, 1, 1],
                "Carl": [0, 0],
                "Adam": [2, 2, 2]
                }
    test_dict = calc_report(tester)
    assert test_dict[a][0] == ex1


#paramtrize
def test_file_creation():
    path = pathlib.Path.cwd()
    os.path.join("Andrew Carnegie_Thank you Letter.txt")
    obj = Path(path)
    assert obj.exists()

#needs more work
def test_body_letter():
    text = "Greetings"
    thank_letter = "Andrew Carnegie_Thank you Letter.txt"
    with open(thank_letter, 'r') as f:
        line = thank_letter.readline()
    assert body_letter == text is True

def test_quit():
    assert quit() == "quit"