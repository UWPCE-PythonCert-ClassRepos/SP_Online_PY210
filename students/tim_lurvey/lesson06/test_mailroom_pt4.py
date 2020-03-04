#!/usr/bin/env python
__author__ = 'Timothy Lurvey'
from mailroom_pt4 import *


def test_RunningTotal_init():
    d = RunningTotal(new_key="Tex Johnson", )
    assert d.key == "Tex Johnson"
    assert d.total == 0.
    assert isinstance(d.total, float)
    assert d.count == 0
    assert isinstance(d.count, int)


def test_RunningTotal_init2():
    d = RunningTotal(new_key="Tex Johnson", total=99)
    assert d.key == "Tex Johnson"
    assert d.total == 99.0
    assert isinstance(d.total, float)
    assert not isinstance(d.total, int)


def test_RunningTotal_init3():
    d = RunningTotal(new_key="Tex Johnson", total=99, count=9)
    assert d.count == 9
    assert not isinstance(d.count, float)
    assert isinstance(d.count, int)


def test_RunningTotal_func():
    d = RunningTotal(new_key="Tex Johnson", total=99, count=9)
    d.add_to_total(1.)
    assert d.total == 99.0 + 1.0
    assert d.count == 10
    assert d.average == 10

def test_RunningTotal_repr():
    d = RunningTotal(new_key="Tex Johnson", total=99, count=9)
    assert repr(d) == "RunningTotal('Tex Johnson', 99.0, 9)"
    assert eval(repr(d)) == d

# data setup
dl = [RunningTotal('x', 10, 2),
      RunningTotal('y', 10, 2),
      RunningTotal('z', 40, 3),
      RunningTotal('x', 40, 3),
      ]


def test_get_name_matches():
    # test
    m = get_name_matches(name='x', data=dl)
    assert len(m) == 2
    assert [o.key for o in m] == ['x', 'x']


def test_add_new_name():
    d2 = []
    #
    add_new_name(new_name='rookie', data=d2)
    assert len(d2) == 1
    assert d2[0].key == 'rookie'


def test_get_data_object():
    o = get_data_object(key='y', data=dl)
    assert o.key == 'y'
    assert id(dl[1]) == id(o)


def test_compose_email():
    m1 = """
Hello y,

Your 2 donations, totaling $ 10.00, are greatly appreciated.

Thank you

"""
    o = get_data_object(key='y', data=dl)
    email = compose_email(name=o.key, data=dl)
    assert email == m1


def test_compose_email2():
    m2 = """
Hello y,

Thank you for your generous donation of $ 123.45.
Your 3 donations, totaling $ 133.45, are greatly appreciated.

Thank you

"""
    o = get_data_object(key='y', data=dl)
    email = compose_email(name=o.key, new_donation=123.45, data=dl)
    assert email == m2


def test_header():
    h = """
Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
"""
    assert report_header() == h


def test_report_line():
    test_l = report_data_line()
    assert test_l == "dafualt key               |       $ 0.00|          1|       $ 0.00\n"


def test_report_line2():
    o = get_data_object(key='z', data=dl)
    test_l = report_data_line(o.key, o.total, o.count)
    assert test_l == 'z                         |      $ 40.00|          3|      $ 13.33\n'

def test_write():
    path = os.path.expanduser("~/Desktop/")
    o = get_data_object(key='z', data=dl)
    write_letter_to_path(pathx=path,
                         name=o.key,
                         message=compose_email(name=o.key,
                                               new_donation=1,
                                               data=dl),
                         )
    new_file = os.path.join(path,"thank_you_z.txt")
    assert os.path.exists(new_file)
