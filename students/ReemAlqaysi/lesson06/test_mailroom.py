#!/usr/bin/env python3

import mailroom
import os


donor_list = {
    "Jan Balard": [600.00,250.00],
    "Joe McHennry": [1500.00,1500.00],
    "Jeff Hansen": [450.00,150.00],
    "Scott Newman": [100.00,5000.00],
    "Rabi Das": [500.00,950.00]
    }

def test_send_letter_text():
   letter = '''\n\nDear Reem Alqaysi:\n Thank you for your donation of $222, we appriciate your support to our service. \n MailRoom Team\n'''
   assert mailroom.thank_you_text('Reem Alqaysi',222) == letter

def test_new_donor():
   fullname = 'Reem Alqaysi'
   mailroom.add_name(fullname)
   assert fullname in donor_list
   #assert donor_list == {'Jan Balard': [600.0, 250.0], 'Joe McHennry': [1500.0, 1500.0], 'Jeff Hansen': [450.0, 150.0], 'Scott Newman': [100.0, 5000.0], 'Rabi Das': [500.0, 950.0], 'Reem Alqaysi': []}

def test_update_donor():
   fullname = 'Rabi Das'
   mailroom.add_name(fullname)
   assert fullname in donor_list

def test_add_amount():
    fullname = 'Reem Alqaysi'
    amount = 222
    mailroom.add_amount(fullname,amount)
    assert donor_list[fullname][-1] == [amount]

def test_create_report():
    report = \
    f'Donor Name        |     Total Given         |Num Gifts                |Average Gift   \n\
    ------------------------------------------------------------------------------------------\n\
    Scott Newman         $      5100.0                2                $      2550.0\n\
    Jeff Hansen          $       600.0                2                $       300.0\n\
    Rabi Das             $      1450.0                2                $       725.0\n\
    Jan Balard           $       850.0                2                $       425.0\n\
    Joe McHennry         $      3000.0                2                $      1500.0\n'

    assert mailroom.create_report() == report


def test_create_report_file():
    mailroom.letter_to_all()
    for name in donor_list:
        filename = name.replace(' ', '_').replace(',', '') + ".txt"
        filename = filename.lower()
        assert os.path.isfile(filename) is True