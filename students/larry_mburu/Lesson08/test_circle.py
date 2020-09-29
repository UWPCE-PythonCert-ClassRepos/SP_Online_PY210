from circle import Circle
from circle import Sphere
import pytest

######
#Step 1
######

def test_init(): 
    """
    Test the initialization of the object
    """
    radius = 10
    c = Circle(radius)
    assert isinstance(c, Circle)
    assert c.radius == radius

#####
#Step 2
#####

def test_get_diameter(): 
    """
    validate the diameter property is correct
    """
    radius = 10
    c = Circle(radius)
    expected_diameter = 20 
    assert expected_diameter == c.diameter

####
#Step 3
####

def test_set_diameter(): 
    """
    validate the diameter setter property
    """
    radius = 10
    c = Circle(radius) 
    expected_diameter = 10 
    c.diameter = expected_diameter 
    assert c.diameter == expected_diameter
    assert c.radius == expected_diameter / 2

####
#Step 4 
####
def test_area_property(): 
    """
    validate area property(readonly)
    """
    from math import pi 
    radius = 10 
    c = Circle(radius) 
    expected_area = 31415926535.89793
    assert c.area == expected_area
    #assert c.area is AttributeError

####
#Step 5
####
def test_from_diameter(): 
    """
    test the @classmethod
    """
    diameter = 10 
    c = Circle.from_diameter(diameter)
    assert c.radius == c.diameter / 2

####
#Step 6
####
def test_str(): 
    """
    test the str representation
    """
    c = Circle(4) 
    assert c.__str__() == 'Circle with radius: 4.000000'

def test_repr():
    """
    the the repr string representation
    """
    c = Circle(4) 
    assert c.__repr__() == 'Circle(4)'

####
#Step 7 
### 
def test_add(): 
    """
    test adding two circle objects
    """
    circle_a = Circle(4) 
    circle_b = Circle(4) 
    expected = circle_a + circle_b
    assert expected.radius == Circle(8).radius

def test_mul(): 
    """
    test the multiplier of two circle objects
    """
    circle = Circle(4)
    expected = circle * 3 
    assert expected.radius == Circle(12).radius

####
#Step 8
#### 
def test_gt_lt(): 
    """
    tests greater than and less than comparison of two circle objects
    """
    circle_a = Circle(2) 
    circle_b = Circle(4) 
    assert (circle_a > circle_b) == False
    assert (circle_a < circle_b) == True

def test_eq(): 
    """
    tests object equality
    """
    circle_a = Circle(2) 
    circle_b = Circle(4)
    assert (circle_a == circle_b) == False

def test_sorting(): 
    """
    test the sorting of circle objects
    """
    circles = [Circle(i) for i in range(10, 1, -1)] 
    sorted_circles = sorted(circles, key=Circle.sort_key)
    assert circles != sorted_circles

def test_reflected_numerics(): 
    """
    test if object * val(int) is the same as val(int) * object 
    """
    circle = Circle(2)
    assert circle * 3 == 3 * circle

def test_iadd(): 
    """ 
    test augmented assignments i.e *=, +=   
    """
    #test instance += instance expression
    circle = Circle(2) 
    circle += circle
    assert circle == Circle(4)
    # test += 2 expression
    circle = Circle(2)
    circle += 2
    assert circle == Circle(4)

def test_idiv(): 
    """
    test augmented division
    """
    circle_a = Circle(10) 
    circle_b = Circle(2) 
    circle_a /= circle_b
    assert circle_a.radius == 5

####
#Step 9 
#### 
def test_sphere_init(): 
    """
    test sphere object creation
    """
    Sphere(5)

def test_sphere_str(): 
    """
    test sphere __str__() 
    """
    sphere = Sphere(5) 
    assert str(sphere) == 'Sphere with radius: 5.000000'

def test_sphere_repr(): 
    """
    test sphere __repr__() 
    """
    sphere = Sphere(5)
    assert repr(sphere) == 'Sphere(5)'

def test_volume_property(): 
    """
    test volume property
    """
    sphere = Sphere(5) 
    assert float(sphere.volume) == 523.6

def test_area_propery(): 
    """
    test area property
    """
    sphere = Sphere(5)
    with pytest.raises(NotImplementedError):
        sphere.area

def test_sphere_add(): 
    """
    test adding 2 spheres 
    """
    sphere_1 = Sphere(2) 
    sphere_2 = Sphere(2) 
    assert (sphere_1 + sphere_2) == Sphere(4) 

def test_sphere_iadd():
    """
    test adding spheres with argumented add
    """ 
    sphere_1 = Sphere(2)
    sphere_1 += sphere_1 
    assert sphere_1 == Sphere(4)