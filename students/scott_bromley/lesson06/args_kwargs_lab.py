#!/usr/bin/env python3

import unittest

# args kwargs exercises described here: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/args_kwargs_lab.html


def main():
    assert colors('red', 'blue', 'yellow', 'chartreuse') == ('red', 'blue', 'yellow', 'chartreuse')
    assert colors(link_color='red', back_color='blue') == ('blue', 'blue', 'red', 'green')
    assert colors('purple', link_color='red', back_color='blue') == ('purple', 'blue', 'red', 'green')
    some_colors = ('red', 'orange', 'grey', 'blue')
    assert colors(*some_colors) == ('red', 'orange', 'grey', 'blue')
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert colors(*regular, **links) == ('red', 'blue', 'chartreuse', 'green')

    assert colors_args_kwargs('red', 'blue', 'yellow', 'chartreuse') == (('red', 'blue', 'yellow', 'chartreuse'), {})
    assert colors_args_kwargs(link_color='red', back_color='blue') == ('blue', 'blue', 'red', 'green')
    assert colors_args_kwargs('purple', link_color='red', back_color='blue') == ('purple', 'blue', 'red', 'green')
    some_colors = ('red', 'orange', 'grey', 'blue')
    assert colors_args_kwargs(*some_colors) == (('red', 'orange', 'grey', 'blue'), {})
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert colors_args_kwargs(*regular, **links) == ('red', 'blue', 'chartreuse', 'green')


def colors(fore_color='blue', back_color='black', link_color='red', visited_color='green'):
    return fore_color, back_color, link_color, visited_color


def colors_args_kwargs(*args, **kwargs):
    if len(args) + len(kwargs.keys()) < 4:
        return colors(*args, **kwargs)
    else:
        return args, kwargs


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)