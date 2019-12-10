#!/usr/bin/env python

print("maknamerr forces a NameError regardless of what you pass for the arg")
print("maktyperr forces a TypeError if you pass a string for the arg")
print("maksynerr forces a SyntaxError if you pass something like !1")
print("makatterr forces an AttributeError if you pass a number for the arg")


def maknamerr(x):
    prantt(x)

def maktyperr(y):
    y+6.0

def maksynerr(z):
    z+1

def makatterr(a):
    a.capitalize()
