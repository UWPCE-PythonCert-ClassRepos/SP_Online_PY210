#!/usr/bin/env python3
# 12/01/2020
# lesson01
# Dev: Cody Yarger
# This script includes four functions that demonstrate four common Exceptions
# NameError, TypeError, SyntaxError and AttributeError.

# Name error function
def name_error():
    x = y

# Type error function
def type_error():
    list = [0, 1, 2]
    return list(3)

# Syntax error function
def syntax_error():
    5 === 5

# Attribute error function
def attribute_error():
    string = "text"
    string.append("attribute error")
