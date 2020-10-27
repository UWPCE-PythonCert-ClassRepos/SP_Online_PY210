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

# def test_donor_init():
#     '''Instantiate donors'''
#     with pytest.raises(AttributeError):
#         d = Donor()
    
#     with pytest.raises(TypeError):
#         d = Donor(15)

#     d = Donor("Morgan Stanley")

# #paramatize
# def test_don_str():
#     '''Donor class string'''
#     Morgan_Stanley = Donor("Morgan Stanley")

#     assert str(Morgan_Stanley) == 'Morgan Stanley'

# #paramatize
# def test_don_repr():
#     '''Donor class repr'''
#     Morgan_Stanley = Donor("Morgan Stanley")

#     assert repr(Morgan_Stanley) == 'Morgan Stanley([])'

# def test_init_donation():
#     '''Creating first donation'''
#     d = Donor('Paul')
#     d.append(15)

#     assert d.donations == [15]
#     d.append([16, 17])
#     assert d.donations == [15, 16, 17]

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

    assert dc.donors == [MS]

def test_col_str():
    dc = Donor_Collect()

    assert str(dc) == "Collection of Donors: Morgan Stanley"

def test_col_repr():
    dc = Donor_Collect()
    d = Donor('Morgan Stanley')

    assert repr(dc) == repr(d)

def test_col_append():
    d = Donor_Collect()
    JDR = Donor('John D. Rockefeller')

    assert JDR in d

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