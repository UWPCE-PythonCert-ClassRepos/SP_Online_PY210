#!/usr/bin/env python

from mailroom_Part_4 import send_thankyou
from mailroom_Part_4 import list_donor

def test_1():
    assert list_donor() == donorlist.keys()