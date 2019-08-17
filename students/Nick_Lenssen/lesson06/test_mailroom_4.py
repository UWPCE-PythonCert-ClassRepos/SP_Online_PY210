import mailroom_4
from mailroom_4 import *
import os
import pytest
import pathlib

donor_db_t = {"William Gates, III": [653772.32, 12.17],
        "Jeff Bezos": [877.33],
        "Paul Allen": [663.23, 43.87, 1.32],
        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
        }
def test_make_file():
    pth = str(pathlib.Path.cwd())+'/' 
    for key, value in donor_db_t.items():
        print (key)
        mydestin = pth + key.replace(", ", "_").replace(" ", "_")+".txt"
        assert mailroom_4.make_mydestin(key, pth) == mydestin

def test_sort_report():

    assert mailroom_4.sort_report() == sorted(donor_db_t.items(), key=itemgetter(1), reverse = True)

def test_send_thanks():
    amount_t = 50
    name = 'Nick L'
    test_text = "Thank you {} for your donation amount of {}$. We thank you for your support".format(name, amount_t)
    assert mailroom_4.send_thanks(name, amount_t) == test_text
    amount_t = 50
    name = 'Jeff Bezos'
    test_text = "Thank you {} for your donation amount of {}$. We thank you for your support".format(name, amount_t)
    assert mailroom_4.send_thanks(name, amount_t) == test_text


def test_get_letter_text():
    expected = "Dear Nick L,\n\t Thank you for your kind donation of 50\n. It will be put to good use\n\tSincerely\n\t\tThe team"
    assert mailroom_4.write_thanks_to_all('Nick L') == expected




#def test_create_report():


