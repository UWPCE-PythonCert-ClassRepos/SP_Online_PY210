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
    c = DonorCollection()
    c.update_donor('A', 100)
    c.update_donor('B', 200)
    assert c.donors['A'].donations == (100,)
    assert c.donors['B'].donations == (200,)


def test_donor_thankyou():
    a = Donor('Brian Campbell')
    a.add_donation(100)
    a.add_donation(200)
    assert a.send_thank_you == thank_you_tmp.format('BRIAN CAMPBELL',
                                               200,
                                               2,
                                               300)


def test_donor_report():
    c = DonorCollection()
    a = Donor('bob wilson')
    b = Donor('frank thompson')
    c.update_donor('bob wilson', 1000)
    c.update_donor('bob wilson', 2000)
    c.update_donor('bob wilson', 600)
    c.update_donor('frank thompson', 800)
    c.update_donor('frank thompson', 800)
    c.update_donor('frank thompson', 800)
    c.update_donor('frank thompson', 800)
    c.update_donor('frank thompson', 1600)
    assert c.report[0] == report_tmp.format('FRANK THOMPSON',
                                            4800,
                                            5,
                                            960)
    assert c.report[1] == report_tmp.format('BOB WILSON',
                                            3600,
                                            3,
                                            1200)


def test_list_donors():
    c = DonorCollection()
    c.update_donor('zach abrams', 100)
    c.update_donor('frank mercer', 200)
    c.update_donor('adam zelick', 300)
    assert c.donor_list == ['ZACH ABRAMS', 'FRANK MERCER', 'ADAM ZELICK']
