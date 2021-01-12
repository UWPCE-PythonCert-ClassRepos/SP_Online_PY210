#!/usr/bin/env python

import mailroom_v4 as mail
import pathlib
import os
from io import StringIO

test_dict = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

test_info = [
                ['Hussein Saffouri', 66100.00, 5, 13220.00],
                ['Andrew Laughlin', 43050.00, 4, 10762.50],
                ['Sutton Keaney', 34000.00, 5, 6800.00],
                ['Christine Ruotolo', 29750.00, 4, 7437.50],
                ['Mary Newcomer', 12800.00, 3, 4266.67],
                ['David Basilio', 9500.00, 7, 1357.14],
                ['Martin Acevedo', 7000.00, 2, 3500],
                ]

def test_create_report():
    all_info = mail.create_report()
    for i in range(len(test_info)):
        expected = list(test_info[i])
        created = list(all_info[i])
        created[1] = round(created[1], 2)
        created[3] = round(created[3], 2)
        assert expected == created

def test_create_dir():
    directory = 'letters'
    mail.create_dir()
    dir_exists = os.path.isdir(directory)
    assert dir_exists == True

def test_write_files():
    mail.write_files('Jane_Doe.txt', 'Jane Doe', 1000)
    assert os.path.exists('Jane_Doe.txt') == True

def test_batch_thanks():
    file_names = ['Mary_Newcomer.txt', 'Christine_Ruotolo.txt', 'Martin_Acevedo.txt', 'Sutton_Keaney.txt', 'David_Basilio.txt', 'Andrew_Laughlin.txt', 'Hussein_Saffouri.txt']
    mail.batch_thanks()
    for file in file_names:
        file = 'letters/' + file
        assert os.path.exists(file)

def test_list_donors():
    mail.list_donors()
    expected = list(test_dict.keys())
    names = list(mail.donorlist_dict.keys())
    assert expected.sort() == names.sort()

def test_add_donor(monkeypatch):
    donor_name = 'Elvis Costello'
    gift = StringIO('1111.11')
    monkeypatch.setattr('sys.stdin', gift)
    mail.update_donor(donor_name)
    expected = list(mail.donorlist_dict.keys())
    donate = mail.donorlist_dict[donor_name][-1]
    assert donor_name in expected
    assert donate == 1111.11

def test_update_donor(monkeypatch):
    donor_name = 'Hussein Saffouri'
    gift = StringIO('666.66')
    monkeypatch.setattr('sys.stdin', gift)
    mail.update_donor(donor_name)
    expected = list(mail.donorlist_dict.keys())
    donate = mail.donorlist_dict[donor_name][-1]
    assert donor_name in expected
    assert donate == 666.66




