#!/usr/bin/env python3

# Russell Felts
# Assignment 6 - Mailroom Unit Tests

import mailroom as mailroom
import datetime
from pathlib import Path


def test_create_report_data():
    """ Use donor_data dict in mailroom to verify the method creates a list of lists containing:
    donor name, total donation amount, number of donation, average donation """

    temp_data = mailroom.create_report_data()

    assert ['Lionel Messi', 100, 1, 100.0] in temp_data
    assert ['Cristiano Ronaldo', 14475, 3, 4825.0] in temp_data
    assert ['Gianluigi Buffon', 1002500.5, 2, 501250.25] in temp_data
    assert ['Neymar', 405.24, 4, 101.31] in temp_data
    assert ['Paolo Maldini', 24039.95, 4, 6009.9875] in temp_data


def test_create_donor_list():
    """ Use a predefined dictionary to verify the method creates a list of dicts containing:
    the donor name, last donation amount, and total donation amount """

    donor_list = mailroom.create_donor_list()

    assert {'name': 'Lionel Messi', 'last_donation': 100, 'total_donations': 100} in donor_list
    assert {'name': 'Cristiano Ronaldo', 'last_donation': 9450, 'total_donations': 14475}
    assert {'name': 'Gianluigi Buffon', 'last_donation': 2500.5, 'total_donations': 1002500.5}
    assert {'name': 'Neymar', 'last_donation': 250, 'total_donations': 405.24}
    assert {'name': 'Paolo Maldini', 'last_donation': 7500, 'total_donations': 24039.95}


def test_write_letter():
    """ Check to see if the requested file is created the file content is checked in test_compose_message"""

    now = datetime.datetime.now()

    mailroom.write_letter(now, {'name': 'Lionel Messi', 'last_donation': 100, 'total_donations': 100})

    config = Path('Lionel Messi' + '_' + str(now.month) + '_' + str(now.year) + '.txt')
    assert config.is_file()


def test_compose_message():
    """ Test the compose message returns the proper string """

    message = mailroom.compose_message({'name': 'Lionel Messi', 'last_donation': 100, 'total_donations': 100})

    assert message == "\nTo: Lionel Messi\nSubject: Thank you.\n\nLionel Messi thank you for your previous generous " \
                      "donation of 100.00.\nYou're total donations to date are now: 100.00."


def test_update_donation_amount():
    """ Test updating the donor list with a new donation amount for a current donor or adding a new donor with a
    donation amount """

    mailroom.update_donation_amount("Russell", 200.50)
    assert "Russell" in mailroom.donor_data
    assert mailroom.donor_data.get("Russell")[-1] == 200.50

    mailroom.update_donation_amount("Neymar", 100)
    assert "Neymar" in mailroom.donor_data
    assert mailroom.donor_data.get("Neymar")[-1] == 100
