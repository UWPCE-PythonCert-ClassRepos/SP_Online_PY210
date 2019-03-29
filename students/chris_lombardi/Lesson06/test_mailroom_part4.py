"""Unit Testing for mailroom_part4.py functions."""

import mailroom_part4 as mailroom
import os.path
import pathlib

def test_create_report():
    """Test whether the report is created as expected"""
    test_string = ('''
Donor Name        | Total Given |  Num Gifts  | Average Gift
-------------------------------------------------------------
George Washington  $    3,587.00            3  $    1,195.67
Theodore Roosevelt $    1,987.00            3  $      662.33
Dwight Eisenhower  $    1,987.00            2  $      993.50
Abraham Lincoln    $    1,877.00            2  $      938.50
James Madison      $    1,813.00            2  $      906.50\n''')
    print(test_string)
    mailroom.initialize_donors()
    assert mailroom.create_report() == test_string

def test_initialize_donors():
    """Test whether the dictionary of donors is created correctly."""
    test_donor_log = {'George Washington': [1789.0, 1.0, 1797.0],
             'Abraham Lincoln': [1861.0, 16.0],
             'James Madison': [1809.0,4.0],
             'Theodore Roosevelt': [1901.0, 26.0, 60.0],
             'Dwight Eisenhower': [1953.00, 34.0]}
    mailroom.initialize_donors()
    assert mailroom.donor_log.get('James Madison') == test_donor_log.get('James Madison')

def test_list_donors():
    """Check that a list of all the donors is returned"""
    mailroom.initialize_donors()
    donor_list = ('George Washington\nAbraham Lincoln\nJames Madison\n' +
                  'Theodore Roosevelt\nDwight Eisenhower')
    assert mailroom.list_donors() == donor_list

def test_thank_you_test():
    """
    Test for the creation of thank you text for a new donation
    Send a thank you note to Mike Jones with a donation of 500.0
    """
    note = ('Dear Mike Jones,\n\n\tThank you for your generous donation of '
        '$500.00!\n\tWe appreciate the '
        '1 total donation(s) that you have made.'
        '\n\tYour donation will be put to good use.'
        '\n\n\tSincerely,\n\t-The Mailroom Team')

    assert mailroom.thankyou_note('Mike Jones', 500, 1) == note

def test_add_new_donor():
    """
    Test that a new donor is added to the donor log successfully
    Add Mike Jones and a donation of 1500.0
    Check donor log to see if there is a key of Mike Jones with a
    corresponding value of [1500.0,]
    """
    mailroom.initialize_donors()
    mailroom.update_donation('Mike Jones', 1500.0)
    assert mailroom.donor_log.get('Mike Jones') == [1500.0]

def test_update_donor_history():
    """
    Test for an update to the donoation list history for a donor
    Add a donation for Abraham Lincoln of 100.0
    Check that donation history updates to [1861.0, 16,0, 100.0]
    """
    mailroom.initialize_donors()
    mailroom.update_donation('Abraham Lincoln', 100)
    assert mailroom.donor_log.get('Abraham Lincoln') == [1861.0, 16.0, 100.0]

def test_send_letters():
    """
    Test whether files are created for the initial donor list
    Check to see if a file named James Madison.txt exists in the directory
    """
    current_dir = pathlib.Path('./').absolute()
    check_pth_file1 = os.path.join(current_dir,'James Madison.txt')
    check_pth_file2 = os.path.join(current_dir, 'Abraham Lincoln.txt')
    mailroom.initialize_donors()
    mailroom.send_letters()
    assert os.path.exists(check_pth_file1)
    assert os.path.exists(check_pth_file2)