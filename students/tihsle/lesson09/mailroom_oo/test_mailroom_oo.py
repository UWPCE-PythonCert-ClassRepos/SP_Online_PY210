#!/usr/bin/env python3
from donor_models import  Donor, DonorCollection

#test Donor
def test_donor_init():
    d = Donor("Tom Thomas", 1000.0)
    assert d.name == "Tom Thomas"
    assert d.gifts == [1000.0]

def test_add_gift():
    d = Donor("Tom Thomas", 1000.0)
    d.add_gift(1000.0)
    assert d.gifts == [1000.0, 1000.0]

def test_other_methods():
    d = Donor("Tom Thomas", 1000.0)
    d.add_gift(1000.0)
    assert d.avg_gift() == 1000.0
    assert d.num_gifts() == 2
    assert d.total_gifts() == 2000.0

def test_thank_you():
    d = Donor("Tom Thomas", 1000.0)
    d.add_gift(1000.0)
    assert "Dear Tom Thomas," in d.send_thank_you()

#test DonorCollection
def test_list_donors():
    dc = DonorCollection()
    assert dc.list_donors() == 'William Gates, III\nMark Zuckerberg\nJeff Bezos\nPaul Allen\nJoe Smithe\n'

def test_report():
    dc = DonorCollection()
    report =  dc.report()
    assert "Donor Name     |    Total Given     |     Num Gifts      |    Average Gift" in report
    for patron in dc.donor_list:
        assert patron.name in report

#all together
test_donor_init()
test_add_gift()
test_other_methods()
test_thank_you()
test_list_donors()
test_report()
