#!/usr/bin/env python3

from squirrel_play import squirrel_play

def test_1():
    assert squirrel_play(70, False) is True


def test_2():
    assert squirrel_play(95, False) is False


def test_3():
    assert squirrel_play(95, True) is True


def test_4():
    assert squirrel_play(90, False) is True


def test_5():
    assert squirrel_play(90, True) is True


def test_6():
    assert squirrel_play(50, False) is False


def test_7():
    assert squirrel_play(50, True) is False


def test_8():
    assert squirrel_play(100, False) is False


def test_9():
    assert squirrel_play(100, True) is True


def test_10():
    assert squirrel_play(105, True) is False


def test_11():
    assert squirrel_play(59, False) is False


def test_12():
    assert squirrel_play(59, True) is False


def test_13():
    assert squirrel_play(60, False) is True