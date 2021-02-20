#!/usr/bin/env python
"""
John Hunter
Lesson 6
Mailroom4 Unit Test
"""

import os.path
import pathlib
import mailroom4

#test donors
DONORS =	{'Tank Ferriwhether' : [10, 15, 100], 'tommy train' : [5, 17, 23],
          'stefanie terrace' : [31, 48, 108], 'samuel robert': [4, 90, 101],
          'sandra cone' : [29, 41, 70], 'shioban roy' : [2, 23000, 19]}
"""
EXPECTED_DONORS = str("List of Current Donors"
                      "Tank Ferriwhether\n"
                      "tommy train\n"
                      "stefanie terrace\n"
                      "samuel robert\n"
                      "sandra cone\n"
                      "shioban roy\n")
"""
EXPECTED_TEXT = str("Dear Tank Ferriwhether,\n\n"
                    "Thank you for your generous donation(s) of $125.\n\n"
                    "Sincerly,\n"
                    "John Hunter\n")


EXPECTED_ORDER = {'shioban roy' : [2, 23000, 19], 'samuel robert': [4, 90, 101],
                  'stefanie terrace' : [31, 48, 108], 'sandra cone' : [29, 41, 70],
                  'Tank Ferriwhether' : [10, 15, 100], 'tommy train' : [5, 17, 23]}

def test_donor_list_format():
    """
    test the return of values needed to format donor list
    """
    assert mailroom4.donor_list_format(DONORS) == [17, ['Tank Ferriwhether',\
    'tommy train', 'stefanie terrace', 'samuel robert', 'sandra cone', 'shioban roy']]

def test_email():
    """
    test generated email text against the expected text
    """
    assert mailroom4.email_text\
    (str(list(DONORS.keys())[0]), sum(DONORS['Tank Ferriwhether'][:])) == EXPECTED_TEXT

def test_saved_emails():
    """
    Test that all thank you emails are saved in the directory
    file names are derived from the original DONORS dict from the mailroom3 script
    """
    mailroom4.save_emails()
    dirpath = pathlib.Path('./').absolute()
    saved_email_1 = os.path.join(dirpath, "frank merriweather.txt")
    saved_email_2 = os.path.join(dirpath, "thomas tran.txt")
    saved_email_3 = os.path.join(dirpath, "stephanie terrance.txt")
    saved_email_4 = os.path.join(dirpath, "sam robidas.txt")
    saved_email_5 = os.path.join(dirpath, "sandy cohen.txt")
    saved_email_6 = os.path.join(dirpath, "shioban kemp.txt")
    assert os.path.exists(saved_email_1)
    assert os.path.exists(saved_email_2)
    assert os.path.exists(saved_email_3)
    assert os.path.exists(saved_email_4)
    assert os.path.exists(saved_email_5)
    assert os.path.exists(saved_email_6)

if __name__ == "__main__":
    #test_add_donations()
    #print("Add Donations Test Pass")
    test_email()
    print("Email Test Pass")
    test_donor_list_format()
    print("Donor List Format Pass")
    test_saved_emails()
    print("All Tests Pass")
