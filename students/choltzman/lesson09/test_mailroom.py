from donor_models import Donor, DonorCollection


def test_donor_name():
    """Test instantiating a donor object."""
    d = Donor("Test User")
    assert d.name == "Test User"
    assert d.donations == []


def test_donor_add_donation():
    """Test add_donation method."""
    d = Donor("Test User")
    d.add_donation(1)
    assert d.donations == [1]
    d.add_donation(2)
    assert d.donations == [1, 2]


def test_donor_donation_properties():
    """Test donations properties."""
    d = Donor("Test User")
    for value in [1, 2, 3, 4]:
        d.add_donation(value)
    assert d.donations_total == 10
    assert d.donations_count == 4
    assert d.donations_avg == 2.5


def test_donorcollection_add_donor():
    """Test the add_donor method."""
    dc = DonorCollection()
    dc.add_donor("Test User")
    assert dc.donors == {'Test User': Donor("Test User")}


def test_donorcollection_get_donor():
    """Test the get_donor method."""
    dc = DonorCollection()
    dc.add_donor("Test User")
    d = dc.get_donor("Test User")
    assert d.name == "Test User"


def test_donorcollection_names():
    """Test the names property."""
    dc = DonorCollection()
    dc.add_donor("Test User 1")
    dc.add_donor("Test User 2")
    assert dc.names == ["Test User 1", "Test User 2"]


def test_donorcollection_names_sorted():
    """Test names_sorted property."""
    dc = DonorCollection()
    dc.add_donor("Test User 1")
    d = dc.get_donor("Test User 1")
    for value in [1, 2, 3, 4]:
        d.add_donation(value)
    dc.add_donor("Test User 2")
    d = dc.get_donor("Test User 2")
    for value in [5, 6, 7, 8]:
        d.add_donation(value)
    assert dc.names_sorted == ["Test User 2", "Test User 1"]
