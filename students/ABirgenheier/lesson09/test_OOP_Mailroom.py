#!/usr/bin/env python

from OOP_Mailroom_Donar_Model import Donar
from OOP_Mailroom_Donar_Model import DonarCollection
import os.path
import pathlib
import pytest

donar = DonarCollection()


def test_donars_history():
    """ Test donar name in the donar dictionary created """
    donar = Donar('Tony')
    assert donar.name == 'Tony'


def test_donars_list():
    """ Test all donar names are returned"""

    donar.add(Donar('Mike', [200.00]))
    donar.add(Donar('Sarah', [500.00]))
    assert 'Mike' in donar.list_of_donars()
    assert 'Sarah' in donar.list_of_donars()
    assert 'Mike\nSarah' in donar.list_of_donars()


def test_donation_update():
    donar = Donar('Sarah', [150.00])
    assert len(donar.donation_amt) == 1
    assert sum(donar.donation_amt) == 150.00


def test_thankyou_note():
    """ Test  Thank you Note """
    donar = Donar('Tony', [50])
    assert '50' in donar.print_thank_you_message()


def test_send_letters():

    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath, 'Mike.txt')
    file2 = os.path.join(dirpath, 'Sarah.txt')
    donar.send_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)
