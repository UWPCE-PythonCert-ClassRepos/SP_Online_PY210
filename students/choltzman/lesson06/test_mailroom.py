#!/usr/bin/env python3
from textwrap import dedent
import os
import mailroom


def test_add_donation_new():
    """Test adding a donation for a new person."""
    mailroom._add_donation("Test User", 12345)
    assert mailroom.donors['Test User'] == [12345]


def test_add_donation_existing():
    """Test adding a donation for an existing person."""
    mailroom._add_donation("Jeff Bezos", 6789)
    assert mailroom.donors['Jeff Bezos'] == [1234567.89, 6789]


def test_send_email():
    """Test formatting an email string."""
    emailstr = mailroom._format_email(
            "Test User",
            "Hello World",
            "Hello World")
    assert emailstr == dedent("""\
    From: "Nameless Charity" <sender@example.com>
    To: "Test User" <receiver@example.com>
    Subject: Hello World

    Hello World
    """)


def test_write_file():
    """Test writing email file."""
    # create file and test that it exists
    mailroom._write_file("Test User", "Test")
    assert os.path.isfile("TestUser.txt")

    # delete the file to try to make this idempotent
    os.remove("TestUser.txt")


def test_donor_sort():
    """Test sorting donors by total donations."""
    donors_sorted = mailroom._sort_donors()
    assert donors_sorted[0][0] == "Jeff Bezos"
    assert donors_sorted[-1][0] == "Paul Allen"


def test_report_row():
    """Test report row formatting."""
    assert mailroom._format_report_row("Test User", [12345]) == \
        f"{'Test User':<25} | {12345:>15.2f} | {1:>9} | {12345:>15.2f}"
