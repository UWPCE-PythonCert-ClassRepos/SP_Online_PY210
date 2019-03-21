"""Unit Testing for mailroom_part4.py functions."""

import mailroom_part4 as mailroom

def test_create_report():
    """Test whether the report is created as expected"""

def test_initialize_donors():
    """Test whether the dictionary of donors is created correctly."""
    test_donor_log = {'George Washington': [1789.0, 1.0, 1797.0],
             'Abraham Lincoln': [1861.0, 16.0],
             'James Madison': [1809.0,4.0],
             'Theodore Roosevelt': [1901.0, 26.0, 60.0],
             'Dwight Eisenhower': [1953.00, 34.0]}
    mailroom.initialize_donors()
    assert mailroom.donor_log.get('James Madison') == test_donor_log.get('James Madison')

def test_total_donation():
    """
    Test whether the total donation amount is correctly computed
    Using Abraham Lincoln as the input
    Expected total is 1877.00
    """
    mailroom.initialize_donors()
    assert mailroom.total_donation('Abraham Lincoln'.title()) == float(1877.0)

def test_list_donors():
    """Check that a list of all the donors is returned"""
    mailroom.initialize_donors()
    donor_list = ('George Washington\nAbraham Lincoln\nJames Madison\n' +
                  'Theodore Roosevelt\nDwight Eisenhower')
    assert mailroom.list_donors() == donor_list

def test_thank_you_test():
    """Test for the creation of thank you text for a new donation"""

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

def test_send_letters_content():
    """
    Test whether the content of the created letter is as expcted
    Check to see if Dwight Eisenhower letter content is correct including
    a total donation of 1987.00
    """