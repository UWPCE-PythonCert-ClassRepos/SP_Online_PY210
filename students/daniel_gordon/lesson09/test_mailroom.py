from donor_models import *
import pytest


def thank_you(name, money):
    """Create thank you text"""
    return f"Thank you {name} for your generous donation of {money:.2f}"
    
def test_donor_init():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    assert fred.name == "Fred"
    assert crissy.name == "Crissy"
    assert deon.name == "Deon Smith"
    
    assert fred.donations == []
    assert crissy.donations == [3000]
    assert deon.donations == [4000, 2000, 7000]

def test_donor_add_donation():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    with pytest.raises(ValueError):
        fred.add_donation("ten thousand")
    fred.add_donation(3000)
    crissy.add_donation(2000)
    deon.add_donation(5000)
    assert len(fred.donations) == 1
    assert len(crissy.donations) == 2
    assert len(deon.donations) == 4

def test_donor_send_thank_you():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    with pytest.raises(IndexError):
        fred.thank_you()
    assert crissy.thank_you() == thank_you("Crissy", 3000)
    assert deon.thank_you() == thank_you("Deon Smith", 7000)
    
def test_donor_report_entry():
    fred = Donor("Fred")
    entry = fred.report_entry()
    print(entry)
    assert entry.startswith("Fred")
    assert entry.endswith("0.00")

    crissy = Donor("Crissy", 3000)
    entry = crissy.report_entry()
    print(entry)
    assert entry.startswith("Crissy")
    assert entry.endswith("3000.00")

    deon = Donor("Deon Smith", [4000, 2000, 7000])
    entry = deon.report_entry()
    print(entry)
    assert entry.startswith("Deon")
    assert entry.endswith("4333.33")

def test_donor_letter():
    fred = Donor("Fred")
    with pytest.raises(IndexError):
        letter = fred.letter()

    crissy = Donor("Crissy", 3000)
    letter = crissy.letter()
    print(letter)
    assert letter.startswith("Dear Crissy")
    assert "3000.00" in letter

    deon = Donor("Deon Smith", [4000, 2000, 7000])
    letter = deon.letter()
    print(letter)
    assert letter.startswith("Dear Deon")
    assert "7000.00" in letter
    
def test_donor_collection_report():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    donors = DonorCollection(fred)
    donors.add_donor(crissy)
    donors.add_donor(deon)
    report = donors.report()
    print(report)
    assert report.startswith("Donor")
    assert report.index("Fred") > report.index("Crissy")
    assert report.index("Crissy") > report.index("Deon")
    report_lines = report.splitlines()
    assert len(report_lines) == 5

def test_donor_collection_from_list():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    donors = DonorCollection.from_list([fred, crissy, deon])
    report = donors.report()
    print(report)
    assert report.startswith("Donor")
    assert report.index("Fred") > report.index("Crissy")
    assert report.index("Crissy") > report.index("Deon")
    report_lines = report.splitlines()
    assert len(report_lines) == 5

def test_donor_collection_loop():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 3000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    items = [fred, crissy, deon]
    donors = DonorCollection.from_list(items)
    for item, donor in zip(items, donors):
        assert item == donor
