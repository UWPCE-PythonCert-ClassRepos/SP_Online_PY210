#!/usr/bin/env python3

import os, random, string, tempfile
from datetime import datetime
from mailroom import donors, generate_email, get_donors, update_donor, generate_report_data, create_directory, write_letters

# Test email generation
def test_email():
    assert generate_email('Janet',100.0,500.0) == """Dear Janet,

Thank you for your generous donation of $100.00.
To date, you have donated a total of $500.00 to our charity.
Your contributions help new arrivals receive the highest quality care possible.
Please know that your donations make a world of difference!

Sincerely,
The Good Place Team"""

# Test get donor list
def test_donor_list():
    assert get_donors(donors) == ['Eleanor Shellstrop','Chidi Anagonye','Tahani Al-Jamil','Jason Mendoza','Mindy St. Claire']

# Test add new donor
def test_new_donor():
    update_donor('Janet',250.0)
    assert donors['Janet'][0] == 250.0

# Test update existing donor
def test_update_donor():
    update_donor('Tahani Al-Jamil',1000.0)
    assert donors['Tahani Al-Jamil'][-1] == 1000.0

# Test report generation
def test_report_generation():
    report = generate_report_data()
    assert len(report) == len(donors)
    assert report[-1] == ('Eleanor Shellstrop', 82.0, 2, 41.0)

# Test letter generation
def test_write_letters():
    # Use temporary directory, will delete automatically
    # Note: The content of the letters has already been verified in the test_email function
    with tempfile.TemporaryDirectory() as target:
        write_letters(target)
        # Check for files with donor name and today's date
        date = datetime.today().strftime('%Y-%m-%d')
        # Make sure all donor files exist
        assert all([ os.path.exists('{}/{}_{}.txt'.format(target, donor.replace(' ','_'), date)) for donor in donors ])
