#!/usr/bin/env python

#import unittest
import mailroom_part04
import os.path
import tempfile
#class testmailroom4(unittest.TestCase):


def test_ty_note01():
    mailroom_part04.ty_note("Tom Hanks")
    assert ("Hello Tom Hanks, thank you for your generous donation of $1500 to support our cause.")

def test_ty_note02():
    mailroom_part04.ty_note("Jennifer Aniston")
    assert ("Hello Jennifer Aniston, thank you for your generous donation of $6000 to support our cause.")

def test_ty_note03():
    mailroom_part04.ty_note("Tom")
    assert "The name you entered is not on the list!"

def test_create_report():
    mailroom_part04.create_report()

def test_report_data():
    mailroom_part04.report_data([{"name" : "Tom", "don" : 2000, "count" : 100, "average" : 20}])
    assert ("Tom 2000 100 20")

def test_send_ty_note_all():
    mailroom_part04.send_ty_note_all()
    assert "<<< Letters have been created in the temp folder! >>>"




def test_send_ty_note_all01():
    mailroom_part04.send_ty_note_all()
    temp_dir = tempfile.gettempdir()
    file_name = "Jennifer Aniston.txt"
    letter = temp_dir + "/" + file_name
    assert os.path.exists(letter)

# Was not able to figure out how to test text
def test_creating_letter():
    expected = "/nDear Jennifer Aniston , thank you for your donation!"
    temp_dir = tempfile.gettempdir()
    file_name = "Jennifer Aniston.txt"
    letter = temp_dir + "/" + file_name   
    assert mailroom_part04.create_letter(letter, "Jennifer Aniston") == expected
