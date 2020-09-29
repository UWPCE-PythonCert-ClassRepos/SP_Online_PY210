"""Unit tests for donor_models.py."""

from donor_models import Donor, DonorCollection
from cli_main import *
import os

sample_donations = {"Rhianna": [747, 3030303, 1968950],
                    "Grumps": [5.99],
                    "EatPraySlay": [100000, 200000, 300000],
                    "Muir": [469503, 50000, 186409],
                    "Spacewalker": [4406, 342]}


def test_donor_type():
    """Donor is a valid class."""
    donor = Donor('test')
    assert type(donor) is Donor


def test_donor_attributes():
    """Donor attributes initialize correctly."""
    donor = Donor('test')
    assert donor.name == 'test'
    assert type(donor.donations) is list


def test_donor_sum_donations():
    """Calculate sum of donations as property."""
    donor = Donor('test', [50, 100, 150])
    assert donor.sum_donations == 300


def test_donor_num_donations():
    """Calculate num donations as property."""
    donor = Donor('test', [50, 100, 150])
    assert donor.num_donations == 3


def test_donor_avg_donation():
    """Calculate average donation as property."""
    donor = Donor('test', [50, 100, 150])
    assert donor.avg_donation == 100


def test_add_donation():
    """Add correct amount to the end of that donor's donation list"""

    donor = Donor('test', [50, 100, 150])
    donor.add_donation(300)
    assert donor.donations[-1] == 300
    assert len(donor.donations) == 4


def test_properties_update():
    """Properties update after a new donation is added."""
    donor = Donor('test', [50, 100, 150])
    donor.add_donation(300)
    assert donor.sum_donations == 600
    assert donor.num_donations == 4
    assert donor.avg_donation == 150


def test_write_letter():
    """Write letter to correct donor for most recent donation."""

    expected_text = "To the esteemed Megatron:\n\nThank you for your " \
                    "generous donation of $17.00. You're a champion!"
    donor = Donor("Megatron", [8, 17])
    assert donor.write_letter() == expected_text


def test_thank_all_1():
    """Create the correct number of files with the correct tiles."""

    donors = DonorCollection.from_dict(sample_donations)
    thank_all()
    txt_files = {f for f in os.listdir() if f.endswith('.txt')}
    expected_files = {donor + ".txt" for donor in donors.list()}
    assert len(txt_files) >= len(donors.list())
    assert expected_files.issubset(txt_files)


def test_thank_all_2():
    """Create files with the correct content."""

    donors = DonorCollection.from_dict(sample_donations)
    thank_all()
    with open("EatPraySlay.txt", 'r') as f:
        assert f.read() == "To the esteemed EatPraySlay:\n\nThank you for" \
                           " your generous donation of $300000.00. You're" \
                           " a champion!"


def test_create_report():
    """Ensure donor records are sorted correctly."""

    donors = DonorCollection.from_dict(sample_donations)

    # Create an ordered list of donor sums
    sum_list = [donor.sum_donations for donor in donors.sorted()]

    # Ensure each sum is greater or equal to than all subsequent sums
    for count, value in enumerate(sum_list):
        for x, y in enumerate(sum_list):
            assert not (x > count and y > value)


if __name__ == "__main__":
    test_donor_type()
    test_donor_attributes()
    test_donor_sum_donations()
    test_donor_num_donations()
    test_donor_avg_donation()
    test_add_donation()
    test_properties_update()
    test_write_letter()
    test_thank_all_1()
    test_thank_all_2()
    test_create_report()
