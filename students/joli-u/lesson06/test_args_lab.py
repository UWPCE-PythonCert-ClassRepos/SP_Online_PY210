#!/usr/bin/env python

"""
test code for args and kwargs lab

lesson 6
joli umetsu
py210

"""

from args_lab import color

# default: print("fore-black, back-white, link-blue, visited-purple")

# positional arguments only 
def test_1():
    assert color('red','blue','yellow','chartreuse') == print("fore-red, back-blue, link-yellow, visited-chartreuse")
    
# keyword arguments only    
def test_2():
    assert color(link_color='red', back_color='blue') == print("fore-black, back-blue, link-red, visited-purple")

# both positional and keyword arguments
def test_3():
    assert color('purple', link_color='red', back_color='blue') == print("fore-purple, back-blue, link-red, visited-purple")
    
# a tuple and a dict as arguments
def test_4():
    regular = ('red', 'blue')
    links = {'link_color':'chartreuse'}
    assert color(*regular,**links) == print("fore-red, back-blue, link-chartreuse, visited-purple")

