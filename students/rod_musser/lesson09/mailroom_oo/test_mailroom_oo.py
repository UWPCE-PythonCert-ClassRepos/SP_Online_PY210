import pytest
from donor_models import Donor
from donor_models import DonorCollection


def test_new_donor():
    d = Donor('John Smith')
    assert d.name == 'John Smith'

    d.name = 'Jane Doe'
    assert d.name == 'Jane Doe'


def test_add_donor_donation():
    d = Donor('Chuck Norris')
    d.add_donation(50.05)
    assert d.num_of_donations == 1
    assert d.sum_of_donations == 50.05
    assert d.average_donation == 50.05

    d.add_donation(49.95)
    assert d.num_of_donations == 2
    assert d.sum_of_donations == 100.00
    assert d.average_donation == 50.00

    d.add_donation(20.211234)
    assert d.num_of_donations == 3
    assert d.sum_of_donations == 120.21
    assert d.average_donation == 40.07

    d.add_donation("39.79")
    assert d.num_of_donations == 4
    assert d.sum_of_donations == 160.00
    assert d.average_donation == 40.00

    with pytest.raises(ValueError):
        d.add_donation('x5z')

    with pytest.raises(ValueError):
        d.add_donation(-5.00)

    with pytest.raises(ValueError):
        d.add_donation(0)


def test_add_donation():
    dc = DonorCollection()
    dc.add_donation('William Shatner', 500.25)
    d = dc.get_donor('William Shatner')
    assert d.name == 'William Shatner'
    assert d.num_of_donations == 1
    assert d.sum_of_donations == 500.25
    assert d.average_donation == 500.25

    dc.add_donation('William Shatner', 100.75)
    d = dc.get_donor('William Shatner')
    assert d.name == 'William Shatner'
    assert d.num_of_donations == 2
    assert d.sum_of_donations == 601.00
    assert d.average_donation == 300.50

    dc.add_donation('Harold Tunas', 45.00)
    d = dc.get_donor('Harold Tunas')
    assert d.name == 'Harold Tunas'
    assert d.num_of_donations == 1
    assert d.sum_of_donations == 45.00
    assert d.average_donation == 45.00


def test_list_donors():
    dc = DonorCollection()
    assert dc.list_donors() == ''

    dc.add_donation('Patrick Stewart', 10000.00)
    dc.add_donation('Lavar Burton', 5000.00)
    dc.add_donation('Michael Dorn', 200.00)
    assert dc.list_donors() == 'Patrick Stewart\nLavar Burton\nMichael Dorn'


def test_get_donor():
    dc = DonorCollection()
    assert dc.get_donor('Leonard Nimoy') is None

    dc.add_donation('Leonard Nimoy', 50000.00)
    assert dc.get_donor('Leonard Nimoy') == Donor('Leonard Nimoy')


def test_has_donor():
    dc = DonorCollection()
    dc.add_donation('Chris Pine', 1.00)
    assert dc.has_donor('Chris Pine') == 'Chris Pine'
    assert dc.has_donor('CHRIS PINE') == 'Chris Pine'
    assert dc.has_donor('chris pine') == 'Chris Pine'
    assert dc.has_donor('James Dohan') is None
