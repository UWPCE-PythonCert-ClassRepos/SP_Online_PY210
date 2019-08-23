#!/usr/bin/env python3

import mailroom

def test_1():
    assert mailroom.format_letter('James K. Polk')[0:4] == "Dear"

def test_2():
    assert mailroom.format_letter('Martin van Buren', True)[0:4] == '\n\n\n\n' # if extra_whitespace is True, there should be extra linefeeds

def test_3():
    assert mailroom.format_letter('Abraham Lincoln') is False
