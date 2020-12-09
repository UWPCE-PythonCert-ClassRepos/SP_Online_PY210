#!/usr/bin/env python

# ------------------------------------------------------------------------ #
# Title:test_mailroom.py
# Description: Assignment for Lesson04
# KODonnell,12.02.2020 unit testing for Mailroom Part 4
# ------------------------------------------------------------------------- #


import mailroom
import os


# test add_donation_amount()
# test new entry
def test_add_donation_amount_2():
    assert mailroom.add_donation_amount("Kelby", 40, {}) == \
           ({"Kelby": [40, 1, 40]}, False)


# test existing entry
def test_add_donation_amount_3():
    db = {"Paul Revere": [72.24, 4, 400]}
    assert mailroom.add_donation_amount("Paul Revere", 60, db) == \
           ({"Paul Revere": [132.24, 5, 26.45]}, True)


# test invalid amount type
def test_add_donation_amount_4():
    db = {"Paul Revere": [72.24, 4, 400]}
    assert mailroom.add_donation_amount("Zsa Zsa Gabor", "forty dollars", db) == (db, False)


# test format_report()
# test table heading
def test_format_report_1():
    db = {"Fred Flinstone": [56.40, 2, 130]}
    heading = "| {dn:<20s}\t| {tg:<15s}\t| {ng:<10s} | {ag:<15s}   |".format
    assert mailroom.format_report(db)[0] == heading(dn="Donor Name", tg="Total Given",
                                                    ng="Num Gifts", ag="Average Gift")


# test row formatting
def test_format_report_2():
    db = {"Marge Simpson": [150.34, 1, 150.34],
          "Fred Flinstone": [56.40, 2, 130],
          "Scooby": [10, 5, 15]}
    row = "{dn:<20s} \t {ds:<1s} {tg:>14.2f} \t " \
          "{ng:>10d} \t {ds2:<1} {ag:>14.2f} ".format
    assert mailroom.format_report(db)[2] == row(dn="Marge Simpson", ds="$", tg=150.34,
                                                ng=1, ds2="$", ag=150.34)


# test send_letters
def test_send_letters():
    db = {"Marge Simpson": [150.34, 1, 150.34],
          "Fred Flinstone, III": [56.40, 2, 130],
          "Scooby": [10, 5, 15]}
    mailroom.send_letters(db)
    assert os.path.isfile("Marge_Simpson.txt")
    assert os.path.isfile("Fred_Flinstone_III.txt")
    assert os.path.isfile("Scooby.txt")


# test letter_text()
def test_letter_text():
    donor_info = ("Marge Simpson", 150.43)
    text = mailroom.letter_text(*donor_info)
    expected = """
    Dear Marge Simpson,
    Thank you for your collective contributions of $150.43 over the years.
    Your generous donations have been put to good use!
    Sincerely,
    Kyle at Kelby Doggo, Inc\n"""
    assert text == expected
