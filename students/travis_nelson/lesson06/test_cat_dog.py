#!

import unittest
import cat_dog


# Return True if the string "cat" and "dog" appear
# the same number of times in the given string.


class CuriousCatDog(unittest.TestCase):
    '''cat_dog(str):
        ...
        ...
        return True or False'''
    known_values = (('catdog', True),
                    ('catcat', False),
                    ('1cat1cadodog', True),
                    ('catxxdogxxxdog', False),
                    ('catxdogxdogxcat', True),
                    ('catxdogxdogxca', False),
                    ('dogdogcat', False),
                    ('dogogcat', True),
                    ('dog', False),
                    ('cat', False),
                    ('ca', True),
                    ('c', True),
                    ('', True)
                    )

    def test_cat_dogs(self):

        for expected_arg, expected_output in self.known_values:
            result = cat_dog.cat_dog(expected_arg)
            self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
