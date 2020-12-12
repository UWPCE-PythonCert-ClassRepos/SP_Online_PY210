"""
Test suite for donor_models.py
"""

import donor_models
import os
import pytest


def test_add_donor():
    donor = donor_models.Donor("Bill Gates")

    assert donor.name == "Bill Gates"

    assert donor.total_donations == 0
    assert donor.number_of_donations == 0
    assert donor.average_gift == 0.0


def test_add_single_donation():
    donor = donor_models.Donor("Bill Gates")

    donor.add_donations(100)
    assert donor.total_donations == 100.0
    assert donor.number_of_donations == 1
    assert donor.average_gift == 100.0

    # Check with string input
    donor.add_donations("100")
    assert donor.total_donations == 200.0
    assert donor.number_of_donations == 2
    assert donor.average_gift == 100.0

    # check for adding negative number
    with pytest.raises(ValueError):
        donor.add_donations(-100)

    # check for adding string
    with pytest.raises(ValueError):
        donor.add_donations("Donation")


def test_add_multiple_list_donations():
    donor = donor_models.Donor("Bill Gates")

    donor.add_donations([100, 200, 300])
    assert donor.total_donations == 600.0
    assert donor.number_of_donations == 3
    assert donor.average_gift == 200.0

    # check with string input
    donor.add_donations(["100", "200", "300"])
    assert donor.total_donations == 1200.0
    assert donor.number_of_donations == 6
    assert donor.average_gift == 200.0

    with pytest.raises(ValueError):
        donor.add_donations([100, -200, 300])

    with pytest.raises(ValueError):
        donor.add_donations(["100", "-200", "300"])

    with pytest.raises(ValueError):
        donor.add_donations([100, -200, "Donation"])


def test_add_multiple_tuple_donations():
    donor = donor_models.Donor("Bill Gates")

    donor.add_donations((100, 200, 300))
    assert donor.total_donations == 600.0
    assert donor.number_of_donations == 3
    assert donor.average_gift == 200.0

    # check with string input
    donor.add_donations(("100", "200", "300"))
    assert donor.total_donations == 1200.0
    assert donor.number_of_donations == 6
    assert donor.average_gift == 200.0

    with pytest.raises(ValueError):
        donor.add_donations((100, -200, 300))

    with pytest.raises(ValueError):
        donor.add_donations(("100", "-200", "300"))

    with pytest.raises(ValueError):
        donor.add_donations((100, -200, "Donation"))


def test_initialize_with_one_donation():
    donor = donor_models.Donor("Bill Gates", 100)
    assert donor.total_donations == 100.0
    assert donor.number_of_donations == 1
    assert donor.average_gift == 100.0


def test_initialize_with_multiple_donations():
    donor = donor_models.Donor("Bill Gates", [100, 200, 300])
    assert donor.total_donations == 600.0
    assert donor.number_of_donations == 3
    assert donor.average_gift == 200.0


def test_read_only_donor_attributes():
    donor = donor_models.Donor("Bill Gates")

    with pytest.raises(AttributeError):
        donor.total_donations = 100

    with pytest.raises(AttributeError):
        donor.number_of_donations = 100

    with pytest.raises(AttributeError):
        donor.average_gift = 100


def test_email_text():
    donor = donor_models.Donor("Bill Gates", 100)

    email_text_1 = donor.compose_email()

    print(email_text_1)

    exemplar_text_1 = "\nDear Bill Gates,\n Thank you for your generous\
 gift of $100.00!  It will help Local Charity achieve our mission.\n\
    Best regards,\n\
    Local Charity\n\n"

    assert email_text_1 == exemplar_text_1

    donor.add_donations(200)

    email_text_2 = donor.compose_email()

    exemplar_text_2 = "\nDear Bill Gates,\n Thank you for your generous\
 gift of $200.00!  It will help Local Charity achieve our mission.\n\
    Best regards,\n\
    Local Charity\n\n"

    assert email_text_2 == exemplar_text_2

    email_text_3 = donor.compose_email(0)  # check non-default email

    exemplar_text_3 = "\nDear Bill Gates,\n Thank you for your generous\
 gift of $100.00!  It will help Local Charity achieve our mission.\n\
    Best regards,\n\
    Local Charity\n\n"

    assert email_text_3 == exemplar_text_3


def test_add_donor_collection():
    donor_collection = donor_models.DonorCollection()

    assert len(donor_collection.donors) == 0

    donor = donor_models.Donor("Bill Gates")

    donor_collection.add_donor_object(donor)

    assert len(donor_collection.donors) == 1

    assert "Bill Gates" in donor_collection.donor_names

    donor_collection.add_donor("Willie Nelson")

    assert len(donor_collection.donors) == 2
    assert "Willie Nelson" in donor_collection.donor_names

    # check to see that commas are removed
    donor_collection.add_donor("William Gates, III")
    assert "William Gates III" in donor_collection.donor_names

    with pytest.raises(NameError):
        donor_collection.add_donor("Willie Nelson")


def test_get_donor_by_name():
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Willie Nelson")
    donor = donor_collection.get_donor_by_name("Willie Nelson")

    assert donor.name == "Willie Nelson"

    with pytest.raises(NameError):
        donor = donor_collection.get_donor_by_name("Chase Dullinger")


def test_add_dononation_to_donor_collection():
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Willie Nelson")
    donor_collection.add_donation_to_donor("Willie Nelson", 100)

    donor = donor_collection.get_donor_by_name("Willie Nelson")

    assert donor.total_donations == 100
    assert donor.number_of_donations == 1
    assert donor.average_gift == 100


def test_donor_list():
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Bill Gates")
    donor_collection.add_donor("Willie Nelson")

    exemplar_text = "\nCurrent donors are:\nBill Gates\nWillie Nelson\n"

    assert donor_collection.get_donor_list_text() == exemplar_text


def test_create_all_letters():
    """Test that all the expected letters were created on disk.
    Note that the letter text was tested in test_email_text
    """
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Bill Gates")
    donor_collection.add_donor("Willie Nelson")
    donor_collection.create_all_letters()
    for donor in donor_collection.donor_names:
        assert os.path.exists(f"{donor}.txt") is True


def test_create_report():
    """Test the create report function"""
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Paul Allen")
    donor_collection.add_donation_to_donor("Paul Allen", [663.23, 43.87, 1.32])
    text_string = donor_collection.create_report()
    reference_text = "Paul Allen                 $      708.42          3 \
 $      236.14"
    assert text_string.split("\n")[-2] == reference_text


def test_save_donation_db():
    """Test that donations can be saved
    """
    donor_collection = donor_models.DonorCollection()
    donor_collection.add_donor("Bill Gates", 100)
    donor_collection.add_donor("Willie Nelson", 200)
    donor_collection.add_donation_to_donor("Willie Nelson", 300)
    donor_collection.add_donor("Jeff Bezos")

    donor_collection.save_donor_db(filename="donor_db_test_save.txt")

    assert os.path.exists("donor_db_test.txt") is True


def test_read_donation_db():
    """Test that donations can be read"""
    donor_collection = donor_models.DonorCollection()
    donor_collection.read_donor_db(filename="donor_db_test_read.txt")
    assert "Bill Gates" in donor_collection.donor_names
    assert "Willie Nelson" in donor_collection.donor_names

    donor = donor_collection.get_donor_by_name("Willie Nelson")
    assert donor.total_donations == 500

    donor = donor_collection.get_donor_by_name("Jeff Bezos")
    assert donor.total_donations == 0
    assert donor.number_of_donations == 0
