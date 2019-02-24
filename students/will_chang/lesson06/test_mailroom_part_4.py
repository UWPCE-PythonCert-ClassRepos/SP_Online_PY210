#!/usr/bin/env python

from mailroom_part_4 import find_max_len_str, list_data, active_names, name_prompt, update_donor_list, thank_you, write_letter
import datetime
import os.path
import pathlib

def test_1():
    test_database = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
    ]
    assert find_max_len_str(test_database) == [14, 10, 1, 8]  # Note: Float will be represented with only one trailing zero after decimal point


def test_2():
    another_database = [
    ["Here is a long test string", .257, 15, 1],
    ["Jim", 150.35, 3000000, 2]
    ]
    assert find_max_len_str(another_database) == [26, 6, 7, 1]


def test_3():
    test_database = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
    ]
    assert active_names(test_database) == ["George Clooney", "Jack Bogle", "Orville Wright", "Warren Buffett", "William Boeing"]
    
    
def test_4():
    test_database = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
    ]
    assert update_donor_list(["George Clooney", 10000.00, 2, 5000.00], 2000) == ["George Clooney", 12000.0, 3, 4000.0]
    assert update_donor_list(["Jack Bogle", 15000.50, 1, 15000.50], .50) == ["Jack Bogle", 15001, 2, 7500.5]
    
    
def test_5():
    test_database = [
    ["Warren Buffett", 650.00, 2, 325.00],
    ["Jack Bogle", 15000.50, 1, 15000.50],
    ["William Boeing", 450.45, 3, 150.15],
    ["George Clooney", 10000.00, 2, 5000.00],
    ["Orville Wright", 95000000.00, 1, 950000.00]
    ]
    write_letter()
    current = datetime.datetime.now()
    abs_path = pathlib.Path('./').absolute()
    final_path = os.path.join(abs_path, "letter_storage/")
    assert "Orville Wright_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")
    assert "Warren Buffett_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")
    assert "Jack Bogle_{:02}_{:02}_{:02}.txt".format(current.month, current.day, current.year) in os.listdir("letter_storage")