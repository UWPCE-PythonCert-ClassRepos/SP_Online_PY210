'''Tests donor_models logic'''

import unittest
import pytest
import donor_models as d
import os

'''Tests for donor object'''
class test_mailroom_donor(unittest.TestCase):
    #Tests donor object initialization
    def test_donor_object(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.donor, 'Alan')
        self.assertEqual(donator.donations, (3,4,5))
        donator2 = d.Donor('Bob')
        self.assertEqual(donator2.donor, 'Bob')
        self.assertEqual(donator2.donations, ())

    #Tests donor sum
    def test_donor_sum(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.sum, 12)

    #Tests donor average
    def test_donor_avg(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.avg, 4)

    #Tests number of donations for a donor
    def test_donor_num_donations(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.num_donations, 3)

    #Tests is donation was added properly
    def test_donor_add_donation(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator.add_donation(6)
        self.assertEqual(donator.donations, (3,4,5,6))
        with pytest.raises(ValueError):
            donator.add_donation('abc')
        with pytest.raises(ValueError):
            donator.add_donation(-5)

    #Tests if last donation of donor is retreived correctly
    def test_get_last_donation(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.last_donation, 5)
        donator2 = d.Donor('Bob')
        with pytest.raises(IndexError):
            donator2.last_donation

    #Tests is file for writing donor exists
    def test_write_donor(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(donator.donor_text, 'Dear {},\n\n Thank you for your generous donation of ${:.2f}! \n It will be put to very good use. \n\nSincerely, \nThe Team\n'.format('Alan', 5))
        donator.write_donor()
        assert os.path.isfile('Alan.txt')

    #Tests if less than is working correctly
    def test_lt(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        self.assertTrue(donator < donator2)
        self.assertFalse(donator > donator2)
        don_list = [donator, donator2]
        don_list.sort(reverse = True)
        self.assertEqual(don_list[0].donor, 'Bob')
        self.assertEqual(don_list[1].donor, 'Alan')

    #Tests is donor is represented correctly
    def test_repr(self):
        donator = d.Donor('Alan', 3, 4, 5)
        self.assertEqual(repr(donator), 'Alan')

'''Tests for donorcollection'''
class test_mailroom_DonorCollection(unittest.TestCase):
    #Tests donorcollection initialization
    def test_donor_object(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        donator3 = d.Donor('Charlie', 9, 10, 11)
        collection = d.DonorCollection(donator, donator2, donator3)
        self.assertIn(donator, collection.donors)
        self.assertIn(donator2, collection.donors)
        self.assertIn(donator3, collection.donors)

    #Tests if donor names are returned correctly
    def test_donor_names(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        donator3 = d.Donor('Charlie', 9, 10, 11)
        collection = d.DonorCollection(donator, donator2, donator3)
        self.assertEqual('Alan\nBob\nCharlie', collection.donor_names)

    #Tests if donor is added to donorcollection correctly
    def test_add_donor(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        collection = d.DonorCollection(donator, donator2)
        collection.add_donor('Charlie')
        donator3 = collection.get_donor('Charlie')
        self.assertIn(donator3, collection.donors)

    #Tests if text for generating report is correct
    def test_report(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        donator3 = d.Donor('Charlie', 9, 10, 11)
        collection = d.DonorCollection(donator, donator2, donator3)
        self.assertEqual(collection.report, '\n' + '{:20}'.format('Donor Name') + '  ' + 'Total Given' + '  ' + 'Num Gifts' + '  ' + 'Average Gift' + '\n' + '\n'
                                            '{:20}'.format('Charlie') + ' $' + '{:11.2f}'.format(30) + '  ' + '{:9.0f}'.format(3) + ' $' + '{:12.2f}'.format(10) + '\n'
                                            '{:20}'.format('Bob') + ' $' + '{:11.2f}'.format(21) + '  ' + '{:9.0f}'.format(3) + ' $' + '{:12.2f}'.format(7) + '\n'
                                            '{:20}'.format('Alan') + ' $' + '{:11.2f}'.format(12) + '  ' + '{:9.0f}'.format(3) + ' $' + '{:12.2f}'.format(4) + '\n')

    #Tests is write donors outputs files for all donors
    def test_write_donors(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        donator3 = d.Donor('Charlie', 9, 10, 11)
        collection = d.DonorCollection(donator, donator2, donator3)
        collection.write_donors()
        assert os.path.isfile('Alan.txt')
        assert os.path.isfile('Bob.txt')
        assert os.path.isfile('Charlie.txt')

    #Tests if certain donor is returned from a donorcollection correctly
    def test_get_donor(self):
        donator = d.Donor('Alan', 3, 4, 5)
        donator2 = d.Donor('Bob', 6, 7, 8)
        donator3 = d.Donor('Charlie', 9, 10, 11)
        collection = d.DonorCollection(donator, donator2, donator3)
        returned_donor2 = collection.get_donor('Alan')
        self.assertEqual(returned_donor2.donor, 'Alan')
        returned_donor = collection.get_donor('Bob')
        self.assertEqual(returned_donor.donor, 'Bob')
        self.assertEqual(returned_donor.donations, (6,7,8))
        returned_donor3 = collection.get_donor('Charlie')
        self.assertEqual(returned_donor3.donor, 'Charlie')
        with pytest.raises(IndexError):
            collection.get_donor('abc')
        with pytest.raises(IndexError):
            collection.get_donor('')