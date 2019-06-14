#!/usr/bin/env python3

import os.path
import datetime
from mailroom_4 import *

def test_check_add_name():
    """
    Testing check_add_name(), calling it with a new name and then checking if that name has been added
    to the donor_list_dic dictionary
    :return:
    """
    check_add_name('peter')
    assert 'peter' in donor_list_dic
    assert 'Ella' not in  donor_list_dic


def test_add_donation():
    add_donation ('peter', 10)
    assert donation_list('peter') == [10]
    add_donation('pooria koleyni', 20)
    assert donation_list('pooria koleyni') == [130,20]


def test_update_total_donation_to_dic():
    update_total_donation_to_dic('meru cheng')
    assert donor_list_dic['meru cheng']['total_donation'] == 580


def test_donation_list():
    donation_list('meru cheng')
    assert donation_list('meru cheng') == [150, 430]
    assert donation_list('john adams') == [200, 340, 560]
    assert donation_list('maysam razm') != [22]


def test_write_letter_to_file():
    write_letter_to_file('peter')
    d = datetime.datetime.today()
    assert os.path.isfile('peter_{}_{}_{}.txt'.format(d.year, d.month, d.day))
    assert not os.path.isfile('per_{}_{}_{}.txt'.format(d.year, d.month, d.day))


def test_write_letter_for_everyone():
    write_letter_for_everyone()
    d = datetime.datetime.today()
    for name in donor_list_dic.keys():
        file_name = '{}_{}_{}_{}.txt'.format(name,d.year, d.month, d.day)
        assert os.path.isfile(file_name)
        assert not os.path.isfile('koleyni_2019_6_5.txt')

