from args_kwargs_lab import key_color, key_color_args_kwargs

def test_1():
    assert key_color('black', 'brown', 'blue', 'yellow') == 'black, brown, blue, yellow'

def test_2():
    assert key_color(link_color = 'red', fore_color = 'white') == 'white, brown, red, yellow'

def test_3():
    assert key_color('white', visited_color = 'orange', link_color = 'indigo') == 'white, brown, indigo, orange'

def test_4():
    test_tup = ('brown', 'yellow', 'blue', 'red')
    assert key_color(*test_tup) == 'brown, yellow, blue, red'

def test_5():
    test_dict = {'fore_color': 'orange', 'back_color': 'white',
                 'link_color': 'blue', 'visited_color': 'rose'}
    assert key_color(**test_dict) == 'orange, white, blue, rose'

def test_6():
    tup_01 = ('brown', 'blue', 'red', 'yellow')
    assert key_color_args_kwargs(*tup_01) == 'brown, blue, red, yellow'

def test_7():
    tup_02 = ('orange', 'green')
    assert key_color_args_kwargs('red', 'yellow', *tup_02) == 'red, yellow, orange, green'

def test_8():
    tup_03 = ('cyan', 'emerald')
    dict_01 = {'fore color': 'turquoise', 'back_color': 'burgundy'}
    assert key_color_args_kwargs(*tup_03, **dict_01) == 'cyan, emerald, turquoise, burgundy'