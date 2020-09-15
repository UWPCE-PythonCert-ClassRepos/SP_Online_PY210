"""
test code for donor_models.py
"""

import os.path
from donor_models import *
from cli_main import *

"""
Donor Class Tests
"""
# Test donor list
def test_donor():
    d = Donor("George Washington")
    assert d.name == "George Washington"

# Test add donor amount
def test_new_donation():
    d = Donor("George Washington", [100])
    d.new_donation(1)
    assert d.donation_total == 101

# Test donation total
def test_donation_total():
    d = Donor("George Washington", [100, 50, 1])
    assert d.donation_total == 151

# Test donor count
def test_donation_count():
    d = Donor("George Washington", [100, 50, 1])
    assert d.donation_count == 3

# Test donor average
def test_donation_avg():
    d = Donor("George Washington", [100, 50])
    assert d.donation_avg == 75

# Test Thank you email
def test_thank_you_letter():
    name = "Tony Stark"
    gift = 100
    email = f"Thank you {name} for your generous donation of ${gift:.2f}, your kindness is very appreciated." + "\n"
    d = Donor(name)
    assert d.thank_you_letter(name, gift) == email

# Test email all
def test_all_letters():
    dc = DonorCollection()
    dc.all_letters()
    assert os.path.isfile('thank_you_john doe.txt')
    assert os.path.isfile('thank_you_jane doe.txt')
    assert os.path.isfile('thank_you_method man.txt')
    assert os.path.isfile('thank_you_the rza.txt')
    assert os.path.isfile('thank_you_ghost face.txt')


# Test report
def test_create_report():
    dc = DonorCollection()
    report = dc.create_report()
    assert report[0] == 'Donor Name           | Total Given | Num Gifts | Average Gift'
    assert report[1] == '-------------------------------------------------------------'
    assert report[2] == 'Ghost Face           $       35.00           3 $       11.67'
    assert report[3] == 'John Doe             $        1.00           1 $        1.00'
    assert report[4] == 'Jane Doe             $    12802.00           4 $     3200.50'
    assert report[5] == 'Method Man           $     3000.00           2 $     1500.00'
    assert report[6] == 'The Rza              $      742.00           5 $      148.40'
