# Author: Brian Minsk

# Some of the test functions below contain multiple tests of the same
# function. I decided not to proliferate test functions.

from mailroom_oo import *
import mailroom_oo_data_cli_main as cli
import random
import pytest

example_names = ("Gonzo Bonzo", "Action Sparxxx", "Ryce Alchemy", "Hoagy Ace")


def test_donorcollection_init():
    """ Test if a DonorCollection object is created correctly.
    """
    dc = DonorCollection()

    assert isinstance(dc, DonorCollection)


def test_donorcollection_is_existing_donor():
    dc = DonorCollection()

    # test if the argument is the appropriate type
    try:
        dc.is_existing_donor(1)
    except TypeError:
        pass
    else:
        assert False

    for name in example_names:
        donor = Donor(full_name=name)
        dc.add_donor(donor)

    assert dc.is_existing_donor("Action Sparxxx")
    assert not dc.is_existing_donor("Shokka Mystik")

    # get a random existing donor and test that it is found
    random_donor = random.sample(dc.donors, 1)[0]
    assert dc.is_existing_donor(random_donor)

    assert not dc.is_existing_donor(Donor("Action Sparxxx"))


def test_donorcollection_add_donor():
    dc = DonorCollection()

    donor1 = dc.add_donor("Action Sparxxx")
    assert isinstance(donor1, Donor)

    donor2 = Donor("Shokka Mystik")
    donor3 = dc.add_donor(donor2)
    assert donor2 == donor3


def test_donorcollection_add_donor_exceptions():
    dc = DonorCollection()
    donor = dc.add_donor("Action Sparxxx")

    # try adding a donor that already exists
    try:
        dc.add_donor(donor)
    except ValueError:
        pass
    else:
        assert False

    try:
        dc.add_donor("Action Sparxxx")
    except ValueError:
        pass
    else:
        assert False

    # test when not passing a string or Donor object
    try:
        dc.add_donor(1)
    except TypeError:
        pass
    else:
        assert False

    # test when passing an invalid name
    try:
        dc.add_donor("Buddy")
    except ValueError:
        pass
    else:
        assert False


def test_donorcollection_get_donor_names():
    dc = DonorCollection()
    for donor_name in example_names:
        dc.add_donor(donor_name)

    returned_names = dc.get_donor_names()
    for returned_name in returned_names:
        assert returned_name in example_names


def test_donor_init():
    donor1 = Donor("Action Sparxxx", 100)
    donor2 = Donor("Hoagy Ace", [20, 150, 30])

    assert donor1.full_name == "Action Sparxxx"
    assert donor2.full_name == "Hoagy Ace"

    dc1 = donor1.donations
    dc2 = donor2.donations

    assert dc1.donations[0].monetary_amount == 100
    assert dc2.donations[2].monetary_amount == 30


def test_donor_full_name_getter_setter():
    donor = Donor()
    donor.full_name = "Hoagy Ace"
    assert donor.full_name == "Hoagy Ace"

    try:
        donor.full_name = 1
    except TypeError:
        pass
    else:
        assert False

    try:
        donor.full_name = "HoagyAce"
    except ValueError:
        pass
    else:
        assert False


def test_donor_first_name_getter_setter():
    donor = Donor("Hoagy Ace")

    assert donor.first_name == "Hoagy"

    try:
        donor.first_name = "Gonzo"
    except AttributeError:
        pass
    else:
        assert False


def test_donor_last_name_getter_setter():
    donor = Donor("Hoagy Ace")

    assert donor.last_name == "Ace"

    try:
        donor.last_name = "Gonzo"
    except AttributeError:
        pass
    else:
        assert False


def test_donor_donations_getter_setter():
    example_donations = [20, 150, 30]
    donor = Donor("Hoagy Ace", example_donations)
    donations_object = donor.donations

    for i, donation in enumerate(donations_object.donations):
        assert donation.monetary_amount == example_donations[i]

    # May seem a bit counter-intuitive but this adds to the existing donations.
    donor.donations = 50
    example_donations.append(50)
    for i, donation in enumerate(donations_object.donations):
        assert donation.monetary_amount == example_donations[i]
    
    donor.donations = (100, 60)
    example_donations.append(100)
    example_donations.append(60)
    for i, donation in enumerate(donations_object.donations):
        assert donation.monetary_amount == example_donations[i]


def test_donor_create_report_row():
    donor = Donor("Hoagy Ace", [20, 150, 30, 500, 700])

    assert donor.create_report_row() == "Hoagy Ace                  $    1400.00          5  $      280.00"


def test_donor_thank_you_message():
    donor = Donor("Hoagy Ace", [20, 150, 30, 500, 700])
    assert donor.thank_you_message() == "\nDear Hoagy Ace,\n     Thank you very much for your generous donation of $700.00.\n     WINNING!\n"


def test_donor_sort():
    """ Build a donor collection with donors with a random number of donations
    for each donor, with random donation amounts and test sorting, non-reversed
    and reversed.
    """

    dc = DonorCollection()

    for name in example_names:
        r = random.randint(0, 5)
        donor = Donor(name)
        for i in range(0, r):
            donor.donations.add_donation(random.randint(50, 1000))
        dc.add_donor(donor)
        print(donor.donations.donations)

    sorted_donors = sorted(dc.donors, key=Donor.sort_key, reverse=False)

    previous_sum = 0
    for donor in sorted_donors:
        current_sum = donor.donations.sum()
        assert current_sum >= previous_sum
        previous_sum = current_sum

    sorted_donors = sorted(dc.donors, key=Donor.sort_key, reverse=True)

    previous_sum = 1000000000000000000000  # some arbitrarily large number
    for donor in sorted_donors:
        current_sum = donor.donations.sum()
        assert current_sum <= previous_sum
        previous_sum = current_sum


def test_donor_test_name():
    donor = Donor()

    assert donor.test_name("Robyn Banks")
    assert donor.test_name("robyn banks")
    with pytest.raises(ValueError):
        assert not donor.test_name("RobynBanks")
        assert not donor.test_name("Robyn  Banks")


def test_donationcollection_init():
    dc = DonationCollection()
    assert isinstance(dc, DonationCollection)


def test_donationcollection_add_donation():
    """ Also tests add_donations()
    """
    dc = DonationCollection()
    dc.add_donation(50)
    assert dc.donations[0].monetary_amount == 50
    dc.add_donations((40, 30, 20))
    assert dc.donations[1].monetary_amount == 40
    assert dc.donations[2].monetary_amount == 30
    assert dc.donations[3].monetary_amount == 20


def test_donationcollection_average():
    donations = [50, 40, 30, 20]
    dc = DonationCollection(donations)
    assert float(dc.average()) == sum(donations) / len(donations)
    donations.append(35.9)
    dc.add_donation(35.9)
    assert float(dc.average()) == sum(donations) / len(donations)


def test_donationcollection_sum():
    donations = [50, 40, 30, 20]
    dc = DonationCollection(donations)
    assert float(dc.sum()) == sum(donations)
    donations.append(35.9)
    dc.add_donation(35.9)
    assert float(dc.sum()) == sum(donations)


def test_donation_init():
    donation = Donation(monetary_amount=50)
    assert isinstance(donation, Donation)
    assert donation.monetary_amount == Decimal(50)


def test_donation_monetary_amount_getter_setter():
    donation = Donation()
    donation.monetary_amount = 50
    assert donation.monetary_amount == Decimal(50)


def test_donation_currency_getter_setter():
    donation = Donation()
    donation.currency = "THB"
    assert donation.currency == "THB"


def test_donation_get_formatted_donation_amount():
    donation1 = Donation(50.325)
    assert donation1.get_formatted_donation_amount() == "50.33"
    donation2 = Donation(50.324)
    assert donation2.get_formatted_donation_amount(with_sign=True) == "$50.32"

    try:
        donation_thb = Donation(50.325, "THB")
        assert donation_thb.get_formatted_donation_amount()
    except NotImplementedError:
        pass
    else:
        assert False
