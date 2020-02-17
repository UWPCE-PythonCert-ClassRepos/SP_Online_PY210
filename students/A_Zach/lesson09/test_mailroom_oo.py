import pytest
from donor_models import *
import os

d = Donor('Fred', [1,2,3])
dc = DonorCollection()
dc.new_donor(d)

def test_donor_input():
    """test that names and donations are being created properly"""
    assert d.name == 'Fred'
    assert d.donation == [1,2,3]


def test_donation_type():
    """tests that a donation must be input as a list"""
    with pytest.raises(TypeError):
        Donor('Fred',(1,2,3))
    
    with pytest.raises(TypeError):
        Donor('Fred','1, 2, 3')
        
    with pytest.raises(TypeError):
        Donor('Fred',3)


def test_new_donation():
    """Tests that a new donation is added to an existing donor"""
    d.new_donation(4)
    assert d.donation == [1,2,3,4]
    with pytest.raises(TypeError):
        d.new_donation([2, '1','d'])
    with pytest.raises(TypeError):
        d.new_donation('3')


def test_new_donor():
    """Tests that a new donor name is added to the list correctly"""
    assert dc.donor_list[0].name == 'Fred'
    assert dc.donor_list[0].donation == [1,2,3,4,]


def test_sort_donation():
    """Tests that a new donor is added correctly or that a donation is appended to an existing donor"""
    dc.sort_donation('Andrew', 1000)
    assert dc.donor_list[1].name == 'Andrew'
    assert dc.donor_list[1].donation == [1000]
    
    dc.sort_donation('Fred', 5)
    assert dc.donor_list[0].donation == [1,2,3,4,5]


def test_list_print():
    """Tests tests that donors names are converted to text correctly for printing"""
    assert dc.list_donors() == 'Fred\nAndrew\n'


def test_compose_email():
    """Test email text is generated correctly"""
    email = dc.compose_email(d.name)
    expected = f"\n\nDear Fred,\n\n\tWe appreciate your generous donations totaling $15.00.\n\nThank you,\nAndrew\n\n" 
    assert email == expected


def test_email_file_write():
    """Test that text files are created corretly in email function"""
    dc.email_all()
    for root, dir, files in os.walk('./lesson09'):
        for donor in dc.donor_list:
            assert any(f==f"Thank_You_to_{donor.name}.txt" for f in files)


def test_build_report():
    """Tests that the report info is built correctly"""
    report = dc.build_report()
    assert report == [('Fred', 15.00, 5, 3.00), ('Andrew', 1000, 1, 1000)]    