#!/usr/bin/env python3

import mailroom, os
from pathlib import Path

def test_1():
    # Validate that the letter is returned
    result = mailroom.format_letter('James K. Polk')
    for segment in mailroom.letter_template.split('{'):
        assert segment.split('}')[-1] in result

def test_2():
    # Validate presence of extra whitespace
    result = mailroom.format_letter('Martin van Buren', True)
    for segment in mailroom.letter_whitespace.format(mailroom.letter_template).split('{}'):
        assert segment.split('}')[-1] in result

def test_3():
    # Invalid donor should result in False retval
    assert mailroom.format_letter('Abraham Lincoln') is False

def test_4():
    # Add a key and an invalid donation
    assert mailroom.add_donor_record('Abraham Lincoln', 'not_a_float') is False

def test_5():
    # Add a key and a valid donation
    assert mailroom.add_donor_record('Abraham Lincoln', '8008.88') is True

def test_6():
    # Add a valid donation to an existing key
    assert mailroom.add_donor_record('James K. Polk', '7007.77') is True

def test_7():
    # Add an invalid donation to an existing key
    assert mailroom.add_donor_record('James K. Polk', 'not_a_float') is False

def test_8():
    # Abraham Lincoln should be a valid key now thanks to test 5, so we should get a valid letter
    result = mailroom.format_letter('Abraham Lincoln')
    for segment in mailroom.letter_template.split('{'):
        assert segment.split('}')[-1] in result

def test_9():
    # The report output list should have n + h elements, where n = donors and h = header rows (2)
    assert len(mailroom.generate_report()) == len(mailroom.donors) + 2

def test_10():
    # Test letter directory creation
    global letter_dir
    letter_dir = mailroom.create_letter_dir('.')
    assert os.path.exists(letter_dir)

def test_11():
    # Test saving letter for a valid donor
    global letter_dir, letter
    letter = mailroom.save_letter(letter_dir, 'Abraham Lincoln')
    assert os.path.exists(letter)

def test_12():
    # Test saving letter for an invalid donor
    global letter_dir
    assert mailroom.save_letter(letter_dir, 'Theodore Roosevelt') == False

def test_13():
    # Check content of letter created in test_11
    global letter
    with letter.open("r") as fileio:
        assert fileio.read() == mailroom.format_letter('Abraham Lincoln')
