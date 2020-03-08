#!/usr/bin/env python3
import os

from mailroom_lesson06 import *

def test_new_donor_name():
    #confirm new donors are added to main dictionary with option 1
    thank_you("New Dude", 45.00)
    assert "New Dude" in donor_dict.keys()


def test_new_donor_amount():
    #test new donor and dollar amount are added to dict with option 1
    thank_you("New Lady", 99.00)
    assert donor_dict["New Lady"] == [99.00]


def test_single_ty_letter():
    #ensure thank you function works for options 1 and 3
    assert ty_letter('New Fella', 75.22) == '\n'.join(('\n''Dear New Fella,\n',
                                            'Thank you for your generous donation of $75.22.',
                                            'Your commitment goes a long way in helping us',
                                            'solve things that need to be solved.' + '\n',
                                            'Warm regards,' + '\n',
                                            'Mama Fratelli'))


def test_report_output():
    #check report format and contents, including the two new donors tested above
    expected = print('\n'.join(('Chester Copperpot    $ 1552409.86    3             $ 517469.95',
                                'Mouth Devereaux      $ 8379.97       2             $ 4189.98',
                                'Mikey Walsh          $ 1210.52       3             $ 403.51',
                                'Andy Carmichael      $ 174.53        2             $ 87.27',
                                'New Lady             $ 99.00         1             $ 99.00',
                                'New Dude             $ 45.00         1             $ 45.00')))
    assert print_report() == expected


def test_letters_created():
    #locate all thank you letters in the current directory
    letters_to_all()
    for file in tuple(donor_dict.keys()):
        assert os.path.isfile(file + '.txt') is True


def test_letter_text():
    #make sure letter is in the directory and contents are as expected
    expected = '\n'.join(('\n''Dear Chester Copperpot,\n',
                                'Thank you for your generous donation of $1552409.86.',
                                'Your commitment goes a long way in helping us',
                                'solve things that need to be solved.' + '\n',
                                'Warm regards,' + '\n',
                                'Mama Fratelli'))
    with open('Chester Copperpot.txt') as test_letter:
        assert test_letter.read() == expected