"""Unit tests for mailroom.py."""

from mailroom import *
import os


def update_all_records():
    """Updates all records as a helper to other functions."""

    for donor in donor_records:
        update_record(donor)


def test_store_donation():
    """Add correct amount to the end of that donor's donation list"""

    store_donation("EatPraySlay", 400000)
    assert donor_records["EatPraySlay"]["donations"][-1] == 400000


def test_update_record_1():
    """Create correct sum, numGifts and avgGift for new donor."""

    donor_records["Watson"] = {"name": "Watson", "donations": [10, 20, 30]}
    update_record("Watson")
    assert donor_records["Watson"]["sum"] == 60
    assert donor_records["Watson"]["numGifts"] == 3
    assert donor_records["Watson"]["avgGift"] == 20


def test_update_record_2():
    """Create correct sum, numGifts and avgGift after a new donation."""

    store_donation("Rhianna", 1000000)
    update_record("Rhianna")
    assert donor_records["Rhianna"]["sum"] == 6000000
    assert donor_records["Rhianna"]["numGifts"] == 4
    assert donor_records["Rhianna"]["avgGift"] == 1500000


def test_write_letter():
    """Write letter to correct donor for most recent donation."""

    expected_text = "To the esteemed Megatron:\n\nThank you for your " \
                    "generous donation of $17.00. You're a champion!"
    store_donation("Megatron", 17)
    assert write_letter("Megatron") == expected_text


def test_thank_all_1():
    """Create the correct number of files with the correct tiles."""

    thank_all()
    txt_files = {f for f in os.listdir() if f.endswith('.txt')}
    expected_files = {donor + ".txt" for donor in donor_records}
    assert len(txt_files) >= len(donor_records)
    assert expected_files.issubset(txt_files)


def test_thank_all_2():
    """Create files with the correct content."""

    store_donation("Bad Panda", 31)
    thank_all()
    with open("Bad Panda.txt", 'r') as f:
        assert f.read() == "To the esteemed Bad Panda:\n\nThank you for your" \
                           " generous donation of $31.00. You're a champion!"


def test_create_report():
    """Ensure donor records are sorted correctly."""

    update_all_records()

    # Create an ordered list of donor sums
    sum_list = [record[1]["sum"] for record in create_report()]

    # Ensure each sum is greater or equal to than all subsequent sums
    for count, value in enumerate(sum_list):
        for x, y in enumerate(sum_list):
            assert not (x > count and y > value)


if __name__ == "__main__":
    test_store_donation()
    test_update_record_1()
    test_update_record_2()
    test_write_letter()
    test_thank_all_1()
    test_thank_all_2()
    test_create_report()


"""
TO DO LATER:
get_donor_name should: # not testing inputs through unit testing yet
    return the correct list of donor names if the donor types list or List
    only allow alpha and basic punctuation
    raise the correct exception if a bad character is included

get_donation should: # not testing inputs through unit testing yet
    not allow negative numbers
    raise an exception if not given a float

thank_donor should: # depends on user inputs, which we're not testing yet
    print the expected text
    add the correct amount to the end of that donor's donation list
"""
