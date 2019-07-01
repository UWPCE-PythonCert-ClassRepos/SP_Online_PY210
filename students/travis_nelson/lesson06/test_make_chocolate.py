#!

import unittest
import make_chocolate

# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always
# use big bars before small bars.
# Return -1 if it can't be done.


class MakeChocolatePackages(unittest.TestCase):
    '''make_chocolate(small, big, goal):
        ...
        ...
        return number_of_packages_possible'''
    known_values = (((4, 1, 9), 4),
                    ((4, 1, 10), -1),
                    ((4, 1, 7), 2),
                    ((6, 2, 7), 2),
                    ((4, 1, 5), 0),
                    ((4, 1, 4), 4),
                    ((5, 4, 9), 4),
                    ((9, 3, 18), 3),
                    ((3, 1, 9), -1),
                    ((1, 2, 7), -1),
                    ((1, 2, 6), 1),
                    ((60, 100, 550), 50)
                    )

    def test_packages(self):

        for expected_arguments, expected_output in self.known_values:
            arg1 = expected_arguments[0]
            arg2 = expected_arguments[1]
            arg3 = expected_arguments[2]
            result = make_chocolate.make_chocolate(arg1, arg2, arg3)
            self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
