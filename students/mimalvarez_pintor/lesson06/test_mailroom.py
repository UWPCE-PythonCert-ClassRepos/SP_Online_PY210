# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:42:15 2020

@author: miriam
"""

import mailroom_Part4 as mailroom
import os.path
import pathlib

mailroom.donors_dict = mailroom.donors()


def test_donors_history():
    history = mailroom.donors()
    assert history['Urias Gramajo'] == [1000]
    assert history['Miriam Pintor'] == [100, 300]


def test_donors_list():
    thislist = ('Waleed Alvarez\n Ricardo Gallegos\n Dina Sayury\n Urias Gramajo')
    assert mailroom.donors_list() == thislist


def test_donation_update():
    mailroom.donate('Miriam Alvarez', 300)
    assert mailroom.donors_dict.get('Miriam Alvarez') == [300.00]


def test_thankyou():
    letter = (f'\nDear Urias Gramajo,'
              f'\nThank you for your very kind donation of $1,000.00'
              '\nIt will be put to very good use.'
              '\n\nSincerely,\n-TheTeam\n')
    assert mailroom.print_thankyou('Urias Gramajo') == letter


def test_send_letters():
    dirpath = pathlib.Path('./').absolute()
    file1 = os.path.join(dirpath, 'Urias Gramajo.txt')
    file2 = os.path.join(dirpath, 'Miriam Pintor.txt')
    mailroom.send_letters_all_donors()
    assert os.path.exists(file1)
    assert os.path.exists(file2)


if __name__ == "__main__":
    test_donors_history()
    test_donation_update()
    test_thankyou()
    test_send_letters()
    print("All Passed")