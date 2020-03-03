#!/usr/bin/env python
__author__ = 'Timothy Lurvey'

import pytest
from donor_classes import *

@pytest.fixture()
def d():
    return Donor('tim', 9999, 1)


@pytest.fixture()
def repo():
    return DonorRepository((Donor('tim', 9999, 1),
                            Donor('tom', 1., 100)))

def test_init_Donor_attributes(d):
    assert isinstance(d, Donor)
    assert isinstance(d, RunningTotal)
    #
    assert d.name == 'tim' == d.key
    #
    assert d.total == 9999.
    assert isinstance(d.total, float)
    assert not isinstance(d.total, int)
    #
    assert d.count == 1
    assert not isinstance(d.count, float)
    assert isinstance(d.count, int)

def test_Donor_methods(d):
    d.name = 'timmy'
    assert d.name == 'timmy'
    #
    d.add_to_total(amount=1.)
    assert d.total == 10000.
    #
    assert d.average == 10000. / 2

def test_DonorRepo_attributes(repo):
    assert repo._REPORT_HEADER == \
           '\n'\
           'Donor Name                | Total Given | Num Gifts | Average Gift\n'\
           '------------------------------------------------------------------\n'
    #
    assert repo.name_list == ('tim', 'tom')

def test_DonorRepo_get_donor(repo):
    # get a return
    assert repo.get_donor('tim').name == 'tim'
    # get an error for missing
    try:
        repo.get_donor('a')
    except Exception as e:
        err = e
    assert isinstance(err, ValueError)
    assert "{}".format(err) == "ValueError: donor.name='a' no found in repository"

def test_DonorRepo_add_new_donor(repo):
    # add complete entry
    repo.add_new_donor(Donor('jim', 50., 1))
    repo.add_new_donor(('kim', 50., 1))
    assert repo.name_list == ('jim', 'kim', 'tim', 'tom')
    # add incomplete entry
    repo.add_new_donor(('ben',))
    assert repo.name_list == ('ben', 'jim', 'kim', 'tim', 'tom')
    assert repo.get_donor('ben').total == 0.
    assert repo.get_donor('ben').count == 0
    # test failure
    try:
        repo.add_new_donor('a')
    except Exception as e:
        err = e
    assert isinstance(err, TypeError)
    assert "{}".format(err) == "TypeError: object must be a Donor object or a sequence of donor datas"

def test_DonorRepo_add_donation(repo):
    repo.add_donation(name='tim', amount=1)
    assert repo.get_donor('tim').total == 10000

def test_DonorRepo_formatted_name_list(repo):
    assert repo.formatted_name_list == '  0 : tim\n  1 : tom'

def test_DonorRepo_get_thank_you_email(repo):
    tim_email = "\nHello tim,\n\nYour 1 donation, totaling $ 9999.00, is greatly appreciated.\n" \
                "\nThank you\n\n"
    #
    assert repo.get_thank_you_email(donor='tim', new_donation=0.) == tim_email

def test_DonorRepo_get_thank_you_email2(repo):
    tim_email = "\nHello tim,\n\nYour 2 donations, totaling $ 10000.00, are greatly appreciated.\n" \
                "\nThank you\n\n"
    #
    repo.add_donation('tim', 1)
    assert repo.get_thank_you_email(donor='tim', new_donation=0.) == tim_email

def test_DonorRepo_report(repo):
    report_test = "\n"\
                  "Donor Name                | Total Given | Num Gifts | Average Gift\n"\
                  "------------------------------------------------------------------\n"\
                  "tim                       |    $ 9999.00|          1|    $ 9999.00\n"\
                  "tom                       |       $ 1.00|        100|       $ 0.01\n"\
                  "------------------------------------------------------------------\n"
    #
    assert repo.report() == report_test
