#!/usr/bin/env python

from advanced_arguments import colors, colors_2


def test_1():
    assert (colors('red', 'blue', 'yellow', 'chartreuse')
            == ['red', 'blue', 'yellow', 'chartreuse'])


def test_2():
    assert (colors(link_color='red', back_color='blue')
            == ['red', 'blue', 'red', 'pink'])


def test_3():
    assert (colors('purple', link_color='red', back_color='blue')
            == ['purple', 'blue', 'red', 'pink'])


def test_4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert (colors(*regular, **links)
            == ['red', 'blue', 'chartreuse', 'pink'])


def test_5():
    colors_tuple = ('turquoise', 'brown')
    colors_dict = {'Best Color': 'Aggie Maroon', 'Worst Color': 'Burnt Orange'}
    assert (colors_2(*colors_tuple, **colors_dict)
            == ([['turquoise', 'brown', 'Aggie Maroon', 'Burnt Orange'],
                ['turquoise', 'brown'], ['Aggie Maroon', 'Burnt Orange']]))
