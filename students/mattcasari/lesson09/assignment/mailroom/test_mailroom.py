from donor_models import *

import pytest

##################
# Test Donor Class
##################

def test_donor_sets_full_name():
    donor_name = "Chuck Yeager"

    d = Donor(donor_name)

    assert donor_name == d.name

def test_donor_sets_full_name_with_title_case():
    donor_name = "chuck yeager"
    d = Donor(donor_name)

    assert "Chuck Yeager" == d.name

def test_donor_name_cannot_be_changed():
    d = Donor("Chuck Y")

    with pytest.raises(AttributeError):
        d.name = "Chuck D"

def test_donor_with_donation_sets_donation():
    d = Donor("Chuck Yeager", [500.00])

    assert  [500.00] == d.donations

def test_donor_with_multiple_initial_donations():
    d = Donor("Chuck Yeager", [500.00, 1500.00])

    assert d.donations == [500.00, 1500.00]

def test_donor_add_donation_fails_for_invalid_value():
    d = Donor("Chuck Yeager")

    with pytest.raises(ValueError):
        d.add_donation("You really augered that one in!")

def test_donor_add_donation():
    d = Donor("Test Donor")

    amount1 = 324.43
    amount2 = 54.94

    d.add_donation(amount1)
    d.add_donation(amount2)

    assert [amount1, amount2] == d.donations

def test_donor_total_donations():
    d = Donor("Test Donor")

    amount1 = 100.00
    amount2 = 200.00

    d.add_donation(amount1)
    d.add_donation(amount2)

    assert 300.00 == d.donation_total

def test_donor_num_donations():
    d = Donor("Test Donor")

    amounts = [100.00, 200.00, 300.00]

    for amount in amounts:
        d.add_donation(amount)

    assert 3 == d.num_donations

def test_donor_average_donation():
    d = Donor("Test Donor")

    amounts = [100.00, 200.00, 300.00]

    for amount in amounts:
        d.add_donation(amount)

    assert 200.00 == d.average_donation

def test_donor_average_if_no_donations():
    d = Donor("Test Donor")

    assert 0.00 == d.average_donation

def test_donor_less_than():
    d1 = Donor("T D1")
    d2 = Donor("T D2")

    d1.add_donation(100.00)
    d2.add_donation(200.00)

    assert d1 < d2

def test_donor_greater_than():
    d1 = Donor("T D1")
    d2 = Donor("T D2")

    d1.add_donation(100.00)
    d2.add_donation(200.00)

    assert d2 > d1

def test_sort_list_of_donors_by_total():
    d1 = Donor("T D1")
    d2 = Donor("T D2")
    d3 = Donor("T D3")
    d4 = Donor("T D4")

    d1.add_donation(100.00)
    d2.add_donation(200.00)
    d2.add_donation(300.00)
    d3.add_donation(400.00)
    d4.add_donation(450.00)

    d = [d1, d2, d3, d4]

    print(d)
    d.sort(reverse=True)
    print(d)

    assert [d2, d4, d3, d1] == d

def test_donor_repr():
    d1 = Donor("Mel C")
    d2 = Donor("Mel B")

    d1.add_donation(1000.00)
    d2.add_donation(2000.00)

    assert "Mel C" == repr(d1)
    assert "Mel B" == repr(d2)

def test_donor_last_donation():
    d1 = Donor("Mel C")
    d1.add_donation(400.00)
    d1.add_donation(1000.00)

    assert 1000.00 == d1.last_donation

def test_donor_create_thank_you_email():
    d1 = Donor("Geri H")

    d1.add_donation(1500.00)
    d1.add_donation(1000.00)

    expected_email = (
    "Dear Geri H,\n\n"
    "Thank you for your last donation of $1000.00.\n"
    "You have contributed a total of $2500.00 over 2 donation(s).\n"
    "Your generosity is appreciated.\n"
    "\nSincerely,\n"
    "-The Team\n\n"
    )

    assert  expected_email == d1.thank_you_email()

def test_donor_collection_thank_you_letter():
    
    expected_letter = (
    """\nDear Geri H,\n"""
    """Thank you for your recent donation of $123.45. """
    """Your donation will help us purchase a taxidermied seagull.\n"""
    """Please consider donating again at your earliest convenience.\n\n"""
    """Sincerely,\n"""
    """The Human Fund\n"""
    )

    d1 = Donor("Geri H")

    d1.add_donation(123.45)

    assert expected_letter == d1.thank_you_letter()

##############################
# Test Donor Collections Class
##############################
def test_donor_collection_init_empty():
    dc = DonorCollection()

    assert [] == dc._donors

def test_donor_collection_add_donor():
    d1 = Donor("Test Donor1")
    d2 = Donor("Test Donor2")

    dc = DonorCollection()

    dc.add_donor(d1)
    dc.add_donor(d2)

    assert [d1,d2] == dc._donors

def test_donor_collection_add_donor_fails_for_non_donor_class():
    dc = DonorCollection()

    with pytest.raises(TypeError):
        dc.add_donor(123.4)

def test_donor_collection_list_donors():
    d1 = Donor("Mel B")
    d2 = Donor("Victoria B")

    dc = DonorCollection()

    dc.add_donor(d1)
    dc.add_donor(d2)

    assert [d1, d2] == dc.donor_list

def test_donor_collection_add_donor_already_exists():
    d1 = Donor("Mel B")
    d2 = Donor("Victoria B")

    dc = DonorCollection()

    dc.add_donor(d1)
    dc.add_donor(d2)

    with pytest.raises(ValueError):
        dc.add_donor(d1)
    
    assert [d1, d2] == dc.donor_list

def test_donor_collection_add_donor_already_exists_append_new_amount():
    print("Testing dc donor already exists")
    dc = DonorCollection()
    dc.add_donor(Donor("Mel B", [400.00]))
    dc.add_donor(Donor("Mel C", [400.00]))
    dc.add_donor(Donor("Mel B", [600.00]))

    assert 600.00 == dc.donor_list[0].last_donation
    print(dc.donor_list[0])
    assert 1000.00 == dc.donor_list[0].donation_total

def test_donor_collection_add_donor_sorts_by_total():
    d1 = Donor("Scary Spice")
    d1.add_donation(1000.00)

    d2 = Donor("Baby Spice")
    d2.add_donation(2000.00)

    d3 = Donor("Sporty Spice")
    d3.add_donation(500.00)

    d4 = Donor("Ginger Spice")
    d4.add_donation(1500.00)

    d5 = Donor("Posh Spice")
    d5.add_donation(1300.00)

    dc = DonorCollection()

    dc.add_donor(d1)
    dc.add_donor(d2)
    dc.add_donor(d3)
    dc.add_donor(d4)
    dc.add_donor(d5)

    assert [d2, d4, d5, d1, d3] == dc.donor_list

def test_donor_collection_max_name_length():
    d1 = Donor("Scary Spice")
    d2 = Donor("Baby Spice")
    d3 = Donor("Sporty Spice")
    d4 = Donor("Ginger Spice")
    d5 = Donor("Posh Spice")

    dc = DonorCollection()
    dc.add_donor(d1)
    dc.add_donor(d2)
    dc.add_donor(d3)
    dc.add_donor(d4)
    dc.add_donor(d5)

    assert 12 == dc.max_name_length

def test_generate_report():
    d1 = Donor("Ginger Spice")
    d1.add_donation(1000.00)
    d1.add_donation(2000.00)

    d2 = Donor("Scary Spice")
    d2.add_donation(1500.00)
    d2.add_donation(2500.00)

    dc = DonorCollection()
    dc.add_donor(d1)
    dc.add_donor(d2)

    print(dc.generate_report())

    report = (" Donor Name   | Total Given | Num Gifts | Average Gift\n"
            "------------------------------------------------------\n"
            "Scary Spice    $     4000.00           2 $     2000.00\n"
            "Ginger Spice   $     3000.00           2 $     1500.00")

    assert report == dc.generate_report()

# def test_donor_collection_repr():
#     d1 = Donor("Scary Spice")
#     d2 = Donor("Baby Spice")
#     d3 = Donor("Sporty Spice")

#     dc = DonorCollection()
#     dc.add_donor(d1)
#     dc.add_donor(d2)
#     dc.add_donor(d3)

#     assert ["Scary Spice", "Baby Spice", "Sporty Spice"] == repr(dc)