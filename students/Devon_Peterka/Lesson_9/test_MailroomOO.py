#!/usr/bin/env python3

import unittest
import MailroomOO as mailroom
import Donor

class test_Donor_Class(unittest.TestCase):
    def SetUp(self):
        donor1 = Donor('Dave', 'Jones')

    def test_new_Donor(self):
        self.assertEqual(donor1.full_name, 'Dave Jones')
        self.assertEqual(donor1.donations, [])
        with self.assertRaises(AttributeError):
            donor1.last_donation()
        donor1.add_donation(500)
        
