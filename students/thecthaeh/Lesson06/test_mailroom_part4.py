#!/usr/bin/env python

""" Test code for mailroom.py.

You can change this import to test different versions starting from mailroom_part4.
"""

from mailroom_part4 import mailroom_part4
# from mailroom_part4 import walnut_party5 as mailroom_part4
# from mailroom_part4 import walnut_party6 as mailroom_part4

#unit tests should test the data manipulation logic code: generating thank you text, adding or updating donors, and listing donors.

#generating thank you letter
def test_thank_you(donor):
    donor = "Jim Newton"
    donation = 600.00
    assert letter == "Dear Jim Newton,\n\nThank you for your donation of $600.00. Your generosty will help us fulfill our plans for the coming year.\n\nThank you!\nThe Team\n"

#adding or updating donors
def test_update_donor(donor, donation)
    #test for an existing donor
    donor = "Grant Hugh"
    donation = 12,000.00
    assert donor_history["Grant Hugh"] == 12,000.00
    
    #test for a new donor
    donor = "Benny Hana"
    donation = 4250.67
    assert donor_history["Benny Hana"] == 4250.67

#listing donors
def test_list_donors():
    menu_select = "list"
    