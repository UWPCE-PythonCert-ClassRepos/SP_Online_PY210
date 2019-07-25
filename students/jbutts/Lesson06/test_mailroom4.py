#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import tempfile
from mailroom4 import *

#  Build our data structure to use in these tests

DONOR_DB = {}  # dict that contains user/donation records
DONOR_DB = populate_data(DONOR_DB)


'''
Lesson 6: Writing Unit Tests

'''


'''
Send Thank You tests
'''


def test_format_email():
    # test normal case for generating mail text
    assert format_email("James Butts", 100.00, 1000.00) == ''.join((
            "Dear James Butts,\n\n",
            "Thank you for your recent contribution of $100.00.\n\n",
            "We appreciate your generosity in support of our mission.\n\n",
            "Thank you for your lifetime contributions of $1000.00.\n\n"
            "Warmest Regards,\n\n",
            "Charity Staff\n"))

    # test for number formatting in mail text
    assert format_email("Joe Biden", 10000.9999, 1000.1) == ''.join((
            "Dear Joe Biden,\n\n",
            "Thank you for your recent contribution of $10001.00.\n\n",
            "We appreciate your generosity in support of our mission.\n\n",
            "Thank you for your lifetime contributions of $1000.10.\n\n"
            "Warmest Regards,\n\n",
            "Charity Staff\n"))

#  Test add_contribution()

#  Add contribution for a new donor
def test_add_contribution():
    add_contribution("James Butts", 100, DONOR_DB)
    assert DONOR_DB["James Butts"][-1:] == [100]
    # Test that we are summing total contributions correctly
    assert sum(DONOR_DB["James Butts"]) == 100


    #  Pass a contribution to a recurring donor
    add_contribution("Daenerys Targaryen", 100, DONOR_DB)
    assert DONOR_DB["Daenerys Targaryen"][-1:] == [100]
    # Test that we are summing total contributions correctly
    assert sum(DONOR_DB["Daenerys Targaryen"]) == 8355.00

    # Pass multiple contributions to a recurring donor
    add_contribution("Daenerys Targaryen", [100, 200], DONOR_DB)
    assert DONOR_DB["Daenerys Targaryen"][-2:] == [100, 200]
    # Test that we are summing total contributions correctly for multiple contributions
    assert sum(DONOR_DB["Daenerys Targaryen"]) == 8655.00

# Test listing of donors
def test_list_donors():
    # Test formatting and sorting of the dictionary when listing donors
    assert str(list_donors(DONOR_DB)).split("\n")[0] == "No.  Name   "
    assert str(list_donors(DONOR_DB)).split("\n")[1] == "==== ======="
    assert str(list_donors(DONOR_DB)).split("\n")[2] == "1    Arya Stark"


'''
Create Report tests
'''

def test_show_donors():
    #  Check calculations
    #  Number of donations
    assert len(DONOR_DB["Melisandre"]) == 4
    #  Total donations
    assert sum(DONOR_DB["Melisandre"]) == 300019.00
    #  Average donation
    assert sum(DONOR_DB["Melisandre"])/len(DONOR_DB["Melisandre"]) == 75004.75

def test_get_donors_details():
    #  Check output and formating of get_donor_details()
    donor_list = get_donors_details(DONOR_DB)
    assert donor_list[1] == 'Arya Stark               $10899.92           5         $2179.98      \n'


'''
Send Letters tests
'''

#  Run the code in question to generate letters
send_letter_to_all(DONOR_DB)
file_to_test = tempfile.gettempdir() + "/James_Butts.txt"

def test_file_created():
    #  Make sure letters are getting created (written to temp)
    assert os.path.exists(file_to_test)



def test_get_letter_text():
    #  Check that the contents of the letter is what we expect
    letter_text = ""

    with open(file_to_test, "r") as letter_file:
        letter_text = letter_file.readlines()
        letter_text = "".join(letter_text)
    assert letter_text == ''.join(("Dear James Butts,\n\n",
        "Thank you for your recent contribution of $100.00.\n\n",
        "We appreciate your generosity in support of our mission.\n\n",
        "Thank you for your lifetime contributions of $100.00.\n\n",
        "Warmest Regards,\n\n",
        "Charity Staff\n"))

