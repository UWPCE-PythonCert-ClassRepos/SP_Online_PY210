from donor_models import Donor


def test_new_donor():
    d = Donor('John Smith')
    assert d.name == 'John Smith'

    d.name = 'Jane Doe'
    assert d.name == 'Jane Doe'


def test_add_donation():
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


