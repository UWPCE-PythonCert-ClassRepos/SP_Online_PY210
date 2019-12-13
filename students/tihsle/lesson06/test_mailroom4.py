#!/usr/bin/env python3

from os import path
import pytest
import mailroom4 as mailroom

# Send Thank You Testing
def test_add_donor():
    donor = "Jack Sprat"
    donation = 10.50
    mailroom.add_donor(donor, donation)
    #print(mailroom.donors)
    #print(donation)
    assert donor in mailroom.donors
    assert float(donation) == mailroom.donors[donor][0]

def test_get_donor_list():
    strList = mailroom.get_donor_list()
    for d in mailroom.donors:
        assert d in strList

#Create Report testing

def test_create_report():
    for d in mailroom.donors:
        dname = d
        dtotal = sum(mailroom.donors[d])
        num_gifts = len(mailroom.donors[d])
        avg_gift = round(dtotal/num_gifts)
        strLine = mailroom.get_report_line(d)
        assert dname in strLine
        assert str(dtotal) in strLine
        assert str(num_gifts) in strLine
        assert str(avg_gift) in strLine

#Send Letters testing

#test file creation for
def test_send_letters():
    mailroom.send_letters()
    for d in mailroom.donors:
        file_name = f"{d}.txt"
        assert path.isfile(file_name)

def test_get_thankyou_text():
    expected = "Dear Paul Allen,"
    assert expected in mailroom.get_thankyou_text("Paul Allen")

test_add_donor()
test_get_donor_list()
test_create_report()
test_send_letters()
test_get_thankyou_text()
