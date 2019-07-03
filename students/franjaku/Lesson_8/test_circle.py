"""
Test code for circle.py
"""

import pytest

from circle import *

########
# Step 1
########
"""
Create a circle class that has c = Circle(5) as the signature
Ensure radius is a required attribute
"""


def test_init():
    """
    Test that we pass the
    """
    # check for missing radius intput
    with pytest.raises(TypeError):
        c = Circle()

    c = Circle(5)
    assert c.radius == 5


########
# Step 2
########
"""
Add a diameter property so the user can get the diameter of the circle
"""
def test_diameter():
    """Test that diameter attribute exists and twice the radius"""
    c = Circle(5)

    assert c.diameter == 10


########
# Step 3
########
"""
Allow the user to set the diameter of the circle.
Ensure that the radius and diameter are always in sync
"""