"""
Test the object-oriented Mailroom program.
"""

import os
import unittest

from donor_models import *
import os


class TestDonor(unittest.TestCase):
    """Tests the Donor class."""

    def setUp(self) -> None:
        self.d1 = Donor("name1")
        self.d2 = Donor("name2", 10)
        self.d3 = Donor("name3", [100, 20])

    def test_get_name(self):
        """Test getting name attribute"""
        assert self.d1.name == "name1"
        assert self.d2.name == "name2"
        assert self.d3.name == "name3"

    def test_set_name(self):
        """Test setting name attribute"""
        self.d1.name = "alternate"
        assert self.d1.name == "alternate"

        # Name must be a string
        for not_string in (32, ['a', 'b'], Donor('other')):
            with self.assertRaises(TypeError):
                self.d1.name = not_string

        # Name must not be empty
        with self.assertRaises(ValueError):
            self.d1.name = ""
        with self.assertRaises(ValueError):
            self.d1.name = " "

    def test_get_donations(self):
        """Test getting donations attribute"""
        assert self.d1.donations == []
        assert self.d2.donations == [10]
        assert self.d3.donations == [100, 20]

    def test_set_donations(self):
        """Test setting donations attribute"""
        with self.assertRaises(AttributeError):
            self.d1.donations = [20]

    def test_add_donation(self):
        """Tests :py:func:`Donor.add_donation`"""
        self.d1.add_donation(10)
        assert self.d1.donations == [10]
        assert self.d1.last_donation() == 10

        self.d2.add_donation(5)
        assert self.d2.donations == [10, 5]
        assert self.d2.last_donation() == 5

    def test_add_donation_bad(self):
        """Tests :py:func:`Donor.add_donation` with bad values"""

        bad_values = (0, -1, -20.2)
        for value in bad_values:
            with self.assertRaises(ValueError):
                self.d1.add_donation(value)

        bad_values = ('a', Donor('hi'))
        for value in bad_values:
            with self.assertRaises(TypeError):
                self.d1.add_donation(value)

    def test_last_donation(self):
        """Tests :py:func:`Donor.last_donation`"""

        assert self.d1.last_donation() is None
        assert self.d2.last_donation() == 10
        assert self.d3.last_donation() == 20

        self.d3.add_donation(1)
        assert self.d3.last_donation() == 1

        self.d1.add_donation(3)
        assert self.d1.last_donation() == 3

    def test_total_donations(self):
        """Tests :py:func:`Donor.total_donations`"""

        assert self.d1.total_donations() == 0
        assert self.d2.total_donations() == 10
        assert self.d3.total_donations() == 120

    def test_thank_you(self):
        """Tests :py:func:`Donor.get_thank_you`"""
        d1_thankyou = DONOR_BLANK_TEMPLATE.format(name="name1")
        d2_thankyou = DONOR_THANK_TEMPLATE.format(name="name2", last_donation=10, total_donation=10)
        d3_thankyou = DONOR_THANK_TEMPLATE.format(name="name3", last_donation=20, total_donation=120)

        assert self.d1.get_thankyou() == d1_thankyou
        assert self.d2.get_thankyou() == d2_thankyou
        assert self.d3.get_thankyou() == d3_thankyou

    def test_get_num_donations(self):
        """Tests :py:func:`Donor.number_of_donations`"""
        assert self.d1.number_of_donations() == 0
        assert self.d2.number_of_donations() == 1
        assert self.d3.number_of_donations() == 2

    def test_average_donation(self):
        """Tests :py:func:`Donor.average_donation`"""
        assert self.d1.average_donation() == 0
        assert self.d2.average_donation() == 10
        assert self.d3.average_donation() == 60


class TestDonorCollection(unittest.TestCase):
    """Tests the DonorCollection class."""

    def setUp(self) -> None:
        self.donor1 = Donor("name1")
        self.donor2 = Donor("name2", [10])
        self.donor3 = Donor("name3", [100, 20])

        self.donors = DonorCollection(self.donor1, self.donor2, self.donor3)

    def tearDown(self) -> None:
        for name in self.donors.get_donor_names():
            try:
                os.remove(f"{name}_thanks.txt")
            except FileNotFoundError:
                pass

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            donors = DonorCollection(self.donor1, self.donor2, 'abd')

    def test_get_donors(self):
        """Tests get donors property"""
        assert self.donors.donors == (self.donor1, self.donor2, self.donor3)

    def test_get_donor_names(self):
        """Tests :py:func:`DonorCollection.get_donor_names`"""
        assert self.donors.get_donor_names() == ("name1", "name2", "name3")

    def test_add_donor(self):
        """Tests :py:func:`DonorCollection.add_donor`"""

        self.donors.add_donor("name4", 10)
        assert "name4" in self.donors.get_donor_names()
        assert self.donors["name4"].donations == [10]

        self.donors.add_donor("name5", [12, 13])
        assert self.donors["name5"].donations == [12, 13]

        self.donors.add_donor("name6")
        assert self.donors["name6"].donations == []

        with self.assertRaises(ValueError):
            self.donors.add_donor('NaME2', 2)

    def test_add_donation(self):
        """Tests :py:func:`DonorCollection.add_donation`"""

        self.donors.add_donation("name1", 2)
        assert self.donors["name1"].last_donation() == 2

        with self.assertRaises(TypeError):
            self.donors.add_donation("name1", None)
        with self.assertRaises(ValueError):
            self.donors.add_donation("name1", -2)

        # New donor as well
        self.donors.add_donation("name4", 1)
        assert self.donors["name4"].last_donation() == 1
        assert self.donors["name4"].total_donations() == 1

        with self.assertRaises(TypeError):
            self.donors.add_donation("name5", 'abc')
        with self.assertRaises(ValueError):
            self.donors.add_donation("name5", 0)

    def test_get_donor(self):
        """Tests [] accessing of donors."""
        assert self.donors["name1"] == self.donor1
        assert self.donors["name2"] == self.donor2

        with self.assertRaises(KeyError):
            x = self.donors["name4"]

    def test_get_report(self):
        """Tests :py:func:`DonorCollection.get_report`"""

        rep = REPORT_HEADER + REPORT_ENTRY.format(name="name3", sm=120, l=2, avg=60)
        rep += REPORT_ENTRY.format(name="name2", sm=10, l=1, avg=10) + \
               REPORT_ENTRY.format(name="name1", sm=0, l=0, avg=0)

        assert self.donors.get_report() == rep

        # Add a new donor with less donation amount
        self.donors.add_donor("name4", 5)
        rep = REPORT_HEADER + REPORT_ENTRY.format(name="name3", sm=120, l=2, avg=60)
        rep += REPORT_ENTRY.format(name="name2", sm=10, l=1, avg=10) + \
               REPORT_ENTRY.format(name="name4", sm=5, l=1, avg=5) + \
               REPORT_ENTRY.format(name="name1", sm=0, l=0, avg=0)

        assert self.donors.get_report() == rep

    def test_write_thank_yous(self):
        """Tests :py:func:`DonorCollection.write_thank_yous`"""

        self.donors.write_thank_yous('.')
        for name in self.donors.get_donor_names():
            assert os.path.exists(f"{name}_thanks.txt")


if __name__ == "__main__":
    if os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))
    unittest.main()
