import pytest

from donor_models import *

def test_donor():
    d = Donor('Brian Campbell', 101.5)
    assert d.name == 'BRIAN CAMPBELL'
    assert d.donations == (101.5,)

def test_donor_input_exception_1():
    with pytest.raises(TypeError, match="Donor class initialization "
                                        "requires a 'str' "
                                        "object as first input argument"):
        d = Donor(123)

def test_donor_input_exception_2():
    with pytest.raises(ValueError):
        d = Donor('Brian Campbell', 'word')

def test_add_donation():
    d = Donor('Brian Campbell', 101.5)
    d.add_donation(99)
    assert d.donations == (101.5, 99.)

def test_avg_donation():
    d = Donor('Brian Campbell', 100)
    d.add_donation(50)
    assert d.avg_donation == 75

def test_donorcollection():
    a = Donor('A')
    b = Donor('B')
    c = DonorCollection(a)
    c.add_donor(b)
    assert c.donors[0].name == 'A'
    assert c.donors[1].name == 'B'
    a.add_donation(100)
    b.add_donation(200)
    assert c.donors[0].donations == (100,)
    assert c.donors[1].donations == (200,)

def test_donorcollection_execption():
    with pytest.raises(TypeError, match="DonorCollection class requires "
                                        "'Donor' object as input"):
        c = DonorCollection('word')

def test_donor_thankyou():
    a = Donor('Brian Campbell')
    c = DonorCollection(a)
    a.add_donation(100)
    a.add_donation(200)
    assert c.thank_you('Brian Campbell') == thank_you_tmp.format('BRIAN CAMPBELL',
                                                                 200,
                                                                 2,
                                                                 300)

def test_donor_report():
    c = DonorCollection()
    a = Donor('bob wilson')
    b = Donor('frank thompson')
    c.add_donor(a)
    c.add_donor(b)
    a.add_donation(1000)
    a.add_donation(2000)
    a.add_donation(600)
    b.add_donation(800)
    b.add_donation(800)
    b.add_donation(800)
    b.add_donation(1600)
    assert c.report[0] == report_tmp.format('FRANK THOMPSON',
                                            4000,
                                            4,
                                            1000)
    assert c.report[1] == report_tmp.format('BOB WILSON',
                                            3600,
                                            3,
                                            1200)

def test_list_donors():
    c = DonorCollection()
    a = Donor('zach abrams')
    b = Donor('frank mercer')
    d = Donor('adam zelick')
    c.add_donor(a)
    c.add_donor(b)
    c.add_donor(d)
    assert c.donor_list == ['ZACH ABRAMS', 'FRANK MERCER', 'ADAM ZELICK']
