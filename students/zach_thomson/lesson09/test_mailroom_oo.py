import pytest
from donor_models import *


def test_donor_class():
    '''Make sure a donor object can be created and have a list of donations'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    assert eddie.name == 'Eddie Vedder'
    assert eddie.donations == [10000.00, 20000.00, 4500.00]


def test_donation_append():
    '''test adding a new donation to a current donor'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    eddie.new_donation(200.0)
    assert eddie.donations == [10000.00, 20000.00, 4500.00, 200.0]


def test_donation_summaries():
    '''test summary functions that will be used to create a report'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    assert eddie.number_of_donations() == 3
    assert eddie.sum_donations() == 34500.0
    assert eddie.avg_donation() == 11500.0


def test_donor_dict():
    '''test DonorCollection creation, new donation, and new donor + donation'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    chris = Donor('Chris Cornell', [100.00, 500.00])
    kurt = Donor('Kurt Cobain', [25.00])
    donor_db = DonorCollection(eddie, chris, kurt)
    assert donor_db.donors == {'Eddie Vedder': eddie, 'Chris Cornell': chris, 'Kurt Cobain': kurt}
    assert kurt.donations == [25.0]
    donor_db.new_donation('Kurt Cobain', 50.00)
    assert kurt.donations == [25.0, 50.0]
    donor_db.new_donation('Zach', 100.0)
    assert 'Zach' in donor_db.donors


def test_email(capsys):
    '''test email creation and printing'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    chris = Donor('Chris Cornell', [100.00, 500.00])
    kurt = Donor('Kurt Cobain', [25.00])
    donor_db = DonorCollection(eddie, chris, kurt)
    donor_db.new_donation('Kurt Cobain', 50.00)
    captured = capsys.readouterr()
    assert captured.out == "\nDear Kurt Cobain,\nThank you for your generous donation of $50.00!\n\n"


def test_create_table():
    '''Confirms entries from database are placed in a list for print table formating'''
    eddie = Donor('Eddie Vedder', [10000.00, 20000.00, 4500.00])
    chris = Donor('Chris Cornell', [100.00, 500.00])
    kurt = Donor('Kurt Cobain', [25.00])
    donor_db = DonorCollection(eddie, chris, kurt)
    test_list = donor_db.get_report()
    assert ('Kurt Cobain', 25.0, 1, 25.0) in test_list
