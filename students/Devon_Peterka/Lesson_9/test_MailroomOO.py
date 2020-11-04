#!/usr/bin/env python3

import unittest
import MailroomOO as mailroom
from Donor import Donor
from DonorCollection import DonorCollection
import io
import sys

class test_Donor(unittest.TestCase):
    '''
    Test for the Donor class object.  Verifies data is stored and can
    be called as expected.
    '''
    def setUp(self):
        '''
        Sets up 3 donors.  One with proper name but no initial donation,
        One with name missing capitalization and single donation,
        and One with missing capitalization and multiple initial
        donations.
        '''
        self.donor1 = Donor('Dave', 'Jones')
        self.donor2 = Donor('Jerry', 'morts', 500)
        self.donor3 = Donor('jack', 'El',  [300,50,9])

    def test_repr(self):
        '''
        Verify repr returns expected representation of object.
        '''
        self.assertEqual(str(self.donor1), "Donor(Dave, Jones)")
        self.assertEqual(str(self.donor2), "Donor(Jerry, Morts)")
        self.assertEqual(str(self.donor3), "Donor(Jack, El)")

    def test_name(self):
        '''
        Verifies name tuple parsed correctly and capitalization errors
        resolved.
        '''
        self.assertEqual(self.donor1.name, ('Dave', 'Jones'))
        self.assertEqual(self.donor2.name, ('Jerry', 'Morts'))
        self.assertEqual(self.donor3.name, ('Jack', 'El'))
    
    def test_full_name(self):
        '''
        Verifies name tuple is read and joined properly into a proper
        name string.
        '''
        self.assertEqual(self.donor1.full_name, 'Dave Jones')
        self.assertEqual(self.donor2.full_name, 'Jerry Morts')
        self.assertEqual(self.donor3.full_name, 'Jack El')

    def test_last_donation(self):
        '''
        Verifies last_donation property does indeed retrieve the last
        donation on record for each donor, or returns error if no
        donations exist.
        '''
        self.assertEqual(self.donor2.last_donation, 500)
        with self.assertRaises(AttributeError):
            self.donor1.last_donation
        self.assertEqual(self.donor3.last_donation, 9)

    def test_add_multiple(self):
        '''
        Verifies multiple new donations can be added as a list.
        '''
        self.donor1.add_donation(500,250,38.72)
        self.assertEqual(self.donor1.donations, [500, 250, 38.72])

    def test_donations(self):
        '''
        Verifies donation history list returns properly when called.
        '''
        self.donor1.add_donation(302.83)
        self.assertEqual(self.donor1.donations, [302.83])
        self.assertEqual(self.donor2.donations, [500])
        self.assertEqual(self.donor3.donations, [300,50,9])

    def test_sort(self):
        d_list = [self.donor1, self.donor2, self.donor3]
        self.assertEqual(sorted(d_list), [self.donor1, self.donor3, self.donor2])
    
    def test_sort_by_name(self):
        d_list = [self.donor1, self.donor2, self.donor3]
        self.assertEqual(sorted(d_list, key=Donor.sort_by_name), [self.donor3, self.donor1, self.donor2])

    def test_sort_by_donation(self):
        d_list = [self.donor1, self.donor2, self.donor3]
        self.assertEqual(sorted(d_list, key=Donor.sort_by_donations,), [self.donor1, self.donor3, self.donor2])
    
    def test_send_thanks(self):
        message = "Dear Jay Marks,\n\nThank you for your generous donation of $3,700.00 toward our cause.  Your gift is most appreciated.\n\nThank you,\nOur Charity"
        self.assertEqual(Donor.send_thanks('Jay', 'Marks', 3700), message)

class test_DonorCollection(unittest.TestCase):
    def setUp(self):
        '''
        Sets up a collection of 4-5 donors each with 1-3 donations each, as per
        assignment prompt.  Mailroom module is left "empty" so a hypothetical user could
        simply populate it and would not have to delete the initial Donor set.
        '''
        self.donor1 = Donor('Dave', 'Jones')
        self.donor2 = Donor('Jerry', 'morts', 500)
        self.donor3 = Donor('jack', 'El',  [300,50,9])
        self.donor4 = Donor('Jenifer', 'Yelb', [12000, 5000])
        self.donor5 = Donor('Ermy', 'Hermy', [0.53])
        donors = [self.donor1, self.donor2, self.donor3,
                  self.donor4, self.donor5]
        # Coincidentally, we're testing the init function here as well.
        self.Donor_List = DonorCollection(donors)

    def test_inits_and_repr(self):
        '''
        Test to verify DonorCollection behaves as expected:
            Throws exceptions with invalid inputs
            Accepts empty inputs
            Accepts multiple inputs (already tested technically)
        '''
        self.assertEqual(str(self.Donor_List), '[Donor(Dave, Jones), Donor(Jerry, Morts), Donor(Jack, El), Donor(Jenifer, Yelb), Donor(Ermy, Hermy)]')

    def test_invalid_init(self):
        '''
        Verify exceptions are raised when invalid inputs are used to
        initialize class object.  Both of the following cases should
        raise an exception:
            1) non-Donor object input
            2) mixture of Donor and non-Donor objects input
        '''
        with self.assertRaises(TypeError):
            D = DonorCollection('Five')

        with self.assertRaises(TypeError):
            bad_list = [self.donor1, self.donor3, 8, '!']
            D = DonorCollection(bad_list)
        
    def test_empty_init(self):
        '''
        Verify DonorCollection object can be initialized empty.
        '''
        D = DonorCollection()
        self.assertEqual(str(D), '[]')

    def test_add_donor(self):
        '''
        Tests that a donor can be added to the collection.
        '''
        donor6 = Donor('Glumpy', 'Terpintine', 800)
        print(type(donor6))
        self.Donor_List.add(donor6)
        self.assertEqual(str(self.Donor_List), '[Donor(Dave, Jones), Donor(Jerry, Morts), Donor(Jack, El), Donor(Jenifer, Yelb), Donor(Ermy, Hermy), Donor(Glumpy, Terpintine)]')

    def test_add_fail(self):
        '''
        Verifies that add donor function exits with exception when fed
        a non-Donor object.
        '''
        with self.assertRaises(TypeError):
            self.Donor_List.add('five')

    def test_new(self):
        '''
        Test functionality to create Donor object and simultaneously add
        it to the DonorCollection object.
        '''
        self.Donor_List.new('Aks', 'Jeeves', [82])
        self.assertEqual(str(self.Donor_List),'[Donor(Dave, Jones), Donor(Jerry, Morts), Donor(Jack, El), Donor(Jenifer, Yelb), Donor(Ermy, Hermy), Donor(Aks, Jeeves)]')

    def test_list(self):
        '''
        Tests alphabetical listing of DonorCollection object
        constituents.
        '''
        self.assertEqual(str(self.Donor_List.list), '[Donor(Jack, El), Donor(Ermy, Hermy), Donor(Dave, Jones), Donor(Jerry, Morts), Donor(Jenifer, Yelb)]')

    def test_list_donations(self):
        '''
        Tests listing of DonorCollection object by net donation.
        '''
        self.assertEqual(str(self.Donor_List.list_by_donation), '[Donor(Jenifer, Yelb), Donor(Jerry, Morts), Donor(Jack, El), Donor(Ermy, Hermy), Donor(Dave, Jones)]')

    def test_indexslice(self):
        '''
        Test that a single, or several, Donor object(s) can be
        "plucked" from the DonorCollection object
        '''
        self.assertEqual(str(self.Donor_List[1]), 'Donor(Jerry, Morts)')
        self.assertEqual(str(self.Donor_List[1:3]), '[Donor(Jerry, Morts), Donor(Jack, El)]')

    def test_report(self):
        '''
        Tests that a report window is generated correctly for printing.
        '''
        report =   ('Donor Name          |  Total Given   | Gifts |  Average Gift  |\n'
                    '--------------------|----------------|-------|----------------|\n'
                    'Jenifer Yelb........| $    17,000.00 |   2   | $     8,500.00 |\n'
                    'Jerry Morts.........| $       500.00 |   1   | $       500.00 |\n'
                    'Jack El.............| $       359.00 |   3   | $       119.67 |\n'
                    'Ermy Hermy..........| $         0.53 |   1   | $         0.53 |\n'
                    'Dave Jones..........| $         0.00 |   0   | $         0.00 |\n'
                    '--------------------|----------------|-------|----------------|\n')
        assert(self.Donor_List.report(self.Donor_List.list_by_donation) == report)

