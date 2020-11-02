# import unittest
# from unittest.mock import patch
#
# from sum import sum
#
# class TestListSum(unittest.TestCase):
#
#     string_of_ints = '1 2 3 4 5'
#
#     string_of_ints_2 = '1 1 1 1 1 1 1 1 1 1'
#
#     @patch('builtins.input', side_effect=[5, string_of_ints])
#     def test_sum_string_of_ints(self, mock_inputs):
#         result = sum()
#         self.assertEqual(result, 15)
#
#     @patch('builtins.input', side_effect=[10, string_of_ints_2])
#     def test_sum_string_of_ints_2self, mock_inputs):
#         result = sum()
#         self.assertEqual(result, 10)

ty_input_tester = "Sarah Paulson"
ty_donation_tester = 5000
donor_dict = {'William Gates': [100.00, 100.00, 100.00], 'Mark Zuckerberg': [20.00, 20.00],
              'Jeff Bezos': [50.00, 50.00, 50.00, 50.00, 50.00], 'Paul Allen': [200.00]}

sorted_donors = sorted(
    ([sum(value), key, len(value), (sum(value) / len(value))] for key, value in donor_dict.items()), reverse=True)
print(sorted_donors)