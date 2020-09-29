"""
Programming In Python - Lesson 1 Task 2: Puzzles - String-1
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# String-1 > hello_name 
def hello_name(name):
    return "Hello " + name

# String-1 > make_abba
def make_abba(a, b):
    return a + b * 2 + a

# String-1 > make_tags 
def make_tags(tag, word):
    return "<{0}>{1}</{0}>".format(tag, word)

# String-1 > make_out_word 
def make_out_word(out, word):
    return out[0:2] + word + out[2:]

# String-1 > extra_end
def extra_end(inString):
    end = inString[len(inString)-2:]
    return end * 3

# String-1 > first_two
def first_two(inString):
    return inString[0:2]

# String-1 > first_half 
def first_half(inString):
    half = len(inString) / 2
    return inString[0:half]

# String-1 > without_end 
def without_end(inString):
  return inString[1:len(inString)-1]

# String-1 > combo_string 
def combo_string(a, b):
    pattern = "{0}{1}{0}"
    if len(a) < len(b):
        return pattern.format(a, b)
    return pattern.format(b, a)

# String-1 > non_start 
def non_start(a, b):
    return a[1:] + b[1:]

# String-1 > left2 
def left2(str):
    start = str[0:2]
    return str[2:] + start
