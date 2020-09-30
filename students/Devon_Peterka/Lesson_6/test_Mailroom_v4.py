#!/usr/bin/env python3

import unittest
import os
from unittest.mock import patch
import Mailroom_v4 as mailroom

'''
NOTE: Some tests give potential false positives when user has
pre-existing files with names 'Bill_500.00_0.txt' and/or 'Bob
Johnson_50.00_0.txt' in their script-created 'Thank_Yous'
directory.  Delete these if they happen to be present.
'''
# Test the add_donation function
class test_block(unittest.TestCase):
    def setUp(self):
        self.donors = {'Bob Johnson' : [500, 27.50],
                  'Jerry' : [53, 802, 6],
                  'Abe' : [.01, 873, 5182.38]}

    def tearDown(self):
        del self.donors

    # Tests to make sure clean_input function returns proper dict
    # key when an argument is given
    @patch('builtins.input', side_effect='2')
    def test_clean_input(self, mock_input):
        dict = {'a' : ['1'], 'b' : ['2'], 'back' : ['3']}
        self.assertEqual(mailroom.clean_input('',dict),'b')

    @patch('builtins.input', side_effect ='FIVE')
    def test_clean_input_invalid(self, mock_input):
        dict = {'a' : ['1'], 'b' : ['2'], 'back' : ['3']}
        self.assertEqual(mailroom.clean_input('',dict),'invalid')

    # Test donor_list extraction of donor names
    def test_donor_list(self):
        expected = ['Bob Johnson', 'Jerry', 'Abe']
        self.assertEqual(mailroom.donor_list(self.donors), expected)

    # Test adding a new donor & donation
    @patch('builtins.input', side_effect=['Bill', '500', 'yes'])
    def test_add_donation1(self, mock_input):#, mock_donors):
        mailroom.add_donation(self.donors)
        expected = {'Bob Johnson' : [500, 27.50],
                    'Jerry' : [53, 802, 6],
                    'Abe' : [.01, 873, 5182.38],
                    'Bill':[500]}
        self.assertEqual(self.donors,expected)

    # Test adding a new donation to existing donor
    @patch('builtins.input', side_effect=['Bob Johnson', '50', 'yes'])
    def test_add_donation2(self, moc_input):
        mailroom.add_donation(self.donors)
        expected = {'Bob Johnson' : [500, 27.50, 50],
                    'Jerry' : [53, 802, 6],
                    'Abe' : [.01, 873, 5182.38]}
        self.assertEqual(self.donors, expected)
    
    '''
    (2) tests to make sure prior test-created files are present
    and contain what is expected.
    '''
    def test_files_content1(self):
        expected = ('Dear Bill,\n'
                   '\n'
                   '\tThank you for your generous donation of '
                   '$500.00'
                   '\n toward our cause.  It is very appreciated.\n'
                   '\n'
                   'Sincerely,\n'
                   'Local Charity Inc.\n')
        with open('Thank_Yous/Bill_500.00_0.txt', 'r') as file:
            result = file.read()
        self.assertEqual(result,expected)
        os.remove('Thank_Yous/Bill_500.00_0.txt')

    def test_files_content2(self):
        expected = ('Dear Bob Johnson,\n'
                   '\n'
                   '\tThank you for your generous donation of '
                   '$50.00'
                   '\n toward our cause.  It is very appreciated.\n'
                   '\n'
                   'Sincerely,\n'
                   'Local Charity Inc.\n')
        with open('Thank_Yous/Bob Johnson_50.00_0.txt', 'r') as file:
            result = file.read()
        self.assertEqual(result,expected)
        os.remove('Thank_Yous/Bob Johnson_50.00_0.txt')

    '''
    (3) tests to ensure back-outs work at each input opportunity
    on 'send_thanks' branch
    '''
    @patch('builtins.input', side_effect=['Bill', 'back'])
    def test_add_donation_backout1(self, mock_input):
        self.assertEqual(mailroom.add_donation(self.donors), 'back')
    
    @patch('builtins.input', side_effect=['exit'])
    def test_add_donation_backout2(self, mock_input):
        self.assertEqual(mailroom.add_donation(self.donors), 'back')

    @patch('builtins.input', side_effect=['Bill', 'quit'])
    def test_add_donation_backout3(self, mock_input):
        self.assertEqual(mailroom.add_donation(self.donors), 'back')

    def test_makes_files(self):
        '''
        Test to make sure 'thank_all_donors' function does indeed thank
        all donors with expected number of .txt files resulting.
        '''
        pre_count = len(os.listdir('Thank_Yous'))
        mailroom.thank_all_donors(self.donors)
        post_count = len(os.listdir('Thank_Yous'))
        self.assertEqual(post_count - pre_count, 3)
        os.remove('Thank_Yous/Bob Johnson_27.50_0.txt')
        os.remove('Thank_Yous/Jerry_6.00_0.txt')
        os.remove('Thank_Yous/Abe_5,182.38_0.txt')

    def test_message1(self):
        '''
        Test to verify message generator handles integer input as
        expected
        '''
        test_value = ('Donor', 15)
        message = ('Dear Donor,\n'
                   '\n'
                   '\tThank you for your generous donation of '
                   '$15.00'
                   '\n toward our cause.  It is very appreciated.\n'
                   '\n'
                   'Sincerely,\n'
                   'Local Charity Inc.\n')
        self.assertEqual(mailroom.thanks_message(*test_value), message)

    def test_message2(self):
        '''
        no longer needed due to exception handling in this
        portion of script
        '''
        #test_value = ('Donor', 'A')
        #self.assertRaises(ValueError,mailroom.thanks_message,*test_value)

    def test_message3(self):
        '''
        Test to verify message function truncates partial cents and
        adds commas as expected
        '''
        test_value = ('Donor', 5000000.999)
        message = ('Dear Donor,\n'
                   '\n'
                   '\tThank you for your generous donation of '
                   '$5,000,001.00'
                   '\n toward our cause.  It is very appreciated.\n'
                   '\n'
                   'Sincerely,\n'
                   'Local Charity Inc.\n')
        self.assertEqual(mailroom.thanks_message(*test_value),message)

    def test_table_rows(self):
        '''test table row generator'''
        expected = [('Abe', 6055.39, 3, 2018.4633333333334),
                    ('Jerry', 861, 3, 287),
                    ('Bob Johnson', 527.50, 2, 263.75)]
        self.assertEqual(mailroom.table_rows(self.donors), expected)
        

if __name__ == '__main__':
    unittest.main()
