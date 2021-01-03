#!/usr/bin/env python
#-------------------------------------------#
#Tittle: test_mailroom_part_04, PYTHON210 - Assignment 05
#Desc: Test Harness for Mailroom Part 4
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Dec-13>, Created file
#Brent Kieszling, <2020-Dec-19>, Wrote tests 3-15
#Brent Kieszling, <2020-Dec-20>, Wrote tests 1 and 2
#-------------------------------------------#
import os
import pickle
#DATA---------------------------------------




#PROCESS------------------------------------




#PRESENTATION INPUT/OUTPUT------------------




from mailroom_part_04 import create_thank_you_file, new_donor,save_donors, load_donors,\
    update_donors, find_donor, thank_you, display_donors,donor_sort, display_report

def test_1():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    create_thank_you_file(test_donors)
    assert os.path.exists("John_Doe.txt") and os.path.exists("Jane_Doe.txt")
    
def test_2():
    test_donors = [{"Name": "JohnDoe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1}]
    create_thank_you_file(test_donors)
    assert os.path.exists("JohnDoe.txt")

def test_3():
    test_donor = {"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1}
    assert new_donor("John Doe", 100.00) == test_donor

def test_4():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    test_save_file = "Test_in.dat"
    save_donors(test_donors, test_save_file)
    assert os.path.exists(test_save_file)

def test_5():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    test_save_file = "Test_out.dat"
    with open(test_save_file, 'wb') as fileObj:
        pickle.dump(test_donors, fileObj)
    check_donors = load_donors(test_save_file)
    assert test_donors == check_donors

def test_6():
    test_donors = []
    test_save_file = ""
    check_donors = load_donors(test_save_file)
    assert test_donors == check_donors

def test_7():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    expected_update_donors = [{"Name": "John Doe", "Donation": [100.00, 100.00], "Total": 200.00, "Average": 100.00, "Gifts": 2},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    check_donors = update_donors(test_donors, "John Doe", 100.00)
    assert check_donors == expected_update_donors

def test_8():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    expected_update_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    check_donors = update_donors(test_donors, "Doe", 100.00)
    assert check_donors == expected_update_donors

def test_9():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    test_donor_name = "John Doe"
    check_donor = find_donor(test_donors, test_donor_name)
    expected_donor = {"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1}
    assert expected_donor == check_donor

def test_10():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
               {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    test_donor_name = ""
    check_donor = find_donor(test_donors, test_donor_name)
    expected_donor = None
    assert expected_donor == check_donor

def test_11():
    expected_thank_you_letter = """
    Dear John Doe,
    
    Thank you for your most recent donation of $100.00. We are humbled by your 
    lifetime contribution of $100.00.
    
    Sincerly,
    Making Good Things Happen"""
    test_donor = {"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1}
    check_thank_you = thank_you(test_donor)
    assert expected_thank_you_letter == check_thank_you


def test_12():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    check_donor_names = display_donors(test_donors)
    expected_donor_name_response = "John Doe\nJane Doe\n"
    assert check_donor_names == expected_donor_name_response
    
def test_13():
    test_donors = []
    check_donor_names = display_donors(test_donors)
    expected_donor_name_response = ""
    assert check_donor_names == expected_donor_name_response

def test_14():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    check_donors = donor_sort(test_donors)
    assert check_donors[0]["Name"] == "Jane Doe"

def test_15():
    test_donors = [{"Name": "John Doe", "Donation": [100.00], "Total": 100.00, "Average": 100.00, "Gifts": 1},
                   {"Name": "Jane Doe", "Donation": [200.00], "Total": 200.00, "Average": 200.00, "Gifts": 1}]
    expected_report = """==================== Donor Report: ==========================
Donor Name           | Total Given | Num Gifts | Average Gift
John Doe             $ 100.00           1      $     100.00
Jane Doe             $ 200.00           1      $     200.00
==============================================================
"""
    check_report = display_report(test_donors)
    assert expected_report == check_report






