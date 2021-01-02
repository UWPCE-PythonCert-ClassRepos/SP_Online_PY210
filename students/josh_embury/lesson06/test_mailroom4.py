#!/usr/bin/env python
#-----------------------------------------------#
# Testing for Send Thank You:
#-----------------------------------------------#
from mailroom4 import add_new_donor
test_dict = {'test_name':[100,200,300]}
def test_1():
    add_new_donor(test_dict, 'test_name', 7)
    assert len(test_dict.keys()) == 1
    assert sum(test_dict['test_name']) == 607
def test_2():
    add_new_donor(test_dict, 'test_name2', 900)
    assert len(test_dict.keys()) == 2
    assert sum(test_dict['test_name2']) == 900

from mailroom4 import list_donors
def test_3():
    assert list_donors(test_dict) == ['test_name', 'test_name2']
#-----------------------------------------------#
# Testing for Create Report:
#-----------------------------------------------#
from mailroom4 import get_report
def test_4(): # Check if report is sorted
    lst_report_rows = [variable.split() for variable in get_report()]
    lst_report_rows.pop(0) # remove header
    lst_report_rows.pop(0) # remove format line
    lst_total_donations = [float(variable[3]) for variable in lst_report_rows]
    lst_total_donations.reverse()
    assert sorted(lst_total_donations) == lst_total_donations
#-----------------------------------------------#
# Testing for Send Letters:
#-----------------------------------------------#
from mailroom4 import write_to_file
def test_5():
    import os.path
    write_to_file(test_dict)
    assert os.path.isfile('test_name.txt') == True

from mailroom4 import thank_you_letter
def test_6():
    expected = 'Dear Mr. Blitzen,\n'\
    '    Thank you so much for the generous gift of 500 dollars. '\
    'This donation is going to help us so much for so many reasons. '\
    'You are incredibly nice and are obviously an outstanding person.\n'\
    '    If you are able to make any further donations please feel free '\
    'to access the Python Donation console application. \n'\
    'Sincerely,\n'\
    'The Python Development Team'
    assert thank_you_letter('Mr. Blitzen', 500) == expected
