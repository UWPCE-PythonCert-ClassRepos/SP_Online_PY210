#!

import unittest
import args_kwargs_lab


class TestArgKwargLab(unittest.TestCase):
    '''color_func(fore_color='red',
                  back_color='blue',
                  link_color='yellow',
                  visited_color='purple'):
        return fore_color, back_color, link_color, visited_color'''

    known_args = ((('red', 'blue', 'yellow', 'green'),
                   ('red', 'blue', 'yellow', 'green')),
                  (('red', 'blue', 'pink', 'purple'),
                   ('red', 'blue', 'pink', 'purple')),
                  (('pink', 'green', 'maroon', 'salmon'),
                   ('pink', 'green', 'maroon', 'salmon'))
                  )

    known_kwargs = ((({'fore_color': 'blue', 'link_color': 'raspberry'}),
                     ('blue', 'blue', 'raspberry', 'purple')),
                    (({'fore_color': 'red'}),
                    ('red', 'blue', 'yellow', 'purple'))
                    )

    def test_args(self):
        for expected_args, expected_output in self.known_args:
            result = args_kwargs_lab.color_func(*expected_args)
            self.assertEqual(result, expected_output)

    def test_kwargs(self):
        for expected_kwargs, expected_output in self.known_kwargs:
            result = args_kwargs_lab.color_func(**expected_kwargs)
            self.assertEqual(result, expected_output)

    def test_combination(self):
        result = args_kwargs_lab.color_func('purple',
                                            link_color='red',
                                            back_color='blue')
        expected_output = ('purple', 'blue', 'red', 'purple')
        self.assertEqual(result, expected_output)

    def test_tuples_n_dicts(self):
        regular = ('red', 'blue')
        links = {'link_color': 'chartreuse'}
        result = args_kwargs_lab.color_func(*regular, **links)
        expected_output = ('red', 'blue', 'chartreuse', 'purple')
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
