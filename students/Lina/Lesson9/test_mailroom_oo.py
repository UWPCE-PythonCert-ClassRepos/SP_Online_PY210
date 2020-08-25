'''
test code for donor_models.py
'''

import pytest
import os
from datetime import date
from donor_models import Donor, DonorCollection
from cli_main import send_letters_to_all_donors

"""
Test Donor class
"""
def test_init_1():
    #No details, donor does not exist
    d = Donor('Joe Smith')
    assert d.full_name == 'Joe Smith'
    assert d.details['gift_amounts'][0] == 0

def test_init_2():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.0]})
    assert d.full_name == 'Joe Smith'
    assert d.details['gift_amounts'][0] == 50.0
    assert d.details['gift_amounts'][1] == 120.0

def test_init_3():
    #No details passed but the donor is in DataCollection
    d = Donor('Jennifer Lee')
    assert d.full_name == 'Jennifer Lee'
    assert d.details['gift_amounts'][0] == 1350.0
    assert d.details['gift_amounts'][1] == 120.17

def test_first_name():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.0]})
    assert d.first_name == 'Joe'

def test_last_name():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.0]})
    assert d.last_name == 'Smith'

def test_total_gift_amount_1():
    #No donation made yet
    d = Donor('Joe Smith', {'gift_amounts' : [0]})
    assert d.total_gift_amount == 0

def test_total_gift_amount_2():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.15]})
    assert d.total_gift_amount == 170.15

def test_total_gift_count_1():
    #No donation made yet
    d = Donor('Joe Smith', {'gift_amounts' : [0]})
    assert d.total_gift_count == 0

def test_total_gift_count_2():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.15]})
    assert d.total_gift_count == 2

def test_total_gift_count_3():
    #It does not make sense to have zero gift amount unless bad data
    #was allowed.
    d = Donor('Joe Smith', {'gift_amounts' : [0, 15.0, 0, 20.0, 50.00]})
    assert d.total_gift_count == 3

def test_total_gift_count_2():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.15]})
    assert d.total_gift_count == 2
def test_avg_gift_amount_1():
    #No donation made yet
    d = Donor('Joe Smith', {'gift_amounts' : [0]})
    assert d.avg_gift_amount == 0

def test_avg_gift_amount_2():
    d = Donor('Joe Smith', {'gift_amounts' : [50.0, 120.15, 80.22]})
    assert d.avg_gift_amount == 83.46

def test_thank_you_letter():
    d = Donor('Jennifer Lee')
    letter = d.thank_you_letter('Jennifer Lee', 250.0)
    print(letter)
    today = date.today().strftime('%m-%d-%Y')
    assert letter.count('Dear Jennifer') == 1
    assert letter.count('   Thank you for your generous gift of $250.00 to support the work of ChangeALife. Your') == 1
    assert letter.count('donation will remain in your local community and be used by ChangeALife to provide programs') == 1
    assert letter.count('and services to those in need.') == 1
    assert letter.count('you know the deep satisfaction of having made a difference in the lives of others.') == 1
    assert letter.count('   On behalf of those whose lives will be impacted, please accept our sincere gratitude. May ') == 1
    assert letter.count('Below is a summary of your gift.') == 1
    assert letter.count('Amount: $250.00') == 1
    assert letter.count(f'Date: {today}') == 1
    assert letter.count('Tiffany Kurnett') == 1
    assert letter.count('President & CEO') == 1

"""
Test DonorCollection class
"""
def test_donor_list():
    dc = DonorCollection()
    assert dc.donor_list() == ['Dmitriy Mikutin', 'Henry Ma', 'Jennifer Lee', 'John Palmer', 'Linda Anderson', 'Melissa Carey']

def test_lookup_donor_1():
    #Donor does not exist
    dc = DonorCollection()
    assert dc.lookup_donor('Mary Hill') is None

def test_lookup_donor_2():
    dc = DonorCollection()
    assert dc.lookup_donor('John Palmer') is not None
    assert dc.lookup_donor('John Palmer') == {'gift_amounts' : [3312.00, 5500.00]}

def test_add_donation_1():
    #New donor
    dc = DonorCollection()
    dc.add_donation('Mary Hill', 370.28)
    assert dc.lookup_donor('Mary Hill') == {'gift_amounts' : [370.28]}

def test_add_donation_2():
    #Add donation from existing donor
    dc = DonorCollection()
    dc.add_donation('Jennifer Lee', 150.0)
    assert dc.lookup_donor('Jennifer Lee') == {'gift_amounts' : [1350.0, 120.17, 150.0]}

def test_donors_summary():
    dc = DonorCollection()
    summary = dc.donors_summary()
    assert summary[0] == ('Dmitriy Mikutin', 16396.1, 3, 5465.37)
    assert summary[1] == ('John Palmer', 8812.00, 2, 4406.00)
    assert summary[2] == ('Jennifer Lee', 1470.17, 2, 735.09)
    assert summary[3] == ('Linda Anderson', 877.33, 1, 877.33)
    assert summary[4] == ('Melissa Carey', 708.42, 3, 236.14)
    assert summary[5] == ('Henry Ma', 526.75, 4, 131.69)

def test_donors_summary_report():
    dc = DonorCollection()
    report = dc.donors_summary_report()
    assert report.count('Donor Name                | Total Given | Num Gifts | Average Gift') == 1
    assert report.count('------------------------------------------------------------------') == 1
    assert report.count('Dmitriy Mikutin            $   16396.10           3  $     5465.37') == 1
    assert report.count('John Palmer                $    8812.00           2  $     4406.00') == 1
    assert report.count('Jennifer Lee               $    1470.17           2  $      735.09') == 1
    assert report.count('Linda Anderson             $     877.33           1  $      877.33') == 1
    assert report.count('Melissa Carey              $     708.42           3  $      236.14') == 1
    assert report.count('Henry Ma                   $     526.75           4  $      131.69') == 1

def test_letters_to_all_donors():
    dc = DonorCollection()
    letters = dc.letters_to_all_donors()
    print(letters)
    #makes sure there is a total of six letters
    assert len(letters) == 6
    #checks content in one of the letters
    letter = letters[0][0]
    assert letter.count('Dear Jennifer,') == 1
    assert letter.count('Whether you are a new donor or have suppported ChangeALife for many years, your compassionate') == 1
    assert letter.count('generosity gives us the vital resource to provide programs and services to those in need. I hope') == 1
    assert letter.count('you will continue to support our work at ChangeALife. Your support means the world to the families') == 1
    assert letter.count('and people we serve.')
    assert letter.count('   On behalf of those whose lives will be impacted and from all of us at ChangeALife, THANK YOU!') == 1
    assert letter.count('Below is a summary of your gift.') == 1
    assert letter.count('Amount: $1470.17') == 1
    assert letter.count('Tiffany Kurnett') == 1
    assert letter.count('President & CEO') == 1
    assert letters[0][1] == 'Jennifer Lee'

"""
Test cli_main user interface
"""
def test_send_letters_to_all_donors():
    #tests files are created for all donors and meet the mininum file size
    send_letters_to_all_donors()
    min_size = 600
    assert os.path.getsize('Dmitriy_Mikutin.txt') > min_size
    assert os.path.getsize('John_Palmer.txt') > min_size
    assert os.path.getsize('Jennifer_Lee.txt') > min_size
    assert os.path.getsize('Linda_Anderson.txt')> min_size
    assert os.path.getsize('Melissa_Carey.txt') > min_size
    assert os.path.getsize('Henry_Ma.txt') > min_size
