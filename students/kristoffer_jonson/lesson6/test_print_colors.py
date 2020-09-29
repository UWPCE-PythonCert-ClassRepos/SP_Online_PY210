from args_kargs_lab import print_colors
from args_kargs_lab import print_colors_args


def test_1():
    assert print_colors('red', 'white','blue','pink') == ('red' ,'white','blue','pink')


def test_2():
    assert print_colors(visited_color = 'red', link_color = 'white') == ('white' ,'white','white','red')


def test_3():
    assert print_colors('red', 'white',visited_color = 'pink') == ('red' ,'white','white','pink')

def test_4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert print_colors(*regular, **links)

def test_5():
    assert print_colors_args('red','blue', link_color = 'chartreuse',visited_color = 'white') == ('red','blue','chartreuse','white')