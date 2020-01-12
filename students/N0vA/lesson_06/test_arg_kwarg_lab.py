### Test Driven Development for Arg Kwarg Lab ###

from arg_kwarg_lab import *

def test_1():
	assert color_scheme('red', 'blue', 'yellow', 'chartreuse') == ['red', 'blue', 'yellow', 'chartreuse']

def test_2():
	assert color_scheme(link_color='red', back_color='blue') == ['green', 'blue', 'red', 'orange']

def test_3():
	assert color_scheme('purple', link_color='red', back_color='blue') == ['purple', 'blue', 'red', 'orange']

def test_4():
	regular = ('red', 'blue')
	links = {'link_color': 'chartreuse'}

	assert color_scheme(*regular, **links) == ['red', 'blue', 'chartreuse', 'orange']

# Run same tests for second function
def test_5():
    assert complex_color_scheme('red', 'blue', 'yellow', 'chartreuse') == ['red', 'blue', 'yellow', 'chartreuse']

def test_6():
    assert complex_color_scheme(link_color='red', back_color='blue') == ['red', 'blue']

def test_7():
    assert complex_color_scheme('purple', link_color='red', back_color='blue') == ['purple', 'red', 'blue']
# There is suppose to be an extra , because *args is expecting a tuple and puple is only 1 item correct?

def test_8():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}

    assert complex_color_scheme(*regular, **links) == ['red', 'blue', 'chartreuse']
