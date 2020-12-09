#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson05
# Exceptions Lab (except_lab.py)
# Steve Long 2020-11-01 | v0
#
# Requirements:
# =============
#
#   Create a wrapper function safe_input() that returns None rather than
#   raising exception KeyboardInterrupt or EOFError when the user enters
#   KeyboardInterrupt (CTRL-C) or EOFError (CTRL-D isotopes of Unix, CTRL-Z
#   for Windows).
#
# Assumptions:
# ============
#
#   Minimalist solutions are satisfactory.
#
# Implementation:
# ===============
#
#   Function safe_input and demo_safe_input.
#
# Dependencies:
# =============
#
#   None
#
# Script Usage:
# =============
#
#   ./exceptions_lab.py
#
# Issues:
# =======
#
#   Requirements are more than a little vague.
#
# History:
# ========
# 000/2020-11-01/sal/Created and completed.
#
# =============================================================================

def safe_input(prompt):
    """
    Return user input, returning None for EOFError or KeyboardInterrupt.

    :param prompt ::= User prompt, usually with directions for input.
    """
    result = None
    try:
        result = input(prompt)
    except (EOFError, KeyboardInterrupt):
        result = None
    return result


def demo_safe_input():
    """
    Demo function for safe_input. Continues to prompt user for input until
    user types ':X'.
    """
    rejection_prompt = ("\nYou cannot escape that way. Enter a value"
                        " or :X to escape> ")
    prompt = "Enter a value or :X to escape> "
    result = ""
    while (result != ":X"):
        result = safe_input(prompt)
        if (result is None):
            prompt = rejection_prompt
        else:
            result = result.upper()
    prompt = "\nYou have escaped. Press any key to exit> "
    result = safe_input(prompt)
    return True


if __name__ == "__main__":
    demo_safe_input()
