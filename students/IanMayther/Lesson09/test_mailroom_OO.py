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
    
    with pytest.raises(AttributeError):
        d = Donor(15)

    d = Donor("Morgan Stanley")

def test_init_donation():
    '''Creating first donation'''
    d = Donor()
    d.append(15)

    assert d.donations == [15]

#paramatize
def test_str():
    Morgan_Stanley = Donor()

    assert str(Morgan_Stanley) == "Morgan Stanley"

#paramatize
def test_repr():
    Morgan_Stanley = Donor()
    Morgan_Stanley.append(16)

    assert repr(Morgan_Stanley) == 'Morgan Stanley([16])'

'''
create donor
track name?
track donations
append donation
init
str
repr



confirm existance

'''