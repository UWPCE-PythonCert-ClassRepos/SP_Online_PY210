#!/usr/bin/env python

""" Test code for mailroom.py.

You can change this import to test different versions starting from mailroom_part4.
"""
import os
from mailroom_part4 import *
# from mailroom_part4 import walnut_party5 as mailroom_part4
# from mailroom_part4 import walnut_party6 as mailroom_part4

#Tests for sending Thank You to single donor
#generating thank you letter
def test_thank_you():
    #tests an existing donor
    assert thank_you("Jim Newton") == "Thank you, Jim Newton, for your generous donation of $5.50."
    
    #tests a nonexistant donor
    assert thank_you("Bob Loble") == "This donor does not exist."

#adding or updating donors
def test_add_donor():
    #test for an existing donor: if the donor exists, the dict is unaltered
    x = donors.keys()
    add_donor("Grant Hugh")
    assert x == donors.keys()
    
    #test for a new donor: if the donor is new, the donor is added to the dict
    add_donor("Benny Hana")
    assert donors["Benny Hana"] == []

#listing donors
def test_list_donors():
    list = []
    for donor in donors: list.append(donor)
    assert list_donors() == "\n".join(list)

#Test for Creating a Report TODO
def test_report():
    test_donor = {'Noah Bunch': [5.00, 5.00], 'Pony Skittle': [10.00, 8.00, 3.00]}
    top_row = 'Donor Name                     |         Total Given |      Num Gifts |       Average Gifts'
    noah_row = ['Noah Bunch', 10.00, 2, 5.00]
    pony_row = ['Pony Skittle', 21.00, 3, 7.00]
    assert report(test_donor) == [top_row, [pony_row, noah_row]]

#Tests for Thank You text files
def test_text_file():
    #text_file(donors)
    #test file creation (one file per donor)
    for donor in donors:
        os.path.exists(f"./{donor}.txt")
    
    #test file content (correct text is generated)
    test_donor = {'Sarah Piper': [40.00]}
    test_letter_dict = {'name': "Sarah Piper", 'total': 40.00}
    test_letter = "Dear {name},\n\nYour total donations to date equal ${total:,.2f}.\n\nWe are grateful for your continued patronage and we can't wait to show you what your generosity will help us achieve.\n\nThank you!\nThe Team\n"
    
    expected = "Dear Sarah Piper,\n\nYour total donations to date equal $40.00.\n\nWe are grateful for your continued patronage and we can't wait to show you what your generosity will help us achieve.\n\nThank you!\nThe Team\n"
    assert test_letter.format(**test_letter_dict) == expected

if __name__ == "__main__":
    unittest.main()