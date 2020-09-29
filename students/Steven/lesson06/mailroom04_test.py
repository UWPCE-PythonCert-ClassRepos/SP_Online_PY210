#! bin/user/env python3

import mailroom04 as mailroom
import os.path
'''
Unit testing for mailroom code
'''

def test_donor_list():
    donor_list = mailroom.donor_list
    assert donor_list['John Doe'] == [2000, 2]
    assert donor_list['Jane Doe'] == [3000, 3]

def test_update_donor_list():
    donor_table = mailroom.update_donor_list('Tony Stark', 101)
    donor_table2 = mailroom.update_donor_list('Andrew Jackson', 200)
    assert donor_table['Tony Stark'] == [101, 1]
    assert donor_table2['Andrew Jackson'] == [220, 3]

def test_thank_you_letter():
    test_letter = "Thank you George Washington for your generous donation of $1.00, your kindness is very appreciated." + "\n"
    assert mailroom.thank_you_letter('George Washington', 1) == test_letter

def test_get_report():
    report = mailroom.get_report
    assert mailroom.get_report == report

def test_all_letters():
    mailroom.all_letters()
    assert os.path.isfile('thank_you_benjamin franklin.txt')

if __name__== "__main__":

    test_donor_list()
    test_update_donor_list()
    test_thank_you_letter()
    test_get_report()
    test_all_letters()
    print("Mailroom unit tests have all passed")