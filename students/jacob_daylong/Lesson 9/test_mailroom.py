import pytest
import tempfile
import mailroom_oo as moo
import mailroom_cli as m_cli

donor = ()
donor_table = {}


def test_donor_table_init():
    moo.Donors.dict_init()
    expected = (['John Doe', 'Jane Doe', 'Johnny Mnemonic', 'Phillip Dick', 'Bobby Newport'])

    assert moo.Donors.create_report() == expected

def test_thankyou_note():
    
    note = (f'\nDear Jake, \nThank you for your donation of ' 
          f'${500:.2f}. \nSincerely, Jake\n')
    
    assert moo.Donor.thankyou_note("Jake", 500) == note

def test_thankyou_print():
    expected = tempfile.gettempdir() + "/"
    assert moo.Donors.thankyou_print() == expected

def test_add_donation():
    expected = ({'Bobby Newport': [2000, 100],
                 'Jake': [500],
                 'Jane Doe': [10000, 4000, 2000],
                 'John Doe': [10000, 2000, 5000, 3000],
                 'Johnny Mnemonic': [900, 800, 1000],
                 'Phillip Dick': [2220]})
    assert moo.Donors.add_donation("Jake", 500) == expected