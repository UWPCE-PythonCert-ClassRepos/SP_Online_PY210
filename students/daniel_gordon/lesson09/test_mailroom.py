from donor_models import *

def test_donor():
    fred = Donor("Fred")
    crissy = Donor("Crissy", 30000)
    deon = Donor("Deon Smith", [4000, 2000, 7000])
    assert fred.name == "Fred"
    assert crissy.name == "Crissy"
    assert deon.name == "Deon Smith"