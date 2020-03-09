# usr/bin/env python3
# test_my_mod.py

import unittest
from my_mod import my_func


class MyFuncTestCase(unittest.TestCase):
    def test_my_func(self):
        test_vals = (2, 3)
        expected = test_vals[0] & test_vals[1]
        actual = my_func(*test_vals)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
