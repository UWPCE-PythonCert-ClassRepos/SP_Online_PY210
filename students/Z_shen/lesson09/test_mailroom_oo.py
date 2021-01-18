from donor_models import *
import os.path
import pathlib
import pytest


donor_list = {'William Gates': [1500.99, 3500, 800.25],
              'Jeff Bezos': [145.72, 1350.25],
              'Paul Allen': [250.00, 57.00],
              'Mark Zuckerberg': [600.00]}


def test_donor():
    a = Donor('William Gates', 123)
    assert a.name == 'William Gates'
    assert a. amount == 123


def test_repr():
    a = Donor('William Gates', 123)
    assert a.__repr__() == 'William Gates donated $123'


def test_str():
    a = Donor('William Gates', 123)
    assert a.__str__() == 'Donor(William Gates, 123)'


def test_send_letter():
    a = Donor('William Gates', 123)
    content = ('''Dear {}, 
            Thank you for your generous donation of ${:,.2f} to us.
            It will be put to very good use.

                                Sincerely,
                                    -The Team
                                              '''.format('William Gates', 123))
    assert a.send_letter() == content


def test_donor_collection():
    b = DonorCollection(donor_list)
    assert b.donors == donor_list


def test_add_new_donor():
    b = DonorCollection()
    test = {'William Gates': [123]}
    assert b.add_new_donor('William Gates', 123) == test


def test_add_amount_same_donor():
    b = DonorCollection({'William Gates': [123]})
    test = {'William Gates': [123, 111]}
    assert b.add_amount_same_donor('William Gates', 111) == test


def test_times():
    b = DonorCollection({'William Gates': [123, 123, 123]})
    assert b.times('William Gates') == 3


def test_total():
    b = DonorCollection({'William Gates': [123, 123, 123]})
    assert b.total('William Gates') == 123*3


def test_sorted():
    b = DonorCollection(donor_list)
    test = ['William Gates', 'Jeff Bezos', 'Mark Zuckerberg', 'Paul Allen']
    assert b.sorted() == test


def test_send_letters_to_all():
    b = DonorCollection(donor_list)
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath, 'Mark_Zuckerberg.txt')
    file2 = os.path.join(dirpath, 'Paul_Allen.txt')
    b.send_letters_to_all()
    assert os.path.exists(file1)
    assert os.path.exists(file2)