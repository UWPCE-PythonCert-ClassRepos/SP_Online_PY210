
import pytest
from donor_models import *


# Testing existing name
def test_thank_you_note(capfd):

    a = Donor("Tom Hanks")
    a.ty_note()
    captured = capfd.readouterr()
    assert captured.out == "\nHello Tom Hanks, thank you for your generous donation of $1500 to support our cause.\n"

# Testing wrong name
def test_thank_you_note_failure(capfd):
    a = Donor("Kevin")
    a.ty_note()
    captured = capfd.readouterr()
    assert captured.out == "\nEntered >> Kevin\n\nThe name you entered is not on the list!\n"


def test_list_through_new_donation(capfd):
    a = Donor("list")
    a.new_donation()
    captured = capfd.readouterr()
    assert "Tom Hanks" in captured.out
    assert "Kevin" not in captured.out

def test_report(capfd):
    DonorCollection.report()
    captured = capfd.readouterr()
    assert "Tom Hanks" in captured.out
    assert "Kevin" not in captured.out
    assert "1500" in captured.out
    assert "33333" not in captured.out


# Using existing name, ignoring donation entery
def test_new_donation(capfd):
    a = Donor("Tom Hanks")
    a.new_donation()
    captured = capfd.readouterr()
    assert "Please enter the donation amount: " in captured.out
    assert "The donation amount has been incorrect or not entered" in captured.out
