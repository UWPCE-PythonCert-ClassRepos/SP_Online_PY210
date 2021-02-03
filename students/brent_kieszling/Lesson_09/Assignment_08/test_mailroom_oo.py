#-------------------------------------------#
#Tittle: test_mailroom_oo.py, PYTHON210 - Assignment 8
#Desc: Test harness for mailroom_oo.py
#Change Log: (Who, When, What)
#Brent Kieszling, 2021-Jan-25, created file
#-------------------------------------------#

import os.path
import pytest
from donor_modles import Donor, Donors

def test_init():
    a = Donor("Scrooge McDuck", 999.91)
    with pytest.raises(TypeError):
        b = Donor(123, 100)
    with pytest.raises(TypeError):
        c = Donor("Bob", "Ten dollars")

def test_name():
    a = Donor("Scrooge McDuck", 999.91)
    print(a.person)
    assert a.person == "Scrooge McDuck"

def test_name_change1():
    a = Donor("Scrooge McDuck", 999.91)
    a.person = "Donald Duck"
    assert a.person == "Donald Duck"

def test_new_donation1():
    a = Donor("Scrooge McDuck", 999.91)
    a.new_donation(100.00)
    assert a.donations == [999.91, 100.00]

def test_new_donation2():
    a = Donor("Scrooge McDuck", 999.91)
    a.new_donation(-100.00)
    assert a.donations == [999.91, 0]

def test_check_donation():
    a = Donor("Scrooge McDuck", 999.91)
    assert a.donations[0] == 999.91
    a.new_donation(100.00)
    a.new_donation(2)
    a.new_donation(300.11)
    assert a.donations[2] == 2.00
    print(a.donations)

def test_change_donation1():
    a = Donor("Scrooge McDuck", 999.91)
    a.new_donation(100.00)
    a.new_donation(2)
    a.change_donation(3, -200)
    assert a.donations[2] == 0.00

def test_change_donation2():
    a = Donor("Scrooge McDuck", 999.91)
    a.new_donation(100.00)
    a.new_donation(2)
    a.change_donation(1, 1000)
    assert a.donations[0] == 1000.00

def test_total_gifts():
    a = Donor("Scrooge McDuck", 999.91)
    a.donations.append(100.00)
    print(a.gifts)
    assert a.gifts == 2

def test_total_donated():
    a = Donor("Scrooge McDuck", 999.91)
    assert a.total == 999.91
    a.donations.append(100.11)
    assert a.total == 1100.02

def test_average_donation():
    a = Donor("Scrooge McDuck", 999.91)
    a.donations.append(100.00)
    print (a.average)
    assert a.average == 549.95

def test_str_donor():
    a = Donor("Scrooge McDuck", 100.11)
    a.donations.append(200.11)
    print(a)
    assert "Scrooge McDuck" in str(a)
    assert "300.22" in str(a)
    assert "150.11" in str(a)
    assert" 2 " in str(a)
    assert str(a) == "\
Donation Summary:\n\
-----------------------------------------------------------------\n\
Donor Name           | Total Given | Num Gifts | Average Gift\n\
-----------------------------------------------------------------\n\
Scrooge McDuck       $ 300.22           2      $     150.11\n\
-----------------------------------------------------------------\n\
Donation 1: $ 100.11\n\
Donation 2: $ 200.11"

def test_repr_donor():
    a = Donor("Scrooge McDuck", 100.11)
    print(repr(a))
    assert repr(a) == "Scrooge McDuck       $ 100.11           1      $     100.11"

def test_thank_you():
    a = Donor("Scrooge McDuck", 100.00)
    print(a.thank_you())
    assert a.thank_you() == """
    Dear Scrooge McDuck,
    
    Thank you for your most recent donation of $100.00. We are humbled by your 
    lifetime contribution of $100.00.
    
    Sincerly,
    Making Good Things Happen"""
    a.new_donation(1000.00)
    assert a.thank_you() == """
    Dear Scrooge McDuck,
    
    Thank you for your most recent donation of $1000.00. We are humbled by your 
    lifetime contribution of $1100.00.
    
    Sincerly,
    Making Good Things Happen"""

def test_donors_init():
    a = Donor("Scrooge McDuck", 100.11)
    x = Donors()
    z = Donors(a)

def test_find_donor1():
    a = Donor("Scrooge McDuck", 100.11)
    z = Donors(a)
    assert z.find_donor("Scrooge McDuck") == a

def test_find_donor2():
    a = Donor("Scrooge McDuck", 100.11)
    z = Donors(a)
    with pytest.raises(IndexError):
        z.find_donor("Scrooge")

def test_new_donor():
    x = Donors()
    a = Donor("Sting", 500.00)
    x.new_donor("Sting", 500.00)
    assert repr(x.find_donor("Sting")) == repr(a)

def test_str_donors():
    a = Donor("Sting", 100.00)
    x = Donors(a)
    x.new_donor("Cher", 200.00)
    x.new_donor("James Bond", 300.00)
    print(str(x))
    assert str(x) =="\
Donor Rankings:\n\
-----------------------------------------------------------------\n\
Donor Name           | Total Given | Num Gifts | Average Gift\n\
1 James Bond           $ 300.00           1      $     300.00\n\
2 Cher                 $ 200.00           1      $     200.00\n\
3 Sting                $ 100.00           1      $     100.00"

def test_edit_a_donor1():
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("Bond James", 500.00)
    p = x.find_donor("Bond James")
    p.person = "James Bond"
    assert str(x) =="\
Donor Rankings:\n\
-----------------------------------------------------------------\n\
Donor Name           | Total Given | Num Gifts | Average Gift\n\
1 James Bond           $ 500.00           1      $     500.00\n\
2 Cher                 $ 400.00           1      $     400.00\n\
3 Sting                $ 300.00           1      $     300.00"

def test_edit_a_donation1():
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("Bond James", 500.00)
    p = x.find_donor("Bond James")
    p.change_donation(1, 1000)
    assert str(x) =="\
Donor Rankings:\n\
-----------------------------------------------------------------\n\
Donor Name           | Total Given | Num Gifts | Average Gift\n\
1 Bond James           $ 1000.00          1      $    1000.00\n\
2 Cher                 $ 400.00           1      $     400.00\n\
3 Sting                $ 300.00           1      $     300.00"

def test_edit_a_donation2():
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("Bond James", 500.00)
    p = x.find_donor("Bond James")
    p.change_donation(1, 200)
    assert str(x) =="\
Donor Rankings:\n\
-----------------------------------------------------------------\n\
Donor Name           | Total Given | Num Gifts | Average Gift\n\
1 Cher                 $ 400.00           1      $     400.00\n\
2 Sting                $ 300.00           1      $     300.00\n\
3 Bond James           $ 200.00           1      $     200.00"

def test_save():
    file = "test_profiles.dat"
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("James Bond", 500.00)
    x.save(file)
    assert os.path.isfile(file) == True

def test_load1():
    file = "test_no_profiles.dat"
    file2 = "does_not_exist.txt"
    x = Donors()
    x.save(file)
    x.load(file)
    assert x.profiles == []
    x.load(file2)
    assert x.profiles == []

def test_load2():
    file = "test_profiles_2.dat"
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("James Bond", 500.00)
    x.save(file)
    z = Donors()
    z.load(file)
    print(x.profiles)
    print(z.profiles)
    assert str(x.profiles) == str(z.profiles)

def test_load3():
    file = "test_profiles_3.dat"
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("James Bond", 500.00)
    x.save(file)
    b = Donor("Michael Bolton", 5000.00)
    z = Donors(b)
    z.load(file)
    print(x.profiles)
    print(z.profiles)
    assert str(x.profiles) == str(z.profiles)

def test_thank_you_file():
    a = Donor("TestSting1", 300.00)
    b = Donor("Test Sting2", 300.00)
    c = Donor("Test-Sting3", 300.00)
    a.create_file()
    b.create_file()
    c.create_file()
    assert os.path.isfile("teststing1.txt") == True
    assert os.path.isfile("test_sting2.txt") == True
    assert os.path.isfile("test-sting3.txt") == True
    with open("teststing1.txt", 'r') as file:
            letter = file.read()
    print(letter)
    print(a.thank_you())
    assert letter == a.thank_you()

def test_thank_you_files1():
    a = Donor("Sting", 300.00)
    x = Donors(a)
    x.new_donor("Cher", 400.00)
    x.new_donor("James Bond", 500.00)
    x.thank_yous()
    assert os.path.isfile("sting.txt") == True
    assert os.path.isfile("cher.txt") == True
    assert os.path.isfile("james_bond.txt") == True

def test_thank_you_files2():
    a = Donor("test1", 300.00)
    x = Donors(a)
    x.new_donor("test2", 400.00)
    x.thank_yous("test1")
    assert os.path.isfile("test1.txt") == True
    assert os.path.isfile("test2.txt") == False

