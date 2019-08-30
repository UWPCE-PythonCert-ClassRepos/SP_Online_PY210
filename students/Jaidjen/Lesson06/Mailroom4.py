import unittest
from Mailroom3 import view_donors, add_donors, main, thankyou_donors


class ViewTestCase(unittest.TestCase):

    def test_view_donors(self):
        view_donor = view_donors('Dohgyu Hwang')
        self.assertEqual(view_donor, 'Dohgyu Hwang')

    def test_sort_donors(self):
        sort_donor = view_donors('1234')
        self.assertEqual(sort_donor, '1234')


class AddTestCase (unittest.TestCase):
    def add_donor(self):
        add_donor_name = add_donors('Anna Smith')
        self.assertEqual(add_donor_name, 'Anna Smith')

    def add_donate(self):
        add_donate = add_donors('1234')
        self.assertEqual(add_donate, '1234')

class ThankYouTestCase(unittest.TestCase):
    def thank_you(self):
        thankyou_letter = thankyou_donors('Anna Smith')
        self.assertEqual(thankyou_letter, 'Anna Smith')


class MainTestCase (unittest.TestCase):
    def choice_prompt(self):
        choice_name = main('2')
        self.assertEqual(MainTestCase, '4')



unittest.main()