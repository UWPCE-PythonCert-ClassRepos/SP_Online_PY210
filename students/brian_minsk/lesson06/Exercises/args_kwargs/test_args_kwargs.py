from args_kwargs import colors, colors1

# fore_color = 'red'
# back_color = 'green'
# link_color = 'blue'
# visited_color = 'yellow'


def test_1():
    assert(colors('red', 'blue', 'yellow', 'chartreuse')
           == ('red', 'blue', 'yellow', 'chartreuse'))


def test_2():
    assert(colors(link_color='red', back_color='blue')
           == ('red', 'blue', 'red', 'yellow'))


def test_3():
    assert(colors('purple', link_color='red', back_color='blue')
           == ('purple', 'blue', 'red', 'yellow'))


def test_4():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert(colors(*regular, **links)
           == ('red', 'blue', 'chartreuse', 'yellow'))


def test_5():
    assert(colors1('red', 'blue', 'yellow', 'chartreuse')
           == ('red', 'blue', 'yellow', 'chartreuse'))


def test_6():
    assert(colors1(link_color='red', back_color='blue')
           == ('red', 'blue', 'red', 'yellow'))


def test_7():
    assert(colors1('purple', link_color='red', back_color='blue')
           == ('purple', 'blue', 'red', 'yellow'))


def test_8():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert(colors1(*regular, **links)
           == ('red', 'blue', 'chartreuse', 'yellow'))
