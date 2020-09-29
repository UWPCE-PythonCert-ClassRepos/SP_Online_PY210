#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: mailroom part 4, unit testing
# Description: unit testing
#
# <07/08/2020>, created unit testing
# ---------------------------------------------------------------------------- #
# imports
import sys
import pytest
import mailroompart4
import os.path


# Testing -------------------------------------------------------------------- #


def test_starter_donor_info():
    '''Verify the initial donor data is matching correctly'''
    donor_info = {"Jim Zorn": [3772.32, 1201.17],
                  "Jermaine Kearse": [877.33],
                  "Marcus Trufant": [1563.23, 1043.87, 1.32],
                  "K.J. Wright": [21663.23, 300.87, 100432.00],
                  "Curt Warner": [663.23, 300.87, 10432.00],
                  }
    assert mailroompart4.donor_info == donor_info


def test_new_donor_add():
    '''Test if new donor will be added to dictionary with name and donation amount'''
    donor_name = "Steve Largent"
    donor_amount = 500.00
    assert mailroompart4.new_donor_add(donor_name, donor_amount) == \
           {"Jim Zorn": [3772.32, 1201.17],
            "Jermaine Kearse": [877.33],
            "Marcus Trufant": [1563.23, 1043.87, 1.32],
            "K.J. Wright": [21663.23, 300.87, 100432.00],
            "Curt Warner": [663.23, 300.87, 10432.00],
            "Steve Largent": [500.00],
            }


def test_exist_donor():
    '''Test if existing donor will append donation amount to donor dictionary'''
    donor_name = "Jim Zorn"
    donor_amount = 1000.00
    assert mailroompart4.exist_donor(donor_name, donor_amount) == \
           {"Jim Zorn": [3772.32, 1201.17, 1000.00],
            "Jermaine Kearse": [877.33],
            "Marcus Trufant": [1563.23, 1043.87, 1.32],
            "K.J. Wright": [21663.23, 300.87, 100432.00],
            "Curt Warner": [663.23, 300.87, 10432.00],
            "Steve Largent": [500.00],
            }


def test_letter():
    '''Test to see if donor name and amount are reflected properly in thank you letter'''
    donor_name = 'Jim Zorn'
    donor_amount = 500
    assert mailroompart4.letter(donor_name, donor_amount) == '''Dear Jim Zorn,\n
Thank you for your recent donation of '$500' to XYZ Nonprofit for children! It really makes a huge impact for
the children in our community.\n
Those three hours after the end of the school day can make a crucial difference in kids’ lives.
Thanks to you, kids have a safe place to go after school. Instead of going home alone while their families are at work,
our kids are learning to play sports, create art, and improving their grades at our Homework Help Center.  All while
forming friendships with peers and relationships with adult mentors and tutors.\n
Thank you again Jim Zorn, for your ongoing support of our kids!\n
Sincerely,\n
XYZ Nonprofit Agency Director'''


def test_report_generator():
    '''Test for entries that are in report'''
    report_generator ='''
    | K.J. Wright        | $122,396.10 |      3      | $40,798.70  |
    | Curt Warner        | $11,396.10  |      3      | $3,798.70   |
    | Jim Zorn           | $5,973.49   |      3      | $1,991.16   |
    | Marcus Trufant     | $2,608.42   |      3      | $869.47     |
    | Jermaine Kearse    | $877.33     |      1      | $877.33     |
    | Steve Largent      | $500.00     |      1      | $500.00     |'''

    assert "Jim Zorn" in report_generator
    assert "122,396.10" in report_generator
    assert "Curt Warner" in report_generator
    assert "877.33" in report_generator
    assert "3" in report_generator
    assert "| Jermaine Kearse    | $877.33     |      1      | $877.33     |" in report_generator


def test_all_thank_you():
    '''Test to see if "thank you" files are being created'''
    mailroompart4.yes_response()
    assert os.path.exists("Jim Zorn.txt")
    assert os.path.exists("Jermaine Kearse.txt")
    assert os.path.exists("Marcus Trufant.txt")
    assert os.path.exists("K.J. Wright.txt")
    assert os.path.exists("Steve Largent.txt")
