#!/usr/bin/env python3

"""Test code for mailroom_oo.py.

"""

from donor_models import *
import cli_main
import pytest

#tests for donor_models.py
def test_name():
    n = Donor("Harry Potter", 42)
    print(n.name)
    
    assert n.name == "Harry Potter"

def test_donation():
    d = Donor("Harry Potter", 42)
    
    print(d.donor_info)
    print(d.donation)
    
    assert d.donation == 42

def test_new_donation():
    n = Donor("Harry Potter", 31)
    n.new_donation = 42
    
    print(n.donor_info)
    print(n.new_donation)
    
    assert n.donation == 42

def test_total_donations():
    n = Donor("Harry Potter", 42)
    n.new_donation = 32
    n.new_donation = 78
    
    print(n.donor_info)
    print(n.total_donations)
    
    assert n.total_donations == 3

def test_total_amount():
    a = Donor("Harry Potter", 42)
    a.new_donation = 32
    a.new_donation = 78
    
    print(a.donor_info)
    print(a.total_amount)
    
    assert a.total_amount == 152

def test_avg_amount():
    a = Donor("Harry Potter", 42)
    a.new_donation = 32
    a.new_donation = 78
    
    print(a.total_amount)
    print(a.avg_amount)
    
    assert a.avg_amount == 50.67

def test_thank_you():
    t = Donor("Harry Potter", 42)
    
    print(t.thank_you)
    
    assert t.thank_you == "Thank you, Harry Potter, for your generous donation of $42.00."

def test_report():
    r = Donor("Harry Potter", 42)
    r.new_donation = 12
    r.new_donation = 5
    r.new_donation = 100
    
    print(r.donor_info)
    print(r.report)
    
    assert r.report == 'Donor Name                     |         Total Given |      Num Gifts |       Average Gifts'