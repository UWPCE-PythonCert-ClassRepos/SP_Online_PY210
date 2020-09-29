'''
Unit tests for the object-oriented mailroom assignment.
'''

import pytest

from donor_models import Donor, DonorCollection

import os

#Tests for Donor class

def test_donor():
    d = Donor("Rei", [50])
    assert d.donations == [50]
    d = Donor("Rei", [50, 100])
    assert d.donations == [50, 100]
    with pytest.raises(TypeError):
        d = Donor(5, [50])
    with pytest.raises(TypeError):
        d = Donor("Rei", 50)
    with pytest.raises(ValueError):
        d = Donor("Rei", ["a"])

def test_add_donation():
    d = Donor("Rei", [50])
    d.add_donation(120)
    assert d.donations == [50, 120]
    with pytest.raises(ValueError):
        d.add_donation("abc")

def test_total_donations():
    d = Donor("Rei", [50])
    d.add_donation(50)
    assert d.total_donations == 100

def test_write_indiv_letter():
    d = Donor("Rei", [50])
    assert d.write_indiv_letter() == "Dear Rei, thank you for your generous donation of $50.00."


#Tests for DonorCollection class

def test_donor_collection():
    dc = DonorCollection()
    assert dc.collection == []

def test_add_donor():
    dc = DonorCollection()
    dc.add_donor("Rei", [50])
    assert dc.collection[0].name == "Rei"
    assert dc.collection[0].donations == [50]

def test_get_donor():
    dc = DonorCollection()
    dc.add_donor("Rei", [50])
    a = dc.get_donor("Rei")
    assert a.name == "Rei"
    assert a.donations == [50]
    assert dc.get_donor("Usagi") is False

def test_display_donors():
    dc = DonorCollection()
    dc.add_donor("Rei", [50])
    dc.add_donor("Usagi", [150])
    assert dc.display_donors() == "Rei: [50]\nUsagi: [150]\n"

def test_generate_report():
    dc = DonorCollection()
    dc.add_donor("Rei", [50])
    dc.add_donor("Usagi", [50, 150])
    dc.add_donor("Minako")
    result = dc.generate_report()
    assert "Donor Name               Total Given  Num Gifts         Average Gift" in result
    assert "Usagi                         200.00          2               100.00" in result
    assert "Rei                            50.00          1                50.00" in result
    assert "Minako                          0.00          0                 0.00" in result

def test_batch_letters():
    dc = DonorCollection()
    dc.add_donor("Rei", [50])
    dc.add_donor("Usagi", [50, 150])
    dc.batch_letters()
    assert os.path.isfile("Rei.txt") is True
    assert os.path.isfile("Usagi.txt") is True
    with open("Rei.txt", "r") as f:
        filetext = f.read()
        assert "Dear Rei," in filetext
        assert "Thank you for your donation of $50.00." in filetext
        assert "Your total donations to date are $50.00." in filetext
        assert "Thanks, the Management." in filetext