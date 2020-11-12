import os
import mailroom as m2
from datetime import datetime
import pytest

# checks the report accuracy
def test_report():
    assert m2.print_donors() == ['Adam A', 'Betty B', 'Carl C', 'Ed E', 'Frank F']

# check report content
def test_report_content():
    report = [('Adam A', [2, 300, 150.0])]
    assert m2.generate_report(report) == 'Adam A              300.00         300       150.00'

# checks thank you note
def test_thankyou_text():
    assert m2.report_text('Adam A', 100) == "Dear Adam A,Thank you for your donation of 100.It will be put to very good use."


# test when user inputs non-valid entry
def test_invalid_entry():
    # This test validates when a new donors is attempted to be added as an existing donor
    assert m2.existing_donors('Ravi G', 100) == 'Invalid entry, donor is a new one'
    # This test validates when a existing donor is added to donors
    assert m2.existing_donors('Adam A', 100) == 'Dear Adam A, Thank you for your donation of 100.'
    # This test validates since donation amount is not valid entry
    assert m2.existing_donors('Adam A', 'one') == 'Invalid entry for donation amount'
    # This test validates since donation amount is not valid entry
    assert m2.existing_donors('Adam A', -1) == 'Invalid entry for donation amount'

    # These are tests for new donors
    # This test validates when a existing donor is attempted to be added as a new donor
    assert m2.add_new_donors('Adam A', 100) == 'Invalid entry, donor is a existing one'
    # This test validates when a new donor is added to donors
    assert m2.add_new_donors('Victor V', 100) == 'Dear Victor V, Thank you for your donation of 100.'
    # This test validates since donation amount is not valid entry
    assert m2.add_new_donors('Vicky V', 'one') == 'Invalid entry for donation amount'
    # This test validates since donation amount is not valid entry
    assert m2.add_new_donors('Vesper V', -1) == 'Invalid entry for donation amount'

# These tests check if there are letters (files) generated in the folder
def test_file_check():
    for k,v in m2.donors.items():
        filename1 = r"C:/Users/ravigant/UW_Python/"+ k.split(' ')[0] + "/"
        filename1 += '20201014.txt' # date of when files ran
        assert os.path.isfile(filename1)
