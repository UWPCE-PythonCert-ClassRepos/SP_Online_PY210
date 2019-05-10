#!/usr/bin/env python3

# Russell Felts
# Assignment 6 - Mailroom Unit Tests

import mailroom as mailroom


def test_create_donor_list():
    """ Use a predefined dictionary to verify the method creates a list of dicts containing:
    the donor name, last donation amount, and total donation amount """

    donor_list = mailroom.create_donor_list()

    assert {'name': 'Lionel Messi', 'last_donation': 100, 'total_donations': 100} in donor_list
    assert {'name': 'Cristiano Ronaldo', 'last_donation': 9450, 'total_donations': 14475}
    assert {'name': 'Gianluigi Buffon', 'last_donation': 2500.5, 'total_donations': 1002500.5}
    assert {'name': 'Neymar', 'last_donation': 250, 'total_donations': 405.24}
    assert {'name': 'Paolo Maldini', 'last_donation': 7500, 'total_donations': 24039.95}


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
