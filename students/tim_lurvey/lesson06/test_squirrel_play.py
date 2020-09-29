#!/usr/bin/env python
from squirrel_play import squirrel_play

def test_01():
    assert squirrel_play(70, False) is True


def test_02():
    assert squirrel_play(95, False) is False


def test_03():
    assert squirrel_play(95, True) is True

