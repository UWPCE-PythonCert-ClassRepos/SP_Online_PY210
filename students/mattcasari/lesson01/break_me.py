#!/usr/bin/python
# -*- coding: ascii -*-

def Test_NameError():
    print(name_fail)

def Test_TypeError():
    l1 = list('123',123)

# def Test_SyntaxError():
#     t = 1 + 2 3

def Test_AttributeError():
    t = 5
    t.length()