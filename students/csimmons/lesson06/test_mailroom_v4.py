#!/usr/bin/env python

import mailroom_v4 as mail
import pathlib
import os

test_info = {
    'Mary Newcomer' : [10000, 2500, 300],
    'Christine Ruotolo' : [3000, 6000, 750, 20000],
    'Martin Acevedo' : [2000, 5000],
    'Sutton Keaney' : [24500, 500, 3000, 5000, 1000],
    'David Basilio' : [750, 750, 750, 750, 5000, 750, 750],
    'Andrew Laughlin' : [2500, 500, 40000, 50],
    'Hussein Saffouri' : [1000, 1000, 2100, 7000, 55000],
    }

def test_create_dir():
    directory = 'letters'
    dir_exists = os.path.isdir(directory)
    assert dir_exists == True

'''

def test_get_letter_text():
    expected = "Frank, thanks a lot!"
    assert get_letter_text("Frank") == expected


def test_2():
    assert write_files(50, False) is True


def test_3():
    assert batch_thanks(70, True) is True


def test_4():
    assert find_donor(30, True) is False


def test_5():
    assert add_donor(50, True) is True


def test_6():
    assert update_donor(60, False) is True


def test_7():
    assert list_donors(61, False) is False


def test_8():
    assert create_report(40, False) is True


def test_9():
    assert print_data(39, False) is False


def test_10():
    assert program_exit(40, True) is True


def test_11():
    assert menu_select(39, True) is False
'''
