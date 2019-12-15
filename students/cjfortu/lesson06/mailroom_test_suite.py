#!/usr/bin/env python

"""
The Mailroom Part 4 test suite.

The tests were written for pytest.
Pytest-mock was installed!

The tests each have their own unique data for calling the tested module's funcitons.

User should inspect line 82 to ensure desired test directory for file writing.
Default is the current working directory.
"""

from mailroom_part4 import *
from io import StringIO
import os


def test_no_new(monkeypatch, capsys):
    """Assert that the 'list' command under option 1 prints the existing names."""
    fake_input = StringIO('list')
    monkeypatch.setattr('sys.stdin', fake_input)
    send_single({'Name1': [17.56], 'Name2': [500.00, 1000.00], 'Name3': [2.00, 0.03, 45.00]})
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == """\nPlease provide a full name (case sensitive).
'list will show the list of donor names.
'quit' exits script.
: 

Name1
Name2
Name3\n"""


def test_new_donor(mocker):
    """Assert that entering a new name with donations will update 'data' accordingly."""
    mocker.patch('builtins.input', side_effect=['Newbie', '5 6.78 99'])
    assert send_single({'Bob': [17.56], 'Billy': [500.00, 1000.00]}) == \
        {'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Newbie': [5, 6.78, 99]}


def test_update_donor(mocker):
    """Assert that entering an existing name with donations will update the data accordingly."""
    mocker.patch('builtins.input', side_effect=['Bob', '100 3 0.01'])
    assert send_single({'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00]})\
        == {'Bob': [17.56, 100, 3, 0.01], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00]}


def test_write_letter(mocker, capsys):
    """Assert that entering a name with donations will result in the appropriate individual letter."""
    mocker.patch('builtins.input', side_effect=['That Gal', '8 800 80'])
    send_single({'Doggle': [17.56], 'Lazer': [500.00, 43], 'Blazer': [2.00]})
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout ==\
        "\n\nHi That Gal,\n\nThank you for your total donation of $888.00.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555\n"


def test_create_report(capsys):
    """Assert that creating a report wil result in the correct output."""
    create_a_report({'Doggle': [17.56], 'Lazer': [500.00, 43], 'Blazer': [2.00, 1, 99]})
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == """

          Donor Name         |  Total Given($)  |# Gifts|   Average Gift   
---------------------------------------------------------------------------
 Lazer                       |           543.00 |     2 |            271.50
 Blazer                      |           102.00 |     3 |             34.00
 Doggle                      |            17.56 |     1 |             17.56\n"""


def test_generate_text():
    """Assert that text generation yields the correct text."""
    assert generate_text('Dumbledorf', 909.09) ==\
"\nHi Dumbledorf,\n\nThank you for your lifetime donations of $909.09.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555"


def test_send_all(monkeypatch):
    """Assert that letter files (not content) are written properly.
    User should inspect line 82 to ensure desired test directory!"""
    patched_directory = os.getcwd() + '/'
    fake_input = StringIO(patched_directory)
    monkeypatch.setattr('sys.stdin', fake_input)
    data_dict = {'Mr Blue': [17.56], 'Miss Green': [500.00, 43], 'The Gray': [2.00, 1, 99]}
    send_all(data_dict)
    for name in data_dict:
        assert os.path.isfile("{}{}.txt".format(patched_directory, name))
