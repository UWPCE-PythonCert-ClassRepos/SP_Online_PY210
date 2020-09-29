"""Test code for mailroom_part4.py"""

import sys  # imports go at the top of the file
import os
from collections import defaultdict
from mailroom_part4 import get_names, update_donor, generate_text, create_report, send_all, get_letter_text

# Initialize dictionary of donors with their names and the amounts they have donated
donor_dict = defaultdict(
    list,
    {
        "William Gates, III": [653772.32, 12.17],
        "Jeff Bezos": [877.33],
        "Paul Allen": [663.23, 43.87, 1.32],
        "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
        "Bill Nordstrom": [2013.25, 23456.78],
    },
)

def test_get_names():
    """Test listing of donor names"""
    names = "William Gates, III\nJeff Bezos\nPaul Allen\nMark Zuckerberg\nBill Nordstrom"
    assert get_names(donor_dict) == names

def test_generate_text():
    """Test generating thank you text"""
    text = "\nDear Bill Nordstrom,\n\n        Thank you for your very kind donation of $1000.00.\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team\n"
    assert generate_text('Bill Nordstrom', 1000) == text
    
def test_create_report():
    """Test final report"""
    text = "William Gates, III         $  653784.49           2  $   326892.24\nBill Nordstrom             $   25470.03           2  $    12735.01\nMark Zuckerberg            $   16396.10           3  $     5465.37\nJeff Bezos                 $     877.33           1  $      877.33\nPaul Allen                 $     708.42           3  $      236.14\n"
    assert create_report() == text

def test_file_creation():
    """Test file creation for each donor"""
    send_all()
    for file_name in ('William_Gates_III.txt', 'Jeff_Bezos.txt', 'Paul_Allen.txt', 'Mark_Zuckerberg.txt', 'Bill_Nordstrom.txt'):
        assert os.path.isfile(file_name) is True

def test_file_content():
    """Test each donor's file content"""
    # Loop thru each donor's name in the dictionary
    for (name, donations) in donor_dict.items():
        # Get the latest amount of donation
        amount = donations[len(donations) - 1]
        # Test
        text = "\nDear {:s},\n\n        Thank you for your very kind donation of ${:.2f}.\n\n        It will be put to very good use.\n\n                       Sincerely,\n                          -The Team\n".format(name, amount)
        assert get_letter_text(name, amount) == text

def test_update_donor():
    """Test adding new donor"""
    assert update_donor(donor_dict, "Bill Nordstrom", 1000) == "Bill Nordstrom: [2013.25, 23456.78, 1000]"
    assert update_donor(donor_dict, "Nam Vo", 100) == "Nam Vo: [100]"
