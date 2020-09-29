#!/usr/bin/env python3

from mailroom_part4 import donation_table
from mailroom_part4 import list_donors, update_donation_table, email_text
from mailroom_part4 import get_report, send_letters_to_all, get_letter_text

import os.path


def test_list_donors():
    donor_list = list_donors(donation_table)
    assert donor_list[0] == "Bill Gates"
    assert donor_list[1] == "Mark Zuckerberg"
    assert donor_list[2] == "Jeff Bezos"
    assert donor_list[3] == "Paul Allen"
    assert donor_list[4] == "Jack Ma"


def test_update_donation_table():
    update_donation_table('Jack Ma', 5000.00)
    assert donation_table == {"Bill Gates": [40000.00, 50000.00, 9000.00],
                              "Mark Zuckerberg": [10000.00, 6500.00],
                              "Jeff Bezos": [1000.00, 40000.00, 7500.00],
                              "Paul Allen": [100000.00, 2000.00],
                              "Jack Ma": [15000.00, 77000.00, 5000.00]
                              }

    update_donation_table('John Chu', 10000.00)
    assert donation_table == {"Bill Gates": [40000.00, 50000.00, 9000.00],
                              "Mark Zuckerberg": [10000.00, 6500.00],
                              "Jeff Bezos": [1000.00, 40000.00, 7500.00],
                              "Paul Allen": [100000.00, 2000.00],
                              "Jack Ma": [15000.00, 77000.00, 5000.00],
                              "John Chu": [10000.00]
                              }


def test_email_text():
    email = email_text('aaa', 500)
    assert email == 'Dear Aaa,' + \
                    '\n\nThank you for your generous donation of $500.00.' + \
                    '\n\nSincerely,' + \
                    '\nThe Team'


def test_get_report():
    report = get_report()
    assert report[0] == 'Donor Name          |  Total Given | Num Gifts |   Average Gift'
    assert report[1] == '---------------------------------------------------------------'
    assert report[2] == 'Paul Allen           $   102000.00           2  $      51000.00'
    assert report[3] == 'Bill Gates           $    99000.00           3  $      33000.00'
    assert report[4] == 'Jack Ma              $    97000.00           3  $      32333.33'
    assert report[5] == 'Jeff Bezos           $    48500.00           3  $      16166.67'
    assert report[6] == 'Mark Zuckerberg      $    16500.00           2  $       8250.00'
    assert report[7] == 'John Chu             $    10000.00           1  $      10000.00'


def test_send_letters_to_all():
    send_letters_to_all()
    assert os.path.isfile('Paul_Allen.txt')
    assert os.path.isfile('Bill_Gates.txt')
    assert os.path.isfile('Jack_Ma.txt')
    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('Mark_Zuckerberg.txt')
    assert os.path.isfile('John_Chu.txt')


def test_get_letter_text():
    letter = get_letter_text('John Chu', 20000.00)
    assert letter == 'Dear John Chu,\n\n' + \
                     ' ' * 8 + 'Thank you for your kind donation of $20000.00.\n\n' + \
                     ' ' * 8 + 'It will be put to good use.\n\n' + \
                     ' ' * 25 + 'Sincerely\n' + ' ' * 28 + '-The Team'