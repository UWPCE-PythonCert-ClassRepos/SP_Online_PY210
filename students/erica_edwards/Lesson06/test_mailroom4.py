#!/usr/bin/env python
import pytest
import mailroom4
import os

email_path = "C:\\Users\\erica\\Desktop\\python210\\SP_Online_PY210\\students\\erica_edwards\\"
donors = {'Sandy Pie': [75],
          'Judy Smith': [75, 100, 1000],
          'Mike Jones': [75, 1000],
          'Joe Smith': [75, 100, 2000],
          'Kelly Blue': [75, 150, 275]}


def test_donation():
    given = {'name': [100, 1000, 10000]}
    mailroom4.donation('name', given, '23')
    assert len(given['name']) == 4
    assert sum(given['name']) == 11123


def test_create_report():
    given = [('name', 1, 2, 3.45)]
    expected = ("\nDonor Name                | Total Given | Num Gifts | Average Gift\n"
                "------------------------------------------------------------------\n"
                "name                       $       1.00           2  $       3.45\n")
    actual = mailroom4.create_report(given)
    assert actual == expected


def test_list_donors():
    given = {'top': [1, 2], 'bottom': [3, 4]}
    expected = 'top\nbottom\n'
    assert mailroom4.list_donors(given) == expected


def test_totals():
    given = {'name': [120, 3.45]}
    expected = [('name', 123.45, 2, 61.725)]
    assert mailroom4.totals(given) == expected


def test_generate_letter():
    given = {'donor_name': 'name', 'total': 123.45}
    expected = 'Thank you name. You have donated a total of $123.45. We appreciate your generous support for our club.'
    assert mailroom4.generate_letter(given) == expected


def test_multi_thanks():
    donor_count = len(donors)
    mailroom4.multi_thanks(donors)
    donor_file_count = len([x for x in os.listdir(email_path) if x.endswith('.txt')])
    assert donor_file_count == donor_count


def test_send_thank_you():
    expected = 'Thank you name for your donation of $123.45. We appreciate your generous support of our club.\n'
    assert mailroom4.send_thank_you('name', 123.45) == expected

