#!/usr/bin/env python3

import unittest
import MailroomOO as mailroom
from Donor import Donor

class test_Donor(unittest.TestCase):
    def setUp(self):
        self.donor1 = Donor('Dave', 'Jones')
        self.donor2 = Donor('Jerry', 'Miles', 500)

    def test_repr(self):
        self.assertEqual(str(self.donor1), "Donor(Dave, Jones)")

    def test_name(self):
        self.assertEqual(self.donor1.name, ['Dave', 'Jones'])
        self.assertEqual(self.donor2.name, ['Jerry', 'Miles'])

    def test_last_donation(self):
        self.assertEqual(self.donor2.last_donation(), 500)

#    def test_new_Donor(self):
#        donor1 = Donor('Dave', 'Jones')
#        self.assertEqual(donor1.full_name, 'Dave Jones')
#        self.assertEqual(donor1.donations, [])
#        with self.assertRaises(AttributeError):
#            donor1.last_donation()
#        donor1.add_donation(500)
#        self.assertEqual(donor1.donations, [500])
#        self.assertEqual(donor1.last_donation(), 500)
        
class test_Mailroom(unittest.TestCase):
    def setUp(self):
        pass
    
