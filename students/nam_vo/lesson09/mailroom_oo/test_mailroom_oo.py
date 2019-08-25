"""
Test code for donor_models.py
"""

import pytest

from donor_models import *

def test_donor_init():
    d1 = Donor('Nam Vo', [100, 50.0])
    print(f"d1 = {d1}")
    assert(d1.name) == 'Nam Vo'
    assert(d1.donations) == [100.0, 50.0]

    d2 = Donor('Vu Vo')
    print(f"d2 = {d2}")

    with pytest.raises(TypeError):
        d3 = Donor(100, 'Nam')
    
    with pytest.raises(ValueError):
        d4 = Donor('Nam', [-10])
        
    # assert False

def test_donor_setter():
    d = Donor('Nam Vo', [100, 50.0])
    d.name = 'Vu Vo'
    d.donations = [40, 55.5]
    print(f"d = {d}")
    assert(d.name) == 'Vu Vo'
    assert(d.donations) == [40.0, 55.5]

    with pytest.raises(TypeError):
        d.name = 1000
    
    with pytest.raises(ValueError):
        d.donations = [30, -15]
        
    # assert False

def test_send_thankyou():
    d = Donor('Nam Vo', [100, 50.0])
    print(f"d.send_thankyou() = {d.send_thankyou()}")
    # assert False

def test_add_donation():
    d = Donor('Nam Vo', [100, 50.0])
    d.add_donation(80)
    print(f"d = {d}")
    assert(d.donations) == [100.0, 50.0, 80.0]
    
    with pytest.raises(ValueError):
        d.add_donation(-10)
    
    # assert False

def test_sum_donations():
    d = Donor('Nam Vo', [100, 50.0, 80.0])
    print(f"d = {d}")
    assert(d.sum_donations) == 230.0
    # assert False

def test_donorcollection_init():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [200])
    dl1 = DonorCollection()
    dl2 = DonorCollection([d1, d2])
    print(f"DonorCollection's mro: {DonorCollection.__mro__}")
    print(f"dl1 = {dl1}")
    print(f"dl2 = {dl2}")
    # assert False

def test_donorcollection_setter():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [200])
    dl = DonorCollection()
    dl.donors = [d1, d2]
    print(f"dl = {dl}")
    assert(dl.donors[0].name) == 'Nam Vo'
    assert(dl.donors[0].donations) == [100.0, 50.0]

    with pytest.raises(TypeError):
        dl.donors = [Donor(None, [100, 50.0])]
    
    with pytest.raises(ValueError):
        dl.donors = [Donor('Nam Vo', [100, -50.0])]
        
    # assert False

def test_search_donor():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [200])
    dl = DonorCollection([d1, d2])
    print(f"dl = {dl}")
    assert(dl.search_donor('Nam Vo')) == 0
    assert(dl.search_donor('Vu Vo')) == 1
    assert(dl.search_donor('None')) == -1
    # assert False

def test_add_donor():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [200])
    dl = DonorCollection([d1, d2])
    print(f"dl = {dl}")
    # Add donation to existing donor
    dl.add_donor('Nam Vo', 65.5)
    assert(dl.donors[0].donations) == [100.0, 50.0, 65.5]
    print(f"dl = {dl}")
    # Add new donor
    dl.add_donor('Paul Allen', 100000)
    assert(dl.donors[2].donations) == [100000.0]
    print(f"dl = {dl}") 
    # assert False
       
def test_sorted():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [80])
    d3 = Donor('Jasmine Vo', [40, 50.0, 20.3])
    dl = DonorCollection([d1, d2, d3])
    print(f"dl = {dl}")
    dl.sort_by_donations(reverse=False)
    print(f"sorted dl ascend = {dl}")
    dl.sort_by_donations(reverse=True)
    print(f"sorted dl descend = {dl}")
    # assert False

def test_create_report():
    d1 = Donor('Nam Vo', [100, 50.0])
    d2 = Donor('Vu Vo', [80])
    d3 = Donor('Jasmine Vo', [40, 50.0, 20.3])
    dl = DonorCollection([d1, d2, d3])
    print(f"dl = {dl}")
    content = dl.create_report()
    print(f"content = {content}")
    # assert False
