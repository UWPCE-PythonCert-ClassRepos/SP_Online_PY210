#!/usr/bin/env python3
import pytest
import donor_models as dm
import cli_main as cm
import statistics as st

'''
Test for the object oriented version of the mailroom program.
'''

# instantiate inital classes to test
d1 = dm.Donor("Dude1")
d2 = dm.Donor("Dude2", [100.00])
d3 = dm.Donor("Dude3", [100.00, 200.00])
dc = dm.DonorCollection({
    d1.name:d1,
    d2.name:d2,
    d3.name:d3
})

email_string = (f"Dear {d3.display_name},\n\n"
           "It is with incredible gratitude that we accept your wonderfully "
           f"generous donation of ${d3.donations[-1]:,.2f}.  Your "
           "contribution will truly make a difference in the path forward "
           "towards funding our common goal."
           "\n\nEver Greatefully Yours,\n\n"
           "X" + ("_" * 20) + "\n")

def test_create_donor():
    assert d1.name == "dude1"
    assert d1.display_name == "Dude1"
    assert d1.donations == []
    assert d2.donations == [100.00]
    assert d3.donations == [100.00, 200.00]

def test_add_donation():
    with pytest.raises(TypeError):
        d1.add_donation("hello")
    with pytest.raises(ValueError):
        d1.add_donation(-200)
    d1.add_donation(10)
    d1.add_donation(20.0)
    assert d1.donations == [10, 20.0]

def test_donor_email_text():
    assert d3.email_text(-1) == email_string
    assert d3.email_text(50) == None

def test_donorcollection():
    # test if checks for invalid input
    with pytest.raises(TypeError):
        dm.DonorCollection("invalid")
    assert dc.names == [d1.name, d2.name, d3.name]
    assert dc.display_names == [d1.display_name, d2.display_name, d3.display_name]
    assert dc.donors[d1.name] == d1
    with pytest.raises(TypeError):
        dc.add_donor("not a Donor")
    d4 = dm.Donor("Dude4")
    dc.add_donor(d4)
    print(d4.__repr__)
    assert d4 in dc.donors.values()

def test_donorcollection_add_donation():
    dc.add_donation("Dude1", 500)
    print(dc.donors['dude1'].donations)
    assert dc.donors["dude1"].donations == [10, 20.0, 500]
    dc.add_donation("Dude5", 1)
    print(dc.donors.items())
    print(dc.donors['dude5'].donations)
    assert dc.donors['dude5'].donations == [1]

def test_report():
    dc.add_donation('Dude4', 5)
    report_string = ("\nDonor Name" + " "*15 + "|  Total Given  | Num Gifts |"
                     "   Average Gift\n")
    for donor in sorted(dc.donors.values(), reverse=True):
        report_string += (f"{donor.display_name:26}"
                        f"${sum(donor.donations):14,.2f}"
                        f"{len(donor.donations):11}  "
                        f"${st.mean(donor.donations):16,.2f}\n")
    print(report_string)
    assert "".join(dc.report()) == report_string
    print("".join(dc.report()))
