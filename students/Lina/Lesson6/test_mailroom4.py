#! python

from mailroom4 import donor_list, donors_summary, add_donation, letter_to_donor, send_letters_to_all_donors
from datetime import date
import os


def test_donor_list():
    assert donor_list() == ['Dmitriy Mikutin', 'Henry Ma', 'Jennifer Lee', 'John Palmer', 'Linda Anderson', 'Melissa Carey']

def test_donors_summary():
    summary = donors_summary()
    assert summary[0] == ('Dmitriy Mikutin', 16396.1, 3, 5465.37)
    assert summary[1] == ('John Palmer', 8812.00, 2, 4406.00)
    assert summary[2] == ('Jennifer Lee', 1470.17, 2, 735.09)
    assert summary[3] == ('Linda Anderson', 877.33, 1, 877.33)
    assert summary[4] == ('Melissa Carey', 708.42, 3, 236.14)
    assert summary[5] == ('Henry Ma', 526.75, 4, 131.69)

def test_add_donation_1():                   #add donation to existing donor
    add_donation('Jennifer Lee', 150)
    summary = donors_summary()               #if donors_summary is passed, then it can be used for assert testing here
    assert summary[2] == ('Jennifer Lee', 1620.17, 3, 540.06)

def test_add_donation_2():                   #add donation of a new donor
    add_donation('Joe Smith', 370.28)
    summary = donors_summary()
    assert summary[6] == ('Joe Smith', 370.28, 1, 370.28)

def test_letter_to_donor_1():                #send a Thank you to a donor
    letter = letter_to_donor('Jennifer Lee', 150, 1)
    today = date.today().strftime('%m-%d-%Y')
    assert letter.count('Dear Jennifer,') == 1              #check first line of the letter
    assert letter.count('   Thank you for your generous gift of $150.00 to support the work of ChangeALife. Your') == 1
    assert letter.count('donation will remain in your local community and be used by ChangeALife to provide programs') == 1
    assert letter.count('and services to those in need.') == 1
    assert letter.count('you know the deep satisfaction of having made a difference in the lives of others.') == 1
    assert letter.count('   On behalf of those whose lives will be impacted, please accept our sincere gratitude. May ') == 1
    assert letter.count('Below is a summary of your gift.') == 1
    assert letter.count('Amount: $150.00') == 1
    assert letter.count(f'Date: {today}') == 1
    assert letter.count('Tiffany Kurnett') == 1
    assert letter.count('President & CEO') == 1             #check last line of the letter

def test_letter_to_donor_2():                #send letters to all donors
    letter = letter_to_donor('Melissa Carey', 708.42, 2)
    assert letter.count('Dear Melissa,') == 1
    assert letter.count('Whether you are a new donor or have suppported ChangeALife for many years, your compassionate') == 1
    assert letter.count('generosity gives us the vital resource to provide programs and services to those in need. I hope') == 1
    assert letter.count('you will continue to support our work at ChangeALife. Your support means the world to the families') == 1
    assert letter.count('and people we serve.')
    assert letter.count('   On behalf of those whose lives will be impacted and from all of us at ChangeALife, THANK YOU!') == 1
    assert letter.count('Below is a summary of your gift.') == 1
    assert letter.count('Amount: $708.42') == 1
    assert letter.count('Tiffany Kurnett') == 1
    assert letter.count('President & CEO') == 1

def test_send_letters_to_all_donors():      #test files are created for all donors and meet the mininum file size
    send_letters_to_all_donors()
    min_size = 600
    assert os.path.getsize('Dmitriy_Mikutin.txt') > min_size
    assert os.path.getsize('John_Palmer.txt') > min_size
    assert os.path.getsize('Jennifer_Lee.txt') > min_size
    assert os.path.getsize('Linda_Anderson.txt')> min_size
    assert os.path.getsize('Melissa_Carey.txt') > min_size
    assert os.path.getsize('Henry_Ma.txt') > min_size
