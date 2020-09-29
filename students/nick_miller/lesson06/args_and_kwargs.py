#!/usr/bin/env python3

"""PY210_SP - args and kwargs
author: Nick Miller"""


def funky(fore_color=None, back_color=None, link_color=None, visited_color=None):
    return fore_color, back_color, link_color, visited_color


def funky2(*args, **kwargs):
    return args, kwargs


print(funky('red', 'blue', 'yellow', 'chartreuse'))
print()
print(funky(link_color='red', back_color='blue'))
print()
print(funky('purple', link_color='red', back_color='blue'))
print()
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
print(funky(*regular, **links))
print()

print("This is for the *args, **kwargs function:")
print()
print(funky2('red', 'blue', 'yellow', 'chartreuse'))
print()
print(funky2(link_color='red', back_color='blue'))
print()
print(funky2('purple', link_color='red', back_color='blue'))
print()
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
print(funky2(*regular, **links))
