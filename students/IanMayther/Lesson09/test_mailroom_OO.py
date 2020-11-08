"""
test code for mailroom_OO.py

"""

import io
import pytest
import math
#import CLI_Main

# import * is often bad form, but makes it easier to test everything in a module.
from Donor_Models import Donor, Donor_Collect
from CLI_Main import *

##############################
# Step 1 - Donor Class Testing
##############################

def test_donor_init():
    '''Instantiate donors'''
    with pytest.raises(AttributeError):
        d = Donor()
    
    with pytest.raises(TypeError):
        d = Donor(15)

    d = Donor("Morgan Stanley")

@pytest.mark.parametrize(
    'a, b', [
        ('M_S', "Morgan Stanley"),
        ('C_V', "Cornelius Vanderbilt"),
        ('J_D_R', "John D. Rockefeller"),
        ('S_G', "Stephen Girard"),
        ('A_C', "Andrew Carnegie"),
    ]
)
def test_don_str(a, b):
    '''Donor class string'''
    a = Donor(b)

    assert str(a) == b

@pytest.mark.parametrize(
    'a, b', [
        ('M_S', "Morgan Stanley"),
        ('C_V', "Cornelius Vanderbilt"),
        ('J_D_R', "John D. Rockefeller"),
        ('S_G', "Stephen Girard"),
        ('A_C', "Andrew Carnegie"),
    ]
)
def test_don_repr(a, b):
    '''Donor class repr'''
    a = Donor(b)

    assert repr(a) == b

def test_init_donation():
    '''Creating first donation'''
    Paul = Donor('Paul')
    Paul.donations = [15]

    assert Paul.donations == [15]
    Paul.append([16, 17])
    assert Paul.donations == [15, 16, 17]

def test_thankyou_note():
    M_S = Donor("Morgan Stanley")
    M_S.donations = [10]
    M_S.append(7.50)

    assert M_S.thank_you() == "Thanks Morgan Stanley for your $17.50 in donations."

def test_thankyou_email():
    '''Test email text'''
    M_S = Donor("Morgan Stanley")
    M_S.donations = [10]
    M_S.append(7.5)

    assert M_S.email().startswith("Greetings Morgan Stanley")
    assert M_S.email().endswith("(DZCAWCRG)\n")

###################################
# Step 2 - Donor Collection Testing
###################################

def test_col_init():
    dc = Donor_Collect()

    assert isinstance(dc.donors, list)

def test_col_append():
    ''''Testing if Donor appends to Donor_Collection'''
    dc = Donor_Collect()
    JDR = Donor('John D. Rockefeller')
    dc.append(JDR)

    ans = False
    for i in dc.donors:
        if i == JDR:
            ans = True
        
    assert ans

    with pytest.raises(AttributeError):
        dc.append('False Item')

def test_sum_gift():
    DC = Donor_Collect()
    WG = Donor('Bill Gates')
    WG.donations = [15]
    WG.append([16, 17])
    DC.append(WG)
    new_dict = DC.calc_report()    

    print(new_dict)

    assert isinstance(new_dict, dict)
    assert new_dict[repr(WG)] is not None
    assert new_dict[repr(WG)][0] == 48.0
    assert new_dict[repr(WG)][1] == 3 
    assert new_dict[repr(WG)][2] == 16.0

def test_print_report():
    '''Confirm list sorting before printing'''
    dc = Donor_Collect()
    JDR = Donor('John D. Rockefeller')
    JDR.donations = [1500]
    dc.append(JDR)

    EJ = Donor('Elton John')
    EJ.donations = [1600]
    dc.append(EJ)

    temp_list = dc.print_report()
   
    assert isinstance(temp_list, list)
    assert isinstance(temp_list[0], tuple)
    assert temp_list[0][0] == str(EJ)
    assert temp_list[1][0] == str(JDR)

###################################
# Step 3 - CLI Testing
###################################

def test_cli_init():
    '''Confirms initial donor set is correct'''
    assert isinstance(don_col.donors, list)
    assert MS in don_col.donors
    assert CV in don_col.donors
    assert JDR in don_col.donors
    assert SG in don_col.donors
    assert AC in don_col.donors

def test_init_values():
    '''Confirms inital donor donation values are correct'''
    assert sum(MS.donations) == 20.01
    assert sum(CV.donations) == 825.00
    assert sum(JDR.donations) == 7175.00
    assert sum(SG.donations) == 60000
    assert sum(AC.donations) == 1000.03

def test_quit():
    assert quit() == "quit"

def test_donor_validation():
    DC = Donor_Collect()
    JDR = Donor("Jonny D. Rose")
    DC.append(JDR)

    Jinny_D_Rose = Donor("Jinny D. Rose")
    EJ = Donor("Elton John")
    DC.append(EJ)

    assert DC.donor_validation(Jinny_D_Rose) == True
    assert DC.donor_validation(EJ) == False