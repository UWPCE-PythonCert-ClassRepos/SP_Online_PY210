#!/usr/bin/env python3

import unittest
import MailroomOO as mailroom
from Donor import Donor

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

class test_Mailroom(unittest.TestCase):
    def setUp(self):
        pass
