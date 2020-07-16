#!/usr/bin/env python3

"""Test code for mailroom_oo.py.

"""

import os
from donor_models import *
import pytest

#tests for class Donor()
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


#tests for class Donor_Collection()
def test_donor_objects():
    p = Donor("Harry Potter", 42)
    g = Donor("Hermione Granger", 41)
    w = Donor("Ron Weasley", 43)
    trio = Donor_Collection(p, g, w)
    
    assert str(trio.donor_objects) == "{'Harry Potter': Donor(Harry Potter: [42]), 'Hermione Granger': Donor(Hermione Granger: [41]), 'Ron Weasley': Donor(Ron Weasley: [43])}"
    
def test_add_donor():
    p = Donor("Harry Potter", 42)
    g = Donor("Hermione Granger", 41)
    w = Donor("Ron Weasley", 43)
    trio = Donor_Collection(p, g, w)
    print(trio.donor_objects)
    
    trio.add_donor_object(Donor("Draco Malfoy", 42))
    print(trio.donor_objects)
    
    assert str(trio.donor_objects) == "{'Harry Potter': Donor(Harry Potter: [42]), 'Hermione Granger': Donor(Hermione Granger: [41]), 'Ron Weasley': Donor(Ron Weasley: [43]), 'Draco Malfoy': Donor(Draco Malfoy: [42])}"
    
def test_list_all_donors():
    p = Donor("Harry Potter", 42)
    g = Donor("Hermione Granger", 42)
    w = Donor("Ron Weasley", 42)
    trio = Donor_Collection(p, g, w)
    
    print(trio.list_all_donors())
    
    assert trio.list_all_donors() == "Harry Potter\nHermione Granger\nRon Weasley"

def test_find_donor():
    p = Donor("Harry Potter", 42)
    g = Donor("Hermione Granger", 42)
    w = Donor("Ron Weasley", 42)
    trio = Donor_Collection(p, g, w)
    
    print(trio.donor_objects)
    trio.find_donor("Draco Malfoy")
    trio.find_donor("Harry Potter")
    
    print(trio.find_donor("Draco Malfoy"))
    print(trio.find_donor("Harry Potter"))
    
    assert "Draco Malfoy" not in trio.donor_objects
    assert trio.find_donor("Draco Malfoy") == "Draco Malfoy is not a current donor."
    assert repr(trio.find_donor("Harry Potter")) == "Donor(Harry Potter: [42])"

def test_donor_updates():
    
    p = Donor("Harry Potter", 42)
    g = Donor("Hermione Granger", 41)
    w = Donor("Ron Weasley", 43)
    
    trio = Donor_Collection(p, g, w)
    trio.donor_letters()
    
    h_letter = os.path.exists(f"./{'Harry Potter'}.txt")
    g_letter = os.path.exists(f"./{'Hermione Granger'}.txt")
    
    assert os.path.exists(h_letter)
    assert os.path.exists(g_letter)

def test_report():
    r = Donor("Harry Potter", 42)
    r.new_donation = 12
    r.new_donation = 5
    r.new_donation = 100
    
    g = Donor("Hermione Granger", 42)
    g.new_donation = 20
    
    w = Donor("Ron Weasley", 42)
    
    trio = Donor_Collection(r, g, w)
    print(trio.donor_objects)
    
    print(trio.report_header())
    print(trio.report_data())
    
    test_header = f"{'Donor Name':30} |{'Total Given':>20} |{'Num Gifts':>15} |{'Avg Gifts':>20}"
    test_header_border = '-' * len(test_header)
    test_donor_objects = (f"{'Harry Potter':30}  ${159:>19,.2f}  {4:>15}  ${39.75:>19,.2f}\n"
                        f"{'Hermione Granger':30}  ${62:>19,.2f}  {2:>15}  ${31.00:>19,.2f}\n"
                        f"{'Ron Weasley':30}  ${42:>19,.2f}  {1:>15}  ${42.00:>19,.2f}")
    
    assert trio.report_data() == test_donor_objects