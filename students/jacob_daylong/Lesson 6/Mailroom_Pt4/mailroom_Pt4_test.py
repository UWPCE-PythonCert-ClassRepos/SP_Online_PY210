import pytest
from mailroom_Pt4 import *

donor = ()

donor_table = {}

def test_donor_table_init():
    dict_init()
    expected = (['John Doe', 'Jane Doe', 'Johnny Mnemonic', 'Phillip Dick', 'Bobby Newport'])

    assert create_report() == expected

def test_thankyou_note():
    
    note = (f'\nDear Jake, \nThank you for your donation of ' 
          f'${500:.2f}. \nSincerely, Jake\n')
    
    assert thankyou_note("Jake", 500) == note