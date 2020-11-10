"""
test code for argument examples
"""

import arguments


def test_kw_args_with_defaults():
    """Test function with default args"""
    assert arguments.fun_opt_kw_params() == ('blue', 'red', 'yellow', 'orange')


def test_kw_args_with_positional():
    """Test function with positional args"""
    assert arguments.fun_opt_kw_params('blue', 'red', 'yellow',
                                       'orange') == ('blue', 'red', 'yellow',
                                                     'orange')


def test_kw_args_with_keywords():
    """Test function with keyword args"""
    assert arguments.fun_opt_kw_params(visited_color='blue',
                                       link_color='red',
                                       back_color='yellow',
                                       fore_color='orange') == ('orange',
                                                                'yellow',
                                                                'red', 'blue')


def test_kw_args_with_tuple():
    """Test function with tuple args"""
    arg_tuple = ('blue', 'red', 'yellow', 'orange')
    assert arguments.fun_opt_kw_params(*arg_tuple) == ('blue', 'red', 'yellow',
                                                       'orange')


def test_kw_args_with_dict():
    """Test function with dict args"""
    arg_dict = {'visited_color': 'blue',
                'link_color': 'red',
                'back_color': 'yellow',
                'fore_color': 'orange'}
    assert arguments.fun_opt_kw_params(**arg_dict) == ('orange', 'yellow',
                                                       'red', 'blue')


def test_kw_args_with_tuple_and_dict():
    """Test function with tuple and dict args"""
    arg_tuple = ('orange', 'yellow')
    arg_dict = {'visited_color': 'blue',
                'link_color': 'red'}

    assert arguments.fun_opt_kw_params(*arg_tuple, **arg_dict) == ('orange',
                                                                   'yellow',
                                                                   'red',
                                                                   'blue')


def test_star_args_with_star_args():
    """Test function with *args and **kwargs args"""

    assert arguments.fun_star_params('orange', 'yellow', visited_color='red',
                                     link_color='blue') == ('orange',
                                                            'yellow',
                                                            'red',
                                                            'blue')


def test_star_args_with_positional():
    """Test function with positional args"""
    assert arguments.fun_star_params('blue', 'red', 'yellow',
                                     'orange') == ('blue', 'red', 'yellow',
                                                   'orange')


def test_star_args_with_keywords():
    """Test function with keyword args"""
    assert arguments.fun_star_params(visited_color='orange',
                                     link_color='yellow',
                                     back_color='red',
                                     fore_color='blue') == ('orange',
                                                            'yellow',
                                                            'red', 'blue')


def test_star_args_with_tuple():
    """Test function with tuple args"""
    arg_tuple = ('blue', 'red', 'yellow', 'orange')
    assert arguments.fun_star_params(*arg_tuple) == ('blue', 'red', 'yellow',
                                                     'orange')


def test_star_args_with_dict():
    """Test function with dict args"""
    arg_dict = {'visited_color': 'orange',
                'link_color': 'yellow',
                'back_color': 'red',
                'fore_color': 'blue'}
    assert arguments.fun_star_params(**arg_dict) == ('orange', 'yellow',
                                                     'red', 'blue')


def test_star_args_with_tuple_and_dict():
    """Test function with tuple and dict args"""
    arg_tuple = ('orange', 'yellow')
    arg_dict = {'visited_color': 'red',
                'link_color': 'blue'}

    assert arguments.fun_star_params(*arg_tuple, **arg_dict) == ('orange',
                                                                 'yellow',
                                                                 'red',
                                                                 'blue')
