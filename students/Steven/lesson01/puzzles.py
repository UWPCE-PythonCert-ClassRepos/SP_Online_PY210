#! bin/user/env python3
'''
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
'''

def hello_name (name):
    return"Hello " + name + "!"

assert hello_name('Bob') == "Hello Bob!"
assert hello_name('Alice') == "Hello Alice!"
assert hello_name('X') == "Hello X!"

