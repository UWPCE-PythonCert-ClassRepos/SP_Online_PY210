import pytest
import os

from mailroom_part4 import *

def test_update_database_current():
    '''Confirm that a donation amount from a donor already in list gets
    properly appended to database'''
    update_database('Kurt Cobain', 1000)
    assert donor_db['Kurt Cobain'] == [25.00, 1000.00]


def test_update_database_new():
    '''Confirm that a donation amount for a new donor gets properly added to database'''
    update_database('Zach Thomson', 250)
    assert donor_db['Zach Thomson'] == [250.00]


def test_ty_letter():
    donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"
    assert donation_email.format('Kurt Cobain', 1000) == "\nDear Kurt Cobain,\nThank you for your generous donation of $1000.00!\n"


def test_create_table():
    '''Confirms entries from database are placed in a list'''
    test_list = create_table(donor_db)
    assert ('Dave Grohl', 50.0, 1, 50.0) in test_list
    assert ('Chris Cornell', 600.0, 2, 300.0) in test_list


def test_table_order():
    '''Confirms entries into list are then sorted in descending order'''
    test_list = create_table(donor_db)
    i = 0
    while i < len(test_list)-1:
        assert test_list[i][1] > test_list[i+1][1]
        i +=1

def test_letter_creation():
    """tests if send_letters creates a file in the current directory"""
    send_letters()
    for key in donor_db:
        assert os.path.basename(str(key) + '.txt') == (str(key) + '.txt')


def test_letter_content():
    """checks proper content in letter"""
    send_letters()
    expected = "Dear Dave Grohl,\n\n\tThank you for donating $50.00!\n\n\tThe kids will greatly appreciate it.\n\n\tSincerely,\n\t  -Our Team"
    with open('Dave Grohl.txt') as f:
        assert f.read() == expected
