#!/usr/bin/env python3

import mailroom

def test_1():
    # Validate that the letter is returned
    result = mailroom.format_letter('James K. Polk')
    for segment in mailroom.letter_template.split('{'):
        assert segment.split('}')[-1] in result

def test_2():
    # Validate presence of extra whitespace
    assert mailroom.format_letter('Martin van Buren', True)[0:4] == '\n\n\n\n'

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
