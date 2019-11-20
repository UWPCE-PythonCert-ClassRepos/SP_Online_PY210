import unittest
from datetime import date

import mailroom4 as mail
import os


class MyTestCase(unittest.TestCase):
    # Setup
    def setUp(self):
        mail.donors = {"Bill Gates": [85, 100],
                       "Jeff Bezos": [65, 25, 55],
                       "Elon Musk": [15, 25],
                       "The Rock": [250, 125, 55],
                       "Kevin Hart": [30]}

    # Test Get Donor Names
    def test_get_donor_names(self):
        self.assertEqual(mail.get_donor_names(), ['Names of Donors: ', 'Bill Gates', 'Jeff Bezos',
                                                  'Elon Musk', 'The Rock', 'Kevin Hart'])

    # Test send_a_thank_you with new donor
    def test_new_donation(self):
        user_action_TY = 'Jon Vu'
        donor_name_list = list(mail.donors.keys())
        Email_Thanks = '{}, your donation of ${:.2f} is greatly appreciated.'
        donation = 25
        self.assertEqual(mail.new_donation(user_action_TY, donor_name_list, donation),
                         Email_Thanks.format(user_action_TY, 25))

    # Test add donation to existing donor
    def test_old_donor(self):
        user_action_TY = 'Bill Gates'
        donor_name_list = list(mail.donors.keys())
        Email_Thanks = '{}, your donation of ${:.2f} is greatly appreciated.'
        donation = 25
        self.assertEqual(mail.new_donation(user_action_TY, donor_name_list, donation),
                         Email_Thanks.format(user_action_TY, 25))

    # Test Create Report
    def test_createAReport(self):
        self.assertEqual(mail.create_a_report(), "\nDonor Name        | Total Given | # Gifts | Average Gift\n" +
                         "------------------------------------------------------------------" +
                         "\nBill Gates        $   185.00           2     $     92.50" +
                         "\nElon Musk         $    40.00           2     $     20.00" +
                         "\nJeff Bezos        $   145.00           3     $     48.33" +
                         "\nKevin Hart        $    30.00           1     $     30.00" +
                         "\nThe Rock          $   430.00           3     $    143.33")

    # Test File Creation in Send Letter
    def test_FileCreation(self):
        mail.send_all_letters()
        assert os.path.isfile('Bill Gates.txt')
        assert os.path.isfile('Elon Musk.txt')
        assert os.path.isfile('Jeff Bezos.txt')
        assert os.path.isfile('Kevin Hart.txt')
        assert os.path.isfile('The Rock.txt')

    # Test Letter Contents
    def test_sendLetter_Contents(self):
        mail.send_all_letters()
        f = open('Bill Gates.txt', "r")
        f1 = f.readlines()
        self.assertEqual(f1[0], '------------------------------------\n')
        self.assertEqual(f1[1], '\n')
        self.assertEqual(f1[2], 'Hello {},\n'.format('Bill Gates'))
        self.assertEqual(f1[3], '\n')
        self.assertEqual(f1[4], 'Thank you for your kind donation of $210. We will use this money for good use! We '
                                'hope to hear from you soon.\n')
        self.assertEqual(f1[5], '\n')
        self.assertEqual(f1[6], 'Yours Truly, \n')
        self.assertEqual(f1[7], '\n')
        self.assertEqual(f1[8], 'Jon\'s Team')

    # Test Program Quits
    def test_quitter(self):
        self.assertEqual(mail.quit_program(), 'exit')


if __name__ == '__main__':
    unittest.main()
