"""
test code for mailroom_OO.py

"""

import io
import pytest
import math

# import * is often bad form, but makes it easier to test everything in a module.
from Donor_Models import *

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

#paramatize
def test_don_str():
    '''Donor class string'''
    Morgan_Stanley = Donor("Morgan Stanley")

    assert str(Morgan_Stanley) == 'Morgan Stanley'

#paramatize
def test_don_repr():
    '''Donor class repr'''
    Morgan_Stanley = Donor("Morgan Stanley")

    assert repr(Morgan_Stanley) == 'Morgan Stanley'

def test_init_donation():
    '''Creating first donation'''
    d = Donor('Paul')
    d.append(15)

    assert d.donations == [15]
    d.append([16, 17])
    assert d.donations == [15, 16, 17]

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

# @pytest.mark.parametrize(
#     'a, expected', [
#         ("Morgan Stanley", True),
#         ("Cornelius Vanderbilt", True),
#         ("John D. Rockefeller", True),
#         ("Stephen Girard", True),
#         ("Andrew Carnegie", True),
#         ("William Gates", False),
#         ("Jeffery Bezos", False)
#     ]
# )
def test_col_init():
    dc = Donor_Collect()
    MS = Donor("Morgan Stanley")
    #MS.donations = []

    print(dc)
    assert "".join(dc.donors) == "Morgan Stanley"

def test_col_str():
    dc = Donor_Collect()

    assert str(dc) == "Collection of Donors: Morgan Stanley"

def test_col_repr():
    dc = Donor_Collect()
    d = Donor('Morgan Stanley')

    assert repr(dc) == repr(d)

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
    dc = Donor_Collect()
    M_S = Donor("Morgan Stanley")
    dc.append(M_S)
    M_S.donations = [10]
    M_S.append(7.50)

    # print(sum(M_S.donations))
    # print(dc.donors)
    new_dict = dc.calc_report()    

    print(M_S.donations)
    print(dc.calc_report())
    assert new_dict[1] == "Morgan Stanley"
    assert new_dict[1][0] == 17.5
    assert new_dict[1][1] == 2 
    assert new_dict[1][2] == 8.75

'''
create donor
track name?
track donations
append donation
init
str
repr


confirm starting dict
confirm existance
don col str
don col repr
report calc
report print
'''