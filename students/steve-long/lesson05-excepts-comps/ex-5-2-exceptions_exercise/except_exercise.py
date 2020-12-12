#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson05
# Exceptions Exercise (except_exercise.py)
# Steve Long 2020-10-31 | v0
#
# Requirements:
# =============
#
#   Listed inline.
#
# Assumptions:
# ============
#
#   Minimalist solutions are satisfactory.
#
# Implementation:
# ===============
#
#   See below. Added print_if helper function to prevent printing "None" when
#   except_test module functions fun or more_fun returns a None value either
#   because of (a) None being returned as a legitimate value or (b) an
#   exception. Code format checked with flake8.
#
# Dependencies:
# =============
#
#   except_test.py
#
# Script Usage:
# =============
#
#   ./except_exercise.py
#
# Issues:
# =======
#
#   Requirements were a little vague.
#
#   I was getting inconsistent behavior with the print functions in
#   except_test.py that are called print with zero or two arguments. I added a
#   version display at the top of the script that revealed that while I am
#   running Python 3.8.2, when I run it as a script, it was executing with the
#   dormant system-loaded version of Python, 2.7.16. I updated the shebang
#   statement to explicitly call out Python version 3 (that's as precise as it
#   gets) but that only promoted it to 3.7.3. It appears that I have 3
#   versions of Python on my machine, the oldest of which is likely tied to
#   some scripts for managing resources for older apps and the OS. Nothing is
#   dependent on version 3.7.3 as far as I know; it's just a version I loaded
#   some time in the past. I then realized I was using the shebang statement
#   from the original except_exercise.py file which was
#
#   #!/usr/bin/python
#
#   To work correctly in my environment (Python 3.8.2 on MacOS 10.15.6) the
#   statement must be
#
#   #!/usr/bin/env python3
#
#   in order to execute against the proper Python version.
#
# History:
# ========
# 000/2020-10-31/sal/Created and completed.
#
# =============================================================================

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.

Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun
import sys

print("Python version: {}".format(sys.version))


def print_if(s):
    """
    Implemented because None prints literally, not as a blank line.
    """
    if (s is not None):
        print(s)


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list

first_try = ["spam", "cheese", "mr death"]

joke = None
try:
    joke = fun(first_try[0])
except NameError:
    joke = fun(first_try[1])
    print_if(joke)
else:
    print_if(joke)

# Here is a try/except block. Add an else that prints not_joke

not_joke = None
try:
    not_joke = fun(first_try[2])
except SyntaxError:
    print("Run away!")
else:
    print_if(not_joke)

# What did that do? You can think of else in this context, as well as in
# loops as meaning: "else if nothing went wrong"
# (no breaks in  loops, no exceptions in try blocks)

# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ["java", "c", "python"]

more_joke = None
try:
    more_joke = more_fun(langs[0])
except (NameError, SyntaxError, IndexError):
    try:
        more_joke = more_fun(langs[1])
    except (NameError, SyntaxError, IndexError):
        try:
            more_joke = more_fun(langs[2])
        except (NameError, SyntaxError, IndexError):
            pass
        else:
            print_if(more_joke)
    else:
        print_if(more_joke)
        more_joke = None
        more_joke = more_fun(langs[2])
        print_if(more_joke)
else:
    print_if(more_joke)
finally:
    last_fun()
