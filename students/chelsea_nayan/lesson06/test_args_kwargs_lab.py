from args_kwargs_lab import color

"""
def color(fore_color="red", back_color="orange", link_color="yellow", visited_color="green"):
    print(fore_color, back_color, link_color, visited_color)
"""


def test1():
    assert color('red', 'blue', 'yellow', 'chartreuse') == 'red blue yellow chartreuse'

def test2():
    assert color(link_color='red', back_color='blue') == "red blue red green"

def test3():
    assert color('purple', link_color='red', back_color='blue') == "purple blue red green"

regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
def test4():
    assert color(*regular, **links) == "red blue orange chartreuse green"
