#!/usr/bin/env python3

import mailroom_pt4 as mailroom
import os

#!/usr/bin/env python3

import mailroom_pt4 as mailroom
import os

def test_generate_report():
    report_output = ['S. Claus                 $ 21200.00            3         $ 7066.67',
                     'Chanandler Bong          $ 19000.00            2         $ 9500.00',
                     'John Jacob               $  1009.25            3         $  336.42',
                     'Jingleheimer Schmidt     $   240.50            1         $  240.50',
                     'Jimni Christmas          $    12.00            1         $   12.00']
    assert mailroom.generate_report() == report_output

def test_sum_donations():
    assert mailroom.sum_donations(('Test', [10, 1000])) == 1010

def test_add_donor():
    # Test for existing donor
    mailroom.add_donor('John Jacob')
    assert mailroom.donors['John Jacob'] == [5.00, 1000.00, 4.25]
    
    # Test for new donor
    mailroom.add_donor('Emory')
    assert mailroom.donors['Emory'] == []

def test_add_donation():
    # Test adding a donation to an existing donor
    mailroom.add_donation('John Jacob', 400)
    assert mailroom.donors['John Jacob'] == [5.00, 1000.00, 4.25, 400]

def test_thanks_letter():
    expected_output = """\n
    Dear Jonah,

    Thank you for your donation(s) of 20.00!
    We really appreciate your support!
    
    Sincerely,
        The Black Mesa Research Foundation"""
    assert mailroom.thanks_letter("Jonah", 20) == expected_output

def test_send_all_thanks():
    mailroom.send_all_thanks()
    assert os.path.isfile("Jimni Christmas.txt") is True