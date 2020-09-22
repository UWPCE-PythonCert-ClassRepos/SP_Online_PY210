#!/usr/bin/env python3

"""
test code for Mailroom

Different scenarios to test:
Thank you:
    Old Donor New Gift
        Pass existing donor
    New Donor New gift
        Pass new gift
        pass gift value

Create report
    create report
    print report

Send Letters
    Body of letters
    Letters are created
"""


# you can change this import to test different versions
from Mailroom import receiver, quit, donors, gift

def test_1():
    assert quit() == "quit"

def test_2():
    assert "Andrew Carnegie" in donors.keys()


