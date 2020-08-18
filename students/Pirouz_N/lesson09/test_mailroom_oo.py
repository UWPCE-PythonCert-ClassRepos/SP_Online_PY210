"""
test code for circle.py
"""

import pytest
import os
from donor_models import *


# Donor class tests
def test_create_donor():
    """Testing donor initializer populates the attributes."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    assert donor.name != 'John Smithy'
    assert donor.name == 'John Smith'
    assert donor.donations != [1000.0, 2000.01]
    assert donor.donations == [1000.0, 2000.0]


def test_add_donation():
    """Testing adding donation is functioning as intended."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    assert donor.donations != [1000.0, 2000.01]
    assert donor.donations == [1000.0, 2000.0]
    donor.add_donation(3000.0)
    assert donor.donations == [1000.0, 2000.0, 3000.0]
    with pytest.raises(TypeError):
        donor.add_donation(3000)
    with pytest.raises(TypeError):
        donor.add_donation('3000')
    with pytest.raises(TypeError):
        donor.add_donation([3000.0])
    with pytest.raises(ValueError):
        donor.add_donation(-10000.0)
    with pytest.raises(ValueError):
        donor.add_donation(0.0)
    with pytest.raises(ValueError):
        donor.add_donation(float('inf'))


def test_all_properties_are_read_only():
    """Testing four class properties are read only since based on current program flow there is no need for setters."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    with pytest.raises(AttributeError):
        donor.name = 'Jake Smith'
    with pytest.raises(AttributeError):
        donor.donations = [10000.0, 20000.0]
    with pytest.raises(AttributeError):
        donor.donations_sum = sum([10000.0, 20000.0])
    with pytest.raises(AttributeError):
        donor.donations_average = sum([10000.0, 20000.0]) / 2


def test_check_name():
    """Testing static method check name."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    with pytest.raises(TypeError):
        donor.check_name(10000)
    with pytest.raises(TypeError):
        donor.check_name(100.0)
    with pytest.raises(TypeError):
        donor.check_name(['Name'])
    with pytest.raises(ValueError):
        donor.check_name('')


def test_check_donation():
    """Testing static method check donation."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    with pytest.raises(TypeError):
        donor.check_donation(10000)
    with pytest.raises(TypeError):
        donor.check_donation('1110.0')
    with pytest.raises(TypeError):
        donor.check_donation([1000.00])
    with pytest.raises(ValueError):
        donor.check_donation(-10000.0)
    with pytest.raises(ValueError):
        donor.check_donation(0.0)
    with pytest.raises(ValueError):
        donor.check_donation(float('inf'))


def test_check_donation_list():
    """Testing method check donation list."""
    with pytest.raises(TypeError):
        Donor.check_donation_list(10000)
    with pytest.raises(TypeError):
        Donor.check_donation_list(10000)
    with pytest.raises(TypeError):
        Donor.check_donation_list(None)
    with pytest.raises(TypeError):
        Donor.check_donation_list([10000, 12222.9])
    with pytest.raises(ValueError):
        Donor.check_donation_list([-10000.0, 12222.9])
    with pytest.raises(ValueError):
        Donor.check_donation_list([0.0, 12222.9])
    with pytest.raises(ValueError):
        Donor.check_donation_list([float('inf'), 12222.9])


def test_magic_method_equals():
    """Testing method that checks magic method equals."""
    donor = Donor('John Smith', [1000.0, 2000.0])
    assert donor == Donor('John Smith', [1000.0, 2000.0])
    assert donor != Donor('John Smith', [1000.0, 2000.01])
    assert donor != Donor('John Smith', [1000.01, 2000.0])
    assert donor != Donor('John Smith', [1000.0, 2000.0, 2003.0])
    assert donor != Donor('John Smithy', [1000.0, 2000.0])
    assert donor != Donor('John Smith', [1000.0])
    with pytest.raises(TypeError):
        donor == 1000
    with pytest.raises(TypeError):
        donor == 'testing'
    with pytest.raises(TypeError):
        donor == None
    with pytest.raises(TypeError):
        donor == ('John Smith', [1000.0, 2000.0])


# DonorCollection class tests ones not specifically included in the functional testing section below
def test_donor_collection_init():
    """Testing donner collection init function."""
    donor_db = [
        ('William Gates, III', [653772.32, 12.17]),
        ('Jeff Bezos', [877.33]),
        ('Paul Allen', [663.234, 43.87, 1.32]),
        ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
        ('Jayz', [999.9, 100.0, 100.0]),
        ('Beyonce', [1000.0, 100.0]),
        ('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
    ]
    donors = DonorCollection(donor_db)
    assert donors.donors == [Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
                             Donor('William Gates, III', [653772.32, 12.17]),
                             Donor('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                             Donor('Jayz', [999.9, 100.0, 100.0]),
                             Donor('Beyonce', [1000.0, 100.0]),
                             Donor('Jeff Bezos', [877.33]),
                             Donor('Paul Allen', [663.234, 43.87, 1.32]),
                             ]


def test_create_table():
    """Testing create table from donors collection method."""
    donor_db = [
        ('William Gates, III', [653772.32, 12.17]),
        ('Jeff Bezos', [877.33]),
        ('Paul Allen', [663.234, 43.87, 1.32]),
        ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
        ('Jayz', [999.9, 100.0, 100.0]),
        ('Beyonce', [1000.0, 100.0]),
        ('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
    ]
    donors = DonorCollection(donor_db)
    donors.add_donor_or_donation('John Smith', 100.0)
    new_db = [('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
              ('William Gates, III', [653772.32, 12.17]),
              ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
              ('Jayz', [999.9, 100.0, 100.0]),
              ('Beyonce', [1000.0, 100.0]),
              ('Jeff Bezos', [877.33]),
              ('Paul Allen', [663.234, 43.87, 1.32]),
              ('John Smith', [100.0]),
    ]
    assert donors.create_donor_table() == new_db


def test_thank_all_donors():
    """Testing writing tank you to all donors is implemented correctly."""
    donor_db = [
        ('William Gates, III', [653772.32, 12.17]),
        ('Jeff Bezos', [877.33]),
        ('Paul Allen', [663.234, 43.87, 1.32]),
        ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
        ('Jayz', [999.9, 100.0, 100.0]),
        ('Beyonce', [1000.0, 100.0]),
        ('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
    ]
    donors = DonorCollection(donor_db)
    assert donors.thank_all_donors() == '\n'.join([donor.generate_letter() for donor in donors.donors]) + '\n'


# Program functionality test
@pytest.fixture
def donors_collection():
    """Setting up donor collection."""
    donor_db = [
        ('William Gates, III', [653772.32, 12.17]),
        ('Jeff Bezos', [877.33]),
        ('Paul Allen', [663.234, 43.87, 1.32]),
        ('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
        ('Jayz', [999.9, 100.0, 100.0]),
        ('Beyonce', [1000.0, 100.0]),
        ('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
    ]
    donors = DonorCollection(donor_db)
    return donors


def test_checking_donor_exists_1(donors_collection):
    """Checking Donor object is in collection."""
    assert Donor('Melinda Gates', [10000000.0, 1000000.0, 999999.0]) not in donors_collection
    assert Donor('Melinda Gates', [10000000.0, 1000000.0]) not in donors_collection
    assert Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]) in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0]) in donors_collection
    assert Donor('Beyonce', [1000.0, 200.0]) not in donors_collection
    assert Donor('Beyonce1', [1000.0, 100.0]) not in donors_collection
    assert Donor('William Gates, III', [653772.32, 12.17]) in donors_collection
    assert Donor('William Gates, III', [653772.32, 12.171]) not in donors_collection


def test_checking_donor_exists_2(donors_collection):
    """Checking donor name is in collection."""
    assert 'William Gates, III' in donors_collection
    assert 'Melinda Gates' in donors_collection
    assert 'Beyonce'in donors_collection
    assert 'John Smith' not in donors_collection
    assert 'Jayzy' not in donors_collection


def test_adding_donor_or_donation_1(donors_collection):
    """Checking donor or donation addition by checking donor name is in collection after addition."""
    assert 'John Smith' not in donors_collection
    donors_collection.add_donor_or_donation('John Smith', 10000.2)
    assert 'John Smith' in donors_collection
    assert Donor('Warren Buffet', [11212.00]) not in donors_collection
    donors_collection.add_donor_or_donation('Warren Buffet', 11212.00)
    assert Donor('Warren Buffet', [11212.00]) in donors_collection


def test_adding_donor_or_donation_2(donors_collection):
    """Checking donor or donation addition by checking Donor object is in collection after addition."""
    assert 'Beyonce' in donors_collection
    donors_collection.add_donor_or_donation('Beyonce', 10000.2)
    assert 'Beyonce' in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0]) not in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0, 10000.2]) in donors_collection
    donors_collection.add_donor_or_donation('Beyonce', 10000.3)
    assert 'Beyonce' in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0, 10000.2]) not in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0, 10000.2, 10000.4]) not in donors_collection
    assert Donor('Beyonce', [1000.0, 100.0, 10000.2, 10000.3]) in donors_collection


def test_adding_donor_or_donation_3(donors_collection):
    """Checking acceptable donation amounts are floats only."""
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation('Melinda Gates', 100)
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation('Melinda Gates', [1000])
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation('Melinda Gates', "100")


def test_adding_donor_or_donation_4(donors_collection):
    """Checking acceptable donor names are strings only."""
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation(100, 100.0)
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation(100.0, 100.0)
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation(['Melinda Gates'], 100.0)


def test_adding_donor_or_donation_5(donors_collection):
    """Checking acceptable donation values are above zero and are not infinity."""
    with pytest.raises(ValueError):
        donors_collection.add_donor_or_donation('Melinda Gates', -100.0)
    with pytest.raises(ValueError):
        donors_collection.add_donor_or_donation('Melinda Gates', 0.0)
    with pytest.raises(TypeError):
        donors_collection.add_donor_or_donation('Melinda Gates', 0)
    with pytest.raises(ValueError):
        donors_collection.add_donor_or_donation('Melinda Gates', float('inf'))


def test_adding_donor_or_donation_6(donors_collection):
    """Checking contents of letter after donation of new donor."""
    assert 'John Smith' not in donors_collection
    new_donor, letter = donors_collection.add_donor_or_donation('John Smith', 10000.2)
    assert new_donor
    assert 'John Smith' in letter
    assert '10000.2' in letter
    assert '1 ' in letter


def test_adding_donor_or_donation_7(donors_collection):
    """Checking contents of letter after donation of existing donor."""
    assert 'John Smith' not in donors_collection
    new_donor, letter = donors_collection.add_donor_or_donation('Melinda Gates', 10000.2)
    assert not new_donor
    assert 'Melinda Gates' in letter
    assert str(sum([10000000.0, 1000000.0, 1000020.0]) + 10000.2) in letter
    assert '4 ' in letter


def test_adding_donor_or_donation_8(donors_collection):
    """Checking order of donors after creation of the collection object."""
    assert donors_collection.donors == [Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
                                        Donor('William Gates, III', [653772.32, 12.17]),
                                        Donor('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                                        Donor('Jayz', [999.9, 100.0, 100.0]),
                                        Donor('Beyonce', [1000.0, 100.0]),
                                        Donor('Jeff Bezos', [877.33]),
                                        Donor('Paul Allen', [663.234, 43.87, 1.32]),
                                        ]


def test_adding_donor_or_donation_9(donors_collection):
    """Checking order of donors after adding a donor."""
    new_donor, letter = donors_collection.add_donor_or_donation('John Smith', 10000000000.2)
    assert donors_collection.donors == [Donor('John Smith', [10000000000.2]),
                                        Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
                                        Donor('William Gates, III', [653772.32, 12.17]),
                                        Donor('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                                        Donor('Jayz', [999.9, 100.0, 100.0]),
                                        Donor('Beyonce', [1000.0, 100.0]),
                                        Donor('Jeff Bezos', [877.33]),
                                        Donor('Paul Allen', [663.234, 43.87, 1.32]),
                                        ]


def test_adding_donor_or_donation_10(donors_collection):
    """Checking order of donors after adding a donor."""
    new_donor, letter = donors_collection.add_donor_or_donation('John Smith', 3000.2)
    assert donors_collection.donors == [Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
                                        Donor('William Gates, III', [653772.32, 12.17]),
                                        Donor('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                                        Donor('John Smith', [3000.2]),
                                        Donor('Jayz', [999.9, 100.0, 100.0]),
                                        Donor('Beyonce', [1000.0, 100.0]),
                                        Donor('Jeff Bezos', [877.33]),
                                        Donor('Paul Allen', [663.234, 43.87, 1.32]),
                                        ]


def test_adding_donor_or_donation_11(donors_collection):
    """Checking order of donors after an existing donor makes a donation."""
    new_donor, letter = donors_collection.add_donor_or_donation('Beyonce', 10000000.2)
    assert donors_collection.donors == [Donor('Melinda Gates', [10000000.0, 1000000.0, 1000020.0]),
                                        Donor('Beyonce', [1000.0, 100.0, 10000000.2]),
                                        Donor('William Gates, III', [653772.32, 12.17]),
                                        Donor('Mark Zuckerberg', [1663.23, 4300.87, 10432.0]),
                                        Donor('Jayz', [999.9, 100.0, 100.0]),
                                        Donor('Jeff Bezos', [877.33]),
                                        Donor('Paul Allen', [663.234, 43.87, 1.32]),
                                        ]


def test_list_donors(donors_collection):
    """Checking donor list creation."""
    assert 'Jeff Bezos                    \t\n' in donors_collection.list_of_donor_names()
    assert 'Melinda Gates                 \t\n' in donors_collection.list_of_donor_names()
    assert 'Beyonce                       \t\n' in donors_collection.list_of_donor_names()
    assert 'Jayz                          \t\n' in donors_collection.list_of_donor_names()
    assert 'Donor Name                    \t\n' in donors_collection.list_of_donor_names()
    assert '---------------------------------\n' in donors_collection.list_of_donor_names()
    assert 'John Smith                    \t\n' not in donors_collection.list_of_donor_names()
    assert 'Warren Buffet                 \t\n' not in donors_collection.list_of_donor_names()
    assert 'Jayzy                         \t\n' not in donors_collection.list_of_donor_names()
    assert 'Jeff Bezoz                    \t\n' not in donors_collection.list_of_donor_names()


def test_donor_report_1(donors_collection):
    """Checking donor names on the report creation."""
    assert 'Jeff Bezos                    \t' in donors_collection.report_all_donors()
    assert 'Melinda Gates                 \t' in donors_collection.report_all_donors()
    assert 'Beyonce                       \t' in donors_collection.report_all_donors()
    assert 'Jayz                          \t' in donors_collection.report_all_donors()
    assert 'John Smith                    \t' not in donors_collection.report_all_donors()
    assert 'Warren Buffet                 \t' not in donors_collection.report_all_donors()
    assert 'Jayzy                         \t' not in donors_collection.report_all_donors()
    assert 'Jeff Bezoz                    \t' not in donors_collection.report_all_donors()


def test_donor_report_2(donors_collection):
    """Checking total donations on report creation."""
    assert str(round(sum([653772.32, 12.17]), 8)) in donors_collection.report_all_donors()
    assert str(round(sum([10000000.0, 1000000.0, 1000020.0]), 8)) in donors_collection.report_all_donors()
    assert str(round(sum([877.33]), 8)) in donors_collection.report_all_donors()
    assert str(round(sum([1000.0, 100.0]), 8)) in donors_collection.report_all_donors()

    assert str(round(sum([653772.32, 12.171]), 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([10000000.0, 1000000.0, 1000020.0, 100.0]), 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([877.33, 1.1]), 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([1000.0, 10.0]), 8)) not in donors_collection.report_all_donors()


def test_donor_report_3(donors_collection):
    """Checking number on report creation."""
    assert ' ' + str(len([653772.32, 12.17])) + '\t' in donors_collection.report_all_donors()
    assert ' ' + str(len([10000000.0, 1000000.0, 1000020.0])) + '\t' in donors_collection.report_all_donors()
    assert ' ' + str(len([877.33])) + '\t' in donors_collection.report_all_donors()

    assert ' ' + str(len([653772.32, 12.17, 1.0, 1029.02])) + '\t' not in donors_collection.report_all_donors()
    assert ' ' + str(len([])) + '\t' not in donors_collection.report_all_donors()
    assert ' ' + str(len([1.0, 2.0, 3.0, 4.0, 5.0])) + '\t' not in donors_collection.report_all_donors()


def test_donor_report_4(donors_collection):
    """Checking average donations on report creation."""
    assert str(round(sum([653772.32, 12.17]) / 2, 8)) in donors_collection.report_all_donors()
    assert str(round(sum([877.33]), 8)) in donors_collection.report_all_donors()
    assert str(round(sum([1000.0, 100.0]) / 2, 8)) in donors_collection.report_all_donors()

    assert str(round(sum([653772.32, 12.171]) / 2, 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([10000000.0, 1000000.0, 1000020.0, 100.0]) / 4, 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([877.33, 1.1]) / 2, 8)) not in donors_collection.report_all_donors()
    assert str(round(sum([1000.0, 10.0]) / 2, 8)) not in donors_collection.report_all_donors()