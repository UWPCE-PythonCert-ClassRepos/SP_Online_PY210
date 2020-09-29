import pytest

from donor_models import Donor
from donor_models import DonorCollection


######
# Donor tests
######

def test_donor_constructor():

    '''
    Tests the Donor's class constructor
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    assert (d.donor_name == expected_donor)
    assert (len(d.donations) == 0)


def test_donor_add_new_donation():

    '''
    Tests the Donor method: adding a new donation amount
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    expected_donation_amount = 100.00
    d.add_donation(expected_donation_amount)
    assert (d.donations[-1] == expected_donation_amount)


def test_donor_total_donations():

    '''
    Tests the sum of donations is as expected
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    expected_donation_amount_1 = 100.00
    expected_donation_amount_2 = 200.00
    d.add_donation(expected_donation_amount_1, expected_donation_amount_2)
    assert (d.total_donations == expected_donation_amount_1 + expected_donation_amount_2)


def test_donor_get_list_of_donations():

    '''
    Tests that the expected donation list is returned
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    expected_donation_amount_1 = 100.00
    expected_donation_amount_2 = 200.00
    d.add_donation(expected_donation_amount_1, expected_donation_amount_2)
    expected_donation_list = [100.00, 200.00]
    assert (d.all_donations == expected_donation_list)


def test_donor_format_thank_you_note():

    '''
    Tests the thank you note is formatted as expected
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    expected_donation_amount = 100.00
    thank_you_note = d.format_thank_you_note(expected_donation_amount)
    assert (thank_you_note.startswith("Dear {}".format(expected_donor)))


def test_donor_number_of_donations():

    '''
    Tests the number of donations are as expected
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor(expected_donor)
    expected_donation_amount_1 = 100.00
    expected_donation_amount_2 = 200.00
    d.add_donation(expected_donation_amount_1, expected_donation_amount_2)
    assert (d.donation_count == 2)


######
# DonorCollection tests
######

def test_donor_collection_empty_constructor():

    '''
    Tests the constructor
    :return: nothing
    '''

    dc = DonorCollection()
    assert (len(dc.donors) == 0)


def test_donor_collection_add_donor():

    '''
    Tests the add donor method
    :return: nothing
    '''

    expected_donor = "Jinee"
    d = Donor("Jinee")
    d.add_donation(100.00)
    dc = DonorCollection()
    dc.add_donor(d)
    assert (dc.get_donors()[0].donor_name == expected_donor)


def test_donor_collection_create_report():

    '''
    Tests creating the report for the given donors
    :return: nothing
    '''

    expected_donor_1 = "Jinee"
    d_jinee = Donor(expected_donor_1)
    d_jinee.add_donation(100.00)

    expected_donor_2 = "Brother"
    d_brother = Donor("Brother")
    d_brother.add_donation(200.00)

    expected_donor_3 = "Mom"
    d_mom = Donor(expected_donor_3)
    d_mom.add_donation(300.00)

    dc = DonorCollection()
    dc.add_donor(d_jinee, d_brother, d_mom)

    report = dc.create_report()

    assert (expected_donor_1 in report)
    assert (expected_donor_2 in report)
    assert (expected_donor_3 in report)


def test_donor_collection_check_if_donor_present_true():

    '''
    Tests if the donor is present in the collection
    :return: nothing
    '''

    expected_donor_1 = "Jinee"
    d_jinee = Donor(expected_donor_1)
    d_jinee.add_donation(100.00)

    expected_donor_2 = "Brother"
    d_brother = Donor("Brother")
    d_brother.add_donation(200.00)

    dc = DonorCollection()
    dc.add_donor(d_jinee, d_brother)

    assert (dc.donor_present(expected_donor_1))







