"""
Test the code for the mailroom code in mailroom assignment 4.
Test send thank you function.
    Focuses:
        Generating thank you text
        Adding or updating donors
        listing donors
Test Create Report function.
    Focuses:
        Creation of report rows
Test Send Letters report.
    Focuses:
        Generation of thank you text
        File creation
"""

import mailroom4 as mailroom
import os

name1 = 'Jim'
name2 = 'Steve'
names = [name1, name2]

donation1 = 123
donation2 = 123.23
donation3 = 'Fred'
donation4 = (123,'Fred')

dict1 = {name1:[donation1]}
dict2 = {name1:[donation1],name2:[donation2]}
dict3 = {name1:[donation1,donation2],name2:[donation2]}

def test_write_email():
    """Test email text is generated correctly"""
    expected = f"\n\nDear Jim,\n\n\tWe appreciate your generous donations totaling $123.00.\n\nThank you,\nAndrew\n\n" 
    assert mailroom.write_email(name1,dict1) == expected

def test_add_donation_new_name():
    """Test that a name and donation are being added correctly to the Donor List"""
    expected = {'Jim': [123.00], 'Steve':[123.23]}
    assert mailroom.add_donation(name2,dict1,str(donation2)) == expected

def test_add_donation_existing_name():
    """Test that a donation is being added to the correct donor"""
    expected = {'Jim': [123.00, 123.23], 'Steve': [123.23]}
    assert mailroom.add_donation(name1,dict1,str(donation2)) == expected

def test_show_list():
    """test list of names is properly displayed"""
    expected = "\n".join(list(dict3))
    assert mailroom.show_list(dict3) == expected

def test_report_sorting():
    """test that the report is generated correctly if second entry donates more than the first"""
    expected = [(name2, donation2, 1, donation2), (name1, donation1, 1, donation1)]
    assert mailroom.build_report(dict2) == expected

def test_email_file_write():
    """Test that text files are created corretly in email function"""
    mailroom.write_email(name1,dict1)
    for root, dir, files in os.walk('./lesson06'):
        assert any(f==f"Thank_You_to_{name1}.txt" for f in files)
