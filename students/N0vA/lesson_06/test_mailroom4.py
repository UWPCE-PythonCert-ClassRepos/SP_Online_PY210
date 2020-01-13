#!/usr/bin/env python3

#### Unit testing for mailroom4 ####

from mailroom4 import *
import os


def test_add_donor():
    
    add_donor('James Albright', 3500000)
    assert 'James Albright' in database.keys() and database['James Albright'] == [3500000]

def test_add_donation():

    add_donation('Bill Gates', 45000000)
    expected = [2000000, 250000000, 45000000]
    assert database['Bill Gates'] == expected

# Test functions
def test_thank_you_text():
    
    expected = ('Dear Bill Gates:\n\n'
                    'On behalf of your Local Charity, I would like to thank you for your generous donation.'
                    'We appreciate your support not only for us but for our cause.\n\n'
                    'We wish you all the best,\n\n'
                    'Local Charity Persident\n')
    assert thank_you_text('Bill Gates') == expected

def test_sort_database():
    
    expected = [('Paul Allen', [450000000]), ('Bill Gates', [2000000, 250000000]), ('Elon Musk', [50000000, 10000000]), ('James Albright', [3500000]), ('Jeff Bezos', [2000000]), ('Howard Schultz', [1000000])]
    assert sort_database(database) == expected

def test_format_report(): # Check if rows for report are formatted properly

    report_data = format_report(sort_database(database))
    donor_1 = report_data[0]
    expected = 'Paul Allen                    $   450,000,000        1        $450,000,000.00'
    assert donor_1 == expected



def test_letter_text():
    """Get text from letter that will be sent to all donors."""

    expected = ('Dear Elon Musk'
                'Thank you for your donations totaling' 
                '$ 60,000,000.  We appreciate your contributions'
                'for the year.\n\nHappy holidays,\n\n' 
                'Your loal charity President')
    assert letter_text("Elon Musk") == expected

def test_send_letters():
    
    send_letters()
    assert os.path.exists("./Elon_Musk.txt")