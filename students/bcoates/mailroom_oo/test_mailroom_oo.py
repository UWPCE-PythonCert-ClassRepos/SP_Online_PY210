#!/usr/bin/env python3

from donor_models import *

def test_new_donor():
    new_donor = Donor("John Doe")
    assert new_donor.full_name == "John Doe"
    assert new_donor.donations == []

def test_add_donation():
    new_donor = Donor("John Doe")
    new_donor.add_donation(50.75)
    assert new_donor.donations == [50.75]

def test_format_thank_you():
    new_donor = Donor("John Doe")
    new_donor.add_donation(50.75)
    print(new_donor.format_thank_you())
    assert new_donor.format_thank_you() == ("Dear John Doe,\n\n"
                                            "Thank you for your generous donation of $50.75!\n\n"
                                            "Sincerely,\n\n"
                                            "The Owners")

def test_donation_total():
    new_donor = Donor("John Doe")
    new_donor.add_donation(50.75)
    new_donor.add_donation(20.25)
    assert new_donor.donation_total == 71.00

def test_donation_count():
    new_donor = Donor("John Doe")
    new_donor.add_donation(50.75)
    new_donor.add_donation(20.25)
    assert new_donor.donation_count == 2

def test_donation_avg():
    new_donor = Donor("John Doe")
    new_donor.add_donation(50.75)
    new_donor.add_donation(20.25)
    assert new_donor.donation_avg == 35.50

def test_new_donor_collection():
    new_collection = DonorCollection()
    assert new_collection.donors == []

def test_add_donor_to_collection():
    new_collection = DonorCollection()   
    donor1 = Donor("John Doe")
    donor1.add_donation(20.00)
    new_collection.add_donor(donor1)
    assert new_collection.donors[0].full_name == "John Doe"

    # Ensure another donor with same name isn't added
    donor2 = Donor("John Doe")
    donor2.add_donation(20.00)
    new_collection.add_donor(donor2)
    print(new_collection.donors)
    assert len(new_collection.donors) == 1

def test_list_donors():
    new_collection = DonorCollection()   
    donor1 = Donor("John Doe")
    new_collection.add_donor(donor1)
    donor2 = Donor("Jane Doe")
    new_collection.add_donor(donor2)
    assert new_collection.list_donors() == "John Doe\nJane Doe\n"

def test_create_report():
    new_collection = DonorCollection() 
    donor1 = Donor("John Doe")
    donor1.add_donation(50.75)
    donor1.add_donation(20.25)
    new_collection.add_donor(donor1)

    donor2 = Donor("Jane Doe")
    donor2.add_donation(150.75)
    donor2.add_donation(120.25)
    new_collection.add_donor(donor2)
    assert (new_collection.create_report()) == [['Jane Doe', 271.0, 2, 135.5], 
                                                ['John Doe', 71.0, 2, 35.5]]


