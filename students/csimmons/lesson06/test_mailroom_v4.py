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

file_info = [
                ['Count_Dracula.txt','Count Dracula', 10000 ],
                ['Count_Chocula.txt','Count Chocula', 50000 ],
                ['Mr_Nosferatu.txt','Mr Nosferatu', 30000 ],
                ['Count_Yorga.txt','Count Yorga', 45000 ],
                ]

def test_create_dir():
    directory = 'letters'
    dir_exists = os.path.isdir(directory)
    mail.create_dir()
    assert dir_exists == True

def test_write_files():
    mail.write_files('Jane_Doe.txt', 'Jane Doe', 1000)
    assert os.path.exists('Jane_Doe.txt') == True

def test_write_multi_files():
    for info in range(len(file_info)):
        a = file_info[info][0]
        b = file_info[info][1]
        c = file_info[info][2]
        mail.write_files(a, b, c)
        assert os.path.exists(a) == True

'''
    mail.write_files('Jane_Doe.txt', 'Jane Doe', 1000)
    assert os.path.exists('Jane_Doe.txt') == True


def test_file_save():
    test_dict = create_test_dict()
    td = os.getcwdb()
    for person, donations in test_dict.items():
        save_file(person, donations, td)

#checks to see if the file was created properly
def test_file_created():
    name = 'Bill Gates'
    test_message = 'This is a test'
    mail.write_file(name,test_message)
    fname = 'Bill Gates.txt'

    assert os.path.isfile(fname) is True

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
